"""Real deep-learning run: why a hidden layer matters. A straight-line (linear) model cannot
bend to a curved target; one hidden layer of nonlinear units can. numpy/torch, tiny."""
import torch
torch.manual_seed(0)
x=torch.linspace(-3,3,300).view(-1,1); y=torch.sin(1.5*x)+0.3*x  # curved target
def fit(model,steps=3000):
    o=torch.optim.Adam(model.parameters(),lr=1e-2)
    for _ in range(steps): o.zero_grad(); (((model(x)-y)**2).mean()).backward(); o.step()
    with torch.no_grad(): return ((model(x)-y)**2).mean().sqrt().item()
lin=torch.nn.Linear(1,1)
net=torch.nn.Sequential(torch.nn.Linear(1,64),torch.nn.Tanh(),torch.nn.Linear(64,1))
big=torch.nn.Sequential(torch.nn.Linear(1,64),torch.nn.Tanh(),torch.nn.Linear(64,64),torch.nn.Tanh(),torch.nn.Linear(64,1))
rl,rn,rb=fit(lin),fit(net),fit(big)
print("=== deep learning: a hidden layer lets a model bend ===")
print(f"  target is a curved function y = sin(1.5x) + 0.3x")
print(f"  straight-line (linear) model      -- error {rl:.3f}  (can only draw a line)")
print(f"  one hidden layer (64 units)       -- error {rn:.3f}")
print(f"  two hidden layers (64+64 units)   -- error {rb:.3f}")
print(f"  => the linear model is stuck; adding a layer of simple nonlinear units lets the")
print(f"     network approximate the curve — stacking such layers is what 'deep' learning is.")
