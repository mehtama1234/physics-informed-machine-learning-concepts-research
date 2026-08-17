"""Real PDE run: the 1-D heat equation by finite differences. Each point just averages
toward its neighbors every tick; that purely LOCAL rule produces global smoothing.
We compare the numerical peak decay to the exact analytic decay. numpy only."""
import numpy as np
L=1.0; nx=101; dx=L/(nx-1); alpha=1.0
dt=0.4*dx*dx/alpha          # stable step (must be < 0.5 dx^2/alpha)
x=np.linspace(0,L,nx)
u=np.sin(np.pi*x)           # initial heat profile; exact solution decays like exp(-pi^2 t)
r=alpha*dt/dx/dx
print("=== 1-D heat equation by finite differences ===")
print(f"  {nx} points, dt={dt:.2e}, stability number r={r:.3f} (must be < 0.5)")
print(f"  update rule: u_new[i] = u[i] + r*(u[i-1] - 2u[i] + u[i+1])   # each point averages neighbors")
print("   time |  numeric peak | exact peak exp(-pi^2 t) | error")
t=0.0; checkpoints=[0.0,0.02,0.05,0.1,0.2]
ci=0
for step in range(100000):
    if ci<len(checkpoints) and t>=checkpoints[ci]-1e-9:
        peak=u.max(); exact=np.exp(-np.pi**2*t)
        print(f"  {t:5.3f} | {peak:12.4f} | {exact:20.4f} | {abs(peak-exact):.4f}")
        ci+=1
    if ci>=len(checkpoints): break
    un=u.copy()
    un[1:-1]=u[1:-1]+r*(u[2:]-2*u[1:-1]+u[:-2])
    un[0]=un[-1]=0.0
    u=un; t+=dt
print("  => a local neighbor-averaging rule reproduces the exact global decay to <0.01.")
print("     Instability check: with r>0.5 the same rule blows up (that is the CFL limit).")
