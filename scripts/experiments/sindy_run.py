"""Real symbolic-regression run (SINDy): recover the Lorenz equations from trajectory data
alone. Build a library of candidate terms, then sparse regression keeps only the few that
matter. We compare recovered coefficients to the true ones. numpy only."""
import numpy as np
np.random.seed(0)
sig,rho,beta=10.0,28.0,8/3
def lorenz(s): x,y,z=s; return np.array([sig*(y-x), x*(rho-z)-y, x*y-beta*z])
dt=0.002; T=5000; S=np.zeros((T,3)); S[0]=[-8,7,27]
for i in range(T-1): S[i+1]=S[i]+dt*lorenz(S[i])
X=S[:-1]; dX=(S[1:]-S[:-1])/dt          # measured states and their time-derivatives
x,y,z=X[:,0],X[:,1],X[:,2]
names=['1','x','y','z','xx','xy','xz','yy','yz','zz']
Theta=np.stack([np.ones_like(x),x,y,z,x*x,x*y,x*z,y*y,y*z,z*z],1)
def stlsq(Theta,d,thr=0.1,iters=10):
    xi=np.linalg.lstsq(Theta,d,rcond=None)[0]
    for _ in range(iters):
        small=np.abs(xi)<thr; xi[small]=0
        big=~small
        if big.any(): xi[big]=np.linalg.lstsq(Theta[:,big],d,rcond=None)[0]
    return xi
print("=== SINDy: recover Lorenz from data (no equations given, just the trajectory) ===")
truth={'dx/dt':{'x':-sig,'y':sig},'dy/dt':{'x':rho,'y':-1,'xz':-1},'dz/dt':{'z':-beta,'xy':1}}
for j,eq in enumerate(['dx/dt','dy/dt','dz/dt']):
    xi=stlsq(Theta,dX[:,j])
    terms={names[i]:float(round(xi[i],3)) for i in range(len(names)) if abs(xi[i])>1e-6}
    print(f"  {eq}: recovered {terms}")
    print(f"         true      {truth[eq]}")
print("  => from a single noisy-free trajectory, sparse regression recovers all 3 Lorenz")
print("     equations and their coefficients (sigma=10, rho=28, beta=2.667) to ~3 decimals,")
print("     while zeroing out every one of the spurious library terms.")
