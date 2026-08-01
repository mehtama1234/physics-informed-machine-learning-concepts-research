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
- formula_guide_count: 8
- misconception_count: 8
- diagram_count: 6
- learning_path_step_count: 7
- glossary_term_count: 10
- domain_guide_count: 5
- reader_check_count: 6
- decision_guide_count: 6
- provenance_guide_count: 6
- coverage_row_count: 14
- dependency_count: 10
- concept_ladder_count: 14
- concept_evidence_packet_count: 14
- quality_rubric_count: 6
- synthesis_guide_count: 4
- review_handoff_count: 1
- review_entrypoint_count: 27
- completion_requirement_count: 7
- review_search_intent_count: 7
- editorial_roadmap_count: 7
- source_anchor_count: 12

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

#### Hand Derivation For Physics-Informed Neural Networks
- Start: Start with an unknown field u. A few measurements tell us u at some points. The equation tells us what u should do between those points. The boundary tells us what must happen at the edge.
- data error: At measured points, the proposed field should match the observed values. This term keeps the answer tied to the sensors. Check: If this term is missing, the field may obey the equation while ignoring the actual measurements.
- equation error: Away from measured points, the proposed field can still be checked by putting it into the known equation and measuring leftover rule-breaking. Check: If this term is small only at easy points, the hard regions still need separate tests.
- boundary error: A field can satisfy the equation in the middle while using the wrong edge or starting values. This term pins down the problem being solved. Check: If boundaries are wrong, the solution can be a solution to a different physical problem.
- Final line: The loss is a written contract: match the measurements, obey the equation, and respect the edge information. The contract is only useful if each part matches the real scientific job.

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

#### Hand Derivation For Operator Learning
- Start: Start with many solved cases. Each case has a whole input field and a whole output field. The unknown object is not one solution; it is the map that turns any allowed input field into its output field.
- input field family: The learner needs to know what kind of inputs it is allowed to receive: source terms, coefficients, shapes, boundaries, or starting fields. Check: If the input family is not named, no one knows where the learned map is allowed to be used.
- field-to-field map: The useful object is the rule from whole input field to whole output field, not a lookup table for one case. Check: If only one output is tested, the page has not shown that a map was learned.
- new field test: The map earns trust only when it works on new input fields from the named family. Check: If the new field changes resolution, boundary type, or geometry, that change must be named and tested.
- Final line: The derivation is a shift in the object being learned: from one answer to a reusable map between fields.

### Surrogate Modeling
- Problem: a trusted simulator may be too slow to run for every design, control, or uncertainty question
- Observed: expensive solver inputs and outputs for a limited set of cases
- Hidden: the solver answer for every new query someone wants to ask
- Plain formula: new query -> fast stand-in -> approximate answer with a stated use range
- Failure test: compare against the full solver on new cases near the edge of the intended use
- Page: derivations/surrogate-modeling.html

#### Hand Derivation For Surrogate Modeling
- Start: Start with a trusted source that is too slow for repeated use. The scientist still needs many answers for design, search, or risk checks.
- trusted source: The stand-in needs something to imitate and something to be checked against. Check: If the trusted source is not named, the surrogate has no clear reference point.
- cheap stand-in: The learned model replaces repeated expensive calls inside a named use range. Check: If the use range is missing, speed can hide bad answers.
- edge check: Errors often matter most near the edge of the range where decisions are tempting and evidence is thin. Check: If only average error is reported, the decision quantity may still be wrong.
- Final line: A surrogate derivation is not just about fitting a curve; it is about earning a cheaper answer while keeping the trusted source in view.

### Uncertainty And Generalization
- Problem: a prediction is not enough unless the user knows when it should be believed
- Observed: training cases, validation cases, prediction errors, and known shifts between cases
- Hidden: how wrong the model may be on a case unlike the ones it learned from
- Plain formula: prediction + tested use range + failure evidence
- Failure test: move one important condition outside the training range and measure the first failure
- Page: derivations/uncertainty-and-generalization.html

#### Hand Derivation For Uncertainty And Generalization
- Start: Start with a model trained on old cases and a new case that may differ. The missing quantity is not only the prediction; it is how much trust the prediction deserves.
- prediction: The model gives an answer for the quantity the scientist asked for. Check: A prediction without a use range is incomplete.
- tested use range: The reader needs to know which cases actually support the answer. Check: If the test cases look like the training cases, changed-case trust is still unproved.
- failure evidence: Knowing where the model breaks is part of knowing where it can be used. Check: If no failure case is named, confidence is just a number without a boundary.
- Final line: The mathematical shape joins answer and boundary: report the prediction together with the evidence that says where belief should weaken.

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

#### Hand Derivation For Symbolic Regression And Model Discovery
- Start: Start with measured variables and a need for a readable law. The unknown object is the relation among the variables, not just the next predicted value.
- candidate ingredients: The search can only build formulas from measured variables and allowed operations. Check: If an important variable is missing, the best formula may still be false.
- searched formulas: Many possible short laws are tried because the correct relation is not known ahead of time. Check: If size is not controlled, the formula may only memorize noise.
- changed experiment: A readable formula becomes a scientific candidate only if it survives a new situation. Check: If it is tested only where it was found, it is not yet a law.
- Final line: The derivation is a search with a burden: the result must be short enough to inspect and strong enough to survive a new experiment.

### Foundation Models For PDEs
- Problem: one trained model may be asked to handle many related equations, grids, parameters, or physical settings
- Observed: many PDE problem instances across equations, grids, parameters, or physical settings
- Hidden: which shared structure carries from one scientific task to another
- Plain formula: many PDE tasks -> shared learned structure -> new task prediction
- Failure test: hold out a new equation family, boundary type, scale, or rare regime and compare against a trusted solver
- Page: derivations/foundation-models-for-pdes.html

#### Hand Derivation For Foundation Models For PDEs
- Start: Start with many PDE tasks. Each task teaches something about fields, equations, boundaries, or solution patterns. The new task is useful only if it shares structure the model actually learned.
- many PDE tasks: Broad training is the source of shared experience across equations or parameter ranges. Check: If the tasks are narrow, the model may only be broad in name.
- shared learned structure: The model must keep something reusable, such as field patterns, operator behavior, or equation-family regularities. Check: If the shared structure is not named, transfer to a new task is only a hope.
- new task prediction: The point is to use old task experience on a held-out scientific case. Check: If the held-out task is too similar to training, the broad claim is not tested.
- Final line: The derivation makes the transfer burden visible: old PDE tasks must carry something real into the new task, and the new task must be different enough to test that claim.


## Plain Formula Guide
### Physics-Informed Neural Networks
- Formula shape: total error = data error + equation error + boundary error
- Parts: total error, data error, equation error, boundary error
- Everyday reading: The equation gives the model a reason not to invent impossible behavior between data points.
- What to check: move the training points, inspect sharp regions, and compare against a numerical solve or held-out measurements

### Partial Differential Equations
- Formula shape: change over time = movement through space + sources + boundary effects
- Parts: change over time, movement through space, sources, boundary effects
- Everyday reading: Most physics-informed machine learning borrows its scientific burden from PDEs.
- What to check: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error

### Operator Learning
- Formula shape: input field -> learned field-to-field map -> output field
- Parts: input field, learned field-to-field map, output field
- Everyday reading: It targets repeated simulation work, where the valuable object is the whole input-output map.
- What to check: change resolution, coefficients, boundary conditions, or forcing and check whether the predicted field still satisfies the scientific quantity being claimed

### Surrogate Modeling
- Formula shape: new query -> fast stand-in -> approximate answer with a stated use range
- Parts: new query, fast stand-in, approximate answer with a stated use range
- Everyday reading: Speed changes what questions scientists and engineers can afford to ask.
- What to check: compare against the full solver on new cases near the edge of the intended use

### Uncertainty And Generalization
- Formula shape: prediction + tested use range + failure evidence
- Parts: prediction, tested use range, failure evidence
- Everyday reading: A scientific model is dangerous when it is most confident exactly where it has the least evidence.
- What to check: move one important condition outside the training range and measure the first failure

### Neural Differential Equations
- Formula shape: current state -> learned change rate -> next state
- Parts: current state, learned change rate, next state
- Everyday reading: It keeps the idea of continuous motion while admitting that part of the motion rule is unknown.
- What to check: run longer than the training window and check whether small rate errors accumulate into drift

### Symbolic Regression And Model Discovery
- Formula shape: candidate ingredients -> searched formulas -> tested small law
- Parts: candidate ingredients, searched formulas, tested small law
- Everyday reading: A compact equation can be criticized and reused in ways a large fitted object cannot.
- What to check: remove a needed variable, add noise, or test a new experiment and see whether the formula still predicts

### Foundation Models For PDEs
- Formula shape: many PDE tasks -> shared learned structure -> new task prediction
- Parts: many PDE tasks, shared learned structure, new task prediction
- Everyday reading: If it works, broad training could reduce repeated model-building for related scientific problems.
- What to check: hold out a new equation family, boundary type, scale, or rare regime and compare against a trusted solver


## Misconception Map
### Physics-Informed Neural Networks
- Correction: A PINN is a fitted field that must answer to both measured values and a known physical rule.
- First-principles test: move the training points, inspect sharp regions, and compare against a numerical solve or held-out measurements
- Wrong turns: A weak answer says only that the neural network fits data.; The page reports only training error.; The hard region has few check points.; The equation is known to be incomplete for the experiment.; No comparison is made against held-out measurements or a trusted solver.

### Partial Differential Equations
- Correction: A PDE is a rule for how a whole field changes across space and time.
- First-principles test: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error
- Wrong turns: The boundary condition is vague.; The learned answer ignores conservation.; The grid or resolution changes the conclusion.; Small visual error hides a large error in the quantity people care about.

### Operator Learning
- Correction: Operator learning tries to learn the machine that turns one field into another field.
- First-principles test: change resolution, coefficients, boundary conditions, or forcing and check whether the predicted field still satisfies the scientific quantity being claimed
- Wrong turns: A weak answer says only that the model is fast.; The training family is not named.; Only one resolution is tested.; The output looks plausible but physical quantities are not checked.; The model is used on a new boundary type without evidence.

### Surrogate Modeling
- Correction: A surrogate is a faster stand-in for a slower trusted process.
- First-principles test: compare against the full solver on new cases near the edge of the intended use
- Wrong turns: A weak answer treats speed as trust.; The surrogate is described without its use range.; The edge cases are not tested.; The output metric ignores the decision people actually make.; The full solver is never used again for spot checks.

### Uncertainty And Generalization
- Correction: This topic asks when a prediction should be believed on a case the model did not learn from.
- First-principles test: move one important condition outside the training range and measure the first failure
- Wrong turns: A weak answer reports one score without saying what changed.; Only familiar cases are reported.; The test set differs from training only in name.; Rare regimes are averaged away.; No one states what condition would make the model unusable.

### Neural Differential Equations
- Correction: A neural differential equation learns the missing rule for how a system changes.
- First-principles test: run longer than the training window and check whether small rate errors accumulate into drift
- Wrong turns: The model is tested only over short times.; Small rate errors accumulate unnoticed.; Known conservation or stability behavior is not checked.; The learned rate fits noise instead of mechanism.

### Symbolic Regression And Model Discovery
- Correction: Symbolic regression searches for a short formula that explains measured behavior.
- First-principles test: remove a needed variable, add noise, or test a new experiment and see whether the formula still predicts
- Wrong turns: A weak answer trusts a neat formula because it fits the original data.; Important variables were never measured.; The formula is selected only on the original data.; Noise creates a fake term.; The search space could not express the real mechanism.

### Foundation Models For PDEs
- Correction: A PDE foundation model tries to reuse structure across many related field-prediction tasks.
- First-principles test: hold out a new equation family, boundary type, scale, or rare regime and compare against a trusted solver
- Wrong turns: A weak answer treats broad training size as proof of broad scientific trust.; The held-out test is too similar to training.; Rare regimes are missing.; New boundaries or quantities are assumed rather than tested.; Scale is treated as a substitute for scientific validation.


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
- Why here: Physics-informed machine learning is not one trick. The method depends on the scientific job, the evidence in hand, and the changed case where a wrong answer would matter.
- Goal: Name the quantity, the domain, the evidence, and the changed case before naming a method.
- First-principles spine: World: a scientist needs an answer for a real quantity.; Evidence: measurements, equations, simulations, or old cases give partial support.; Missing piece: the quantity needed for the next case is not directly known.; Mathematical move: choose the smallest learning route that carries the needed evidence.; Reject it when: a changed case breaks the quantity the scientist actually needs.
- Checkpoint: You can say what answer the scientist wants and what would make that answer unusable.

### 2. Understand Fields And Equations
- Question: Why is one number not enough?
- Why here: Many scientific problems are fields: temperature, pressure, velocity, concentration, stress, or displacement across space and time.
- Goal: See why boundaries, neighbors, rates of change, and starting values carry the scientific burden.
- First-principles spine: World: the answer lives across space or time, not in one number.; Evidence: some values, edges, starting values, and physical rules are known.; Missing piece: the full field is unknown between measured or simulated cases.; Mathematical move: describe how nearby values, rates, and boundaries restrict the answer.; Reject it when: the field violates edges, neighbors, or measured behavior in a changed case.
- Checkpoint: You can explain why a field prediction must respect boundaries and nearby values.

### 3. Use Physics As A Check
- Question: How can a model be corrected where there are no measurements?
- Why here: Sparse data leaves empty space. A known equation can check that empty space if the equation is trusted.
- Goal: Understand PINNs as fitted fields that answer to both data and an equation.
- First-principles spine: World: the true field should obey a known physical rule.; Evidence: measured points, boundaries, starting values, and the equation are available.; Missing piece: most field values are unmeasured.; Mathematical move: score both data mismatch and equation mismatch.; Reject it when: the fitted field matches points but breaks the equation, boundary, or changed test case.
- Checkpoint: You can state the data error, equation error, boundary error, and the test case.

### 4. Learn Maps Between Fields
- Question: What if the job is not one solution, but many related solutions?
- Why here: Engineering and science often need repeated solves for many inputs, shapes, materials, or conditions.
- Goal: Separate learning one answer from learning the map that turns an input field into an output field.
- First-principles spine: World: many related scientific cases share an input-to-output relation.; Evidence: solved examples show input fields paired with output fields.; Missing piece: the full output field for a new input is unknown.; Mathematical move: learn the map from whole input fields to whole output fields.; Reject it when: a new input outside the learned family gives a bad field or a bad scientific quantity.
- Checkpoint: You can name the family of inputs and outputs where the learned map is allowed to be used.

### 5. Use Speed Without Hiding Risk
- Question: When is a fast approximation useful?
- Why here: A fast model is valuable only if the slow trusted source still defines where the fast answer is valid.
- Goal: Treat surrogates as checked stand-ins with a stated use range.
- First-principles spine: World: the scientist needs many answers faster than the trusted source can provide them.; Evidence: trusted simulations or experiments define examples and limits.; Missing piece: a cheap answer is needed for repeated choices.; Mathematical move: train a stand-in and compare it against the trusted source inside a named range.; Reject it when: speed hides error near the edge of the range or in the quantity used for the decision.
- Checkpoint: You can say what the surrogate replaces, what it does not replace, and where it was checked.

### 6. Make Trust A Testable Claim
- Question: When should a prediction be believed?
- Why here: Scientific mistakes often happen when a model is used outside the cases that taught it.
- Goal: Attach every prediction to a use range, changed-case test, and failure boundary.
- First-principles spine: World: the next scientific case may differ from the old cases.; Evidence: training and validation cases show only part of the possible range.; Missing piece: the model's reliability on the new case is unknown.; Mathematical move: measure error, doubt, and changed-case behavior instead of reporting only a prediction.; Reject it when: the model stays confident where the evidence no longer supports confidence.
- Checkpoint: You can name the first changed condition that should make the model fail.

### 7. Look For Readable Laws When Needed
- Question: When is prediction not enough?
- Why here: Sometimes the scientific product is a rule people can inspect, criticize, and reuse.
- Goal: Understand symbolic regression and neural differential equations as routes toward candidate mechanisms.
- First-principles spine: World: the scientist wants a rule, not only an answer.; Evidence: measured variables and changes over time suggest possible relations.; Missing piece: the governing relation is unknown.; Mathematical move: search for a small rule or learned rate that explains the observations.; Reject it when: the rule fails a new experiment or depends on a missing variable.
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


## Concept Dependency Map
### Physics-Informed Neural Networks
- Learn first: Partial Differential Equations, Deep Learning, Optimization For Learning
- Why: A PINN combines a fitted neural network, a differential equation check, and a training score.
- Confusion prevented: Without the dependencies, a reader may think a PINN is just a neural network with physics language attached.

### Operator Learning
- Learn first: Partial Differential Equations, Deep Learning, Surrogate Modeling
- Why: Operator learning makes sense when the job is a fast map between full fields across many related solves.
- Confusion prevented: Without fields and surrogates, a reader may mistake it for one more predictor on a table.

### Surrogate Modeling
- Learn first: Deep Learning, Uncertainty And Generalization
- Why: A surrogate is useful only when its repeated query family and tested use range are named.
- Confusion prevented: Without uncertainty, speed can be mistaken for scientific trust.

### Uncertainty And Generalization
- Learn first: Deep Learning, Scientific Machine Learning
- Why: Uncertainty and generalization ask whether fitted behavior survives a changed scientific case.
- Confusion prevented: Without the scientific job, uncertainty can look like a decorative confidence number.

### Neural Differential Equations
- Learn first: Partial Differential Equations, Deep Learning, Optimization For Learning
- Why: The learned part is a rate or missing change rule placed inside a time-evolution calculation.
- Confusion prevented: Without differential equations, a reader may miss why small rate errors can accumulate over time.

### Symbolic Regression And Model Discovery
- Learn first: Optimization For Learning, Uncertainty And Generalization
- Why: Symbolic regression searches for a readable rule, then needs changed-case tests to reject neat but wrong formulas.
- Confusion prevented: Without changed-case testing, a compact equation can be mistaken for truth.

### Graphs And Geometric Learning
- Learn first: Deep Learning, Scientific Machine Learning
- Why: Geometric learning keeps connections, shapes, and symmetries visible inside learned prediction.
- Confusion prevented: Without the scientific object, graph structure can look like a modeling fashion rather than required information.

### Attention For Scientific Fields
- Learn first: Operator Learning, Graphs And Geometric Learning
- Why: Attention is a way to move selected information across large fields or connected objects.
- Confusion prevented: Without fields and connections, attention can be misread as proof that all important interactions were captured.

### Generative Modeling
- Learn first: Deep Learning, Uncertainty And Generalization
- Why: Generated scientific samples need checks for validity, rarity, and downstream use.
- Confusion prevented: Without validation, plausible samples can be mistaken for physically useful samples.

### Foundation Models For PDEs
- Learn first: Operator Learning, Partial Differential Equations, Uncertainty And Generalization
- Why: Broad PDE models depend on field-to-field maps, equation families, and tests on held-out task families.
- Confusion prevented: Without these dependencies, scale can be mistaken for coverage of a new scientific case.


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


## Concept Evidence Packets
### Deep Learning
- Problem: scientists often have examples of behavior but no short rule that predicts the next case
- Domain: scientific prediction from large measured or simulated data sets
- Evidence anchors: 6
- Packet: evidence-packets/deep-learning.html

### Physics-Informed Neural Networks
- Problem: measurements may be sparse, but the answer must still respect a known physical equation
- Domain: differential equations in science and engineering
- Evidence anchors: 6
- Packet: evidence-packets/physics-informed-neural-networks.html

### Partial Differential Equations
- Problem: a quantity changes over space and time, so one number is not enough to describe the situation
- Domain: fluids, heat, waves, mechanics, chemistry, climate, and other changing fields
- Evidence anchors: 6
- Packet: evidence-packets/partial-differential-equations.html

### Operator Learning
- Problem: one simulation answer is not enough when engineers need the whole map from inputs to solution fields
- Domain: fast prediction for families of scientific simulations
- Evidence anchors: 6
- Packet: evidence-packets/operator-learning.html

### Scientific Machine Learning
- Problem: scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time
- Domain: using data-driven models inside scientific workflows
- Evidence anchors: 6
- Packet: evidence-packets/scientific-machine-learning.html

### Surrogate Modeling
- Problem: a trusted simulator may be too slow to run for every design, control, or uncertainty question
- Domain: expensive simulation and design loops
- Evidence anchors: 6
- Packet: evidence-packets/surrogate-modeling.html

### Uncertainty And Generalization
- Problem: a prediction is not enough unless the user knows when it should be believed
- Domain: model use under new conditions
- Evidence anchors: 6
- Packet: evidence-packets/uncertainty-and-generalization.html

### Optimization For Learning
- Problem: learning needs a way to decide which model settings are better or worse
- Domain: turning model fitting into a repeatable computation
- Evidence anchors: 6
- Packet: evidence-packets/optimization-for-learning.html

### Generative Modeling
- Problem: some tasks need many possible examples, not one predicted answer
- Domain: creating plausible scientific samples, fields, or candidate designs
- Evidence anchors: 6
- Packet: evidence-packets/generative-modeling.html

### Graphs And Geometric Learning
- Problem: many scientific objects are not simple rows of numbers; their connections matter
- Domain: systems made of interacting parts, meshes, molecules, or spatial relations
- Evidence anchors: 6
- Packet: evidence-packets/graphs-and-geometric-learning.html

### Neural Differential Equations
- Problem: scientists may know that a system changes continuously but not know the exact rule for that change
- Domain: changing systems where time evolution is part of the model
- Evidence anchors: 6
- Packet: evidence-packets/neural-differential-equations.html

### Symbolic Regression And Model Discovery
- Problem: a scientist may need a readable equation, not only a model that predicts well
- Domain: turning data into equations people can inspect
- Evidence anchors: 6
- Packet: evidence-packets/symbolic-regression.html

### Foundation Models For PDEs
- Problem: one trained model may be asked to handle many related equations, grids, parameters, or physical settings
- Domain: broad families of PDE problems and scientific fields
- Evidence anchors: 6
- Packet: evidence-packets/foundation-models-for-pdes.html

### Attention For Scientific Fields
- Problem: a local patch of a field may depend on faraway information, but looking everywhere can be expensive
- Domain: large scientific fields where distant parts may interact
- Evidence anchors: 6
- Packet: evidence-packets/attention-for-scientific-fields.html


## Selected Source Anchors

### Physics Informed Neural Networks
- Source: ETH Zurich AISE 2025: Lecture 3 Physics-Informed Neural Networks Introduction
- Page: videos/eth-aise-2025-003-eth-zrich-aise-2025-lecture-3-physics-informed-neural-networks-introduction.html
- Claim anchored: PINNs are introduced as learned fields checked against both measured data and physical equations.
- Why this source: This is the 2025 introductory PINNs lecture in the local transcript set.
- Limit: The source supports the course placement and core idea; it does not prove performance on every PDE or boundary setting.

- Source: ETH Zurich AISE 2025: Lecture 4 PINNs Theoretical Insights
- Page: videos/eth-aise-2025-004-eth-zrich-aise-2025-lecture-4-pinns-theoretical-insights.html
- Claim anchored: PINNs need theory and failure checks because satisfying a written training score is not the same as proving the field is right everywhere.
- Why this source: This lecture is the 2025 theory follow-up for PINNs.
- Limit: The source anchors the need for theoretical care; the page still needs task-specific validation for any scientific claim.


### Operator Learning
- Source: ETH Zurich AISE 2025: Lecture 5 Operator Learning Introduction
- Page: videos/eth-aise-2025-005-eth-zrich-aise-2025-lecture-5-operator-learning-introduction.html
- Claim anchored: Operator learning is about learning maps from whole input fields or functions to whole output fields or functions.
- Why this source: This is the 2025 introduction to the operator-learning block.
- Limit: The source supports the object being learned; it does not prove the learned map works outside the named input family.

- Source: ETH Zurich AISE 2025: Lecture 6 Operator Learning FNO
- Page: videos/eth-aise-2025-006-eth-zrich-aise-2025-lecture-6-operator-learning-fno.html
- Claim anchored: Fourier neural operators are one route for learning field-to-field maps in PDE settings.
- Why this source: This lecture is the 2025 FNO treatment inside the operator-learning sequence.
- Limit: The source anchors the method family; reliability still depends on the training range, resolution, geometry, and target quantity.


### Surrogate Modeling
- Source: ETH Zurich AISE 2024: Introduction to Hybrid Workflows Part 1
- Page: videos/eth-aise-2024-019-eth-zrich-aise-introduction-to-hybrid-workflows-part-1.html
- Claim anchored: Surrogates are useful when repeated scientific choices need answers faster than a trusted simulation or experiment can provide them.
- Why this source: This lecture starts the local hybrid-workflow block where learned components are placed next to trusted scientific tools.
- Limit: The source supports the need for faster learned components; it does not prove a surrogate is valid outside checked cases.

- Source: ETH Zurich AISE 2024: Introduction to Hybrid Workflows Part 2
- Page: videos/eth-aise-2024-020-eth-zrich-aise-introduction-to-hybrid-workflows-part-2.html
- Claim anchored: A learned stand-in remains tied to the trusted source and must be checked where it will be used.
- Why this source: This lecture continues the hybrid-workflow treatment in the local transcript set.
- Limit: The source supports the review route; task-level error checks are still needed before using any stand-in for a decision.


### Uncertainty And Generalization
- Source: ETH Zurich AISE 2024: Windowed Attention and Scaling Laws
- Page: videos/eth-aise-2024-018-eth-zrich-aise-windowed-attention-and-scaling-laws.html
- Claim anchored: Trust depends on changed-case behavior, not only on matching familiar examples.
- Why this source: This source sits in the sequence where model behavior is discussed beyond a single training case.
- Limit: The source anchors the need to discuss scale and changed behavior; it does not certify uncertainty estimates for a specific domain.

- Source: ETH Zurich AISE 2025: Lecture 12 Foundation Models for PDEs Poseidon
- Page: videos/eth-aise-2025-012-eth-zrich-aise-2025-lecture-12-foundation-models-for-pdes-poseidon.html
- Claim anchored: Foundation and operator-style PDE models need evaluation on held-out scientific cases before broad use.
- Why this source: This lecture anchors the broad PDE-model part of the 2025 playlist.
- Limit: The source supports the need for held-out case checks; it does not prove broad transfer for every equation family.


### Symbolic Regression
- Source: ETH Zurich AISE 2024: Symbolic Regression and Model Discovery
- Page: videos/eth-aise-2024-024-eth-zrich-aise-symbolic-regression-and-model-discovery.html
- Claim anchored: Symbolic regression aims for a readable candidate law, not just a fitted prediction.
- Why this source: This is the local lecture dedicated to symbolic regression and model discovery.
- Limit: The source supports the concept and goal; a discovered law still needs a new-experiment test and measured variables that cover the real cause.

- Source: ETH Zurich AISE 2024: Neural Differential Equations
- Page: videos/eth-aise-2024-021-eth-zrich-aise-neural-differential-equations.html
- Claim anchored: Neural differential equations are a related route when the unknown object is the rate or rule of change.
- Why this source: This lecture anchors the neighboring model-discovery route in the source set.
- Limit: The source supports the relation between learned dynamics and model discovery; it does not prove interpretability by itself.


### Foundation Models For Pdes
- Source: ETH Zurich AISE 2025: Lecture 12 Foundation Models for PDEs Poseidon
- Page: videos/eth-aise-2025-012-eth-zrich-aise-2025-lecture-12-foundation-models-for-pdes-poseidon.html
- Claim anchored: Foundation PDE models try to carry structure from many PDE tasks into a new PDE case.
- Why this source: This lecture is the 2025 source page for foundation models for PDEs.
- Limit: The source anchors the ambition and lecture treatment; the page must still state which new PDE case was held out and what failed.

- Source: ETH Zurich AISE 2025: Lecture 5 Operator Learning Introduction
- Page: videos/eth-aise-2025-005-eth-zrich-aise-2025-lecture-5-operator-learning-introduction.html
- Claim anchored: Broad PDE models build on operator-learning ideas because both care about maps between fields across many cases.
- Why this source: This lecture anchors the operator-learning prerequisite for later broad PDE models.
- Limit: The source supports the dependency; it does not imply that a broad model works on every PDE family.


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
- Claim: Physics-informed machine learning asks how a learned answer can stay tied to the real scientific problem when measurements are sparse, equations are partial, simulations are costly, and future cases are different.
- Explanation: Start with the world, not the model. A scientist needs a quantity such as a temperature field, a force, a molecule property, or a failure risk. The available evidence is incomplete: some measurements, some equations, some solved cases, some trusted simulations. The mathematical job is to carry that evidence into a new case while leaving a clear test that can reject the answer.
- Reader takeaway: A strong explanation names five things: the real quantity, the evidence, the missing quantity, the mathematical move, and the changed case that could reject the claim.

### Main Moves
- Claim: The main mathematical moves are different answers to different shortages: too few measurements, too many related solves, too much simulation cost, too much change between cases, or too little understanding of the rule.
- Explanation: PINNs add equation checks where measurements are missing. Operator learning learns a field-to-field map when many related solves are needed. Surrogates build a fast checked stand-in when the trusted source is too slow. Uncertainty asks when belief should weaken. Symbolic regression asks whether the data can support a readable rule.
- Reader takeaway: Choose the move by naming the shortage first. If the shortage is unclear, the method choice is not yet justified.

### Proof Burden
- Claim: A method name never proves a scientific claim. The claim needs a test tied to the domain quantity the scientist will use.
- Explanation: A transcript mention shows that a topic appears in the course. A training score shows that a model matched a written score. Neither one alone proves that the model is safe for a new scientific use. The page has to state the domain, quantity, use range, evidence, and failure test.
- Reader takeaway: Every strong page should say what the source supports, what remains unproved, and what changed case would expose a bad claim.

### Field Map
- Claim: The field is best read as a map from scientific jobs to mathematical moves, not as a list of model names.
- Explanation: Sparse measurements point toward physics checks. Many solved fields point toward operator learning. Repeated costly decisions point toward surrogates. New settings point toward uncertainty. Need for a readable law points toward model discovery. Each route starts with a real quantity and ends with a failure test.
- Reader takeaway: Start from the job, identify the shortage, then choose the concept family that carries the right evidence.


## Review Handoff
- Purpose: Give a reviewer the shortest reliable route through the package and the checks that prove the generated site is coherent.

### Start Here
- Field Synthesis: synthesis.html
- Learning Path: learning-path.html
- Coverage Matrix: coverage.html
- Editorial Roadmap: editorial-roadmap.html
- Decision Guide: decision-guide.html
- Provenance: provenance.html

### Remaining Editorial Work
- Use the editorial roadmap to turn the strongest generated pages into hand-written teaching pages.
- Add lecture-specific quotes after checking the transcript excerpts against the source videos.
- Add real figures or mathematical sketches where a static flow diagram is not enough.
- Deepen the derivations where the current page names the formula shape but does not yet walk through enough algebra.

## Review Entrypoints

### Start The Review
- Purpose: Use these pages to see the whole argument before inspecting details.
- Review Handoff: handoff.html | What exists now, and what still needs hand-written depth?
- Find Pages By Question: review-search.html | Which page should I open for the question I have right now?
- Completion Audit: completion-audit.html | What is locally verified, and what is still outside the workspace?
- Editorial Roadmap: editorial-roadmap.html | What is the meaty next goal after the generated first pass?
- Field Synthesis: synthesis.html | What problem holds the field together?
- Learning Path: learning-path.html | What should a new reader read first, second, and third?
- Concept Ladder: concept-ladder.html | Can each concept be explained without starting from the method name?
- Dependency Map: dependencies.html | Which missing prerequisite is making the concept feel vague?
- Core Derivations: derivations.html | Can the reader see how the formula shape follows from the scientific problem?
- Formula Guide: formula-guide.html | Can the reader understand what the formula carries without knowing notation first?
- Misconception Map: misconceptions.html | Which vague or overconfident explanation should the reader avoid?

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
- Evidence Packets: evidence-packets.html | Can a reviewer audit one concept without hunting through the whole site?
- Quality Rubric: quality.html | Does each page avoid empty language and explain the real problem?
- Provenance: provenance.html | Could another CLI rebuild this package from the same sources?
- Cross-Channel Playbook: provenance/cross-channel-playbook.html | What exact source, concept, evidence, page, and validation steps should the next build follow?

## Find Pages By Question

### I need the big picture first.
- Look for: central problem, field map, learning order, and completion state
- Completion Audit: completion-audit.html
- Editorial Roadmap: editorial-roadmap.html
- Field Synthesis: synthesis.html
- Learning Path: learning-path.html
- Review Handoff: handoff.html

### I need to know the next serious goal.
- Look for: priorities, hand-written depth tasks, target pages, and acceptance checks
- Editorial Roadmap: editorial-roadmap.html
- Review Entrypoints: review-entrypoints.html
- Quality Rubric: quality.html
- Core Derivations: derivations.html

### I need to understand a concept from first principles.
- Look for: problem, observed evidence, hidden quantity, formula shape, and failure test
- Concept Ladder: concept-ladder.html
- Dependency Map: dependencies.html
- Formula Guide: formula-guide.html
- Misconception Map: misconceptions.html

### I need transcript support for a claim.
- Look for: source video, transcript excerpt, support limit, and review links
- Evidence Packets: evidence-packets.html
- Evidence Ledger: evidence-ledger.html
- Transcripts: transcripts.html
- Coverage Matrix: coverage.html

### I need to choose a method for a scientific job.
- Look for: domain, quantity, method route, use range, and required evidence
- Decision Guide: decision-guide.html
- Domain Guides: domains.html
- Worked Examples: worked-examples.html
- Comparisons: comparisons.html

### I need to audit quality.
- Look for: plain language, failure boundary, evidence discipline, and connected map
- Quality Rubric: quality.html
- Reader Checks: reader-checks.html
- Misconception Map: misconceptions.html
- Completion Audit: completion-audit.html

### I need another CLI to reproduce this for a different channel.
- Look for: source capture, transcript extraction, analysis build, site generation, and review gates
- Cross-Channel Playbook: provenance/cross-channel-playbook.html
- CLI Reproduction Checklist: provenance/cli-reproduction.html
- Transcript Extraction: provenance/transcript-extraction.html
- Analysis Build: provenance/analysis-build.html

## Editorial Roadmap
### P0 Pin Down The Core Argument
- Goal: Make the first review route say one thing clearly: physics-informed machine learning is about making learned answers answerable to data, physical rules, and changed scientific cases.
- Why it matters: Without this, readers see a pile of methods. With it, every concept becomes a different answer to the same scientific pressure.
- Target pages: synthesis.html, learning-path.html, handoff.html, completion-audit.html
- Work: Rewrite the opening paragraphs so they start from the scientific problem before naming methods.; Make every route explain what is observed, what is hidden, what rule is kept, and what changed case can reject the claim.; Remove any sentence that sounds impressive but does not name evidence, domain, quantity, or failure test.
- Acceptance check: A new reader can say the field's common problem in one sentence before opening any topic page.

### P0 Add Source Anchors To Core Concepts
- Goal: Turn the main topic pages and evidence packets into source-backed teaching pages, not only generated summaries.
- Why it matters: The package is transcript-backed only if the important claims point to lecture-specific support and state what that support does not prove.
- Target pages: topics/physics-informed-neural-networks.html, topics/operator-learning.html, topics/uncertainty-and-generalization.html, topics/foundation-models-for-pdes.html, evidence-packets.html
- Work: Manually review the transcript excerpts for each core concept and choose the best source anchors.; Add a short source note beside each major claim: what the lecture supports, and what it does not settle.; Prefer concrete lecture moments over broad statements.
- Acceptance check: Each core concept has at least two reviewed transcript anchors and one clear limit statement.

### P0 Deepen The Hand Derivations
- Goal: Make the math feel inevitable from the problem instead of appearing as a finished formula.
- Why it matters: The reader should see why the terms show up: data error comes from measured points, physics error comes from the equation, uncertainty comes from possible wrong answers, and operators come from learning a map between fields.
- Target pages: derivations.html, derivations/physics-informed-neural-networks.html, derivations/operator-learning.html, derivations/foundation-models-for-pdes.html, formula-guide.html
- Work: Add one handwritten derivation from observed evidence to loss shape for PINNs.; Add one derivation showing why operator learning maps a whole input field to a whole output field.; Add one derivation showing what must be shared before a PDE model can transfer to a new equation case.; Keep each line in everyday language before adding symbols.
- Acceptance check: A reader who skips the formula can still explain why each term exists and what would make it fail.

### P1 Add Figures And Mathematical Sketches
- Goal: Replace purely textual explanation where a picture would reveal the object being learned or checked.
- Why it matters: Some ideas are spatial: a PDE field, a boundary, a residual point, an input field, an output field, or a shifted test case. A sketch can make the hidden quantity visible.
- Target pages: diagrams.html, topics/physics-informed-neural-networks.html, topics/operator-learning.html, topics/surrogate-modeling.html, topics/uncertainty-and-generalization.html
- Work: Add one sketch for measured points plus equation-check points.; Add one sketch for input field to output field.; Add one sketch for a fast surrogate inside repeated scientific choices.; Add one sketch for a shifted case where the model should admit doubt.
- Acceptance check: Each sketch names input, output, kept rule, and failure case in the caption.

### P1 Strengthen Domain Examples
- Goal: Make chemistry, materials, climate, fluids, and geometry pages show real scientific jobs rather than generic use cases.
- Why it matters: The math matters because a scientist needs a quantity for a decision: a molecule property, stress field, flow force, climate risk, or field on an irregular shape.
- Target pages: domains.html, worked-examples.html, worked-examples/molecule-property-from-structure.html, worked-examples/material-stress-from-sparse-tests.html, worked-examples/climate-risk-under-shifted-conditions.html
- Work: Add one richer concrete example per domain.; Name the observed evidence, hidden quantity, decision, and changed-case test.; Tie each example back to one concept page, one derivation, and one evidence packet.
- Acceptance check: Each domain page contains a concrete scientific job that cannot be mistaken for a generic prediction task.

### P1 Sharpen Nearby Method Comparisons
- Goal: Make the comparison pages teach what changes when two methods sound similar.
- Why it matters: Readers often confuse fitting data, obeying a rule, learning a solver shortcut, and building a cheap stand-in. The package should separate those by job and evidence.
- Target pages: comparisons.html, decision-guide.html, misconceptions.html, dependencies.html
- Work: For each comparison, add one situation where the left method is right and one where the right method is right.; Add one wrong-choice example and the evidence that would expose it.; Keep the language tied to the scientific job, not method labels.
- Acceptance check: A reader can choose between two nearby methods by naming the job, evidence, and failure case.

### P2 Finish Replication And Remote State
- Goal: Make the package easy for another CLI to reproduce and push once the GitHub repository exists.
- Why it matters: Local validation proves the package files. The final handoff also needs a verified remote so another person can clone and continue.
- Target pages: provenance/cross-channel-playbook.html, provenance.html, completion-audit.html, handoff.html
- Work: Create or grant access to the GitHub repository named by origin.; Push main and verify the branch exists remotely.; Record the clone URL and latest commit in the handoff.
- Acceptance check: git ls-remote origin main returns a commit hash that matches the local main branch.


## Completion Audit
### Preserve transcript-backed source material for the two playlist family.
- Status: locally verified
- Evidence: summary reports 2 playlists, 40 videos, and 40 available transcripts; provenance pages name playlists, caption extraction, and local files.

### Explain mathematical concepts from first principles without assuming prior jargon.
- Status: locally verified
- Evidence: topic pages, concept ladder, glossary, derivations, and quality rubric require problem, domain, observed evidence, hidden quantity, formula shape, and failure test.

### Connect concepts to real domains and concrete scientific jobs.
- Status: locally verified
- Evidence: summary reports 5 domain guides and 8 worked examples; worked examples include end-to-end flow traces.

### Separate transcript support from proof and show limits of every claim.
- Status: locally verified
- Evidence: evidence ledger and 14 concept evidence packets state transcript anchors, review links, and what evidence does not prove.

### Give reviewers and another CLI an end-to-end route through the package.
- Status: locally verified
- Evidence: review map, editorial roadmap, handoff, provenance, and cross-channel playbook name review route, extraction steps, build outputs, next tasks, and validation checks.

### Run local checks proving generated pages, links, counts, and wording gates are coherent.
- Status: locally verified
- Evidence: make check runs Python compile, build validation, and standalone generated-site validation; validator expects the manifest page count and required sections.

### Create or verify the GitHub remote repository and push main.
- Status: external blocker
- Evidence: local origin is configured, but GitHub currently returns Repository not found for the configured URL.

