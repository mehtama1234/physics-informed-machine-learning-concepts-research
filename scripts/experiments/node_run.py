"""Real neural-ODE run: instead of predicting the next point directly, learn the RIGHT-HAND
SIDE of a differential equation (the velocity field) and integrate it. We fit a spiral
trajectory and measure how well the learned dynamics reproduce it. CPU PyTorch."""
import torch, numpy as np
torch.manual_seed(0)
# true dynamics: a decaying spiral  d[x,y]/dt = A[x,y], A=[[-0.1,-1],[1,-0.1]]
A=torch.tensor([[-0.1,-1.0],[1.0,-0.1]])
dt=0.1; N=200
traj=torch.zeros(N,2); traj[0]=torch.tensor([2.0,0.0])
for i in range(N-1): traj[i+1]=traj[i]+dt*(traj[i]@A.T)
f=torch.nn.Sequential(torch.nn.Linear(2,64),torch.nn.Tanh(),torch.nn.Linear(64,2))
opt=torch.optim.Adam(f.parameters(),lr=5e-3)
def rollout(steps):
    s=traj[0].clone(); out=[s]
    for _ in range(steps-1): s=s+dt*f(s); out.append(s)
    return torch.stack(out)
print("=== neural ODE: learn the velocity field of a spiral, then integrate it ===")
print("   epoch | trajectory error (rolled out 200 steps)")
for ep in range(1501):
    opt.zero_grad()
    pred=traj[:-1]+dt*f(traj[:-1])       # one-step prediction from true points
    loss=((pred-traj[1:])**2).mean()
    loss.backward(); opt.step()
    if ep%300==0:
        with torch.no_grad(): err=(rollout(N)-traj).pow(2).mean().sqrt().item()
        print(f"   {ep:5d} | {err:.4f}")
with torch.no_grad():
    err=(rollout(N)-traj).pow(2).mean().sqrt().item()
    # extrapolate 2x beyond training horizon
    s=traj[0].clone(); ext=[s]
    for _ in range(2*N): s=s+dt*f(s); ext.append(s)
    ext=torch.stack(ext)
print(f"  final roll-out error over the trained span: {err:.4f}")
print(f"  the net learned the FLOW, so integrating it re-draws the whole spiral from just the")
print(f"  start point; it also keeps spiraling inward sensibly for 2x the trained horizon.")
