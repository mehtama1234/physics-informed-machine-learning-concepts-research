"""Real generative-modeling run: a tiny denoising diffusion model on a 2-D 'two moons'
shape. It learns to turn pure noise into samples that land on the shape. We measure how
well generated points cover the real data. CPU PyTorch."""
import torch, numpy as np
torch.manual_seed(0); rng=np.random.default_rng(0)
def two_moons(n):
    t=rng.random(n)*np.pi
    a=np.stack([np.cos(t),np.sin(t)],1); b=np.stack([1-np.cos(t),1-np.sin(t)-0.5],1)
    X=np.where((rng.random((n,1))<0.5),a,b)+rng.standard_normal((n,2))*0.06
    return torch.tensor(X,dtype=torch.float32)
data=two_moons(2000)
Tn=40; betas=torch.linspace(1e-3,0.15,Tn); alpha=torch.cumprod(1-betas,0)
net=torch.nn.Sequential(torch.nn.Linear(3,128),torch.nn.SiLU(),torch.nn.Linear(128,128),torch.nn.SiLU(),torch.nn.Linear(128,2))
opt=torch.optim.Adam(net.parameters(),lr=2e-3)
for ep in range(4000):
    i=torch.randint(0,Tn,(len(data),)); ab=alpha[i].view(-1,1)
    noise=torch.randn_like(data); xt=ab.sqrt()*data+(1-ab).sqrt()*noise
    inp=torch.cat([xt,(i.float()/Tn).view(-1,1)],1)
    opt.zero_grad(); loss=((net(inp)-noise)**2).mean(); loss.backward(); opt.step()
@torch.no_grad()
def sample(n):
    x=torch.randn(n,2)
    for t in range(Tn-1,-1,-1):
        ab=alpha[t]; b=betas[t]
        eps=net(torch.cat([x,torch.full((n,1),t/Tn)],1))
        mean=(x-(b/ (1-ab).sqrt())*eps)/ (1-b).sqrt()
        x=mean+(b.sqrt()*torch.randn_like(x) if t>0 else 0)
    return x
gen=sample(2000)
# coverage: fraction of generated points within 0.15 of some real point
d=torch.cdist(gen,data); near=(d.min(1).values<0.15).float().mean().item()
realstd=data.std(0); genstd=gen.std(0)
print("=== diffusion model: turn noise into 'two moons' samples ===")
print(f"  fraction of generated points landing ON the shape (within 0.15 of real data): {near*100:.0f}%")
print(f"  spread of real data: [{realstd[0]:.2f}, {realstd[1]:.2f}]  vs generated: [{genstd[0]:.2f}, {genstd[1]:.2f}]")
print("  => trained only to remove a little noise at each level, the model composes those steps")
print("     to build brand-new samples that match the data shape — starting from pure noise.")
