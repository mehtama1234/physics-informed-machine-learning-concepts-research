"""Real graph-learning run: a task whose answer depends on a node's NEIGHBORS, not just its
own features. A message-passing step (average your neighbors) cracks it; an MLP that sees
only each node in isolation cannot. numpy only (closed-form linear readouts)."""
import numpy as np
rng=np.random.default_rng(0)
def make(n=400,d=6):
    # random graph; each node has random features; LABEL = sign of the mean of NEIGHBOR feature-0
    A=(rng.random((n,n))<0.03).astype(float); np.fill_diagonal(A,0); A=np.maximum(A,A.T)
    X=rng.standard_normal((n,d))
    deg=A.sum(1,keepdims=True); deg[deg==0]=1
    nbr_mean=(A@X)/deg               # message passing: average of neighbors' features
    y=(nbr_mean[:,0]>0).astype(float)
    return X,nbr_mean,y
X,nbr,y=make()
def acc(feat):
    # simple linear classifier (least squares) on the given features
    Phi=np.concatenate([feat,np.ones((len(feat),1))],1)
    w=np.linalg.lstsq(Phi,y*2-1,rcond=None)[0]
    return ((Phi@w>0).astype(float)==y).mean()
print("=== graph learning: the label depends on your NEIGHBORS ===")
print("  task: each node's label = is the average of its neighbors' first feature positive?")
print(f"  classifier on the node's OWN features only (no graph): accuracy {acc(X):.3f}")
print(f"  classifier after ONE message-passing step (average neighbors): accuracy {acc(nbr):.3f}")
print("  => the node's own features are blind to the answer (~chance); one round of passing")
print("     messages along edges makes it easy. That neighbor-mixing step IS a graph network.")
