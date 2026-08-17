"""Real uncertainty run: train an ENSEMBLE of networks on the same data. Where there is
data they agree; away from the data they disagree — and that disagreement is a usable
'I don't know' signal. CPU PyTorch."""
import torch, numpy as np
torch.manual_seed(0)
# data only in [-2,-0.5] and [0.5,2]; a GAP in the middle and nothing outside +-2
xl=torch.linspace(-2,-0.5,40); xr=torch.linspace(0.5,2,40)
xtr=torch.cat([xl,xr]).view(-1,1); ytr=torch.sin(2*xtr)+0.05*torch.randn_like(xtr)
def train_one(seed):
    torch.manual_seed(seed)
    n=torch.nn.Sequential(torch.nn.Linear(1,64),torch.nn.Tanh(),torch.nn.Linear(64,64),torch.nn.Tanh(),torch.nn.Linear(64,1))
    o=torch.optim.Adam(n.parameters(),lr=5e-3)
    for _ in range(2000): o.zero_grad(); (((n(xtr)-ytr)**2).mean()).backward(); o.step()
    return n
ens=[train_one(s) for s in range(8)]
def spread(x):
    with torch.no_grad():
        P=torch.stack([n(x) for n in ens],0)   # 8 predictions
        return P.std(0).mean().item()
print("=== deep-ensemble uncertainty: disagreement grows where there is no data ===")
regions={
 'inside the left data band (-1.5)': torch.tensor([[-1.5]]),
 'inside the right data band (1.2)': torch.tensor([[1.2]]),
 'in the GAP with no data (0.0)':    torch.tensor([[0.0]]),
 'far outside all data (4.0)':       torch.tensor([[4.0]]),
}
print("  region | ensemble disagreement (std of 8 nets)")
for name,x in regions.items(): print(f"  {name:34s} | {spread(x):.4f}")
print("  => the 8 nets agree tightly where they saw data and fan out in the gap and outside it.")
print("     That spread is a free, honest 'here be dragons' flag — the basis of ML uncertainty.")
