"""Real operator-learning run (DeepONet): learn a whole OPERATOR — a map from an input
function to an output function — here the antiderivative (integration). Train on random
functions, then test on functions it never saw. CPU PyTorch."""
import torch, numpy as np
torch.manual_seed(0)
m=50; grid=torch.linspace(0,1,m)
def rand_funcs(n):
    # random smooth functions: sums of a few sines with random amplitudes
    a=torch.randn(n,4)*0.6; out=torch.zeros(n,m)
    for k in range(4): out+=a[:,k:k+1]*torch.sin((k+1)*np.pi*grid)
    return out
def antideriv(u):  # cumulative integral on the grid (trapezoid)
    dx=grid[1]-grid[0]; c=torch.cumsum((u[:,1:]+u[:,:-1])/2*dx,1)
    return torch.cat([torch.zeros(u.shape[0],1),c],1)
branch=torch.nn.Sequential(torch.nn.Linear(m,80),torch.nn.Tanh(),torch.nn.Linear(80,80))
trunk =torch.nn.Sequential(torch.nn.Linear(1,80),torch.nn.Tanh(),torch.nn.Linear(80,80),torch.nn.Tanh())
opt=torch.optim.Adam(list(branch.parameters())+list(trunk.parameters()),lr=2e-3)
U=rand_funcs(1000); G=antideriv(U); ycol=grid.view(-1,1)
def predict(u):   # DeepONet: dot(branch(u), trunk(y)) for each query y
    b=branch(u); t=trunk(ycol); return b@t.T
for ep in range(3000):
    opt.zero_grad(); loss=((predict(U)-G)**2).mean(); loss.backward(); opt.step()
Ut=rand_funcs(200); Gt=antideriv(Ut)
with torch.no_grad(): rmse=((predict(Ut)-Gt)**2).mean().sqrt().item()
print("=== operator learning (DeepONet): learn the integration operator ===")
print(f"  trained on 1000 random functions to map each function -> its running integral.")
print(f"  test error on 200 UNSEEN functions (root-mean-square): {rmse:.4f}")
print(f"  the network learned the OPERATION 'integrate', not one answer — so it integrates")
print(f"  functions it never saw. This map-a-function-to-a-function ability is what lets one")
print(f"  trained operator solve a whole family of PDEs at once.")
