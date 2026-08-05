# DDPS To AISE 2025 Theme Bridge

The AISE 2025 course is a structured course. The DDPS playlist is a seminar series. That changes how to read it.

AISE gives the spine:

1. Start with scientific and engineering questions.
2. Learn deep learning as input-to-output fitting.
3. Add equations through PINNs.
4. Move from one solve to many solves through operator learning.
5. Handle grids, time, irregular geometry, graphs, attention, and generative futures.
6. End by applying similar representation questions to chemistry and biology.

DDPS should be read as a set of deeper side rooms around that spine. Each DDPS talk usually takes one hard issue and pushes it further: training failure, model reduction, numerical stability, differentiable simulation, inverse problems, uncertainty, scientific discovery, or domain-specific simulation.

The first bridge is PINNs.

AISE teaches:

The PINN loss combines data, PDE residual, and boundary or initial information.

DDPS video 1 adds:

That combined loss can be hard to train. The failure is not just a coding problem. It can come from the shape of the optimization problem, the balance between loss terms, and the way gradients move during training.

So the plain learning path should be:

1. Understand the PINN idea from AISE.
2. Read the DDPS failure talk.
3. Ask why the loss is hard to train.
4. Only then trust or reject a PINN result.

This is the standard for future DDPS bridges: do not merely say "this connects to PINNs" or "this connects to operators." Name the exact missing burden that the DDPS talk adds.

The second bridge is reduced-order modeling.

AISE teaches:

A surrogate model can make repeated scientific solves cheaper.

DDPS video 2 adds:

Cheaper is not enough. The surrogate has to compress the right thing. If a pulse, front, interface, or shock is moving through the domain, a fixed small set of shapes can fail even when the physics is simple. The missing burden is to notice motion as motion. The model may need to learn how the feature travels, not merely store many copies of the feature in different positions.

So the plain learning path should be:

1. Understand that a PDE solution is a field over space and time.
2. Notice whether the field changes by changing shape or by moving features.
3. If features move, ask whether the model represents the motion directly.
4. Only then judge whether the reduced model is actually useful.
