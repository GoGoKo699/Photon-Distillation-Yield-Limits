#!/usr/bin/env python3
"""Focused distillation-yield audit and stability corollary.

Run: python check_review.py --output evidence/new.json
Never overwrites reports. All claims are analytical; finite checks are diagnostics.
The preceding scientific files are imported without modification.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, itertools, json, math, sys, unittest
from pathlib import Path
sys.dont_write_bytecode = True
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("prior_yield",ROOT/"prior/check_followup.py")
prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
old=prior.old
REPORT={}

def occupations(total, modes):
    if modes==1:
        yield (total,);return
    for i in range(total+1):
        for rest in occupations(total-i,modes-1):
            yield (i,)+rest

def permanent_direct(A):
    n=len(A)
    return sum(np.prod(A[np.arange(n),perm]) for perm in itertools.permutations(range(n)))

def vectors_by_permanents(U,n):
    """Independent repeated-row permanent computation in normalized Fock basis."""
    keys=list(occupations(n-1,len(U)-1))
    out=np.zeros((len(keys),n),complex)
    for r,occ in enumerate(keys):
        rows=np.repeat(np.arange(1,len(U)),occ)
        scale=math.sqrt(math.prod(math.factorial(k) for k in occ))
        for i in range(n):
            columns=[j for j in range(n) if j!=i]
            out[r,i]=U[0,i]*permanent_direct(U[np.ix_(rows,columns)])/scale
    return keys,out

def band_data(p,delta):
    p=np.asarray(p,float)
    mask=p>delta;m=int(mask.sum())
    lam=float(p[~mask].sum());omega=lam/(1+lam)
    t=np.ones(len(p));t[mask]=omega
    return mask,m,lam,omega,t

def product2(ps,x):
    f,df,ddf=1.,0.,0.
    for p in ps:
        f,df,ddf=f*(1-p*x),df*(1-p*x)-p*f,ddf*(1-p*x)-2*p*df
    return f,df,ddf

def grouped_repeated(heavy,lam,nlight):
    """Quadrature for arbitrary fixed heavy set and nlight equal light factors."""
    sig=sum(heavy);om=lam/(1+lam);p=lam/nlight
    def fun(x,limit=False):
        f,fp,fpp=product2(heavy,x)
        if limit:
            g=np.exp(-lam*x);gp=-lam*g;gpp=lam*lam*g
        else:
            v=1-p*x
            g=v**nlight;gp=-nlight*p*v**(nlight-1)
            gpp=nlight*(nlight-1)*p*p*v**(nlight-2) if nlight>1 else 0.
        return np.exp(-x)*(-f*(gp+x*gpp)-2*om*x*fp*gp-om*om*g*(fp+x*fpp))
    # Direct full-range quadrature segmented before the negligible tail.
    Q=sum(quad(fun,a,b,epsabs=2e-12,epsrel=2e-12,limit=150)[0]
          for a,b in ((0,1),(1,10),(10,40),(40,160)))
    Qstar=sum(quad(lambda x:fun(x,True),a,b,epsabs=2e-12,epsrel=2e-12,limit=150)[0]
          for a,b in ((0,1),(1,10),(10,40),(40,160)))
    return Q,Qstar

# Independent exact integer multivariate polynomial implementation.
ZERO=(0,)*5
def const(c): return {} if c==0 else {ZERO:int(c)}
def var(i):
    e=list(ZERO);e[i]=1;return {tuple(e):1}
def add(*polys):
    d={}
    for p in polys:
        for e,c in p.items():d[e]=d.get(e,0)+c
    return {e:c for e,c in d.items() if c}
def scale(p,c):return {e:c*v for e,v in p.items() if c*v}
def mul(p,q):
    d={}
    for e,c in p.items():
        for f,v in q.items():
            k=tuple(a+b for a,b in zip(e,f));d[k]=d.get(k,0)+c*v
    return {e:c for e,c in d.items() if c}
def power(p,n):
    out=const(1)
    for _ in range(n):out=mul(out,p)
    return out
def sym(qs,k):
    out={}
    for subset in itertools.combinations(qs,k):
        a=const(1)
        for q in subset:a=mul(a,q)
        out=add(out,a)
    return out

def integer_certificate():
    a,b,c,d,v=[var(i) for i in range(5)]
    qs=[a,add(a,b),add(a,b,c),add(a,b,c,d)]
    S,T,R,W=[sym(qs,k) for k in (1,2,3,4)];La=add(S,v)
    first=mul(power(R,2),add(scale(mul(S,power(La,3)),8),
          scale(mul(power(S,2),power(La,2)),-12),
          scale(mul(power(S,3),La),9),scale(power(S,4),-3)))
    second=scale(mul(mul(W,R),add(power(La,3),
          scale(mul(S,power(La,2)),-1),scale(mul(T,La),2),scale(R,-6))),-128)
    third=scale(mul(power(W,2),add(scale(power(La,2),8),scale(mul(S,La),-6))),128)
    return add(first,second,third)

class Review(unittest.TestCase):
    def test_01_physical_amplitudes_and_arbitrary_acceptance(self):
        rng=np.random.default_rng(28311);errors=[];slacks=[];cases=0
        for n in (2,3,4,5):
            modes=n+1
            U,_=np.linalg.qr(rng.normal(size=(modes,modes))+1j*rng.normal(size=(modes,modes)))
            keys,V=vectors_by_permanents(U,n)
            ok,OV=old.vectors(U,n);lookup={k:OV[j] for j,k in enumerate(ok)}
            err=max(np.max(abs(V[j]-lookup.get(k,np.zeros(n)))) for j,k in enumerate(keys))
            self.assertLess(err,3e-13);errors.append(float(err))
            p=np.abs(U[0,:n])**2
            self.assertLess(np.max(abs(V.conj().T@V-old.gram(p))),2e-12)
            for repeat in range(8):
                accept=rng.random(len(keys))>.35;A=V[accept]
                w=A.sum(axis=1);p0=float(np.vdot(w,w).real)
                if p0<1e-13:continue
                coef=float(np.linalg.norm(A)**2/p0)
                err2=np.linalg.norm(A-w[:,None]/n)**2
                self.assertAlmostEqual((coef-1/n)*p0,float(err2),places=12)
                for delta in (.1,.25,.5):
                    H,m,lam,om,z=band_data(p,delta)
                    Q=float(np.linalg.norm(V@z)**2)
                    lower=p0*max(0.,1-(1-om)*math.sqrt(m*coef))**2
                    self.assertLessEqual(lower,Q+2e-12)
                    # Full underlying triangle bound, before coefficient relaxation.
                    heavy=A[:,H].sum(axis=1) if m else np.zeros(len(w),complex)
                    self.assertLessEqual(max(0.,math.sqrt(p0)-(1-om)*np.linalg.norm(heavy)),
                                         np.linalg.norm(A@z)+2e-12)
                    slacks.append(Q-lower);cases+=1
        REPORT["physical"]={"independent_permanent_max_errors":errors,"triangle_cases":cases,
            "minimum_squared_bound_slack":min(slacks),"largest_optical_unitary":6,
            "largest_permanent_size":4}

    def test_02_near_optimal_coherent_relaxation(self):
        rows=[]
        for ps in ([.4,.1,.1,.1,.1,.1,.1],[.45,.13,.12,.1,.08],[.5,.1,.1,.1,.1]):
            G=old.gram(ps);val,U=np.linalg.eigh(G)
            self.assertGreater(val.min(),0)
            V=(U*np.sqrt(val))@U.T
            n=len(ps);ones=np.ones(n);v=V@ones
            W=V[:,:-1]-V[:,-1:]
            res=v-W@np.linalg.lstsq(W,v,rcond=None)[0]
            e=res/np.linalg.norm(res)
            h=W[:,0]-e*np.dot(e,W[:,0]);h/=np.linalg.norm(h)
            for angle in (0.,.001,.02,.15):
                a=(np.cos(angle)*e+np.sin(angle)*h)@V
                p0=float(a.sum()**2);coef=float(np.dot(a,a)/p0)
                self.assertGreaterEqual(coef,1/n-3e-13)
                if angle==0:self.assertAlmostEqual(coef,1/n,places=11)
                H,m,lam,om,z0=band_data(ps,.25)
                Q=float(z0@G@z0)
                self.assertLessEqual(p0*max(0.,1-(1-om)*np.sqrt(m*coef))**2,Q+2e-12)
                # Equality-defect-sensitive version recovers the older exact constraint.
                beta=n/z0.sum();z=beta*z0
                defect=max(0.,coef-1/n);e_norm=np.linalg.norm(z-1)
                self.assertLessEqual(p0*max(0.,1-e_norm*np.sqrt(defect))**2,
                                     float(z@G@z)+3e-12)
                rows.append({"N":n,"angle":angle,"success":p0,"coefficient":coef,
                             "exact_optimal_coefficient":1/n,"heavy_inputs":m})
        REPORT["relaxed_detector_controls"]={"rows":rows,
             "scope":"Arbitrary coherent detector projectors test an upper-bound relaxation, not new optical implementations."}

    def test_03_uniform_grouping_and_architecture_limits(self):
        rows=[]
        for a in (0.,.2,.5,.8):
            lam=1-a;heavy=[] if a==0 else [a]
            for nlight in (8,32,128,512):
                Q,Qstar=grouped_repeated(heavy,lam,nlight)
                expected=.25 if a==0 else 2*lam*lam/(1+lam)**3
                self.assertAlmostEqual(Qstar,expected,places=11)
                self.assertLessEqual(abs(Q-Qstar),96*lam*lam/nlight+2e-12)
                self.assertLessEqual(Qstar,lam/(1+lam)**2+2e-12)
                rows.append({"heavy_intensity":a,"light_count":nlight,"Q":Q,
                    "Q_limit":Qstar,"mean_one_photon_bound":lam/(1+lam)**2})
        # Algebraically: a nonzero macroscopic survivor coupling leaves a strict gap.
        import sympy as sp
        a=sp.Symbol("a",real=True)
        self.assertEqual(sp.factor(sp.Rational(1,4)-(1-a)/(2-a)**2-a*a/(4*(2-a)**2)),0)
        # Coarse all-protocol bound evaluated by exact arithmetic for c=a^3.
        vals=[]
        for reciprocal in (1000,10000,100000):
            e=sp.Rational(1,reciprocal);coef=e**3;delta=e
            bound=(sp.Rational(1,4)+96*delta)/(1-sp.sqrt(coef/delta))**2
            self.assertEqual(sp.sqrt(coef/delta),e)
            vals.append({"coefficient":str(coef),"delta":str(delta),"coarse_upper_bound":float(bound)})
        REPORT["uniform_audit"]={"rows":rows,"bound_examples":vals,
           "note":"Constants are conservative; asymptotic proof is not inferred from the finite rows."}

    def test_04_independent_integer_certificate_and_uniqueness(self):
        poly=integer_certificate()
        stored={tuple(t["powers"]):int(t["coefficient"]) for t in
                json.loads((ROOT/"prior/certificates/four_photon_positive.json").read_text())}
        self.assertEqual(poly,stored)
        self.assertEqual(len(poly),613)
        self.assertTrue(all(c>0 for c in poly.values()))
        self.assertTrue(all(sum(e)==10 for e in poly))
        # These monomials prove strictness for a positive minimum p_i and any imbalance.
        for monomial,expected in { (6,4,0,0,0):480, (6,0,4,0,0):512, (6,0,0,4,0):480}.items():
            self.assertEqual(poly[monomial],expected)
        import sympy as sp
        x=sp.Symbol("x")
        polynomial=8-24*x+27*x*x-12*x**3
        lo=sp.Rational(783216061320573254247041,1000000000000000000000000)
        hi=sp.Rational(783216061320573254247042,1000000000000000000000000)
        self.assertGreater(polynomial.subs(x,lo),0)
        self.assertLess(polynomial.subs(x,hi),0)
        # P4' strictly decreases; uniqueness of its zero was proved in prior text.
        eta=brentq(lambda x:8-24*x+27*x*x-12*x**3,0,1,xtol=1e-14)
        REPORT["four_photon_certificate"]={"terms":len(poly),"minimum_coefficient":min(poly.values()),
             "homogeneous_degree":10,"strictness_monomials":["480 a^6 b^4","512 a^6 c^4","480 a^6 d^4"],
             "eta_bracket_exact":[str(lo),str(hi)],"eta":eta,"success":float(prior.P4(eta)),
             "interpretation":"The optimal survivor intensity row is unique up to permutations; the full interferometer need not be."}

    def test_05_physical_attainment_with_suboptimal_coefficient(self):
        rows=[]
        # Embed an m-photon purifier and route N-m other photons to dedicated detectors.
        # This is still one fixed passive unitary and one predetermined survivor.
        for active,total in ((2,4),(3,6),(4,7)):
            for eta in (.8,):
                small=old.tapped_fourier(active,eta)
                M=total+1;U=np.zeros((M,M),complex)
                # input total is the extra vacuum; keep occupied inputs 0..total-1.
                mapping=list(range(active))+[total]
                U[np.ix_(mapping,mapping)]=small
                for i in range(active,total):U[i,i]=1
                keys,V=old.vectors(U,total)
                good=np.array([all(occ[j-1]==1 for j in range(active,total)) and
                   sum(j*occ[j-1] for j in range(1,active))%active==0 for occ in keys])
                a=V[good].sum(axis=1);p0=float(np.vdot(a,a).real)
                coef=float(np.linalg.norm(V[good])**2/p0)
                expected=float(old.success_poly(active).subs(next(iter(old.success_poly(active).free_symbols)),eta))
                self.assertAlmostEqual(p0,expected,places=12)
                self.assertAlmostEqual(coef,1/active,places=12)
                self.assertGreater(coef,1/total)
                rows.append({"inputs":total,"active_inputs":active,"eta":eta,
                             "p0":p0,"coefficient":coef,"best_coefficient_at_total":1/total})
        # Fourier/tap ideal one-photon probabilities converge to eta/(1+eta)^2.
        limits=[]
        for eta in (.3,.7,1.):
            for n in (32,128,512):
                def fun(t):return eta*np.exp(-t)*t*(1-eta*t/n)**(n-1)
                p=quad(fun,0,120,epsabs=3e-13,epsrel=3e-13,limit=180)[0]
                lim=eta/(1+eta)**2
                if n==512:self.assertLess(abs(p-lim),.001)
                limits.append({"N":n,"eta":eta,"success":p,"known_limit":lim})
        REPORT["attainment"]={"embedded_protocols":rows,"Fourier_tap_limits":limits,
            "scope":"Sharpness uses known Fourier purification; suboptimal coefficient examples do not claim finite-error guarantees."}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()
    if args.output.exists():ap.error("Refusing to overwrite a report.")
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Review))
    REPORT.update(status="PASS" if result.wasSuccessful() else "FAIL",tests_run=result.testsRun,
       scope="Author-side proof audit; finite diagnostics do not establish asymptotic uniformity.")
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open("x") as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write("\n")
    raise SystemExit(0 if result.wasSuccessful() else 1)
if __name__=="__main__":main()
