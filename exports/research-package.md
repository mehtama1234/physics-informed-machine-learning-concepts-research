# Physics-Informed Machine Learning Concepts Research

## Summary
- title: Physics-Informed Machine Learning Concepts Research
- playlist_count: 2
- video_count: 40
- available_transcripts: 40
- missing_transcripts: 0
- concept_count: 14
- theme_count: 7
- family_count: 4
- comparison_count: 4
- worked_example_count: 8
- deep_dive_count: 8
- core_derivation_count: 8
- diagram_count: 6
- learning_path_step_count: 7
- glossary_term_count: 10
- domain_guide_count: 5
- reader_check_count: 6
- decision_guide_count: 6
- provenance_guide_count: 6
- coverage_row_count: 14
- concept_ladder_count: 14
- quality_rubric_count: 6
- synthesis_guide_count: 4
- review_handoff_count: 1
- review_entrypoint_count: 20

## Concepts
### Deep Learning
- Problem: scientists often have examples of behavior but no short rule that predicts the next case
- Domain: scientific prediction from large measured or simulated data sets
- Why: it can learn useful patterns when hand-written rules are incomplete, but the result still needs tests outside the examples used for fitting
- Failure: the model can fit familiar examples while failing on a new material, geometry, scale, or boundary condition

### Physics-Informed Neural Networks
- Problem: measurements may be sparse, but the answer must still respect a known physical equation
- Domain: differential equations in science and engineering
- Why: it lets known physics push the fit toward physically possible behavior instead of treating data points as the only evidence
- Failure: the equation penalty can look small while the solution is wrong in hard regions, sharp layers, or unseen boundary cases

### Partial Differential Equations
- Problem: a quantity changes over space and time, so one number is not enough to describe the situation
- Domain: fluids, heat, waves, mechanics, chemistry, climate, and other changing fields
- Why: PDEs are the language many scientific models use before machine learning enters the story
- Failure: a learned shortcut can ignore boundary conditions or conservation behavior that the PDE was carrying

### Operator Learning
- Problem: one simulation answer is not enough when engineers need the whole map from inputs to solution fields
- Domain: fast prediction for families of scientific simulations
- Why: it can replace many expensive solves with a fast approximation when the requested cases stay inside the tested family
- Failure: the learned map can give plausible-looking fields that violate the equation or fail on a shifted input family

### Scientific Machine Learning
- Problem: scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time
- Domain: using data-driven models inside scientific workflows
- Why: it connects flexible prediction to the checks scientists already need: units, conservation, boundaries, uncertainty, and failure cases
- Failure: the method becomes a generic fitting tool if the physical quantity, scientific claim, and validation case are not named

### Surrogate Modeling
- Problem: a trusted simulator may be too slow to run for every design, control, or uncertainty question
- Domain: expensive simulation and design loops
- Why: it makes repeated scientific decisions possible when full simulation cost would stop the workflow
- Failure: speed can hide missing physics when the surrogate is used beyond the regime where it was checked

### Uncertainty And Generalization
- Problem: a prediction is not enough unless the user knows when it should be believed
- Domain: model use under new conditions
- Why: scientific models are used to make decisions, so the cost of being confidently wrong can be high
- Failure: training error can look good while the model fails under a new geometry, parameter range, sensor, or physical regime

### Optimization For Learning
- Problem: learning needs a way to decide which model settings are better or worse
- Domain: turning model fitting into a repeatable computation
- Why: the model only learns what the training score asks it to improve
- Failure: a model can optimize the written score while missing the scientific behavior the score failed to name

### Generative Modeling
- Problem: some tasks need many possible examples, not one predicted answer
- Domain: creating plausible scientific samples, fields, or candidate designs
- Why: it can explore candidate fields, shapes, or scenarios when direct enumeration is impossible
- Failure: generated samples can look realistic while breaking constraints, conservation, or rare-event behavior

### Graphs And Geometric Learning
- Problem: many scientific objects are not simple rows of numbers; their connections matter
- Domain: systems made of interacting parts, meshes, molecules, or spatial relations
- Why: it lets the model respect the structure of the object instead of flattening away important relations
- Failure: the graph can encode the wrong neighborhood, hide missing interactions, or fail when the mesh changes

### Neural Differential Equations
- Problem: scientists may know that a system changes continuously but not know the exact rule for that change
- Domain: changing systems where time evolution is part of the model
- Why: it lets learning focus on the missing change rule while the time update still carries the idea of continuous evolution
- Failure: small learned-rate errors can accumulate until long-time predictions drift away from the real system

### Symbolic Regression And Model Discovery
- Problem: a scientist may need a readable equation, not only a model that predicts well
- Domain: turning data into equations people can inspect
- Why: a short equation can be tested, criticized, and reused more easily than a large fitted model
- Failure: a neat formula can fit the training data while using the wrong variables or failing on a changed experiment

### Foundation Models For PDEs
- Problem: one trained model may be asked to handle many related equations, grids, parameters, or physical settings
- Domain: broad families of PDE problems and scientific fields
- Why: a broad model could reduce repeated training cost if it keeps the physical features that matter across tasks
- Failure: the model can look broad while missing rare regimes, new boundary conditions, or quantities not represented in training

### Attention For Scientific Fields
- Problem: a local patch of a field may depend on faraway information, but looking everywhere can be expensive
- Domain: large scientific fields where distant parts may interact
- Why: it gives the model a way to move information across a field without treating every location as isolated
- Failure: windowing or scaling choices can miss long-range effects that matter for the scientific quantity being predicted


## Paper Family Routes
### Physics Constraints Family
- Problem: You have some observations, but the answer must also obey a rule scientists already trust.
- Domain: heat flow, fluids, waves, elasticity, reaction systems, and other systems described by differential equations
- What the math buys: The equation turns empty space between measurements into a checkable demand. The model cannot claim success only by touching the measured points.
- Failure boundary: This family fails when the written equation is incomplete, the boundary information is wrong, or the training process avoids the hard regions where the rule matters most.

### Neural Operators Family
- Problem: One solved simulation is not enough; the scientific job needs the map from many inputs to many full fields.
- Domain: repeated PDE solves, design sweeps, weather-like fields, fluids, materials, and parameter studies
- What the math buys: The object being learned is a map between functions. That matters because a field is not a single row of numbers; it is a whole spatial object.
- Failure boundary: This family fails when the new query is outside the learned family, when resolution changes reveal hidden errors, or when the output looks smooth but breaks the physical claim.

### Model Discovery Family
- Problem: Prediction alone is not enough when the scientist needs a readable law or missing change rule.
- Domain: mechanism discovery, dynamics, lab measurements, simplified physical laws, and interpretable scientific modeling
- What the math buys: A compact equation is easier to inspect, criticize, and reuse than a large fitted object. The math turns a fit into a candidate explanation.
- Failure boundary: This family fails when the needed variable was not measured, the experiment did not excite the important behavior, or the search space cannot express the true rule.

### Scientific Surrogates Family
- Problem: The trusted simulator is too slow for repeated decisions, but a fast answer is dangerous if nobody states where it is valid.
- Domain: engineering design, uncertainty sweeps, control loops, inverse problems, and expensive simulation workflows
- What the math buys: The approximation becomes useful only after the input family, output quantity, error measure, and rejected cases are named.
- Failure boundary: This family fails when speed hides missing physics, when users ask new questions the surrogate was not trained for, or when uncertainty is treated as decoration.


## Comparisons
### PINNs vs Neural Operators
- Shared problem: Both try to predict scientific fields without ignoring the physics that makes those fields meaningful.
- Key difference: A PINN usually learns one field while being punished for breaking an equation. A neural operator learns the input-to-solution map for a named family of fields.
- Wrong turn: Do not use either word as a badge of trust. Ask what changed case was tested.

### Solvers vs Learned Surrogates
- Shared problem: Both produce answers for scientific or engineering questions.
- Key difference: A solver follows the written equations step by step. A surrogate imitates the solver's input-output behavior inside a tested use range.
- Wrong turn: A fast surrogate is not a replacement for the solver outside the cases where it was checked.

### Symbolic Regression vs Large Fitted Prediction
- Shared problem: Both use data to make future or unseen cases easier to understand.
- Key difference: Symbolic regression searches for a small formula. Large fitted prediction can carry more detail but usually gives less direct explanation.
- Wrong turn: A neat formula is not automatically true; it must survive changed data and missing-variable checks.

### Data-Only vs Physics-Informed Learning
- Shared problem: Both try to turn examples into predictions.
- Key difference: Data-only learning listens to examples. Physics-informed learning also listens to rules about what answers are allowed.
- Wrong turn: Adding physics language does not help if the added rule is wrong, too weak, or never tested against the claim.


## Worked Examples
### Heat Equation From Few Measurements
- Domain: heat moving through a rod, wall, chip, or material sample
- Question: What is the temperature everywhere if sensors only report a few places?
- Observed: sensor readings, starting temperature, boundary temperature, and the rule that heat flows from hot regions toward cold regions
- Hidden: temperature at every unsensed point and later time

### Fast Fluid Field Surrogate
- Domain: air or liquid flow around shapes
- Question: How can engineers test many shapes without running a full simulation every time?
- Observed: many prior simulations connecting shape, conditions, and resulting velocity or pressure fields
- Hidden: the flow field for a new shape or new condition

### Discovering A Small Law From Motion
- Domain: a measured system changing over time
- Question: Can data reveal a short rule for how the system moves?
- Observed: measurements of position, speed, concentration, or another changing quantity
- Hidden: the rate rule that causes the next moment

### Molecule Property From Structure
- Domain: chemistry and biology, where atoms, bonds, shape, and measured activity all matter
- Question: Can a model predict a useful molecular property without flattening away the structure that causes it?
- Observed: molecular graphs, atom types, bond patterns, shape information, and measured properties from experiments or trusted calculations
- Hidden: which structural relations control the property for a new molecule

### Material Stress From Sparse Tests
- Domain: materials and mechanics, where stress and strain depend on shape, load, defects, and boundary conditions
- Question: How can a model estimate stress inside a material when only a few tests or simulations are available?
- Observed: sample geometry, load conditions, a few measured displacements or strains, and known mechanical balance laws
- Hidden: the internal stress field and the weak region where failure may begin

### Mesh Field On Irregular Geometry
- Domain: scientific fields on meshes, surfaces, networks, and irregular engineering shapes
- Question: How can a model predict a field when the points are connected in an uneven shape instead of a neat grid?
- Observed: mesh points, connections, boundary labels, local features, and solution fields from prior solves
- Hidden: how information should move across the irregular geometry for a new case

### Foundation PDE Model On A New Equation
- Domain: many PDE tasks where one broad model is asked to help with a new scientific equation
- Question: When can a model trained on many PDE examples help with a new equation family?
- Observed: many prior equation tasks, grids, parameters, boundary types, and solution fields
- Hidden: which shared structure carries to the new equation and which parts do not

### Climate Risk Under Shifted Conditions
- Domain: climate, weather, and environmental fields where future conditions may differ from old data
- Question: How should a model report risk when the future case is not just another familiar example?
- Observed: historical fields, simulation ensembles, forcing conditions, regional measurements, and known physical constraints
- Hidden: how wrong the prediction may be under a changed climate, rare event, or new regional pattern


## Core Topic Deep Dives
### Physics Informed Neural Networks
- One sentence: A PINN is a fitted field that must answer to both measured values and a known physical rule.
- Use when: Use it when measurements are sparse, the equation is trusted, and the scientific job is one specific field or parameter case.
- Do not use when: Do not treat it as magic for hard PDEs; if boundary data, scales, or sharp regions are poorly handled, the equation penalty can mislead.
- Plain formula: total error = data error + equation error + boundary error
- Why it matters: The equation gives the model a reason not to invent impossible behavior between data points.

### Partial Differential Equations
- One sentence: A PDE is a rule for how a whole field changes across space and time.
- Use when: Use it when one value is not enough because neighbors, boundaries, and time all matter.
- Do not use when: Do not reduce the problem to independent points if movement, flow, stress, diffusion, or waves connect those points.
- Plain formula: change over time = movement through space + sources + boundary effects
- Why it matters: Most physics-informed machine learning borrows its scientific burden from PDEs.

### Operator Learning
- One sentence: Operator learning tries to learn the machine that turns one field into another field.
- Use when: Use it when you have many solved examples and need fast answers for new inputs from the same named family.
- Do not use when: Do not use it as proof of broad scientific skill unless the new equation, boundary, grid, and parameter range were tested.
- Plain formula: input field -> learned field-to-field map -> output field
- Why it matters: It targets repeated simulation work, where the valuable object is the whole input-output map.

### Surrogate Modeling
- One sentence: A surrogate is a faster stand-in for a slower trusted process.
- Use when: Use it when repeated simulation, design, or uncertainty questions would be too slow with the full solver.
- Do not use when: Do not use it outside the query family where it has been compared against the trusted source.
- Plain formula: new query -> fast stand-in -> approximate answer with a stated use range
- Why it matters: Speed changes what questions scientists and engineers can afford to ask.

### Uncertainty And Generalization
- One sentence: This topic asks when a prediction should be believed on a case the model did not learn from.
- Use when: Use it whenever a model will guide a scientific or engineering decision under changed conditions.
- Do not use when: Do not replace changed-case testing with a confident-looking number.
- Plain formula: prediction + tested use range + failure evidence
- Why it matters: A scientific model is dangerous when it is most confident exactly where it has the least evidence.

### Neural Differential Equations
- One sentence: A neural differential equation learns the missing rule for how a system changes.
- Use when: Use it when time evolution is central but the exact rate rule is partly unknown.
- Do not use when: Do not trust long-time behavior just because short training windows fit well.
- Plain formula: current state -> learned change rate -> next state
- Why it matters: It keeps the idea of continuous motion while admitting that part of the motion rule is unknown.

### Symbolic Regression
- One sentence: Symbolic regression searches for a short formula that explains measured behavior.
- Use when: Use it when a readable equation is part of the scientific goal.
- Do not use when: Do not believe a neat formula unless it survives missing-variable, noise, and changed-experiment checks.
- Plain formula: candidate ingredients -> searched formulas -> tested small law
- Why it matters: A compact equation can be criticized and reused in ways a large fitted object cannot.

### Foundation Models For Pdes
- One sentence: A PDE foundation model tries to reuse structure across many related field-prediction tasks.
- Use when: Use it when many PDE tasks share enough structure that one broad model may reduce repeated training.
- Do not use when: Do not confuse broad training with proof that a new scientific regime is covered.
- Plain formula: many PDE tasks -> shared learned structure -> new task prediction
- Why it matters: If it works, broad training could reduce repeated model-building for related scientific problems.


## Core Derivations
### Physics-Informed Neural Networks
- Problem: measurements may be sparse, but the answer must still respect a known physical equation
- Observed: some measured values, boundary values, starting values, and a known differential equation
- Hidden: the full field value at every point in space and time
- Plain formula: total error = data error + equation error + boundary error
- Failure test: move the training points, inspect sharp regions, and compare against a numerical solve or held-out measurements
- Page: derivations/physics-informed-neural-networks.html

### Partial Differential Equations
- Problem: a quantity changes over space and time, so one number is not enough to describe the situation
- Observed: a field such as temperature, pressure, concentration, velocity, or displacement
- Hidden: how every point in the field affects nearby points over time
- Plain formula: change over time = movement through space + sources + boundary effects
- Failure test: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error
- Page: derivations/partial-differential-equations.html

### Operator Learning
- Problem: one simulation answer is not enough when engineers need the whole map from inputs to solution fields
- Observed: many example inputs and their full solution fields
- Hidden: the rule that maps a new input field to its new solution field
- Plain formula: input field -> learned field-to-field map -> output field
- Failure test: change resolution, coefficients, boundary conditions, or forcing and check whether the predicted field still satisfies the scientific quantity being claimed
- Page: derivations/operator-learning.html

### Surrogate Modeling
- Problem: a trusted simulator may be too slow to run for every design, control, or uncertainty question
- Observed: expensive solver inputs and outputs for a limited set of cases
- Hidden: the solver answer for every new query someone wants to ask
- Plain formula: new query -> fast stand-in -> approximate answer with a stated use range
- Failure test: compare against the full solver on new cases near the edge of the intended use
- Page: derivations/surrogate-modeling.html

### Uncertainty And Generalization
- Problem: a prediction is not enough unless the user knows when it should be believed
- Observed: training cases, validation cases, prediction errors, and known shifts between cases
- Hidden: how wrong the model may be on a case unlike the ones it learned from
- Plain formula: prediction + tested use range + failure evidence
- Failure test: move one important condition outside the training range and measure the first failure
- Page: derivations/uncertainty-and-generalization.html

### Neural Differential Equations
- Problem: scientists may know that a system changes continuously but not know the exact rule for that change
- Observed: measurements of a system changing over time
- Hidden: the rate rule that moves the present value into the future
- Plain formula: current state -> learned change rate -> next state
- Failure test: run longer than the training window and check whether small rate errors accumulate into drift
- Page: derivations/neural-differential-equations.html

### Symbolic Regression And Model Discovery
- Problem: a scientist may need a readable equation, not only a model that predicts well
- Observed: measured variables and candidate mathematical ingredients
- Hidden: which short formula, if any, actually explains the measured change
- Plain formula: candidate ingredients -> searched formulas -> tested small law
- Failure test: remove a needed variable, add noise, or test a new experiment and see whether the formula still predicts
- Page: derivations/symbolic-regression.html

### Foundation Models For PDEs
- Problem: one trained model may be asked to handle many related equations, grids, parameters, or physical settings
- Observed: many PDE problem instances across equations, grids, parameters, or physical settings
- Hidden: which shared structure carries from one scientific task to another
- Plain formula: many PDE tasks -> shared learned structure -> new task prediction
- Failure test: hold out a new equation family, boundary type, scale, or rare regime and compare against a trusted solver
- Page: derivations/foundation-models-for-pdes.html


## Diagrams
### Data-Only Learning Flow
- Purpose: Show what a model sees when examples are the only source of correction.
- Flow: past examples -> adjustable model -> prediction -> compare with known answers -> test on a changed case
- Watch for: If the changed case is too similar to the past examples, the test says little about scientific use.

### Physics-Informed Learning Flow
- Purpose: Show how measured data and a known physical rule both push on the fitted field.
- Flow: sparse measurements -> known equation -> fitted field -> data check plus equation check -> held-out sensor or trusted solve
- Watch for: The equation check must be hard enough to catch mistakes between measured points.

### PDE Field Reasoning Flow
- Purpose: Show why fields need boundaries, neighbors, and time rather than isolated numbers.
- Flow: field value -> nearby values -> boundary or starting information -> local change rule -> future field
- Watch for: A learned shortcut that ignores boundaries can look smooth while answering the wrong physical question.

### Operator Learning Flow
- Purpose: Show the difference between learning one answer and learning a map from input fields to output fields.
- Flow: many input fields -> many solved output fields -> learned field-to-field map -> new input field -> new output field
- Watch for: The map is useful only for the named family of equations, grids, parameters, and boundaries.

### Surrogate Validation Flow
- Purpose: Show how a fast stand-in earns trust only by being checked against the slow source.
- Flow: expensive solver -> training cases -> fast stand-in -> edge-case comparison -> stated use range
- Watch for: A speed claim is incomplete until the use range and failure case are stated.

### Model Discovery Flow
- Purpose: Show how measurements can lead to a candidate rule rather than only a prediction.
- Flow: measured motion -> candidate variables -> searched rule or learned rate -> readable law -> new experiment check
- Watch for: A short law can be wrong if important variables were never measured.


## Learning Path
### 1. Start With The Scientific Question
- Question: What is being predicted, explained, designed, or checked?
- Why here: Physics-informed machine learning is not one trick. The method depends on the scientific job.
- Goal: Name the quantity, the domain, the evidence, and the changed case before naming a method.
- Checkpoint: You can say what answer the scientist wants and what would make that answer unusable.

### 2. Understand Fields And Equations
- Question: Why is one number not enough?
- Why here: Many scientific problems are fields: temperature, pressure, velocity, concentration, stress, or displacement across space and time.
- Goal: See why boundaries, neighbors, rates of change, and starting values carry the scientific burden.
- Checkpoint: You can explain why a field prediction must respect boundaries and nearby values.

### 3. Use Physics As A Check
- Question: How can a model be corrected where there are no measurements?
- Why here: Sparse data leaves empty space. A known equation can check that empty space if the equation is trusted.
- Goal: Understand PINNs as fitted fields that answer to both data and an equation.
- Checkpoint: You can state the data error, equation error, boundary error, and the test case.

### 4. Learn Maps Between Fields
- Question: What if the job is not one solution, but many related solutions?
- Why here: Engineering and science often need repeated solves for many inputs, shapes, materials, or conditions.
- Goal: Separate learning one answer from learning the map that turns an input field into an output field.
- Checkpoint: You can name the family of inputs and outputs where the learned map is allowed to be used.

### 5. Use Speed Without Hiding Risk
- Question: When is a fast approximation useful?
- Why here: A fast model is valuable only if the slow trusted source still defines where the fast answer is valid.
- Goal: Treat surrogates as checked stand-ins with a stated use range.
- Checkpoint: You can say what the surrogate replaces, what it does not replace, and where it was checked.

### 6. Make Trust A Testable Claim
- Question: When should a prediction be believed?
- Why here: Scientific mistakes often happen when a model is used outside the cases that taught it.
- Goal: Attach every prediction to a use range, changed-case test, and failure boundary.
- Checkpoint: You can name the first changed condition that should make the model fail.

### 7. Look For Readable Laws When Needed
- Question: When is prediction not enough?
- Why here: Sometimes the scientific product is a rule people can inspect, criticize, and reuse.
- Goal: Understand symbolic regression and neural differential equations as routes toward candidate mechanisms.
- Checkpoint: You can explain why a short formula still needs a changed-experiment test.


## Plain-Language Glossary
### Field
- Everyday meaning: a value spread across space or time, like temperature across a room
- Problem it names: one number cannot describe the whole situation
- Why it matters: many scientific predictions are about complete fields, not single answers
- Watch for: a method that predicts isolated points may miss how neighboring points affect each other

### Boundary Condition
- Everyday meaning: what is known at the edge of the problem
- Problem it names: a field can have many possible answers unless the edges or starting situation are pinned down
- Why it matters: boundaries often decide the scientific answer as much as the equation does
- Watch for: a model can look accurate inside the domain while quietly violating the edge information

### Residual
- Everyday meaning: the leftover rule-breaking after a proposed answer is checked
- Problem it names: a prediction may match measured points but still break the equation between them
- Why it matters: PINNs use this leftover error to push a fitted field toward physically allowed behavior
- Watch for: a small reported residual does not prove the answer is correct in hard regions

### Loss
- Everyday meaning: the score the training process tries to lower
- Problem it names: a model needs a written way to decide which answer is better
- Why it matters: the model learns what the score asks for, not what the reader hoped it meant
- Watch for: if the score forgets a scientific requirement, training can improve while the science gets worse

### Operator
- Everyday meaning: a machine that takes one whole function or field and returns another
- Problem it names: some tasks need the full input-to-output rule, not one solved example
- Why it matters: operator learning targets families of simulations where inputs and outputs are fields
- Watch for: the learned machine only deserves trust inside the named family of cases

### Surrogate
- Everyday meaning: a faster stand-in for something slower
- Problem it names: trusted simulations or experiments may be too expensive to run repeatedly
- Why it matters: a checked stand-in can make design, search, and uncertainty studies possible
- Watch for: speed is useful only where the stand-in has been compared against the trusted source

### Generalization
- Everyday meaning: whether a model still works on a new case
- Problem it names: training examples do not cover every situation where the model may be used
- Why it matters: scientific use depends on changed cases, not only familiar examples
- Watch for: a test that barely differs from training can create false confidence

### Uncertainty
- Everyday meaning: a warning about how much the answer may be wrong
- Problem it names: a single prediction hides how much evidence supports it
- Why it matters: scientific decisions need to know where belief should weaken
- Watch for: uncertainty is weak if it is not tied to changed-case testing

### Symbolic Regression
- Everyday meaning: searching for a short formula that fits measured behavior
- Problem it names: sometimes a scientist needs a readable rule, not only a prediction
- Why it matters: a compact formula can be inspected, criticized, and reused
- Watch for: a neat formula can be wrong if key variables were missing from the search

### Foundation Model
- Everyday meaning: one broad model trained across many related tasks
- Problem it names: training a new model for every scientific task can be expensive
- Why it matters: shared structure may reduce repeated training if the new task truly belongs to the learned family
- Watch for: broad training is not proof that a new regime, boundary, or quantity is covered


## Domain Guides
### Heat And Diffusion
- Real quantity: temperature, concentration, or another quantity spreading through space
- Why hard: measurements may be sparse, but the unsensed region still matters
- Common question: What is happening between sensors, later in time, or under a changed boundary?
- Failure test: Change the boundary temperature, source strength, or sensor placement and see whether the prediction still follows the physical rule.

### Fluids And Flow
- Real quantity: velocity, pressure, vorticity, drag, lift, or other flow quantities
- Why hard: small changes in shape, boundary, or regime can create large changes in the field
- Common question: Can we predict flow fields or forces quickly enough for design while still catching important failures?
- Failure test: Hold out a new geometry or flow condition near the edge of the intended design range.

### Materials And Mechanics
- Real quantity: stress, strain, displacement, failure location, or material response
- Why hard: the same load can produce different behavior when geometry, defects, or material parameters change
- Common question: Can a model predict how a material or structure responds under a new load or shape?
- Failure test: Change the geometry, mesh, defect, or load path and check the physical quantity used for decisions.

### Chemistry And Biology
- Real quantity: molecular property, reaction behavior, concentration, binding, or biological response
- Why hard: the object may be a graph, a field, a time process, or a set of interacting parts
- Common question: Can learned structure help predict scientific behavior while respecting the object being studied?
- Failure test: Test on a changed molecule, condition, experiment, or biological setting that was not close to training.

### Many PDE Tasks
- Real quantity: solution fields across many equations, grids, parameters, or boundary settings
- Why hard: a model may look broad while only covering the cases it saw often
- Common question: Can one trained model reuse structure across many related scientific tasks?
- Failure test: Withhold a full equation family, boundary type, or scale and check whether the model still earns the claim.


## Reader Checks
### PINNs Reader Check
- Setup: A wall has only a few temperature sensors, but the heat equation is trusted.
- Strong answer: Observed: sensor values, starting or boundary values, and the heat equation. Hidden: the full temperature field. The equation residual checks unsensed locations. The score needs data error, equation error, and boundary or starting error. A changed boundary, source, or held-out sensor should test the claim.
- Weak answer warning: A weak answer says only that the neural network fits data.

### Operator Learning Reader Check
- Setup: You have many solved PDE examples and want fast predictions for new input fields.
- Strong answer: The input is a whole field or function, and the output is a whole solution field. The equation, boundary, grid, parameter, and geometry family must be named. The method learns a map between fields, not one field. A new boundary, resolution, parameter range, or equation family should test the claim.
- Weak answer warning: A weak answer says only that the model is fast.

### Surrogate Reader Check
- Setup: A trusted simulation is too slow for a design loop.
- Strong answer: The surrogate replaces a named solver or experiment only inside a named query family. Inputs and outputs must match the decision. The stand-in should be checked near the edge of intended use, and the full solver should return when the query leaves that range or when errors affect the decision quantity.
- Weak answer warning: A weak answer treats speed as trust.

### Uncertainty Reader Check
- Setup: A model works on familiar examples and is now proposed for a new scientific setting.
- Strong answer: The answer names the actual shift, such as geometry, parameter range, sensor, scale, boundary, or regime. It measures the error that matters for the scientific decision, states the use range, and names a condition that would stop use.
- Weak answer warning: A weak answer reports one score without saying what changed.

### Symbolic Regression Reader Check
- Setup: Measurements suggest there may be a short law behind a changing system.
- Strong answer: The answer lists measured variables, allowed operations or ingredients, and the formula's claim about the system. It names at least one missing variable or untested regime and demands a changed experiment before calling the formula useful.
- Weak answer warning: A weak answer trusts a neat formula because it fits the original data.

### Foundation PDE Model Reader Check
- Setup: One broad model is trained across many PDE tasks.
- Strong answer: The answer names included and held-out task families, the shared structure being claimed, and a trusted solver or measurement for checking. It rejects broad claims when new equations, boundaries, scales, or rare regimes were not tested.
- Weak answer warning: A weak answer treats broad training size as proof of broad scientific trust.


## Decision Guide
### Sparse Data, Known Equation
- Situation: You have few measurements, but a trusted equation and boundary or starting information exist.
- Start with: Physics-informed neural networks
- Why: The equation can check the fitted field where measurements are missing.
- Evidence needed: held-out measurements, boundary checks, equation residual checks, and comparison against a trusted solve when possible

### Many Related Simulations
- Situation: You have many solved examples and need fast answers for new inputs from the same family.
- Start with: Operator learning
- Why: The useful object is the map from input fields to output fields, not one solved field.
- Evidence needed: held-out fields, changed resolution tests, boundary tests, and checks on the scientific output quantity

### Expensive Repeated Decisions
- Situation: A trusted solver or experiment is too slow for design, search, control, or uncertainty sweeps.
- Start with: Surrogate modeling
- Why: A fast stand-in can answer repeated questions if its use range is stated and checked.
- Evidence needed: full-solver comparisons near the edge of use, decision-metric error, and a stated use range

### Need A Readable Law
- Situation: Prediction is not enough; the output should be a formula or mechanism people can inspect.
- Start with: Symbolic regression or neural differential equations
- Why: The scientific product is a candidate rule, not only a number returned by a fitted model.
- Evidence needed: changed-experiment tests, missing-variable checks, noise checks, and scientific inspection of the selected rule

### New Setting Risk
- Situation: A model trained in one setting is being used in another setting.
- Start with: Uncertainty and generalization checks
- Why: The main question is whether the prediction should be believed under the change.
- Evidence needed: changed-case tests, use-range statements, error on the decision quantity, and first-failure examples

### Broad PDE Coverage
- Situation: One model is proposed for many equations, grids, parameters, or scientific tasks.
- Start with: Foundation models for PDEs
- Why: The claim is about shared structure across tasks, so whole task families must be tested.
- Evidence needed: held-out task-family tests, trusted-solver comparisons, boundary and scale tests, and failure reports


## Provenance And Reproduction
### Source Playlists
- Purpose: Name the exact course sources used by the package.
- Local files: raw-material/playlists/eth-aise-2024.json, raw-material/playlists/eth-aise-2025.json
- Checks: 40 video records are present, each record has a source URL, each record has at least one concept

### Transcript Extraction
- Purpose: Show how captions become local source material.
- Local files: raw-material/transcripts/eth-aise-2024/raw-vtt/, raw-material/transcripts/eth-aise-2024/clean/, raw-material/transcripts/eth-aise-2025/raw-vtt/, raw-material/transcripts/eth-aise-2025/clean/
- Checks: available transcript count equals 40, clean transcript paths are recorded, raw caption paths are recorded when present

### Analysis Build
- Purpose: Show how source text becomes concepts, themes, evidence, and pages.
- Local files: analysis/summary.json, analysis/concept_atlas.json, analysis/evidence_ledger.json, analysis/
- Checks: concept atlas has required fields, evidence ledger names support type and limit, summary counts match generated pages

### Site Generation
- Purpose: Show how the package turns analysis data into reviewable pages.
- Local files: site/index.html, site/page-manifest.json, site/topics/, site/videos/
- Checks: page manifest has the expected page count, required guide pages exist, local HTTP checks return OK

### CLI Reproduction Checklist
- Purpose: Give another CLI enough detail to reproduce this package for another channel.
- Local files: scripts/build_physics_informed_ml_research_package.py, README.md, Makefile
- Checks: repo has a clear topic name, raw source material is preserved, generated pages are validated, commits are small enough to review

### Cross-Channel Replication Playbook
- Purpose: Give another CLI an end-to-end operating plan for building the same kind of package from a different channel or playlist family.
- Local files: raw-material/playlists/, raw-material/metadata/, raw-material/transcripts/, analysis/, site/, exports/research-package.md
- Checks: source URLs are named, raw and clean transcripts are preserved, concept pages explain problem/domain/importance/failure, review entrypoints and coverage pages exist, validation commands pass


## Coverage Matrix
### Deep Learning
- Videos: 38
- Deep dive: no
- Diagram: yes
- Reader check: no
- Evidence items: 6

### Physics-Informed Neural Networks
- Videos: 28
- Deep dive: yes
- Diagram: yes
- Reader check: yes
- Evidence items: 6

### Partial Differential Equations
- Videos: 34
- Deep dive: yes
- Diagram: yes
- Reader check: no
- Evidence items: 6

### Operator Learning
- Videos: 33
- Deep dive: yes
- Diagram: yes
- Reader check: yes
- Evidence items: 6

### Scientific Machine Learning
- Videos: 33
- Deep dive: no
- Diagram: yes
- Reader check: no
- Evidence items: 6

### Surrogate Modeling
- Videos: 35
- Deep dive: yes
- Diagram: yes
- Reader check: yes
- Evidence items: 6

### Uncertainty And Generalization
- Videos: 39
- Deep dive: yes
- Diagram: yes
- Reader check: yes
- Evidence items: 6

### Optimization For Learning
- Videos: 40
- Deep dive: no
- Diagram: no
- Reader check: no
- Evidence items: 6

### Generative Modeling
- Videos: 33
- Deep dive: no
- Diagram: no
- Reader check: no
- Evidence items: 6

### Graphs And Geometric Learning
- Videos: 31
- Deep dive: no
- Diagram: no
- Reader check: no
- Evidence items: 6

### Neural Differential Equations
- Videos: 40
- Deep dive: yes
- Diagram: yes
- Reader check: no
- Evidence items: 6

### Symbolic Regression And Model Discovery
- Videos: 33
- Deep dive: yes
- Diagram: yes
- Reader check: yes
- Evidence items: 6

### Foundation Models For PDEs
- Videos: 6
- Deep dive: yes
- Diagram: yes
- Reader check: yes
- Evidence items: 6

### Attention For Scientific Fields
- Videos: 28
- Deep dive: no
- Diagram: yes
- Reader check: no
- Evidence items: 6


## Concept Ladder
### Deep Learning
- Problem: scientists often have examples of behavior but no short rule that predicts the next case
- Observed: many input-output examples from experiments, simulations, or measurements
- Hidden: the exact rule that connects the input to the output
- Mathematical move: adjust many weights until the model maps familiar inputs to the right outputs
- Shape: input -> layered adjustable calculation -> prediction
- Failure test: hold out a changed material, geometry, parameter range, or sensor condition

### Physics-Informed Neural Networks
- Problem: measurements may be sparse, but the answer must still respect a known physical equation
- Observed: some measured values, boundary values, starting values, and a known differential equation
- Hidden: the full field value at every point in space and time
- Mathematical move: fit a neural network while also measuring how badly its output violates the known equation
- Shape: prediction error + equation error + boundary error
- Failure test: move the training points, inspect sharp regions, and compare against a numerical solve or held-out measurements

### Partial Differential Equations
- Problem: a quantity changes over space and time, so one number is not enough to describe the situation
- Observed: a field such as temperature, pressure, concentration, velocity, or displacement
- Hidden: how every point in the field affects nearby points over time
- Mathematical move: write a local change rule that uses rates across space and time
- Shape: future change = spatial change + sources + boundary information
- Failure test: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error

### Operator Learning
- Problem: one simulation answer is not enough when engineers need the whole map from inputs to solution fields
- Observed: many example inputs and their full solution fields
- Hidden: the rule that maps a new input field to its new solution field
- Mathematical move: learn the map from problem input to solution, not only one solution at a time
- Shape: input function -> learned map -> output function
- Failure test: change resolution, coefficients, boundary conditions, or forcing and check whether the predicted field still satisfies the scientific quantity being claimed

### Scientific Machine Learning
- Problem: scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time
- Observed: data, equations, units, simulation outputs, and domain limits
- Hidden: which parts of the scientific system are missing, noisy, or too costly to compute directly
- Mathematical move: combine learned prediction with scientific checks that name what the claim is allowed to mean
- Shape: data fit + scientific structure + validation case
- Failure test: state the scientific quantity first, then test it under a changed case that matters in that domain

### Surrogate Modeling
- Problem: a trusted simulator may be too slow to run for every design, control, or uncertainty question
- Observed: expensive solver inputs and outputs for a limited set of cases
- Hidden: the solver answer for every new query someone wants to ask
- Mathematical move: train a cheaper stand-in for the expensive input-output behavior
- Shape: query -> fast stand-in -> approximate answer
- Failure test: compare against the full solver on new cases near the edge of the intended use

### Uncertainty And Generalization
- Problem: a prediction is not enough unless the user knows when it should be believed
- Observed: training cases, validation cases, prediction errors, and known shifts between cases
- Hidden: how wrong the model may be on a case unlike the ones it learned from
- Mathematical move: separate fit on familiar examples from evidence on changed examples
- Shape: prediction + error check + stated use range
- Failure test: move one important condition outside the training range and measure the first failure

### Optimization For Learning
- Problem: learning needs a way to decide which model settings are better or worse
- Observed: a written score that says which model behavior is better or worse
- Hidden: whether that score matches the scientific behavior the user actually cares about
- Mathematical move: change model settings to lower the written score
- Shape: choose settings that reduce data error, physics error, or design cost
- Failure test: inspect what the score ignores, then check whether the ignored behavior fails after training

### Generative Modeling
- Problem: some tasks need many possible examples, not one predicted answer
- Observed: examples of fields, molecules, flows, shapes, or other scientific objects
- Hidden: the spread of possible valid objects beyond the examples
- Mathematical move: learn how to sample new candidates that resemble the training family
- Shape: random seed + learned sampler -> candidate scientific object
- Failure test: measure constraints, rare cases, conservation, and downstream task performance on generated samples

### Graphs And Geometric Learning
- Problem: many scientific objects are not simple rows of numbers; their connections matter
- Observed: objects with parts and connections, such as meshes, molecules, or interacting components
- Hidden: which neighboring and long-range interactions control the scientific quantity
- Mathematical move: let information move along the object connections instead of flattening the object into a plain row
- Shape: nodes + edges + update rule -> predicted property or field
- Failure test: change the mesh, rotate or move the object, or add missing interactions and inspect what breaks

### Neural Differential Equations
- Problem: scientists may know that a system changes continuously but not know the exact rule for that change
- Observed: measurements of a system changing over time
- Hidden: the rate rule that moves the present value into the future
- Mathematical move: learn the missing rate rule and place it inside a time-evolution calculation
- Shape: current state -> learned rate -> next state
- Failure test: run longer than the training window and check whether small rate errors accumulate into drift

### Symbolic Regression And Model Discovery
- Problem: a scientist may need a readable equation, not only a model that predicts well
- Observed: measured variables and candidate mathematical ingredients
- Hidden: which short formula, if any, actually explains the measured change
- Mathematical move: search for a readable equation that fits the data and survives a changed case
- Shape: candidate formulas -> selected formula -> held-out test
- Failure test: remove a needed variable, add noise, or test a new experiment and see whether the formula still predicts

### Foundation Models For PDEs
- Problem: one trained model may be asked to handle many related equations, grids, parameters, or physical settings
- Observed: many PDE problem instances across equations, grids, parameters, or physical settings
- Hidden: which shared structure carries from one scientific task to another
- Mathematical move: train one broad model to reuse structure across many related field-prediction tasks
- Shape: many PDE tasks -> shared learned representation -> new task prediction
- Failure test: hold out a new equation family, boundary type, scale, or rare regime and compare against a trusted solver

### Attention For Scientific Fields
- Problem: a local patch of a field may depend on faraway information, but looking everywhere can be expensive
- Observed: large fields where one location may depend on other locations
- Hidden: which distant parts matter for the local prediction
- Mathematical move: let the model choose which parts of the field exchange information
- Shape: field pieces -> selected information exchange -> updated field pieces
- Failure test: change the window size, inspect long-range effects, and compare behavior near boundaries or sharp structures


## Editorial Quality Rubric
### First Principles
- Standard: The page starts from the real problem, observed evidence, hidden quantity, and scientific job before naming a method.
- Strong page: A reader can say what exists in the world, what is measured, what is missing, and why the method is needed.
- Weak page: The page starts by naming a method and assumes the reader already knows why it matters.
- Check: Look for sections that name the common problem, domain, observed quantity, hidden quantity, and changed-case test.

### Plain Language
- Standard: The page translates technical terms into everyday meaning without hiding the mathematical idea.
- Strong page: Terms such as field, residual, operator, loss, and generalization are tied to concrete jobs.
- Weak page: The page uses method names, benchmark language, or vague praise instead of explaining the idea.
- Check: Look for glossary links, everyday anchors, concrete domain stories, and plain formulas.

### Domain Grounding
- Standard: The page says where the concept matters in science or engineering and what quantity is being predicted or explained.
- Strong page: The domain, real quantity, and domain-specific failure test are visible.
- Weak page: The page describes a general model but never says what scientific object or quantity it serves.
- Check: Look for domain guide links, worked examples, and concrete anchor pages.

### Failure Boundary
- Standard: The page states what the concept does not prove and what changed case could reject the claim.
- Strong page: A reader sees the use range, red flags, and first failure test.
- Weak page: The page says the method works without stating where it breaks.
- Check: Look for failure boundary, red flags, reader checks, and decision guide evidence requirements.

### Evidence Discipline
- Standard: The page separates transcript support from scientific proof.
- Strong page: Transcript evidence is shown as support that a concept appears, while validation claims require explicit tests.
- Weak page: The page treats a lecture mention as proof that a method works broadly.
- Check: Look for transcript evidence, support type, and explicit evidence limits.

### Connected Map
- Standard: The page connects the concept to nearby concepts, families, diagrams, decisions, or checks.
- Strong page: A reader can move from the concept to a route, comparison, diagram, or decision case.
- Weak page: The page is isolated and does not show how the idea fits into the field.
- Check: Look for concept links, families, comparisons, visual maps, and coverage matrix entries.


## Field Synthesis
### Central Problem
- Claim: Physics-informed machine learning asks how data, equations, simulations, and scientific checks can work together without pretending any one of them is enough.
- Explanation: Data gives examples. Equations give rules. Simulations give trusted cases. Validation gives the right to use a model under a named condition. The field exists because scientific prediction often needs all four.
- Reader takeaway: Do not ask first which model is popular. Ask what scientific quantity is needed, what evidence exists, and what changed case would reject the answer.

### Main Moves
- Claim: The recurring moves are fitting from data, constraining with physics, learning maps between fields, replacing expensive solves, estimating trust, and searching for readable rules.
- Explanation: PINNs use equations as checks. Neural operators learn field-to-field maps. Surrogates trade full cost for checked speed. Uncertainty asks when belief should weaken. Symbolic regression asks whether data can support a small law.
- Reader takeaway: Each method is a response to a different pressure. Confusing those pressures is how vague explanations start.

### Proof Burden
- Claim: A method name never proves a scientific claim; only a named test under a meaningful changed case can carry that burden.
- Explanation: A transcript mention shows that a topic appears in the course. A training score shows that a model matched a written score. A scientific claim needs more: a domain, quantity, use range, and failure test.
- Reader takeaway: Every strong page should say what the transcript supports and what it does not prove.

### Field Map
- Claim: The field is best read as a map of scientific jobs, not a list of model names.
- Explanation: Sparse measurements point toward physics checks. Many solved fields point toward operator learning. Repeated expensive decisions point toward surrogates. New settings point toward uncertainty. Need for a readable law points toward model discovery.
- Reader takeaway: Start from the job, then choose the concept family that carries the right evidence.


## Review Handoff
- Purpose: Give a reviewer the shortest reliable route through the package and the checks that prove the generated site is coherent.

### Start Here
- Field Synthesis: synthesis.html
- Learning Path: learning-path.html
- Coverage Matrix: coverage.html
- Decision Guide: decision-guide.html
- Provenance: provenance.html

### Remaining Editorial Work
- Hand-write richer derivations for the highest-value concepts after reviewing the generated structure.
- Add lecture-specific quotes and figures to the worked examples after reviewing the transcript excerpts.
- Add real figures or mathematical sketches where a static flow diagram is not enough.
- Review transcript excerpts for places where better quotes or lecture-specific anchors should be selected.

## Review Entrypoints

### Start The Review
- Purpose: Use these pages to see the whole argument before inspecting details.
- Review Handoff: handoff.html | What exists now, and what still needs hand-written depth?
- Field Synthesis: synthesis.html | What problem holds the field together?
- Learning Path: learning-path.html | What should a new reader read first, second, and third?
- Concept Ladder: concept-ladder.html | Can each concept be explained without starting from the method name?
- Core Derivations: derivations.html | Can the reader see how the formula shape follows from the scientific problem?

### Inspect Core Concepts
- Purpose: Use these pages to judge whether the main mathematical ideas are explained from first principles.
- PINNs: topics/physics-informed-neural-networks.html | How can a learned curve be pushed to obey a known physical rule?
- Operator Learning: topics/operator-learning.html | When is the object being learned a whole solver shortcut?
- Surrogate Modeling: topics/surrogate-modeling.html | When is speed useful, and where does it stop being trustworthy?
- Uncertainty And Generalization: topics/uncertainty-and-generalization.html | How does the page say where the model may be wrong?
- Symbolic Regression: topics/symbolic-regression.html | When is a short formula a scientific claim instead of a curve fit?
- Foundation Models For PDEs: topics/foundation-models-for-pdes.html | What must carry from old equation cases to a new one?

### Use The Package
- Purpose: Use these pages when choosing a method for a concrete scientific situation.
- Decision Guide: decision-guide.html | Which method family fits the job in front of the reader?
- Domain Guides: domains.html | What quantity does this domain actually need?
- Worked Examples: worked-examples.html | Can the reader follow one scientific job all the way through?
- Comparisons: comparisons.html | What changes when two methods sound similar?

### Check Coverage And Sources
- Purpose: Use these pages to audit completeness, source support, and wording quality.
- Coverage Matrix: coverage.html | Which important concepts still need more support?
- Evidence Ledger: evidence-ledger.html | What does the transcript support, and what does it not prove?
- Quality Rubric: quality.html | Does each page avoid empty language and explain the real problem?
- Provenance: provenance.html | Could another CLI rebuild this package from the same sources?
- Cross-Channel Playbook: provenance/cross-channel-playbook.html | What exact source, concept, evidence, page, and validation steps should the next build follow?
