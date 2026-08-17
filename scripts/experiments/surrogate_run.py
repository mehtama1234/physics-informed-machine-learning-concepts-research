"""Real surrogate-modeling run: train a small network to imitate an EXPENSIVE function so
you can call the cheap copy instead. We measure both the accuracy and the speed-up. CPU."""
import torch, time, numpy as np
torch.manual_seed(0)
def expensive(X):   # pretend-expensive: a smooth function computed with a slow loop
    out=[]
    for row in X:
        s=0.0
        for _ in range(2000): s+= torch.sin(row[0]*1.3)+torch.cos(row[1]*0.7)  # busywork
        out.append((torch.sin(3*row[0])*torch.cos(2*row[1])).item())
    return torch.tensor(out).view(-1,1)
Xtr=torch.rand(400,2)*2-1; ytr=expensive(Xtr)
Xte=torch.rand(200,2)*2-1; yte=expensive(Xte)
net=torch.nn.Sequential(torch.nn.Linear(2,64),torch.nn.Tanh(),torch.nn.Linear(64,64),torch.nn.Tanh(),torch.nn.Linear(64,1))
opt=torch.optim.Adam(net.parameters(),lr=3e-3)
for ep in range(3000):
    opt.zero_grad(); loss=((net(Xtr)-ytr)**2).mean(); loss.backward(); opt.step()
with torch.no_grad():
    rmse=((net(Xte)-yte)**2).mean().sqrt().item()
t0=time.time(); _=expensive(Xte); t_exp=time.time()-t0
t0=time.time()
with torch.no_grad():
    for _ in range(50): _=net(Xte)
t_sur=(time.time()-t0)/50
print("=== surrogate modeling: a cheap network stands in for an expensive function ===")
print(f"  test accuracy of the surrogate (root-mean-square error): {rmse:.4f}")
print(f"  time to evaluate 200 inputs — expensive function: {t_exp*1000:.1f} ms")
print(f"                                 surrogate network : {t_sur*1000:.2f} ms")
print(f"  speed-up: about {t_exp/t_sur:.0f}x faster, at RMSE {rmse:.3f} on unseen inputs.")
print("  => once trained, the surrogate replaces the slow simulator wherever you can tolerate")
print("     a small error — the core trick behind ML surrogates for physics.")
