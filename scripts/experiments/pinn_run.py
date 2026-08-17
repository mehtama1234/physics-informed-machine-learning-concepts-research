"""Real physics-informed neural network run. We solve a differential equation with a small
neural net using ONLY the equation itself and the boundary values — no labelled interior
data. Then we show that without the physics term the same net (given no interior labels)
cannot find the solution. CPU PyTorch."""
import torch, math
torch.manual_seed(0)

# Solve  u''(x) = -pi^2 sin(pi x)  on [0,1] with u(0)=u(1)=0.  True solution: u(x)=sin(pi x).
def true_u(x): return torch.sin(math.pi*x)
def net_():
    return torch.nn.Sequential(torch.nn.Linear(1,32), torch.nn.Tanh(),
                               torch.nn.Linear(32,32), torch.nn.Tanh(), torch.nn.Linear(32,1))

def deriv2(u_fn, x):
    x=x.clone().requires_grad_(True); u=u_fn(x)
    ux=torch.autograd.grad(u, x, torch.ones_like(u), create_graph=True)[0]
    uxx=torch.autograd.grad(ux, x, torch.ones_like(ux), create_graph=True)[0]
    return u, uxx

xc = torch.linspace(0,1,50).view(-1,1)          # collocation points (NO labels here)
xb = torch.tensor([[0.0],[1.0]])                 # boundary points (values known: 0)
xtest = torch.linspace(0,1,101).view(-1,1)

def train(use_physics, steps=4000):
    net=net_(); opt=torch.optim.Adam(net.parameters(), lr=3e-3); hist=[]
    for it in range(steps):
        opt.zero_grad()
        # boundary loss (both cases know the two endpoints = 0)
        lb=((net(xb)-0.0)**2).mean()
        if use_physics:
            u,uxx=deriv2(net, xc)
            f=-(math.pi**2)*torch.sin(math.pi*xc)
            lp=((uxx-f)**2).mean()
            loss=lp+20*lb
        else:
            # no physics, no interior labels: only the 2 boundary points constrain it
            lp=torch.tensor(0.0); loss=20*lb
        loss.backward(); opt.step()
        if it%500==0 or it==steps-1:
            with torch.no_grad():
                err=(net(xtest)-true_u(xtest)).abs().max().item()
            hist.append((it, float(lp) if use_physics else 0.0, err))
    with torch.no_grad():
        maxerr=(net(xtest)-true_u(xtest)).abs().max().item()
    return hist, maxerr

print("=== PINN: solve u''=-pi^2 sin(pi x), u(0)=u(1)=0, true u=sin(pi x) ===")
print("    (50 interior points, NO labels there — only the equation. Plus the 2 boundary values.)")
hp, errp = train(use_physics=True)
print("  WITH the physics term:")
print("    step | physics-residual loss | max error vs true solution")
for it,lp,err in hp:
    print(f"    {it:5d} | {lp:20.4e} | {err:.4f}")
print(f"  final max error across [0,1]: {errp:.4f}  (the net matches sin(pi x) it was never shown)")

hn, errn = train(use_physics=False)
print("\n  WITHOUT the physics term (same net, only the 2 boundary points, no interior labels):")
print(f"    final max error vs true solution: {errn:.4f}  (it satisfies the endpoints but the")
print(f"    interior is a meaningless guess — nothing pins it to the real curve)")
print(f"\n  => the physics residual is the teacher: it drops the error from {errn:.2f} to {errp:.3f}")
print(f"     using the EQUATION in place of thousands of labelled interior points.")
