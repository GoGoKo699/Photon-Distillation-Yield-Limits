#!/usr/bin/env python3
"""Checks of optimal-first-order distillation yield bounds.

Usage: python check_followup.py --output evidence/new.json
Refuses to overwrite reports. The general theorem is proved in FOLLOWUP.md;
finite checks do not prove its uniform asymptotics. Original pilot is unchanged.
"""
from __future__ import annotations
import argparse
import importlib.util
import itertools
import json
import math
from pathlib import Path
import unittest
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('preserved_pilot',ROOT/'prior/check_pilot.py')
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
REPORT={}
X=sp.Symbol('x')


def elementary(xs):
    e=[sp.Integer(1)]
    for x in xs:
        a=[sp.Integer(0)]*(len(e)+1)
        for k,c in enumerate(e): a[k]+=c; a[k+1]+=c*x
        e=a
    return e


def gram_exact(ps):
    n=len(ps)
    def integ(xs,offset=0):
        return sum((-1)**k*sp.factorial(k+offset)*e for k,e in enumerate(elementary(xs)))
    G=sp.zeros(n)
    for i in range(n):
        G[i,i]=ps[i]*integ([ps[k] for k in range(n) if k!=i])
        for j in range(i):
            G[i,j]=G[j,i]=-ps[i]*ps[j]*integ([ps[k] for k in range(n) if k not in (i,j)],1)
    return G


def integrate_polynomial(poly,rate=sp.Integer(1)):
    return sum(c*sp.factorial(k[0])/rate**(k[0]+1) for k,c in sp.Poly(sp.expand(poly),X).terms())


def grouped(ps,heavy):
    heavy=set(heavy)
    a=[ps[i] for i in range(len(ps)) if i in heavy]
    d=[ps[i] for i in range(len(ps)) if i not in heavy]
    lam=sum(d,sp.Integer(0)); omega=lam/(1+lam)
    f=sp.prod(1-p*X for p in a);g=sp.prod(1-p*X for p in d)
    fp=sp.diff(f,X);gp=sp.diff(g,X)
    Q=integrate_polynomial(-f*(gp+X*sp.diff(gp,X))-2*omega*X*fp*gp-omega**2*g*(fp+X*sp.diff(fp,X)))
    Qstar=lam/(1+lam)*integrate_polynomial(f,1+lam)
    z=sp.Matrix([omega if i in heavy else 1 for i in range(len(ps))])
    return Q,Qstar,z,lam,sum(p*p for p in d)


def P4(s): return s-sp.Rational(3,2)*s*s+sp.Rational(9,8)*s**3-sp.Rational(3,8)*s**4


def U4(ps):
    _,s,t,r,w=elementary(ps)
    return 16*w/r*(1-s+2*t-6*r)-16*w*w/(r*r)*(8-6*s)


def gram_bound_exact(ps):
    G=gram_exact(ps);o=sp.ones(len(ps),1)
    return sp.factor(len(ps)**2/(o.T*G.inv()*o)[0])


def product_derivatives(ps,x):
    """Independent product rule, with no division by a factor that may vanish."""
    g,gp,gpp=1.,0.,0.
    for p in ps:
        factor=1-p*x
        g,gp,gpp=g*factor,gp*factor-p*g,gpp*factor-2*p*gp
    return g,gp,gpp


class Checks(unittest.TestCase):
    def test_01_grouped_quadratic_and_physical_gram(self):
        cases=[([sp.Rational(1,3),sp.Rational(1,6),sp.Rational(1,12),sp.Rational(1,12)],{0}),
               ([sp.Rational(1,5)]*5,{0,1}),([sp.Rational(1,4)]*4,set()),
               ([sp.Rational(1,7)]*5,{0,2,4}),([sp.Rational(1,8)]*3,{0,1,2})]
        exact=[]
        for ps,A in cases:
            Q,Qstar,z,lam,v2=grouped(ps,A)
            self.assertEqual(sp.simplify((z.T*gram_exact(ps)*z)[0]-Q),0)
            self.assertGreaterEqual(Qstar,0)
            self.assertLessEqual(Qstar,sp.Rational(1,4))
            self.assertLessEqual(abs(Q-Qstar),96*v2)
            n=len(ps); beta=sp.Rational(n)/(n-len(A)+len(A)*lam/(1+lam))
            self.assertEqual(sum(beta*z),n)
            exact.append(dict(p=list(map(str,ps)),heavy=sorted(A),Q=str(Q),Qstar=str(Qstar),v2=str(v2)))
        rng=np.random.default_rng(6401);errors=[]
        for n in range(2,7):
            M=rng.normal(size=(n+1,n+1))+1j*rng.normal(size=(n+1,n+1))
            U,_=np.linalg.qr(M)
            _,V=old.vectors(U,n)
            err=float(np.max(abs(V.conj().T@V-old.gram(abs(U[0,:n])**2))))
            self.assertLess(err,2e-12);errors.append(err)
        REPORT['grouped_identity']={'exact_cases':exact,'physical_gram_errors':errors,'largest_optical_unitary':7}

    def test_02_global_product_bounds_and_constant(self):
        for y in np.r_[np.linspace(0,4,101),np.linspace(4,100,50)]:
            self.assertLessEqual(abs(1-y)*np.exp(-y/2),1+1e-14)
            rem=np.expm1(-y)+y
            self.assertGreaterEqual(rem,-1e-14)
            self.assertLessEqual(rem,y*y/2+1e-13)
        rng=np.random.default_rng(851);count=0;ratios=np.zeros(3)
        for n in (1,2,4,9,20):
            for rep in range(10):
                ps=rng.dirichlet(np.ones(n))*rng.uniform(.02,1.)
                lam=ps.sum();v2=np.dot(ps,ps)
                for x in np.r_[0.,np.geomspace(1e-5,80,45),1/ps.max()]:
                    g,gp,gpp=product_derivatives(ps,x)
                    target=np.exp(-lam*x)*np.array([1.,-lam,lam**2])
                    err=abs(np.array([g,gp,gpp])-target)
                    bd=v2*np.exp(lam*x/2)*np.array([x*x/2,x+lam*x*x/2,1+2*lam*x+lam*lam*x*x/2])
                    self.assertTrue(np.all(err<=bd+2e-13))
                    ratios=np.maximum(ratios,np.divide(err,bd,out=np.zeros(3),where=bd>1e-10))
                    count+=1
        # The numerical constant integrates the stated uniform polynomial envelope.
        integ=2*sp.factorial(1)*2**2+sp.Rational(5,2)*sp.factorial(2)*2**3+sp.Rational(1,2)*sp.factorial(3)*2**4
        self.assertEqual(integ,96)
        for lam in np.linspace(0,1,31):
            for sigma in np.linspace(0,1-lam,13):
                w=lam/(1+lam)
                self.assertLessEqual(2.5*lam+2*w*sigma+w*w*sigma/2,2.5+1e-14)
                self.assertLessEqual(.5*(lam+w*sigma)**2,.5+1e-14)
        REPORT['uniform_bounds']={'evaluations':count,'max_error_to_bound_ratios':ratios.tolist(),'integrated_constant':96,
                                  'scope':'Finite checks of inequalities whose all-x proofs are in FOLLOWUP.md.'}

    def test_03_no_click_probability_and_heavy_light_bound(self):
        examples=[]
        for ps,A in [([sp.Rational(3,5)]+[sp.Rational(1,10)]*4,{0}),
                     ([sp.Rational(1,3),sp.Rational(1,4)]+[sp.Rational(1,12)]*5,{0,1}),
                     ([sp.Rational(1,9)]*6,set())]:
            Q,Qstar,z,lam,v2=grouped(ps,A)
            a=[ps[i]/(1+lam) for i in sorted(A)]
            # Gaussian creation-mode norm equals the no-click probability.
            if a:
                vec=np.sqrt(np.array(list(map(float,a))))
                R=np.eye(len(a))-np.outer(vec,vec)
                eigen,W=np.linalg.eigh(R)
                C=(W*np.sqrt(np.maximum(eigen,0)))@W.T
                state=old.creation_product([C[:,i] for i in range(len(a))])
                p_no=sum(abs(amp)**2 for amp in state.values())
            else:p_no=1.
            integral=integrate_polynomial(sp.prod(1-p*X for p in a))
            self.assertAlmostEqual(p_no,float(integral),places=12)
            self.assertEqual(sp.simplify(Qstar-lam/(1+lam)**2*integral),0)
            self.assertGreaterEqual(integral,0);self.assertLessEqual(integral,1)
            examples.append(dict(no_click=float(integral),light_intensity=str(lam),Qstar=float(Qstar)))
        rng=np.random.default_rng(9751)
        max_tested=0.
        for n in range(3,13):
            for rep in range(6):
                ps=rng.dirichlet(np.full(n,.8))*rng.uniform(.2,1)
                delta=1/math.sqrt(n);A=np.flatnonzero(ps>delta)
                lam=ps[ps<=delta].sum();w=lam/(1+lam)
                beta=n/(n-len(A)+len(A)*w)
                z=np.full(n,beta);z[A]*=w
                G=old.gram(ps);trial=float(z@G@z)
                global_bound=(.25+96*delta)/(1-1/(n*delta))**2
                self.assertAlmostEqual(z.sum(),n,places=12)
                self.assertLessEqual(old.relaxed_bound(G),trial+2e-10)
                self.assertLessEqual(trial,global_bound)
                max_tested=max(max_tested,trial)
        # A missing coupling cannot meet equal-amplitude erasure with nonzero yield.
        G=old.gram([0.,.2,.2,.2]);self.assertEqual(old.relaxed_bound(G),0.)
        REPORT['heavy_light']={'no_click_controls':examples,'max_trial_in_diagnostics':max_tested,
                              'finite_bound':'(1/4+96*delta)/(1-1/(N*delta))^2; delta>1/N; may be capped at 1',
                              'caveat':'The conservative finite bound is not a tight finite-N estimate.'}

    def test_04_exact_four_photon_certificate(self):
        a,b,c,d,v=sp.symbols('a b c d v',nonnegative=True)
        qs=[a,a+b,a+b+c,a+b+c+d]
        _,S,T,R,W=elementary(qs);L=S+v
        poly=sp.Poly(sp.expand(R**2*(8*S*L**3-12*S**2*L**2+9*S**3*L-3*S**4)
                    -128*W*R*(L**3-S*L**2+2*T*L-6*R)+128*W**2*(8*L**2-6*S*L)),a,b,c,d,v)
        terms={tuple(t['powers']):sp.Integer(t['coefficient']) for t in json.loads((ROOT/'certificates/four_photon_positive.json').read_text())}
        self.assertEqual(dict(poly.terms()),terms)
        self.assertEqual(len(terms),613)
        self.assertTrue(all(k>=0 and k.is_Integer for k in terms.values()))
        self.assertTrue(all(sum(p)==10 for p in terms))
        self.assertEqual(sp.expand(poly.as_expr().subs({b:0,c:0,d:0})),0)
        # Check that the certificate is exactly the desired cleared-denominator gap.
        for vals in [(1,2,1,3,4),(2,0,3,1,0),(1,0,0,0,5)]:
            subs=dict(zip((a,b,c,d,v),vals));den=L.subs(subs)
            ps=[q.subs(subs)/den for q in qs];r=elementary(ps)[3]
            gap=8*den**10*r*r*(P4(sum(ps))-U4(ps))
            self.assertEqual(sp.factor(gap-poly.as_expr().subs(subs)),0)
            G=gram_exact(ps);recips=sp.Matrix([1/p for p in ps]);z=4*recips/sum(recips)
            self.assertEqual(sp.factor((z.T*G*z)[0]-U4(ps)),0)
        s=sp.Symbol('s',real=True)
        self.assertEqual(sp.expand(sp.diff(P4(s),s,2)+sp.Rational(3,4)*(6*s*s-9*s+4)),0)
        eta=brentq(lambda t:8-24*t+27*t*t-12*t**3,0,1,xtol=1e-14)
        prob=float(P4(eta))
        for e in (eta,.8):
            keys,V=old.vectors(old.tapped_fourier(4,e),4)
            A=V[old.symmetric_patterns(keys,4)];out=A.sum(axis=1)
            p=float(np.vdot(out,out).real);err=float(np.sum(abs(A)**2)/p)
            self.assertAlmostEqual(p,float(P4(e)),places=12)
            self.assertAlmostEqual(err,.25,places=12)
            self.assertLess(float(np.linalg.norm(A-out[:,None]/4)),2e-13)
        self.assertEqual(P4(sp.Rational(4,5)),sp.Rational(164,625))
        REPORT['four_photon']={'positive_monomials':len(terms),'minimum_coefficient':int(min(terms.values())),
                              'homogeneous_degree':10,'optimal_eta':eta,'optimal_success':prob,'photon_cost':4/prob,
                              'rational_success':'164/625 at eta=4/5','proof':'exact nonnegative polynomial plus physical Fourier/tap equality'}

    def test_05_balancing_counterexample_and_small_case_controls(self):
        ps=list(map(sp.Rational,['1/10','1/1000','2/5','2/5']))
        averaged=list(map(sp.Rational,['1/4','1/1000','2/5','1/4']))
        before=gram_bound_exact(ps);after=gram_bound_exact(averaged)
        self.assertEqual(sum(ps),sum(averaged));self.assertGreater(before,after)
        rng=np.random.default_rng(1573);slacks=[]
        for rep in range(160):
            ps=rng.dirichlet(np.ones(4))*rng.uniform(.05,1.)
            B=old.relaxed_bound(old.gram(ps));upper=float(U4(list(map(sp.Float,ps))))
            self.assertLessEqual(B,upper+5e-11)
            self.assertLessEqual(upper,float(P4(ps.sum()))+5e-11)
            slacks.append(float(P4(ps.sum()))-B)
        REPORT['balancing']={'before_exact':str(before),'after_exact':str(after),'positive_difference':str(sp.factor(before-after)),
                             'before':float(before),'after':float(after),'minimum_random_four_photon_gap':min(slacks),
                             'conclusion':'Schur-concavity is false already at N=4; balanced global N=4 optimum follows from the separate certificate.'}

    def test_06_known_achieving_sequence_and_coherent_control(self):
        vals=[]
        for n in (2,3,4,5,10,30,100,300,1000):
            def integrand(x):
                return math.exp(-x)*x*(1-x/n)**(n-1)
            # For large n the omitted tail from x>=n is explicitly bounded.
            cutoff=min(n,120.)
            value=quad(integrand,0,cutoff,epsabs=3e-13,epsrel=3e-13,limit=200)[0]
            if n<120:
                value+=quad(integrand,n,120,epsabs=3e-13,epsrel=3e-13,limit=200)[0]
            tail_bound=(2*120+4)*math.exp(-120/2)
            self.assertLess(tail_bound,3e-24)
            if n<=10:self.assertAlmostEqual(value,float(old.success_poly(n).subs({'eta':1})),places=11)
            vals.append(dict(N=n,Fourier_success=value,photons_per_output=n/value))
        self.assertLess(abs(vals[-1]['Fourier_success']-.25),.0001)
        # Ordinary single-photon routing gives unit success, but no purification.
        _,V=old.vectors(np.eye(5,dtype=complex),4)
        out=V.sum(axis=1);p=float(np.vdot(out,out).real);coef=float(np.sum(abs(V)**2)/p)
        self.assertEqual(p,1.);self.assertEqual(coef,1.)
        REPORT['achievability']={'known_Fourier_sequence':vals,'integral_tail_bound':tail_bound,
                               'routing_control':dict(success=p,error_coefficient=coef),
                               'credit':'The balanced-family 1/4 limit is inherited from Saied et al., Theorem III.5; the new result is the all-network converse.',
                               'limit_order':'epsilon -> 0 at each fixed N, then N -> infinity; not fixed-epsilon performance.'}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    if args.output.exists():ap.error('Refusing to overwrite report')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',tests_run=result.testsRun,
                  boundary='Author-side analytical proof; no repository operations; no generic finite-N>=5 optimum or finite-error guarantee.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)

if __name__=='__main__':main()
