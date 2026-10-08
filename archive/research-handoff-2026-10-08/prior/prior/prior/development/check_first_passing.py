#!/usr/bin/env python3
"""Checks for optimal first-order photon distillation and heralding yield.

Original analysis for an independent research pilot. No legacy scripts imported.
Run: python check_pilot.py --output evidence/new.json
Reports never overwrite an existing path. Numerical checks are not a global
optimality proof; all-resource optimal heralding remains unresolved for N>=4.
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
from pathlib import Path
import unittest
import numpy as np
import sympy as sp
from scipy.linalg import null_space
from scipy.optimize import brentq

REPORT = {}


def tapped_fourier(n: int, eta: float) -> np.ndarray:
    if n < 2 or not 0 <= eta <= 1:
        raise ValueError('Require n>=2 and 0<=eta<=1')
    idx = np.arange(n)
    F = np.exp(2j*np.pi*np.outer(idx,idx)/n)/np.sqrt(n)
    U = np.eye(n+1,dtype=complex)
    U[:n,:n] = F
    B = np.eye(n+1,dtype=complex)
    B[0,0] = B[n,n] = np.sqrt(eta)
    B[0,n] = np.sqrt(1-eta)
    B[n,0] = -np.sqrt(1-eta)
    return B@U


def creation_product(columns: list[np.ndarray]) -> dict[tuple[int,...],complex]:
    """Normalized-Fock coefficients of product of specified creation operators."""
    if not columns:
        raise ValueError('Need at least one vector')
    dim = len(columns[0])
    state = {(0,)*dim: 1.+0j}
    for col in columns:
        nxt = {}
        for occ,amp in state.items():
            for mode,c in enumerate(col):
                if abs(c)<1e-15:
                    continue
                key=list(occ); key[mode]+=1; key=tuple(key)
                nxt[key]=nxt.get(key,0j)+amp*c*np.sqrt(occ[mode]+1)
        state=nxt
    return state


def vectors(U: np.ndarray,n: int):
    """vi: good detector state if photon i is the sole bad retained photon."""
    dicts=[]
    for i in range(n):
        d=creation_product([U[1:,j] for j in range(n) if j!=i])
        dicts.append({k:U[0,i]*a for k,a in d.items()})
    keys=sorted(set().union(*(set(d) for d in dicts)))
    V=np.array([[d.get(k,0j) for d in dicts] for k in keys])
    return keys,V


def symmetric_patterns(keys,n):
    # Detector rows: Fourier characters 1,...,n-1 and the tap of character 0.
    return np.array([sum(j*occ[j-1] for j in range(1,n))%n==0 for occ in keys])


def elementary(ps):
    e=[1.]
    for p in ps:
        nxt=[0.]*(len(e)+1)
        for k,v in enumerate(e):
            nxt[k]+=v; nxt[k+1]+=p*v
        e=nxt
    return np.asarray(e)


def gram(ps):
    ps=np.asarray(ps,dtype=float); n=len(ps)
    if np.any(ps < -1e-12) or ps.sum()>1+1e-10:
        raise ValueError('Physical row intensities need p>=0, sum p<=1')
    def integ(xs,off=0):
        return sum((-1)**k*math.factorial(k+off)*x for k,x in enumerate(elementary(xs)))
    G=np.empty((n,n))
    for i in range(n):
        G[i,i]=ps[i]*integ(np.delete(ps,i))
        for j in range(i):
            G[i,j]=G[j,i]=-ps[i]*ps[j]*integ(np.delete(ps,[i,j]),1)
    return G


def relaxed_bound(G):
    """min z^*Gz subject to sum z=n, including singular cases."""
    n=len(G); vals,W=np.linalg.eigh((G+G.T.conj())/2)
    coeff=W.T.conj()@np.ones(n)
    small=vals<1e-11
    if np.sum(abs(coeff[small])**2)>1e-10:
        return 0.
    den=np.sum(abs(coeff[~small])**2/vals[~small])
    return float(n*n/den) if den>1e-14 else 0.


def success_poly(n):
    e=sp.symbols('eta',real=True)
    return sp.expand(sum((-1)**(k-1)*k*sp.factorial(k)*sp.binomial(n,k)*(e/n)**k
                         for k in range(1,n+1)))


def fock_mask(U,n,mask,common_bad=False,symmetry=True):
    """Full internal-mode calculation, not a single-error truncation."""
    labels=[(1 if common_bad else i+1) if mask>>i&1 else 0 for i in range(n)]
    d=max(labels)+1; modes=len(U)
    columns=[]
    for i,lab in enumerate(labels):
        col=np.zeros(modes*d,dtype=complex)
        col[lab::d]=U[:,i]
        columns.append(col)
    state=creation_product(columns)
    norm=0.; prob=0.; bad=0.
    for occ,amp in state.items():
        w=abs(amp)**2; norm+=w
        occ=np.asarray(occ).reshape(modes,d)
        totals=occ.sum(axis=1)
        herald=(totals[0]==1 and (not symmetry or sum(j*totals[j] for j in range(1,n))%n==0))
        if herald:
            prob+=w
            if occ[0,1:].sum()==1: bad+=w
    return float(norm),float(prob),float(bad)


def full_polynomials(n,eta,common_bad=False):
    U=tapped_fourier(n,eta); H=np.zeros(n+1); B=np.zeros(n+1)
    for mask in range(1<<n):
        norm,h,b=fock_mask(U,n,mask,common_bad)
        if abs(norm-1)>5e-12: raise ArithmeticError('Fock norm failure')
        H[mask.bit_count()]+=h; B[mask.bit_count()]+=b
    return H,B


def evaluate(H,B,epsilon):
    n=len(H)-1
    wt=np.array([epsilon**k*(1-epsilon)**(n-k) for k in range(n+1)])
    h=float(H@wt); err=float(B@wt/h)
    return {'epsilon':epsilon,'success':h,'conditional_error':err,'photons_per_success':n/h}


class Pilot(unittest.TestCase):
    def test_01_general_gram_and_equality(self):
        rng=np.random.default_rng(811); rows=[]
        for n,m in [(2,2),(2,4),(3,3),(3,5),(4,4),(4,6),(5,6)]:
            Q,_=np.linalg.qr(rng.normal(size=(m,m))+1j*rng.normal(size=(m,m)))
            keys,V=vectors(Q,n); G=gram(abs(Q[0,:n])**2)
            err=float(np.linalg.norm(V.T.conj()@V-G)); self.assertLess(err,2e-12)
            v=V.sum(axis=1); mask=rng.random(len(keys))>.4
            vP=v[mask]; VP=V[mask]
            p=float(np.vdot(vP,vP).real)
            numerator=float(np.linalg.norm(VP)**2)
            residual=float(np.linalg.norm(VP-vP[:,None]/n)**2)
            self.assertAlmostEqual(numerator-p/n,residual,places=12)
            self.assertGreaterEqual(numerator-p/n,-1e-12)
            W=V[:,:-1]-V[:,-1:]
            if np.linalg.norm(W)>1e-13:
                projection=v-W@np.linalg.lstsq(W,v,rcond=1e-11)[0]
            else: projection=v
            direct=float(np.vdot(projection,projection).real)
            hb=relaxed_bound(G)
            self.assertAlmostEqual(direct,hb,places=10)
            rows.append({'n':n,'modes':m,'gram_error':err,'relaxed_upper_bound':hb,
                         'independent_projection':direct,'cauchy_excess':residual})
        REPORT['gram_identity']=rows

    def test_02_balanced_constructive_saturation(self):
        rows=[]
        for n in range(2,7):
            for eta in (.5,.8,1.):
                U=tapped_fourier(n,eta)
                self.assertLess(np.linalg.norm(U.conj().T@U-np.eye(n+1)),3e-14)
                keys,V=vectors(U,n); mask=symmetric_patterns(keys,n)
                v=V.sum(axis=1); p=float(np.linalg.norm(v[mask])**2)
                err=float(np.linalg.norm(V[mask]-v[mask,None]/n))
                self.assertLess(err,4e-14)
                self.assertLess(np.linalg.norm(v[~mask]),4e-14)
                val=float(success_poly(n).subs('eta',eta)) if False else float(success_poly(n).subs({next(iter(success_poly(n).free_symbols)):eta}))
                self.assertAlmostEqual(p,val,places=11)
                self.assertAlmostEqual(relaxed_bound(gram(np.ones(n)*eta/n)),p,places=10)
                if p>1e-12:
                    self.assertAlmostEqual(np.linalg.norm(V[mask])**2/p,1/n,places=12)
                rows.append({'n':n,'eta':eta,'ideal_success':p,'equality_residual':err})
        REPORT['balanced_family']=rows

    def test_03_four_photon_exact_certificate(self):
        e=sp.symbols('eta',real=True); P=success_poly(4)
        self.assertEqual(sp.expand(P-(e-sp.Rational(3,2)*e**2+sp.Rational(9,8)*e**3-sp.Rational(3,8)*e**4)),0)
        self.assertEqual(P.subs(e,sp.Rational(4,5)),sp.Rational(164,625))
        self.assertEqual(P.subs(e,1),sp.Rational(1,4))
        dP=sp.lambdify(e,sp.diff(P,e),'numpy')
        opt=brentq(dP,0.,1.,xtol=1e-14)
        # P''=-(3/4)(6 eta^2-9 eta+4); negative by discriminant -15.
        self.assertEqual(sp.expand(sp.diff(P,e,2)+sp.Rational(3,4)*(6*e**2-9*e+4)),0)
        self.assertLess(9**2-4*6*4,0)
        U=tapped_fourier(4,.8)
        norm,p,b=fock_mask(U,4,0)
        self.assertAlmostEqual(norm,1.,places=12);self.assertAlmostEqual(p,164/625,places=12)
        self.assertEqual(b,0.)
        one=[fock_mask(U,4,1<<k)[2] for k in range(4)]
        self.assertAlmostEqual(sum(one)/p,.25,places=12)
        REPORT['four_photon']={'success_polynomial':str(P),'rational_setting':'4/5',
          'exact_ideal_success':'164/625','old_ideal_success':'1/4',
          'relative_success_improvement':float(sp.Rational(164,625)*4-1),
          'photons_per_success':float(sp.Rational(4)*625/164),
          'optimal_eta_within_tapped_family':float(opt),
          'optimal_success_within_tapped_family':float(P.subs(e,opt)),
          'first_order_error_coefficient':sum(one)/p,
          'scope':'Optimum only in the tapped Fourier family; global optical optimum unresolved.'}

    def test_04_exact_finite_error_counting(self):
        rows=[]; coefficient_records=[]
        for common in (False,True):
            for eta in (1.,.8):
                H,B=full_polynomials(4,eta,common)
                self.assertAlmostEqual(B[0],0.,places=12)
                self.assertAlmostEqual(B[1]/H[0],.25,places=12)
                if eta==1. and common:
                    # Appendix F of Saied et al., Fourier n=4 SBB formula.
                    self.assertLess(np.linalg.norm(H-np.array([1/4,1/4,1/2,1/4,1/4])),2e-12)
                    self.assertLess(np.linalg.norm(B-np.array([0,1/16,1/4,3/16,1/4])),2e-12)
                coefficient_records.append({'common_bad':common,'eta':eta,
                    'H_mask_sums':H.tolist(),'B_mask_sums':B.tolist()})
                for eps in (.001,.01,.05):
                    z=evaluate(H,B,eps);z.update(common_bad=common,eta=eta);rows.append(z)
        REPORT['finite_error']=rows
        REPORT['finite_error_polynomial_coefficients']=coefficient_records

    def test_05_hypotheses_and_small_case_bounds(self):
        # An identity device has unit yield but does not achieve epsilon/n suppression.
        n=3;U=np.eye(3,dtype=complex);keys,V=vectors(U,n);v=V.sum(axis=1)
        p=float(np.linalg.norm(v)**2);c=float(np.linalg.norm(V)**2/p)
        self.assertAlmostEqual(p,1.);self.assertAlmostEqual(c,1.)
        self.assertAlmostEqual(relaxed_bound(gram(np.array([1.,0.,0.]))),0.)
        # Ignoring the Fourier syndrome after the tap admits first-order bad outputs.
        U=tapped_fourier(4,.8); p=fock_mask(U,4,0,symmetry=False)[1]
        coef=sum(fock_mask(U,4,1<<i,symmetry=False)[2] for i in range(4))/p
        self.assertGreater(coef,.25+.01)
        # Exact universal relaxation at n=2, including any vacuum inputs.
        p1,p2=sp.symbols('p1 p2',positive=True)
        G=sp.Matrix([[p1*(1-p2),-p1*p2],[-p1*p2,p2*(1-p1)]])
        exact=sp.factor(4*G.det()/sum(G.adjugate()))
        self.assertEqual(sp.simplify(exact-4*p1*p2*(1-p1-p2)/(p1+p2)),0)
        # Fixed N=3 with NO vacuum coupling to the retained port: bound 9 p1 p2 p3 <= 1/3.
        a,b,c3=sp.symbols('a b c',positive=True)
        G3=sp.Matrix([[a*(1-b-c3+2*b*c3),-a*b*(1-2*c3),-a*c3*(1-2*b)],
                      [-a*b*(1-2*c3),b*(1-a-c3+2*a*c3),-b*c3*(1-2*a)],
                      [-a*c3*(1-2*b),-b*c3*(1-2*a),c3*(1-a-b+2*a*b)]])
        numerator=9*G3.det();den=sum(G3.adjugate())
        self.assertEqual(sp.factor((numerator-9*a*b*c3*den).subs(c3,1-a-b)),0)
        REPORT['controls']={'identity_yield':1.,'identity_error_coefficient':1.,
          'tap_without_symmetry_check_coefficient':coef,
          'two_photon_upper_bound':str(exact),
          'two_photon_global_success_upper_bound':.25,
          'three_photon_no_vacuum_row_success_upper_bound':1/3,
          'limitations':'No general global success optimum proved for N>=4; first order is at fixed N.'}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    if args.output.exists():ap.error('Refusing to overwrite report')
    res=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Pilot))
    REPORT.update(status='PASS' if res.wasSuccessful() else 'FAIL',tests_run=res.testsRun,
      scope='Ideal passive photon distillation with one retained port; no device or global-optimum claim.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if res.wasSuccessful() else 1)

if __name__=='__main__':main()
