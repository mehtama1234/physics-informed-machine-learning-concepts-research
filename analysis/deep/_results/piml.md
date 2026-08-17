# Physics-Informed ML — verified measured results (all self-contained, numpy/PyTorch on CPU)

Every number below is measured from a small experiment we actually ran. The physics generates
its own data (a PDE solution, a simulated trajectory, random functions), so no external dataset
is needed. Scripts in scripts/experiments/. Cite numbers verbatim; do NOT invent new ones.

## PINN — solve a differential equation with a net using ONLY the equation (script: pinn_run.py)
Concept: physics-informed-neural-networks (and the umbrella scientific-machine-learning).
- Task: solve u''(x) = -pi^2 sin(pi x) on [0,1] with u(0)=u(1)=0. True answer: u = sin(pi x).
- 50 interior points with NO labels there — only the equation — plus the 2 boundary values.
- WITH the physics term: the equation-residual loss falls from 46 to 3.6e-5; the max error versus
  the true solution falls from 0.895 to **0.000** (essentially exact) — the net matches sin(pi x)
  it was never shown.
- WITHOUT the physics term (same net, only the 2 boundary points, no interior labels): max error
  stays **0.99** — it hits the endpoints but the interior is a meaningless guess.
- Insight: the equation itself is the teacher. It replaces thousands of labelled interior points and
  drops the error from 0.99 to 0.000. (For scientific-machine-learning, frame this as: adding a known
  physical law to a data-driven model is what the whole field is about.)

## Heat equation by finite differences (script: pde_run.py)  — concept: partial-differential-equations
- Rule: each point nudges toward the average of its neighbors every tick,
  u_new[i] = u[i] + r*(u[i-1] - 2u[i] + u[i+1]), with stability number r = 0.4 (must stay < 0.5).
- Numeric peak vs the exact decay exp(-pi^2 t): at t = 0, 0.02, 0.05, 0.1, 0.2 the peaks are
  1.000, 0.821, 0.611, 0.373, 0.139 — matching the exact value to **0.0000** at every checkpoint.
- With r > 0.5 the same rule blows up (the CFL stability limit).
- Insight: a purely LOCAL neighbor-averaging rule reproduces the exact GLOBAL smoothing/decay.

## SINDy — recover equations from data (script: sindy_run.py)  — concept: symbolic-regression
- From a single clean Lorenz trajectory (no equations given), build a library of candidate terms
  and use sparse regression. Recovered, exactly, all three equations and coefficients:
  dx/dt = -10 x + 10 y ; dy/dt = 28 x - y - x z ; dz/dt = -2.667 z + x y (true sigma=10, rho=28, beta=2.667).
- Every one of the spurious library terms was driven to zero.
- Insight: with the right sparse penalty, regression discovers the compact governing law behind data.

## Optimization — gradient descent vs momentum (script: opt_run.py)  — concept: optimization-for-learning
- Ill-conditioned bowl; condition number = how much steeper the steepest direction is than the flattest.
- Steps to converge: condition 1 -> GD 1 / momentum 1; 10 -> 60 / 24; 100 -> 593 / 83; 1000 ->
  5930 / 282; 10000 -> 40000 / 953. Speed-up grows to **42x**.
- Insight: plain gradient descent slows in proportion to the condition number; momentum needs only
  about its SQUARE ROOT — the harder the problem, the bigger momentum's win. Why conditioning and
  normalization matter so much in training.

## Neural ODE — learn the velocity field, then integrate (script: node_run.py)  — concept: neural-differential-equations
- Fit a decaying spiral by learning the right-hand side of an ODE (the velocity field) and integrating it.
- Roll-out error over 200 steps fell 4.39 -> 0.09 -> 0.05 -> 0.02 -> 0.013 -> **0.0067** over training.
- Integrating the learned flow re-draws the whole spiral from just the start point, and keeps
  spiraling inward sensibly for 2x the trained horizon.
- Insight: learn the DYNAMICS (how things change), not the next point directly — then any integrator
  produces the trajectory, and it respects the continuous structure.

## Surrogate modeling (script: surrogate_run.py)  — concept: surrogate-modeling
- Train a small net to imitate an expensive function, then call the cheap copy.
- Test accuracy (root-mean-square error): **0.018** on unseen inputs.
- Time to evaluate 200 inputs: expensive function ~4971 ms vs surrogate ~0.12 ms — about **42,000x faster**.
- Insight: once trained, the surrogate replaces the slow simulator wherever a small error is tolerable.

## Uncertainty — deep ensemble (script: uq_run.py)  — concept: uncertainty-and-generalization
- Train 8 nets on data present only in two bands (a gap in the middle, nothing beyond +-2).
- Ensemble disagreement (std of the 8 predictions): 0.0038 and 0.0036 INSIDE the data bands, but
  **0.069 in the empty gap and 0.109 far outside** — roughly 20-30x higher where there is no data.
- Insight: the spread of an ensemble is a free, honest "I don't know" signal that grows off-data.

## Operator learning — DeepONet (script: operator_run.py)  — concept: operator-learning
- Train on 1000 random functions to map each function to its running integral (the antiderivative operator).
- Test error on **200 unseen functions**: root-mean-square **0.0098**.
- Insight: the network learned the OPERATION "integrate," not one answer, so it integrates functions
  it never saw. Learning a function-to-function map is what lets one trained operator solve a whole
  family of PDEs at once (foundation-models-for-pdes builds on this).

## Graph learning — message passing (script: gnn_run.py)  — concept: graphs-and-geometric-learning
- Task: each node's label = is the average of its NEIGHBORS' first feature positive?
- Classifier on the node's own features only (no graph): accuracy **0.537** (~chance).
- After ONE message-passing step (average neighbors): accuracy **0.965**.
- Insight: the answer lives in the graph structure; mixing information along edges (message passing)
  is exactly what a graph neural network does.

## Attention on fields (script: attention_run.py)  — concept: attention-for-scientific-fields
- Task: position 0 says "fetch index j"; the answer lives at position j, anywhere in the sequence.
- Content-based attention picks the correct far position **100%** of the time; a fixed local window
  (looks only near position 0) gets it **10%** of the time.
- Insight: attention routes information from wherever it is needed, however far; a fixed-distance
  filter is blind past its window. That any-to-any routing is why attention works on fields too.

## Generative modeling — diffusion (script: generative_run.py)  — concept: generative-modeling
- A tiny denoising diffusion model on a 2-D "two moons" shape.
- **91%** of generated points land on the shape (within 0.15 of a real point); spread of real data
  [0.87, 0.49] vs generated [0.85, 0.49].
- Insight: trained only to remove a little noise at each level, the model composes those steps to
  build brand-new samples that match the data shape, starting from pure noise.

## Deep learning — why a hidden layer matters (script: deeplearning_run.py)  — concept: deep-learning
- Curved target y = sin(1.5x) + 0.3x. Fit error: straight-line model **0.692** (can only draw a line);
  one hidden layer (64 units) **0.008**; two hidden layers **0.002**.
- Insight: a linear model is stuck; a layer of simple nonlinear units lets the network bend to the
  curve, and stacking such layers is what "deep" learning is.

## Foundation model for PDEs — pretrain then adapt (script: foundation_run.py)  — concept: foundation-models-for-pdes
- Pretrain one net on 8 related fields, then adapt to a NEW shifted family with only 3 examples.
- Error on unseen cases of the new family: trained from scratch on the 3 examples **0.997**;
  fine-tuned from the pretrained model **0.746**.
- Insight: the pretrained model already knows the "shape" of such fields, so a few examples adapt it;
  from scratch, 3 examples are far too few. That is the foundation-model bet, applied to PDEs.
