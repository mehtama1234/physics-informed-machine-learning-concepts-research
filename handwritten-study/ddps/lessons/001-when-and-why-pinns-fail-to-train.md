# 001 - When And Why Physics-Informed Neural Networks Fail To Train

Video: https://www.youtube.com/watch?v=xvOsV106kuA

Transcript used: `raw-material/transcripts/ddps/raw-vtt/001-xvOsV106kuA-DDPS ｜ ＂When and why physics-informed neural networks fail to train＂ by Paris Perdikaris.en.vtt`

This talk belongs right after the AISE PINN introduction and theory lectures. The AISE course told us what a PINN is: a neural network is used as a possible solution, and the training loss checks data, the equation residual, and boundary or initial conditions. This DDPS talk asks the next, harder question: if that idea sounds so clean, why does training still break?

The speaker first sets up the ordinary PINN promise. We have a differential equation, maybe a few observations, and boundary or starting information. Instead of building a mesh solver in the usual way, we let a neural network represent the unknown solution. Then we train it against several demands at once:

- match any observed data
- make the PDE residual small
- satisfy initial or boundary conditions

That is the same basic story as the AISE lectures. The important shift in this DDPS talk is that the loss is not treated as a magic score. The talk is about the behavior of the training problem itself.

The first-principles issue is this:

When several errors are put into one training objective, the optimizer may not hear them equally.

In plain words, imagine trying to learn from three teachers at once. One teacher says the data points are wrong. One says the equation is wrong. One says the boundary is wrong. If one teacher shouts and the others whisper, the learner may improve one part while ignoring another. A PINN can fail in that kind of way: not because the physical idea is useless, but because the training process does not balance the demands well.

The transcript repeatedly returns to training, gradients, residuals, differential equations, data fit, boundary conditions, and composite loss. That tells us the talk is not mainly about inventing a new scientific system. It is inspecting the training mechanics inside a PINN.

The simple learner version is:

A PINN does not just ask, "Does the answer obey physics?" It asks, "Can gradient-based training actually find an answer that obeys all the pieces we put into the loss?"

That matters because a small reported loss can be misleading. If the residual term, data term, and boundary term fight each other or have very different scales, the training path can stall or favor the wrong part of the problem. The model may look like it is learning while the physical answer still fails where it matters.

Connection back to AISE:

- AISE Lecture 3 explained the PINN recipe.
- AISE Lecture 4 warned that PINNs need theory and checks before they are trusted.
- This DDPS talk gives a concrete reason for that warning: training a multi-part physics loss is itself a scientific and numerical problem.

What this adds to the bigger course:

The course should not teach PINNs as "add a physics term and trust it." The real lesson is narrower and more honest: a PINN tries to use the equation as training evidence, but the training process can fail when the loss terms, gradients, or equation behavior make the optimization problem hard.

What not to overclaim:

This transcript does not prove that all PINNs fail. It also does not prove that a single fix solves PINN training. It supports a more careful claim: PINN training can fail for structural reasons inside the optimization problem, so a reader must ask how the loss terms are balanced and how failure is detected.

One sentence to keep:

A PINN is only as trustworthy as the training process that makes data error, equation error, and boundary error all matter at the same time.
