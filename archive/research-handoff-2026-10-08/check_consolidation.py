#!/usr/bin/env python3
"""Photon-number mechanism checks for the fixed-output distillation theorem.

Run with --output path. Refuses to overwrite. Standard formula checks and exact
finite certificates do not replace the asymptotic proof in PHYSICAL_MECHANISM.md.
The implementation of Fock amplitudes and number probabilities is independent of
prior checkers; those sources remain unmodified and are rerun separately.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import itertools
import json
import math
from pathlib import Path
import sys
import unittest
sys.dont_write_bytecode = True
import numpy as np
from scipy.integrate import quad
from scipy.special import eval_laguerre

REPORT = {}

def number_distribution(ps):
    """Exact recurrence for PGF sum_k k! e_k(p) (z-1)^k."""
    ps=[F(p) for p in ps]
    if any(p<0 for p in ps) or sum(ps)>1:
        raise ValueError('Physical nonnegative occupied row with sum <= 1 required')
    out=[F(1)]
    for p in ps:
        d=len(out); nxt=[]
        for m in range(d+1):
            here=out[m] if m<d else F(0)
            down=out[m-1] if m else F(0)
            up=out[m+1] if m+1<d else F(0)
            nxt.append(here+p*(m*down-(2*m+1)*here+(m+1)*up))
        out=nxt
    return out

def factorial_distribution(ps):
    """Independent elementary-symmetric expansion of the same probabilities."""
    es=[F(1)]
    for p in ps:
        p=F(p);new=es+[F(0)]
        for k in range(1,len(new)):new[k]+=p*es[k-1]
        es=new
    N=len(ps)
    return [sum(((-1)**(k-m)*math.comb(k,m)*math.factorial(k)*es[k]
                 for k in range(m,N+1)),F(0)) for m in range(N+1)]

def thermal(s,m):
    return s**m/(1+s)**(m+1)

def exact_tv(ps):
    p=number_distribution(ps);s=sum(ps,F(0));N=len(ps)
    return (sum((abs(v-thermal(s,m)) for m,v in enumerate(p)),F(0))
            +(s/(1+s))**(N+1))/2

def fock_state(U,internal):
    """All occupied inputs appear once. Internal labels 0/1 are not measured."""
    M=U.shape[0];st={(0,)*(2*M):1.+0j}
    for i,label in enumerate(internal):
        nxt={}
        for occ,amp in st.items():
            for r in range(M):
                coeff=U[r,i]
                if coeff==0:continue
                t=r+M*label;new=list(occ);new[t]+=1;new=tuple(new)
                nxt[new]=nxt.get(new,0j)+amp*coeff*math.sqrt(occ[t]+1)
        st=nxt
    return st

def marginal_number(st,M,N):
    out=np.zeros(N+1)
    for occ,amp in st.items():out[occ[0]+occ[M]]+=abs(amp)**2
    return out

def tapped_fourier(n,eta):
    Fmat=np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/n)/math.sqrt(n)
    U=np.eye(n+1,dtype=complex);U[:n,:n]=Fmat
    B=np.eye(n+1);B[0,0]=B[n,n]=math.sqrt(eta)
    B[0,n]=math.sqrt(1-eta);B[n,0]=-math.sqrt(1-eta)
    return B@U

def herald(st,n,rule,bad=False):
    M=n+1;val=0.
    for occ,amp in st.items():
        if occ[0]+occ[M]!=1:continue
        if rule=='phase' and sum(r*(occ[r]+occ[M+r]) for r in range(1,n))%n:continue
        if bad and occ[M]!=1:continue
        val+=abs(amp)**2
    return val

def laguerre_constant(m):
    return 4*sum(math.comb(m,k)*2**k*(k+1)*(k+2) for k in range(m+1))

class Checks(unittest.TestCase):
    def test_01_number_law_against_fock_amplitudes(self):
        rng=np.random.default_rng(105631);errs=[];phaseerrs=[];tested=0;maxstates=0
        for N in (2,3,4,5):
            M=N+1
            Q,_=np.linalg.qr(rng.normal(size=(M,M))+1j*rng.normal(size=(M,M)))
            for R in (Q,tapped_fourier(N,.8)):
                st=fock_state(R,[0]*N);maxstates=max(maxstates,len(st))
                actual=marginal_number(st,M,N)
                ps=[F(float(abs(R[0,i])**2)) for i in range(N)]
                self.assertLess(sum(ps),1)
                exact=np.array([float(x) for x in number_distribution(ps)])
                errs.append(float(np.max(abs(actual-exact))))
                self.assertLess(errs[-1],3e-12)
                self.assertLess(abs(actual.sum()-1),3e-12)
                for xi in (.1,.7,2.,5.):
                    v1=np.exp(-xi/2)*np.dot(actual,[eval_laguerre(m,xi) for m in range(N+1)])
                    v2=np.exp(-xi/2)*np.prod([1-float(p)*xi for p in ps])
                    self.assertLess(abs(v1-v2),3e-12)
                s=float(sum(ps));v2=float(sum(p*p for p in ps))
                nums=np.arange(N+1)
                self.assertLess(abs(actual@nums-s),3e-12)
                self.assertLess(abs(actual@(nums*(nums-1))-2*(s*s-v2)),4e-12)
                # A different detector-row completion retains the selected first row.
                D,_=np.linalg.qr(rng.normal(size=(M-1,M-1))+1j*rng.normal(size=(M-1,M-1)))
                mix=np.eye(M,dtype=complex);mix[1:,1:]=D
                changed=marginal_number(fock_state(mix@R,[0]*N),M,N)
                phaseerrs.append(float(np.max(abs(changed-actual))))
                self.assertLess(phaseerrs[-1],4e-12);tested+=1
        REPORT['fock_dictionary']={'cases':tested,'max_probability_error':max(errs),
            'max_completion_error':max(phaseerrs),'max_optical_matrix':6,'max_occupation_entries':maxstates,
            'independent_method':'normalized creation amplitudes versus exact rational PGF recurrence'}

    def test_02_full_distribution_and_thermal_limit(self):
        rows=[];certified=0
        small=[[F(1,2),F(1,2)],[F(1,10),F(1,5),F(2,5)],
               [F(1,5)]*4,[F(1,13)]*8]
        for ps in small:
            p=number_distribution(ps);self.assertEqual(p,factorial_distribution(ps))
            self.assertEqual(sum(p),1);self.assertTrue(all(x>=0 for x in p))
            self.assertEqual(sum(F(m)*v for m,v in enumerate(p)),sum(ps))
            s=sum(ps);v2=sum(t*t for t in ps)
            for m in range(len(ps)+1):
                difference=abs(p[m]-thermal(s,m))
                self.assertLessEqual(difference,laguerre_constant(m)*v2);certified+=1
                # Independent scalar spectral integral (small degree, complete half-line).
                def fun(x):
                    return np.exp(-x)*eval_laguerre(m,x)*np.prod([1-float(t)*x for t in ps])
                val=quad(fun,0,np.inf,epsabs=2e-11,epsrel=2e-11,limit=150)[0]
                self.assertLess(abs(val-float(p[m])),5e-10)
        for s in (F(2,3),F(1)):
            for N in (4,16,64,128):
                for unequal in (False,True):
                    ps=[s*F(1,N)]*N if not unequal else [s*F(1,2*N)]*(N//2)+[s*F(3,2*N)]*(N//2)
                    p=number_distribution(ps)
                    self.assertEqual(sum(p),1);self.assertTrue(all(x>=0 for x in p))
                    v2=sum(t*t for t in ps);K=2
                    l1=2*exact_tv(ps)
                    bound=v2*sum(laguerre_constant(m) for m in range(K+1))+2*s/F(K+1)
                    self.assertLessEqual(l1,bound)
                    rows.append({'N':N,'s':str(s),'unequal':unequal,'P0':float(p[0]),
                        'P1':float(p[1]),'P_at_least_2':float(1-p[0]-p[1]),
                        'trace_distance_to_thermal':float(l1/2),'sum_p_squared':float(v2)})
        REPORT['thermal_controls']={'finite_exact_coefficient_bounds':certified,'rows':rows,
             'scope':'Complete finite distributions use rational arithmetic. Convergence is proved analytically, not fitted.'}

    def test_03_photon_number_does_not_certify_purification(self):
        rows=[]
        for N,eta in ((2,F(1,2)),(3,F(1)),(4,F(1)),(4,F(4,5))):
            U=tapped_fourier(N,float(eta));ideal=fock_state(U,[0]*N)
            ps=[eta/N]*N;pdist=number_distribution(ps)
            zero_reduced=number_distribution(ps[:-1])[0]
            coeff_all=eta*zero_reduced/pdist[1]
            vals={}
            for rule in ('all','phase'):
                p0=herald(ideal,N,rule);numerator=0.
                for i in range(N):
                    internal=[0]*N;internal[i]=1;err=fock_state(U,internal)
                    self.assertLess(abs(sum(abs(a)**2 for a in err.values())-1),3e-12)
                    numerator+=herald(err,N,rule,bad=True)
                c=numerator/p0
                self.assertLess(abs(p0-float(pdist[1])),3e-12)
                target=float(coeff_all) if rule=='all' else 1/N
                self.assertLess(abs(c-target),3e-12)
                vals[rule]={'p0':p0,'coefficient':c}
            rows.append({'N':N,'eta':str(eta),'p0_exact':str(pdist[1]),
                         'unfiltered_coefficient_exact':str(coeff_all),'values':vals})
        limit_rows=[]
        for N in (16,64,128):
            p=number_distribution([F(1,N)]*N)
            zero=number_distribution([F(1,N)]*(N-1))[0]
            limit_rows.append({'N':N,'p0':float(p[1]),'unfiltered_c':float(zero/p[1]),'Fourier_c':1/N})
        REPORT['selection_control']={'finite_Fock_rows':rows,'same_photon_number_limit':limit_rows,
            'message':'The ideal one-photon weight is the same with or without the Fourier character rule; only the latter purifies.'}

    def test_04_macroscopic_coupling_and_cost_identities(self):
        rows=[];a=F(1,2);lam=1-a
        # Limit for one macroscopic occupied coupling plus many weak ones.
        def derivative_tau(lam,m):
            if m==0:return -1/(1+lam)**2
            return (m*lam**(m-1)-lam**m)/(1+lam)**(m+2)
        limiting=[thermal(lam,m)+a*derivative_tau(lam,m) for m in range(6)]
        self.assertEqual(limiting[1],F(8,27))
        grouped=2*lam**2/(1+lam)**3
        self.assertEqual(grouped,F(4,27));self.assertLess(grouped,F(1,4))
        for n in (8,32,128):
            ps=[a]+[lam/n]*n;p=number_distribution(ps)
            self.assertEqual(sum(p),1);self.assertTrue(all(v>=0 for v in p))
            rows.append({'weak_inputs':n,'P1':float(p[1]),'P1_limit':float(limiting[1]),
                         'small_c_limiting_Q_upper':float(grouped)})
        rng=np.random.default_rng(7249);res=[]
        for N in (2,3,8,11):
            A=rng.normal(size=(5,N))+1j*rng.normal(size=(5,N))
            aa=A.sum(axis=1);p0=float(np.vdot(aa,aa).real)
            c=float(np.linalg.norm(A)**2/p0)
            error=abs(N*np.linalg.norm(A-aa[:,None]/N)**2/p0-(N*c-1))
            self.assertLess(error,1e-12);res.append(error)
        # For cost-target protocols, the exact identity bounds relative Cauchy error.
        for N,R in ((10,F(19,2)),(40,F(399,10)),(100,F(9999,100))):
            c=F(1,N)+(F(1,R)-F(1,N))/2
            self.assertGreaterEqual(N*c,1);self.assertLessEqual(N*c,N/R)
        REPORT['necessity_controls']={'heavy_rows':rows,'max_Cauchy_residual_error':max(res),
          'scope':'The heavy-row P1 is not a purification yield. Near-minimal cost forces N/R -> 1 and Nc -> 1 algebraically.'}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    if a.output.exists():ap.error('Refusing to overwrite report')
    r=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if r.wasSuccessful() else 'FAIL',test_groups=r.testsRun,
                  scope='Physical interpretation and fixed-scope consolidation. No finite-error or hardware claim.')
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with a.output.open('x') as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if r.wasSuccessful() else 1)
if __name__=='__main__':main()
