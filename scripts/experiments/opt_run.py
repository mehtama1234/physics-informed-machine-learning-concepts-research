"""Real optimization run: gradient descent vs momentum on an ill-conditioned bowl.
Plain gradient descent slows in proportion to the condition number (how much steeper the
steepest direction is than the flattest); momentum (heavy-ball) needs only about its
square root. numpy only."""
import numpy as np
def run(kappa, method, steps=40000, tol=1e-5):
    # f(x)=.5(x0^2 + kappa*x1^2); L=kappa, mu=1; grad=[x0, kappa*x1]
    x=np.array([1.0,1.0])
    if method=='gd':
        lr=2.0/(kappa+1.0)                       # optimal GD step for this quadratic
    else:
        sk=np.sqrt(kappa)
        lr=(2.0/(sk+1.0))**2                      # optimal heavy-ball step
        beta=((sk-1.0)/(sk+1.0))**2               # optimal heavy-ball momentum
    v=np.zeros(2)
    for it in range(1,steps+1):
        g=np.array([x[0], kappa*x[1]])
        if method=='gd': x=x-lr*g
        else: v=beta*v-lr*g; x=x+v
        if np.linalg.norm(x)<tol: return it
    return steps
print("=== gradient descent vs momentum on an ill-conditioned bowl ===")
print("  condition number = how much steeper the steepest direction is than the flattest")
print(f"  {'condition #':>12} | {'plain GD steps':>14} | {'momentum steps':>14} | {'speedup':>8}")
for k in [1,10,100,1000,10000]:
    gd=run(k,'gd'); mo=run(k,'mom')
    print(f"  {k:>12} | {gd:>14} | {mo:>14} | {gd/max(mo,1):>7.1f}x")
print("  => GD steps grow with the condition number; momentum grows with its SQUARE ROOT,")
print("     so the harder the problem, the bigger momentum's win. This is why conditioning")
print("     and normalization matter so much when training networks.")
