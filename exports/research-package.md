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
- deep_dive_count: 14
- teaching_note_count: 14
- core_derivation_count: 14
- formula_guide_count: 14
- misconception_count: 14
- diagram_count: 9
- sketch_count: 4
- learning_path_step_count: 12
- glossary_term_count: 15
- domain_guide_count: 9
- reader_check_count: 14
- decision_guide_count: 13
- provenance_guide_count: 6
- coverage_row_count: 14
- dependency_count: 10
- concept_ladder_count: 14
- concept_evidence_packet_count: 14
- quality_rubric_count: 6
- synthesis_guide_count: 4
- review_handoff_count: 1
- review_entrypoint_count: 29
- completion_requirement_count: 8
- review_search_intent_count: 7
- review_queue_count: 14
- review_queue_p0_count: 0
- review_queue_p1_count: 0
- hand_polish_review_count: 14
- editorial_roadmap_count: 7
- editorial_roadmap_completed_count: 7
- source_anchor_count: 28
- meaty_goal_count: 1
- meaty_goal_coverage_count: 14

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
- Concrete family case: A lab wants the temperature inside a wall, but sensors only touch a few points. The heat equation is not extra decoration; it is the reason the unsensed middle is not free to take any shape it wants.
- What the math buys: The equation turns empty space between measurements into a checkable demand. The model cannot claim success only by touching the measured points.
- Failure boundary: This family fails when the written equation is incomplete, the boundary information is wrong, or the training process avoids the hard regions where the rule matters most.

#### Why The Concepts Appear In This Order
- The PDE comes first because it says what kind of object the answer is: a field tied together by neighbors, time, and boundaries.
- The PINN appears next because the field is unknown and must be fitted while still answering to the equation.
- Optimization appears because fitting is not wishing; the model follows the written error score, including any bad weighting choices.
- Uncertainty appears last because a fitted field is still only useful inside the changed cases where it has been tested.

#### Evidence Chain To Track
- which measured values anchor the answer
- which rule is trusted enough to police the empty places
- which boundary or starting information defines the physical case
- which changed boundary, source, scale, or hard region could reject the result

#### Concept Responsibilities
- Partial Differential Equations: handles a quantity changes over space and time, so one number is not enough to describe the situation Keeps: a field, its rates of change, and the boundary or starting information needed to evolve it Failure: a learned shortcut can ignore boundary conditions or conservation behavior that the PDE was carrying
- Physics-Informed Neural Networks: handles measurements may be sparse, but the answer must still respect a known physical equation Keeps: a neural network prediction plus a penalty for violating the known equation Failure: the equation penalty can look small while the solution is wrong in hard regions, sharp layers, or unseen boundary cases
- Optimization For Learning: handles learning needs a way to decide which model settings are better or worse Keeps: a written score that compares model output against data, physics penalties, or design goals Failure: a model can optimize the written score while missing the scientific behavior the score failed to name
- Uncertainty And Generalization: handles a prediction is not enough unless the user knows when it should be believed Keeps: error checks, changed-case tests, and limits on where the model was trained Failure: training error can look good while the model fails under a new geometry, parameter range, sensor, or physical regime

#### Evidence Needed Before Trusting The Family
- Strong evidence: the route names the scientific quantity, input family, output quantity, and changed-case test.
- Too weak: the family is described as useful, fast, broad, or accurate without a rejecting changed case.

### Neural Operators Family
- Problem: One solved simulation is not enough; the scientific job needs the map from many inputs to many full fields.
- Domain: repeated PDE solves, design sweeps, weather-like fields, fluids, materials, and parameter studies
- Concrete family case: A research group has thousands of solved flow cases for different inlet shapes. The next useful object is not one more solved flow; it is a checked way to turn a new inlet field into the whole resulting flow field.
- What the math buys: The object being learned is a map between functions. That matters because a field is not a single row of numbers; it is a whole spatial object.
- Failure boundary: This family fails when the new query is outside the learned family, when resolution changes reveal hidden errors, or when the output looks smooth but breaks the physical claim.

#### Why The Concepts Appear In This Order
- Operator learning comes first because the thing being learned is the whole input-field to output-field map.
- Surrogate modeling names the practical reason this map matters: repeated solves are too slow for design or exploration.
- Attention and geometric structure appear when local neighborhoods are not enough to carry the field information.
- Foundation models appear only after many task families exist, and their burden is proving that a new task shares the structure learned from old tasks.

#### Evidence Chain To Track
- which family of equations, boundaries, geometries, grids, and parameters was included
- which full-field quantity the model must return
- which field structure the architecture keeps visible
- which held-out family or changed resolution could expose a smooth but wrong field

#### Concept Responsibilities
- Operator Learning: handles one simulation answer is not enough when engineers need the whole map from inputs to solution fields Keeps: a learned map from a forcing, coefficient, shape, or starting field to a solution field Failure: the learned map can give plausible-looking fields that violate the equation or fail on a shifted input family
- Surrogate Modeling: handles a trusted simulator may be too slow to run for every design, control, or uncertainty question Keeps: the input-output behavior needed for a specified family of queries Failure: speed can hide missing physics when the surrogate is used beyond the regime where it was checked
- Attention For Scientific Fields: handles a local patch of a field may depend on faraway information, but looking everywhere can be expensive Keeps: selected interactions between parts of the input field Failure: windowing or scaling choices can miss long-range effects that matter for the scientific quantity being predicted
- Foundation Models For PDEs: handles one trained model may be asked to handle many related equations, grids, parameters, or physical settings Keeps: shared structure across many scientific problem instances Failure: the model can look broad while missing rare regimes, new boundary conditions, or quantities not represented in training

#### Evidence Needed Before Trusting The Family
- Strong evidence: the route names the scientific quantity, input family, output quantity, and changed-case test.
- Too weak: the family is described as useful, fast, broad, or accurate without a rejecting changed case.

### Model Discovery Family
- Problem: Prediction alone is not enough when the scientist needs a readable law or missing change rule.
- Domain: mechanism discovery, dynamics, lab measurements, simplified physical laws, and interpretable scientific modeling
- Concrete family case: A scientist records how a chemical concentration changes but does not know the rate law. The goal is not merely to predict the next measurement; the goal is to find a small candidate rule that can be argued about and tested in a new experiment.
- What the math buys: A compact equation is easier to inspect, criticize, and reuse than a large fitted object. The math turns a fit into a candidate explanation.
- Failure boundary: This family fails when the needed variable was not measured, the experiment did not excite the important behavior, or the search space cannot express the true rule.

#### Why The Concepts Appear In This Order
- Symbolic regression appears when the desired answer is a readable formula, not only a large fitted predictor.
- Neural differential equations appear when the missing object is a rate rule that moves the state through time.
- Scientific machine learning keeps the proposed rule tied to measured variables, units, and known scientific constraints.
- Optimization appears because the search is shaped by the score, the candidate operations, and the penalty for extra terms that do not earn their keep.

#### Evidence Chain To Track
- which variables were actually measured
- which hidden mechanism or rate rule is being proposed
- which operations or learned terms were allowed in the search
- which changed experiment, noise check, or missing-variable check could reject the proposed law

#### Concept Responsibilities
- Symbolic Regression And Model Discovery: handles a scientist may need a readable equation, not only a model that predicts well Keeps: candidate formulas that can be written, checked, and compared Failure: a neat formula can fit the training data while using the wrong variables or failing on a changed experiment
- Neural Differential Equations: handles scientists may know that a system changes continuously but not know the exact rule for that change Keeps: a learned rate rule inside a time-stepping calculation Failure: small learned-rate errors can accumulate until long-time predictions drift away from the real system
- Scientific Machine Learning: handles scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time Keeps: data evidence, scientific structure, and validation against changed cases Failure: the method becomes a generic fitting tool if the physical quantity, scientific claim, and validation case are not named
- Optimization For Learning: handles learning needs a way to decide which model settings are better or worse Keeps: a written score that compares model output against data, physics penalties, or design goals Failure: a model can optimize the written score while missing the scientific behavior the score failed to name

#### Evidence Needed Before Trusting The Family
- Strong evidence: the route names the scientific quantity, input family, output quantity, and changed-case test.
- Too weak: the family is described as useful, fast, broad, or accurate without a rejecting changed case.

### Scientific Surrogates Family
- Problem: The trusted simulator is too slow for repeated decisions, but a fast answer is dangerous if nobody states where it is valid.
- Domain: engineering design, uncertainty sweeps, control loops, inverse problems, and expensive simulation workflows
- Concrete family case: An engineering team needs to screen many wing shapes, but each trusted flow solve is expensive. A surrogate is useful only if it stays tied to the same shape family and to the actual decision quantity, such as drag, lift, or a stress peak.
- What the math buys: The approximation becomes useful only after the input family, output quantity, error measure, and rejected cases are named.
- Failure boundary: This family fails when speed hides missing physics, when users ask new questions the surrogate was not trained for, or when uncertainty is treated as decoration.

#### Why The Concepts Appear In This Order
- Surrogate modeling comes first because the shortage is cost: the trusted process is too slow to call for every query.
- Deep learning appears as one way to fit the stand-in from many checked examples.
- Operator learning appears when each query and answer is a whole field rather than a few numbers.
- Uncertainty appears because a fast answer without a tested use range can make the wrong decision faster.

#### Evidence Chain To Track
- which trusted solver, experiment, or workflow the stand-in imitates
- which repeated query family it is allowed to answer
- which decision quantity matters more than visual or average error
- which edge-of-use comparison sends the user back to the trusted source

#### Concept Responsibilities
- Surrogate Modeling: handles a trusted simulator may be too slow to run for every design, control, or uncertainty question Keeps: the input-output behavior needed for a specified family of queries Failure: speed can hide missing physics when the surrogate is used beyond the regime where it was checked
- Deep Learning: handles scientists often have examples of behavior but no short rule that predicts the next case Keeps: many adjustable weights that turn inputs into predictions Failure: the model can fit familiar examples while failing on a new material, geometry, scale, or boundary condition
- Operator Learning: handles one simulation answer is not enough when engineers need the whole map from inputs to solution fields Keeps: a learned map from a forcing, coefficient, shape, or starting field to a solution field Failure: the learned map can give plausible-looking fields that violate the equation or fail on a shifted input family
- Uncertainty And Generalization: handles a prediction is not enough unless the user knows when it should be believed Keeps: error checks, changed-case tests, and limits on where the model was trained Failure: training error can look good while the model fails under a new geometry, parameter range, sensor, or physical regime

#### Evidence Needed Before Trusting The Family
- Strong evidence: the route names the scientific quantity, input family, output quantity, and changed-case test.
- Too weak: the family is described as useful, fast, broad, or accurate without a rejecting changed case.


## Comparisons
### PINNs vs Neural Operators
- Shared problem: Both try to predict scientific fields without ignoring the physics that makes those fields meaningful.
- Key difference: A PINN usually learns one field while being punished for breaking an equation. A neural operator learns the input-to-solution map for a named family of fields.
- Shortage that creates the choice: The shortage is either missing values for one field, or missing fast solves for many related fields. Those are different shortages.
- Evidence carried by Physics-informed neural networks: one physical case, sparse measurements, boundary or starting values, and a trusted equation residual
- Evidence carried by Neural operators: many paired input fields and output fields from a named equation, boundary, geometry, grid, and parameter family
- First wrong answer to look for: the model gives a smooth-looking field while the boundary case, equation residual, or target physical quantity is wrong
- Left case: A wall has a few temperature sensors and a trusted heat equation. Use a PINN to fit one temperature field while checking data, equation, and boundary errors.
- Right case: A lab has thousands of solved heat-flow cases for many source fields. Use an operator model to learn the input-field to solution-field map.
- Wrong choice case: Using an operator model from one family on a boundary type it never saw, or using a PINN when the real need is thousands of fast repeated solves.
- Evidence that exposes it: Hold out a changed boundary or input-field family and compare the full field and the scientific quantity, not only visual similarity.
- Wrong turn: Do not use either word as a badge of trust. Ask what changed case was tested.
- Decision burden: name the observed evidence, hidden quantity, decision quantity, use range, and changed case before choosing either side.
- Swap test: if swapping sides does not break a named claim, the comparison is still too vague.

### Solvers vs Learned Surrogates
- Shared problem: Both produce answers for scientific or engineering questions.
- Key difference: A solver follows the written equations step by step. A surrogate imitates the solver's input-output behavior inside a tested use range.
- Shortage that creates the choice: The shortage is time. The solver carries the rule directly, but may be too slow for many repeated decisions.
- Evidence carried by Trusted numerical solvers: the written equation, numerical method, mesh, boundary data, and known checks for conservation or stability
- Evidence carried by Learned surrogates: trusted solver examples from a named query family plus error checks near the edge of use
- First wrong answer to look for: the surrogate is used on a design edge case and misses the decision quantity that the solver would have caught
- Left case: A safety decision depends on a stress peak near a crack. Use the trusted solver because the local failure quantity matters more than speed.
- Right case: A design team needs to screen thousands of similar wing shapes before choosing a few expensive solver runs. Use a surrogate inside that named shape family.
- Wrong choice case: Replacing the solver everywhere because the surrogate is fast, including edge cases where no solver comparison exists.
- Evidence that exposes it: Compare against the solver near the design boundary and inspect the decision quantity, such as drag, lift, stress peak, or failure location.
- Wrong turn: A fast surrogate is not a replacement for the solver outside the cases where it was checked.
- Decision burden: name the observed evidence, hidden quantity, decision quantity, use range, and changed case before choosing either side.
- Swap test: if swapping sides does not break a named claim, the comparison is still too vague.

### Symbolic Regression vs Large Fitted Prediction
- Shared problem: Both use data to make future or unseen cases easier to understand.
- Key difference: Symbolic regression searches for a small formula. Large fitted prediction can carry more detail but usually gives less direct explanation.
- Shortage that creates the choice: The shortage is either a readable law or a strong predictor. A readable law is useful only if the measured variables are enough to support it.
- Evidence carried by Symbolic regression: measured variables, allowed operations, a small candidate formula, and changed-experiment checks
- Evidence carried by Large fitted prediction: many examples, richer input detail, prediction error on held-out cases, and a stated use range
- First wrong answer to look for: a short formula fits the original data but fails when a missing variable, noise pattern, or new experiment is introduced
- Left case: A lab tracks a simple motion and wants a small equation that explains the rate of change. Use symbolic regression and test the law on a new experiment.
- Right case: A molecular property depends on many structural details and the goal is accurate screening. Use a larger fitted predictor with clear use-range checks.
- Wrong choice case: Treating a neat formula as a law when an important variable was never measured, or demanding a tiny formula for a pattern that needs richer structure.
- Evidence that exposes it: Run a changed experiment, add missing-variable checks, and compare error on cases that differ from the data that selected the formula.
- Wrong turn: A neat formula is not automatically true; it must survive changed data and missing-variable checks.
- Decision burden: name the observed evidence, hidden quantity, decision quantity, use range, and changed case before choosing either side.
- Swap test: if swapping sides does not break a named claim, the comparison is still too vague.

### Data-Only vs Physics-Informed Learning
- Shared problem: Both try to turn examples into predictions.
- Key difference: Data-only learning listens to examples. Physics-informed learning also listens to rules about what answers are allowed.
- Shortage that creates the choice: The shortage is whether examples alone carry enough evidence. When examples are thin between measurements, a trusted rule may carry information the data do not.
- Evidence carried by Data-only learning: many checked examples from the same source, scale, target quantity, and use range
- Evidence carried by Physics-informed learning: examples plus a trusted equation, boundary condition, conservation law, unit rule, or symmetry check
- First wrong answer to look for: a model fits familiar examples but breaks the rule exactly where measurements are sparse or the regime changes
- Left case: A measured property has many examples and no trusted equation for the target. Use data-only learning with a clear held-out test.
- Right case: A temperature field has sparse measurements and a trusted heat equation. Add the physical rule so unsensed places are checked.
- Wrong choice case: Adding a physical rule that is incomplete or wrong for the experiment, or ignoring a trusted rule when data are sparse.
- Evidence that exposes it: Compare changed cases where the rule matters: boundaries, conservation, units, symmetry, or regions between measurements.
- Wrong turn: Adding physics language does not help if the added rule is wrong, too weak, or never tested against the claim.
- Decision burden: name the observed evidence, hidden quantity, decision quantity, use range, and changed case before choosing either side.
- Swap test: if swapping sides does not break a named claim, the comparison is still too vague.


## Worked Examples
### Heat Equation From Few Measurements
- Domain: heat moving through a rod, wall, chip, or material sample
- Question: What is the temperature everywhere if sensors only report a few places?
- Observed: sensor readings, starting temperature, boundary temperature, and the rule that heat flows from hot regions toward cold regions
- Hidden: temperature at every unsensed point and later time
- Decision quantity: temperature at unsensed places and later times
- First failure signal: the fitted field matches sensor points but gives the wrong temperature between them or after the starting time

#### Why Each Step Follows
- Draw the unknown temperature as a field, not as one number. Reason: A field is needed because the answer lives between sensors, not only at sensor points.
- Use the measured points as anchors. Reason: The measurements stop the fitted field from drifting away from what was actually observed.
- Use the heat rule as a check between anchors. Reason: The heat rule tells the unsensed middle how it is allowed to connect hot and cold regions.
- Compare with held-out sensors or a trusted solve. Reason: Held-out sensors or a trusted solve check whether the rule helped rather than only making the fit look tidy.

### Fast Fluid Field Surrogate
- Domain: air or liquid flow around shapes
- Question: How can engineers test many shapes without running a full simulation every time?
- Observed: many prior simulations connecting shape, conditions, and resulting velocity or pressure fields
- Hidden: the flow field for a new shape or new condition
- Decision quantity: velocity, pressure, drag, lift, or another flow quantity used for the design choice
- First failure signal: the shortcut is fast but misses a force, vortex, or boundary effect that changes the engineering choice

#### Why Each Step Follows
- Name the range of shapes and flow conditions. Reason: The range of shapes and conditions defines what the shortcut is allowed to answer.
- Train a model on full fields from trusted simulations. Reason: Full trusted fields teach the shortcut both local details and larger flow patterns.
- Predict a new field quickly. Reason: Fast prediction matters only because the same kind of query must be answered many times.
- Reject the shortcut if it misses boundary behavior, vortices, or pressure forces that matter. Reason: Boundary behavior and forces are checked because they can decide the design even when the picture looks smooth.

### Discovering A Small Law From Motion
- Domain: a measured system changing over time
- Question: Can data reveal a short rule for how the system moves?
- Observed: measurements of position, speed, concentration, or another changing quantity
- Hidden: the rate rule that causes the next moment
- Decision quantity: the rate rule that explains and predicts the measured change
- First failure signal: the rule fits the original trace but breaks when the starting condition, forcing, or measured setting changes

#### Why Each Step Follows
- Measure the variables that might matter. Reason: Only measured variables can fairly appear in the proposed rule.
- Estimate how they change from moment to moment. Reason: Change from moment to moment is the evidence for the missing rate.
- Search for a short rule or learn the missing rate. Reason: A short rule or learned rate is the candidate bridge from the present state to the next one.
- Test on a new experiment, not only the original trace. Reason: A new experiment checks whether the rule is about the system rather than one recorded trace.

### Molecule Property From Structure
- Domain: chemistry and biology, where atoms, bonds, shape, and measured activity all matter
- Question: Can a model predict a useful molecular property without flattening away the structure that causes it?
- Observed: molecular graphs, atom types, bond patterns, shape information, and measured properties from experiments or trusted calculations
- Hidden: which structural relations control the property for a new molecule
- Decision quantity: the molecular property or activity that will guide a chemistry or biology choice
- First failure signal: the model works on familiar molecules but fails on a new scaffold, rare atom type, or changed assay

#### Why Each Step Follows
- Represent the molecule as connected parts, not as an unordered list. Reason: The molecule's connections are part of the object, so flattening them can remove the reason the property appears.
- Let information move along bonds and nearby spatial relations. Reason: Information moves along bonds and spatial neighbors because atoms affect one another through structure.
- Predict the target property for a new molecule. Reason: The prediction is useful only when it names the property being used for the next choice.
- Reject the claim if a new scaffold, rare atom type, or changed assay breaks the prediction. Reason: New scaffolds, rare atoms, and changed assays test whether the model learned chemistry or only familiar examples.

### Material Stress From Sparse Tests
- Domain: materials and mechanics, where stress and strain depend on shape, load, defects, and boundary conditions
- Question: How can a model estimate stress inside a material when only a few tests or simulations are available?
- Observed: sample geometry, load conditions, a few measured displacements or strains, and known mechanical balance laws
- Hidden: the internal stress field and the weak region where failure may begin
- Decision quantity: internal stress, strain, or the location where failure may begin
- First failure signal: the model has low average error but misses the local stress concentration that drives failure

#### Why Each Step Follows
- Name the material quantity that matters for the decision. Reason: The decision quantity matters because average error can hide the weak region.
- Use sparse measurements as anchors for the unknown field. Reason: Sparse measurements anchor the unknown field to real tests or trusted simulations.
- Use mechanical balance as a check between measured places. Reason: Mechanical balance limits what can happen between measured places.
- Compare against held-out tests, changed loads, and trusted simulations near failure regions. Reason: Changed loads and near-failure regions check the place where a wrong field would be most costly.

### Mesh Field On Irregular Geometry
- Domain: scientific fields on meshes, surfaces, networks, and irregular engineering shapes
- Question: How can a model predict a field when the points are connected in an uneven shape instead of a neat grid?
- Observed: mesh points, connections, boundary labels, local features, and solution fields from prior solves
- Hidden: how information should move across the irregular geometry for a new case
- Decision quantity: the field value on the connected shape, especially near boundaries and refined regions
- First failure signal: renumbering, refining, rotating, or changing the boundary makes the field answer change for the wrong reason

#### Why Each Step Follows
- Keep the mesh connections visible. Reason: Connections tell the model which points can physically or geometrically affect one another.
- Pass information along nearby and important distant relations. Reason: Nearby and distant relations both matter when boundary regions or long paths carry influence.
- Predict the field on the same kind of geometric object. Reason: The prediction must live on the same kind of connected object, not on a shuffled table.
- Test changed meshes, boundaries, rotations, and refined regions before trusting the answer. Reason: Changed meshes and rotations check whether the answer follows the shape rather than the file layout.

### Foundation PDE Model On A New Equation
- Domain: many PDE tasks where one broad model is asked to help with a new scientific equation
- Question: When can a model trained on many PDE examples help with a new equation family?
- Observed: many prior equation tasks, grids, parameters, boundary types, and solution fields
- Hidden: which shared structure carries to the new equation and which parts do not
- Decision quantity: whether the new PDE task can be answered with reused structure from previous tasks
- First failure signal: the model looks broad but fails on the held-out equation family, boundary type, scale, or quantity

#### Why Each Step Follows
- List what the broad model has seen before. Reason: The training history defines what shared structure the broad model could have learned.
- Name what is different about the new equation, boundary, scale, or field. Reason: The new equation, boundary, scale, or field names the gap that must not be hidden.
- Use the model only as a candidate shortcut for the new task. Reason: Calling it a candidate shortcut keeps the claim smaller than proof of broad skill.
- Compare against a trusted solve and look for the first changed condition where it fails. Reason: A trusted solve on the changed task checks whether reused structure still carries the needed answer.

### Climate Risk Under Shifted Conditions
- Domain: climate, weather, and environmental fields where future conditions may differ from old data
- Question: How should a model report risk when the future case is not just another familiar example?
- Observed: historical fields, simulation ensembles, forcing conditions, regional measurements, and known physical constraints
- Hidden: how wrong the prediction may be under a changed climate, rare event, or new regional pattern
- Decision quantity: the risk quantity for a region, time window, rare event, or changed forcing condition
- First failure signal: the model reports confident risk while rare events, changed forcing, or the target region were not tested

#### Why Each Step Follows
- Name the risk quantity before choosing a model. Reason: The risk quantity comes first because different risks need different evidence.
- Separate familiar held-out cases from truly changed future conditions. Reason: Familiar held-out cases do not prove behavior under a changed future condition.
- Report prediction with the tested use range. Reason: The use range is part of the answer because it says where the prediction has support.
- Reject confident claims when rare events, regions, or forcing changes have not been checked. Reason: Rare events and changed forcing are checked because they are often where the decision matters most.


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

### Deep Learning
- One sentence: Deep learning fits a flexible rule from examples when the useful pattern is hard to write by hand.
- Use when: Use it when there are many checked examples and the job is to predict, classify, compress, or complete a new case from the same kind of source.
- Do not use when: Do not use a good fit on old examples as proof that the model understands a new physical regime, new sensor, new scale, or new boundary.
- Plain formula: input example -> adjustable rule -> predicted answer -> error check
- Why it matters: It can use large example collections, but the examples define the world it has evidence for.

### Scientific Machine Learning
- One sentence: Scientific machine learning uses data and scientific rules together so the answer is useful for a named scientific question.
- Use when: Use it when measurements alone are incomplete and hand-written equations alone are incomplete, too slow, or partly uncertain.
- Do not use when: Do not call a model scientific just because the data came from science; the physical quantity, rule, and failure test must be explicit.
- Plain formula: measurements + known rule + learned missing part -> checked scientific answer
- Why it matters: It turns machine learning from a general prediction tool into a disciplined way to answer a scientific question with stated evidence.

### Optimization For Learning
- One sentence: Optimization is the process of changing a model until a written error score gets smaller.
- Use when: Use it whenever a model has adjustable parts and there is a clear score saying what counts as a better answer.
- Do not use when: Do not mistake a lower training score for a better scientific model if the score omits boundaries, rare cases, units, or the decision quantity.
- Plain formula: current model -> error score -> change model -> check again
- Why it matters: The training score is the contract the model follows; if the contract is wrong, the learned answer can be wrong in a polished way.

### Generative Modeling
- One sentence: Generative modeling learns how to make possible examples, not just score one existing example.
- Use when: Use it when the job is to sample plausible fields, fill missing parts, create candidate designs, or explore many possible futures.
- Do not use when: Do not treat a plausible-looking sample as a valid scientific answer unless constraints, measurements, and use-range checks are passed.
- Plain formula: known conditions + variation -> candidate example -> realism and rule checks
- Why it matters: Many scientific decisions need a range of possible cases, not a single average case.

### Graphs And Geometric Learning
- One sentence: Graph and geometric learning keeps the connections and shape of the object visible to the model.
- Use when: Use it when the data lives on meshes, molecules, surfaces, sensor networks, or other connected shapes where nearby relations matter.
- Do not use when: Do not flatten connected scientific data into an ordinary table if the connections carry the physical meaning.
- Plain formula: connected shape + local values -> relation-aware updates -> field or object answer
- Why it matters: Many scientific objects are defined partly by their shape and connections, so the model must preserve that structure to ask the right question.

### Attention For Scientific Fields
- One sentence: Attention lets a model decide which other parts of a field matter for the point or region being predicted.
- Use when: Use it when distant regions, boundary information, or multi-scale structure may influence the local answer.
- Do not use when: Do not treat attention weights as scientific proof unless the learned relations survive physical and changed-case tests.
- Plain formula: current field part + relevant other parts -> weighted information -> updated field part
- Why it matters: Scientific fields often have nonlocal influence, and a purely local rule can miss how far-away structure changes the answer.


## Hand Teaching Notes
### Deep Learning
- Plain problem: The world gives many examples, but not a hand-written rule for the next one. Deep learning is the attempt to shape a rule from those examples without pretending the examples cover every future case.
- Why the math follows: The adjustable layers are useful because the relation from input to answer may be too tangled to write directly. The training score is only evidence inside the world represented by the examples and tests.
- Say it back: Deep learning is example-shaped prediction; its boundary is the first new case where the examples no longer carry the target quantity.

### Physics Informed Neural Networks
- Plain problem: The scientist wants a whole field, but measurements cover only a few places. A known equation can check the empty places if the equation is trusted for that case.
- Why the math follows: The loss needs data error because sensors matter, equation error because unsensed points still have rules, and boundary error because the edge defines the physical problem.
- Say it back: A PINN fits a field that must satisfy both observed values and a known rule, then earns trust only through held-out physical checks.

### Partial Differential Equations
- Plain problem: Some quantities live across space and time, so one point cannot be understood apart from neighbors, boundaries, sources, and rates of change.
- Why the math follows: A PDE appears because the question is about local change inside a connected field. The formula states how time change, spatial movement, sources, and boundaries constrain one another.
- Say it back: A PDE is the bookkeeping rule for a changing field, and it fails when the field breaks conservation, boundaries, or measured behavior.

### Operator Learning
- Plain problem: The job is not one solved field. The job is many related solves, where each new input field needs its own output field.
- Why the math follows: The learned object must be a map from function to function because the input and output are whole fields. Testing must change the input field while staying inside the named family.
- Say it back: Operator learning learns a reusable field-to-field map, not proof that the map works outside the tested equation, boundary, grid, or parameter family.

### Scientific Machine Learning
- Plain problem: Scientific data alone may be thin, and scientific rules alone may be partial or slow. The page must say exactly which scientific quantity the learned part supports.
- Why the math follows: The math joins measured evidence, known rules, and a learned missing part because none of those pieces is enough by itself for the named scientific job.
- Say it back: Scientific machine learning is useful only when the target quantity, trusted rule, learned part, and changed-case test are all named.

### Surrogate Modeling
- Plain problem: A trusted simulation or experiment may be too slow to call thousands of times, but the decision still needs many answers.
- Why the math follows: A surrogate is trained as a cheap stand-in because repeated queries are the bottleneck. Its authority comes from comparison against the trusted source, especially near the edge of use.
- Say it back: A surrogate is a fast checked replacement for repeated use, not a replacement for the trusted source outside its tested range.

### Uncertainty And Generalization
- Plain problem: A model can be most tempting exactly where old evidence is weakest: a new regime, rare case, or changed condition.
- Why the math follows: The answer must include both prediction and use range because the missing quantity is not only what will happen, but how much support the old evidence gives the new case.
- Say it back: Uncertainty is the warning boundary around a prediction, and it must be tied to changed-case tests rather than a confident-looking number.

### Optimization For Learning
- Plain problem: Training changes a model to satisfy a score, but the score may not be the same thing as the scientific burden.
- Why the math follows: The update rule follows the written score because the model has no access to the reader's hopes. Every loss term is a contract term that should correspond to a scientific requirement.
- Say it back: Optimization makes the model obey the training score, so the score must include the quantity, boundary, rule, and failure case that matter.

### Generative Modeling
- Plain problem: Some scientific jobs need many possible fields, designs, or futures, not just a single average answer.
- Why the math follows: The model needs a source of variation because the output is a set of candidates. Each candidate still needs condition checks, rule checks, and use-range checks.
- Say it back: Generative modeling makes possible candidates; science begins when those candidates are tested against measurements, rules, and the intended use family.

### Graphs And Geometric Learning
- Plain problem: Meshes, molecules, surfaces, and networks are not unordered bags of values. Their connections are part of the scientific object.
- Why the math follows: The model passes information along connections because the answer often depends on which parts touch, which parts are nearby, and how shape carries physical influence.
- Say it back: Graph and geometric learning keeps shape and connection evidence visible, then must survive changed meshes, rotations, and boundary cases.

### Neural Differential Equations
- Plain problem: The current state is observed over time, but the exact rule that moves it forward may be missing.
- Why the math follows: A learned rate enters because time evolution needs a change rule at each moment. The time solver then exposes whether small rate errors accumulate.
- Say it back: A neural differential equation learns the missing change rule, and long-time or changed-start tests decide whether that rule is usable.

### Symbolic Regression
- Plain problem: Sometimes the desired output is not only an answer but a small rule people can inspect, question, and reuse.
- Why the math follows: The search over formulas follows from not knowing which measured variables and operations form the relation. Smallness matters because an unreadable formula can hide memorization.
- Say it back: Symbolic regression proposes a readable law, but the law is not scientific until it survives noise, missing-variable checks, and a changed experiment.

### Foundation Models For Pdes
- Plain problem: A broad PDE model is useful only if old equation tasks carry structure that the new task truly shares.
- Why the math follows: Many tasks are used to learn shared field behavior, but the proof burden is a held-out equation family, boundary type, scale, or quantity.
- Say it back: A PDE foundation model reuses shared structure across tasks, and the first question is what the new task shares with the old ones.

### Attention For Scientific Fields
- Plain problem: A local field value may depend on distant boundaries, forcing patterns, or large structures, not only nearby cells.
- Why the math follows: Attention compares one part of the field with other parts because relevant information may be far away. The comparison is useful only if physical tests confirm the relation.
- Say it back: Attention is a way to gather relevant field information, not proof that the displayed weights explain the physics.


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

### Deep Learning
- Problem: scientists often have examples of behavior but no short rule that predicts the next case
- Observed: many input-output examples from experiments, simulations, or measurements
- Hidden: the exact rule that connects the input to the output
- Plain formula: input example -> adjustable rule -> predicted answer -> error check
- Failure test: hold out a changed material, geometry, parameter range, or sensor condition
- Page: derivations/deep-learning.html

### Scientific Machine Learning
- Problem: scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time
- Observed: data, equations, units, simulation outputs, and domain limits
- Hidden: which parts of the scientific system are missing, noisy, or too costly to compute directly
- Plain formula: measurements + known rule + learned missing part -> checked scientific answer
- Failure test: state the scientific quantity first, then test it under a changed case that matters in that domain
- Page: derivations/scientific-machine-learning.html

### Optimization For Learning
- Problem: learning needs a way to decide which model settings are better or worse
- Observed: a written score that says which model behavior is better or worse
- Hidden: whether that score matches the scientific behavior the user actually cares about
- Plain formula: current model -> error score -> change model -> check again
- Failure test: inspect what the score ignores, then check whether the ignored behavior fails after training
- Page: derivations/optimization-for-learning.html

### Generative Modeling
- Problem: some tasks need many possible examples, not one predicted answer
- Observed: examples of fields, molecules, flows, shapes, or other scientific objects
- Hidden: the spread of possible valid objects beyond the examples
- Plain formula: known conditions + variation -> candidate example -> realism and rule checks
- Failure test: measure constraints, rare cases, conservation, and downstream task performance on generated samples
- Page: derivations/generative-modeling.html

### Graphs And Geometric Learning
- Problem: many scientific objects are not simple rows of numbers; their connections matter
- Observed: objects with parts and connections, such as meshes, molecules, or interacting components
- Hidden: which neighboring and long-range interactions control the scientific quantity
- Plain formula: connected shape + local values -> relation-aware updates -> field or object answer
- Failure test: change the mesh, rotate or move the object, or add missing interactions and inspect what breaks
- Page: derivations/graphs-and-geometric-learning.html

### Attention For Scientific Fields
- Problem: a local patch of a field may depend on faraway information, but looking everywhere can be expensive
- Observed: large fields where one location may depend on other locations
- Hidden: which distant parts matter for the local prediction
- Plain formula: current field part + relevant other parts -> weighted information -> updated field part
- Failure test: change the window size, inspect long-range effects, and compare behavior near boundaries or sharp structures
- Page: derivations/attention-for-scientific-fields.html


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

### Deep Learning
- Formula shape: input example -> adjustable rule -> predicted answer -> error check
- Parts: input example, adjustable rule, predicted answer, error check
- Everyday reading: It can use large example collections, but the examples define the world it has evidence for.
- What to check: hold out a changed material, geometry, parameter range, or sensor condition

### Scientific Machine Learning
- Formula shape: measurements + known rule + learned missing part -> checked scientific answer
- Parts: measurements + known rule + learned missing part, checked scientific answer
- Everyday reading: It turns machine learning from a general prediction tool into a disciplined way to answer a scientific question with stated evidence.
- What to check: state the scientific quantity first, then test it under a changed case that matters in that domain

### Optimization For Learning
- Formula shape: current model -> error score -> change model -> check again
- Parts: current model, error score, change model, check again
- Everyday reading: The training score is the contract the model follows; if the contract is wrong, the learned answer can be wrong in a polished way.
- What to check: inspect what the score ignores, then check whether the ignored behavior fails after training

### Generative Modeling
- Formula shape: known conditions + variation -> candidate example -> realism and rule checks
- Parts: known conditions + variation, candidate example, realism and rule checks
- Everyday reading: Many scientific decisions need a range of possible cases, not a single average case.
- What to check: measure constraints, rare cases, conservation, and downstream task performance on generated samples

### Graphs And Geometric Learning
- Formula shape: connected shape + local values -> relation-aware updates -> field or object answer
- Parts: connected shape + local values, relation-aware updates, field or object answer
- Everyday reading: Many scientific objects are defined partly by their shape and connections, so the model must preserve that structure to ask the right question.
- What to check: change the mesh, rotate or move the object, or add missing interactions and inspect what breaks

### Attention For Scientific Fields
- Formula shape: current field part + relevant other parts -> weighted information -> updated field part
- Parts: current field part + relevant other parts, weighted information, updated field part
- Everyday reading: Scientific fields often have nonlocal influence, and a purely local rule can miss how far-away structure changes the answer.
- What to check: change the window size, inspect long-range effects, and compare behavior near boundaries or sharp structures


## Misconception Map
### Physics-Informed Neural Networks
- Correction: A PINN is a fitted field that must answer to both measured values and a known physical rule.
- First-principles test: move the training points, inspect sharp regions, and compare against a numerical solve or held-out measurements
- Wrong turns: A weak answer says only that the neural network fits data.; The page reports only training error.; The hard region has few check points.; The equation is known to be incomplete for the experiment.; No comparison is made against held-out measurements or a trusted solver.

### Partial Differential Equations
- Correction: A PDE is a rule for how a whole field changes across space and time.
- First-principles test: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error
- Wrong turns: A weak answer says only that Partial Differential Equations is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.; The boundary condition is vague.; The learned answer ignores conservation.; The grid or resolution changes the conclusion.; Small visual error hides a large error in the quantity people care about.

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
- Wrong turns: A weak answer says only that Neural Differential Equations is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.; The model is tested only over short times.; Small rate errors accumulate unnoticed.; Known conservation or stability behavior is not checked.; The learned rate fits noise instead of mechanism.

### Symbolic Regression And Model Discovery
- Correction: Symbolic regression searches for a short formula that explains measured behavior.
- First-principles test: remove a needed variable, add noise, or test a new experiment and see whether the formula still predicts
- Wrong turns: A weak answer trusts a neat formula because it fits the original data.; Important variables were never measured.; The formula is selected only on the original data.; Noise creates a fake term.; The search space could not express the real mechanism.

### Foundation Models For PDEs
- Correction: A PDE foundation model tries to reuse structure across many related field-prediction tasks.
- First-principles test: hold out a new equation family, boundary type, scale, or rare regime and compare against a trusted solver
- Wrong turns: A weak answer treats broad training size as proof of broad scientific trust.; The held-out test is too similar to training.; Rare regimes are missing.; New boundaries or quantities are assumed rather than tested.; Scale is treated as a substitute for scientific validation.

### Deep Learning
- Correction: Deep learning fits a flexible rule from examples when the useful pattern is hard to write by hand.
- First-principles test: hold out a changed material, geometry, parameter range, or sensor condition
- Wrong turns: A weak answer says only that Deep Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.; The page talks about accuracy without naming the test cases.; The model is used after the data source or physical scale changes.; The important scientific quantity is not the quantity being checked.; No one asks what pattern the examples could not possibly teach.

### Scientific Machine Learning
- Correction: Scientific machine learning uses data and scientific rules together so the answer is useful for a named scientific question.
- First-principles test: state the scientific quantity first, then test it under a changed case that matters in that domain
- Wrong turns: A weak answer says only that Scientific Machine Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.; The target quantity is vague.; The known rule is mentioned but not actually checked.; The learned part can violate conservation, boundaries, or units without penalty.; The result is not compared against a changed experiment or trusted solve.

### Optimization For Learning
- Correction: Optimization is the process of changing a model until a written error score gets smaller.
- First-principles test: inspect what the score ignores, then check whether the ignored behavior fails after training
- Wrong turns: A weak answer says only that Optimization For Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.; The loss terms are listed but their relative weight is not justified.; Only the final score is reported.; A hard constraint is treated as a soft suggestion without checking the damage.; Training succeeds while the physical test fails.

### Generative Modeling
- Correction: Generative modeling learns how to make possible examples, not just score one existing example.
- First-principles test: measure constraints, rare cases, conservation, and downstream task performance on generated samples
- Wrong turns: A weak answer says only that Generative Modeling is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.; Samples look realistic but violate a known equation or boundary.; Diversity is reported without saying whether the candidates are valid.; The model creates cases outside the evidence family.; The generated object is used as data without marking it as generated.

### Graphs And Geometric Learning
- Correction: Graph and geometric learning keeps the connections and shape of the object visible to the model.
- First-principles test: change the mesh, rotate or move the object, or add missing interactions and inspect what breaks
- Wrong turns: A weak answer says only that Graphs And Geometric Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.; Mesh order changes the answer when the geometry did not change.; The model ignores boundaries or long-distance connections that matter physically.; It is tested only on one mesh resolution.; A rotated or refined shape breaks the result without explanation.

### Attention For Scientific Fields
- Correction: Attention lets a model decide which other parts of a field matter for the point or region being predicted.
- First-principles test: change the window size, inspect long-range effects, and compare behavior near boundaries or sharp structures
- Wrong turns: A weak answer says only that Attention For Scientific Fields is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.; Attention maps are shown as explanation without validation.; The method ignores conservation or boundary checks.; It works only at the trained resolution or patch size.; Long-range influence is claimed but not stress-tested.


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

### Training Score Flow
- Purpose: Show that training follows the written score, so the score must match the scientific job.
- Flow: scientific quantity -> error terms -> adjustable model -> lower training score -> changed-case check
- Watch for: A lower score is not enough if the score leaves out the boundary, equation, rare case, or decision quantity.

### Candidate Generation Flow
- Purpose: Show how a model makes possible candidates that still need scientific checks.
- Flow: known conditions -> source of variation -> generated candidate -> measurement and rule checks -> accepted or rejected candidate
- Watch for: A candidate that looks familiar can still break the equation, boundary, measurement, or intended use family.

### Connected Geometry Flow
- Purpose: Show why meshes, molecules, surfaces, and networks must keep their connections visible.
- Flow: connected object -> values on points or edges -> information moves through connections -> field or property prediction -> changed mesh or shape test
- Watch for: If changing point order, mesh detail, rotation, or boundary region changes the claim without a physical reason, the structure is not being handled correctly.


## Mathematical Sketches
### PINNs: Points Plus Rule Checks
- Input: few measured points, boundary values, and a known equation
- Output: a fitted field for the whole domain
- Kept rule: the field should match data and leave little equation-breaking between data points
- Failure case: the field matches sensors but breaks the equation, boundary, or held-out measurements
- Caption: Input: measured points and equation. Output: full field. Kept rule: data plus equation checks. Failure case: correct-looking fit that breaks physics in unmeasured regions.

### Operator Learning: Field To Field
- Input: a whole input field from a named family
- Output: the whole output field for that input
- Kept rule: the learned object is a reusable map between fields, not one solved example
- Failure case: a new input field changes the family, boundary, geometry, or resolution beyond the tested range
- Caption: Input: whole field. Output: whole field. Kept rule: reusable map between related cases. Failure case: new field outside the named family.

### Surrogate Modeling: Fast Stand-In With Boundaries
- Input: queries that would normally require a trusted slow source
- Output: fast approximate answers for repeated choices
- Kept rule: the stand-in remains checked against the trusted source inside a named use range
- Failure case: the stand-in is used near an edge case where the trusted source has not checked it
- Caption: Input: repeated query. Output: fast answer. Kept rule: checked against trusted source. Failure case: fast answer outside the tested use range.

### Uncertainty: New Case Near The Edge
- Input: training cases and a new case that may be different
- Output: prediction with a tested use range
- Kept rule: belief should weaken when the new case leaves the evidence range
- Failure case: the model stays confident where training and validation no longer support confidence
- Caption: Input: old cases plus new case. Output: prediction with use range. Kept rule: doubt grows near the edge. Failure case: confident answer outside evidence.


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

### 8. Learn From Examples Without Forgetting The Boundary
- Question: What can examples teach, and what can they not teach?
- Why here: Deep learning is useful when examples carry repeated structure, but the examples also set the edge of the evidence.
- Goal: Understand a learned predictor as an adjustable rule whose authority comes from checked examples and changed-case tests.
- First-principles spine: World: many past cases have known inputs and answers.; Evidence: the repeated input-answer pairs show patterns the model can copy.; Missing piece: the answer for a new case is unknown.; Mathematical move: adjust a flexible rule until its answers match checked examples.; Reject it when: the new case changes the source, scale, boundary, or quantity that the examples did not cover.
- Checkpoint: You can say what the examples prove, what they leave unproved, and what changed case should be tested.

### 9. Generate Many Valid Candidates
- Question: When is one predicted answer too narrow?
- Why here: Some scientific jobs need a range of possible fields, designs, or futures instead of one average answer.
- Goal: Treat generative modeling as candidate-making under evidence and rule checks, not as a source of automatic truth.
- First-principles spine: World: more than one answer may be possible under the known conditions.; Evidence: old examples show what valid candidates tend to look like.; Missing piece: the set of plausible new candidates is unknown.; Mathematical move: combine known conditions with controlled variation to make candidate examples.; Reject it when: samples look plausible but violate measurements, boundaries, equations, or the tested use family.
- Checkpoint: You can distinguish a plausible-looking generated candidate from a checked scientific candidate.

### 10. Keep Connected Shapes Connected
- Question: What changes when the data is a mesh, molecule, surface, or network?
- Why here: Some scientific objects are not flat tables. Their shape and connections are part of the evidence.
- Goal: See graph and geometric learning as a way to preserve the object being studied while information moves through it.
- First-principles spine: World: the object is made of connected points, edges, surfaces, or regions.; Evidence: values live on that connected shape and the connections affect the answer.; Missing piece: the field, label, or property for a new connected object is unknown.; Mathematical move: pass information along the meaningful connections while preserving the shape.; Reject it when: changing point order, mesh resolution, rotation, or boundary regions breaks the claim.
- Checkpoint: You can explain why the connections are evidence, not decoration.

### 11. Read Training As A Contract
- Question: What is the model actually being rewarded for?
- Why here: A model follows the score it is trained on. If that score omits the scientific burden, training can improve the wrong thing.
- Goal: Understand optimization as repeatedly changing a model to reduce a written error score, then checking whether that score matches the scientific job.
- First-principles spine: World: the model has adjustable parts.; Evidence: a score says which answers count as better or worse.; Missing piece: the adjusted model that performs the needed job is unknown.; Mathematical move: update the adjustable parts to reduce the score.; Reject it when: the score goes down while the boundary, equation, rare case, or decision quantity fails.
- Checkpoint: You can name the score, the adjustable parts, and the scientific check the score might miss.

### 12. Ask Which Far-Away Information Matters
- Question: When can a local prediction depend on distant parts of the field?
- Why here: Scientific fields can have long-range influence through boundaries, waves, pressure, coherent structures, or global constraints.
- Goal: Use attention as a way to select relevant field parts, while keeping physical validation separate from visual explanation.
- First-principles spine: World: a field part may depend on nearby and far-away information.; Evidence: field examples show which parts tend to affect each other.; Missing piece: the relevant information for a new point, patch, or region is unknown.; Mathematical move: compare field parts, weight the ones judged useful, and update the prediction.; Reject it when: the selected relations fail under changed boundaries, resolution, conservation checks, or physical stress tests.
- Checkpoint: You can explain the difference between useful long-range information and an unvalidated attention picture.


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

### Example-Trained Rule
- Everyday meaning: a rule shaped by many past input-answer pairs
- Problem it names: some useful patterns are hard to write down by hand
- Why it matters: deep learning can turn many checked examples into a reusable predictor
- Watch for: the predictor has evidence only for the kinds of cases the examples and tests actually cover

### Scientific Target
- Everyday meaning: the exact quantity the scientist needs to know or decide from
- Problem it names: a model can optimize a convenient score while missing the quantity that matters
- Why it matters: scientific machine learning starts to make sense only after the target quantity is named
- Watch for: phrases like better prediction are too weak unless the measured or decided quantity is explicit

### Candidate Sample
- Everyday meaning: one possible object made by a model
- Problem it names: some tasks need many plausible futures, fields, or designs rather than one answer
- Why it matters: generative modeling is useful only when candidates are checked against conditions and rules
- Watch for: a candidate that looks realistic may still violate measurements, boundaries, or the tested use family

### Connected Representation
- Everyday meaning: a way to keep track of which points, parts, or regions are linked
- Problem it names: meshes, molecules, surfaces, and networks lose meaning when treated as unordered tables
- Why it matters: graph and geometric learning keeps the shape and connections available to the model
- Watch for: if changing point order or mesh resolution changes the claim, the representation may not be carrying the right structure

### Relevance Weight
- Everyday meaning: a learned amount saying how much one part should listen to another part
- Problem it names: a local field value may depend on distant boundaries, regions, or patterns
- Why it matters: attention for scientific fields gives the model a way to gather far-away information
- Watch for: a displayed weight is not an explanation unless the relation survives physical and changed-case tests


## Domain Guides
### Heat And Diffusion
- Real quantity: temperature, concentration, or another quantity spreading through space
- Why hard: measurements may be sparse, but the unsensed region still matters
- Common question: What is happening between sensors, later in time, or under a changed boundary?
- Scientific job: Estimate the full temperature field inside a wall after a boundary temperature changes.
- Observed evidence: a few sensor readings, starting temperature, boundary temperature, material constants, and the heat equation
- Hidden quantity: the temperature at unsensed locations and later times
- Decision: decide whether the wall, chip, or sample will exceed a safe temperature
- Changed-case test: move the heat source or change the boundary temperature and compare against held-out sensors or a trusted solve
- Failure test: Change the boundary temperature, source strength, or sensor placement and see whether the prediction still follows the physical rule.

### Fluids And Flow
- Real quantity: velocity, pressure, vorticity, drag, lift, or other flow quantities
- Why hard: small changes in shape, boundary, or regime can create large changes in the field
- Common question: Can we predict flow fields or forces quickly enough for design while still catching important failures?
- Scientific job: Predict pressure and velocity around a new wing or channel shape before running the full solver.
- Observed evidence: trusted simulations for earlier shapes, boundary conditions, inflow speed, and resulting velocity or pressure fields
- Hidden quantity: the field and forces for a new shape near the edge of the design range
- Decision: screen designs and decide which cases deserve expensive solver runs
- Changed-case test: hold out a new geometry or flow regime and check drag, lift, boundary behavior, and vortices
- Failure test: Hold out a new geometry or flow condition near the edge of the intended design range.

### Materials And Mechanics
- Real quantity: stress, strain, displacement, failure location, or material response
- Why hard: the same load can produce different behavior when geometry, defects, or material parameters change
- Common question: Can a model predict how a material or structure responds under a new load or shape?
- Scientific job: Find the stress field and likely weak region in a part with a new load or defect pattern.
- Observed evidence: geometry, mesh, loads, material parameters, sparse strain measurements, and trusted simulations
- Hidden quantity: internal stress and the local region where failure may begin
- Decision: decide whether the part is safe enough or needs a changed design
- Changed-case test: change the load path, defect, mesh, or boundary and check stress near failure regions
- Failure test: Change the geometry, mesh, defect, or load path and check the physical quantity used for decisions.

### Chemistry And Biology
- Real quantity: molecular property, reaction behavior, concentration, binding, or biological response
- Why hard: the object may be a graph, a field, a time process, or a set of interacting parts
- Common question: Can learned structure help predict scientific behavior while respecting the object being studied?
- Scientific job: Predict a molecule property or biological activity for a new structure.
- Observed evidence: atoms, bonds, shape, assay conditions, measured properties, and trusted calculations where available
- Hidden quantity: which structural relations control the property or response in the new molecule
- Decision: choose which candidate molecules deserve synthesis, testing, or closer calculation
- Changed-case test: test on a new scaffold, rare atom type, changed assay, or biological condition outside the familiar set
- Failure test: Test on a changed molecule, condition, experiment, or biological setting that was not close to training.

### Many PDE Tasks
- Real quantity: solution fields across many equations, grids, parameters, or boundary settings
- Why hard: a model may look broad while only covering the cases it saw often
- Common question: Can one trained model reuse structure across many related scientific tasks?
- Scientific job: Use a broad PDE model on a new equation case without pretending breadth is proof.
- Observed evidence: many prior PDE tasks, fields, grids, parameters, boundary types, and trusted solution fields
- Hidden quantity: which shared structure transfers to the new PDE case and which parts do not
- Decision: decide whether the broad model is a useful shortcut or whether a task-specific solve is still needed
- Changed-case test: withhold a full equation family, boundary type, scale, or quantity and compare against trusted solves
- Failure test: Withhold a full equation family, boundary type, or scale and check whether the model still earns the claim.

### Data-Rich Scientific Prediction
- Real quantity: a measured or simulated quantity predicted from many prior examples
- Why hard: many examples can teach repeated patterns but cannot prove the next case belongs to the same evidence range
- Common question: Can a learned predictor answer a new scientific case without pretending the examples cover every future use?
- Scientific job: Predict a property, field summary, or class for a new case using many checked examples.
- Observed evidence: past inputs, known answers, data source details, measurement conditions, and held-out examples
- Hidden quantity: the answer for a new case whose source, scale, or condition may differ from the old cases
- Decision: decide whether the prediction is good enough for screening, measurement, or closer simulation
- Changed-case test: hold out a new source, scale, sensor condition, or rare case and check the quantity used for decisions
- Failure test: Change the source, scale, or measured condition and check whether the target quantity still holds.

### Scientific Model Building
- Real quantity: the physical or scientific quantity the model is supposed to explain, predict, or support
- Why hard: data, equations, and training scores can point in different directions unless the scientific target is explicit
- Common question: How should a learned model combine measurements and known rules for a named scientific job?
- Scientific job: Build a model for a named scientific quantity when neither data alone nor a hand-written rule is enough.
- Observed evidence: measurements, partial equations, known units, boundaries, trusted simulations, and known failure modes
- Hidden quantity: the missing relation or field value needed for the scientific question
- Decision: decide whether the combined learned-and-scientific model can support a claim, design, or experiment
- Changed-case test: change the experiment, boundary, scale, or measured variable and verify the scientific target directly
- Failure test: Change the experimental setting or target quantity and check whether the claimed scientific answer still survives.

### Learned Time Dynamics
- Real quantity: the future state, path, rate of change, or event time of a system
- Why hard: small errors in the learned change rule can grow as the system is marched forward
- Common question: Can a model learn the missing rule for how a system changes while keeping time behavior testable?
- Scientific job: Predict how a measured system evolves when part of the rate law is unknown.
- Observed evidence: state histories, time stamps, known conservation or stability facts, controls, and measured changes
- Hidden quantity: the missing rate rule and the future path under a new starting condition or input
- Decision: decide whether the learned dynamics can be used for forecasting, control, or experiment planning
- Changed-case test: start from a new condition, run longer than the training window, and check drift, stability, and conserved quantities
- Failure test: Run beyond the training window or change the starting state and check accumulated error, stability, and known invariants.

### Training Score Design
- Real quantity: the scientific quantity encoded by the terms of the training score
- Why hard: the model reduces the written score even when that score leaves out the real scientific burden
- Common question: What should the training process reward so the learned answer serves the scientific job?
- Scientific job: Choose training terms that reward the behavior needed by the scientific claim.
- Observed evidence: data errors, equation errors, boundary errors, weights between terms, constraints, and held-out checks
- Hidden quantity: whether the trained model is good because the science is right or only because the written score is easy to lower
- Decision: decide whether the loss is a faithful contract for the claim being made
- Changed-case test: change the weights, hold out hard regions, and check the physical or decision quantity directly
- Failure test: Lower the training score while checking a hard held-out region; reject the setup if the scientific quantity gets worse.


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

### Deep Learning Reader Check
- Setup: A reader is deciding whether Deep Learning fits a scientific job in scientific prediction from large measured or simulated data sets.
- Strong answer: Observed: many input-output examples from experiments, simulations, or measurements. Hidden: the exact rule that connects the input to the output. The mathematical move is to adjust many weights until the model maps familiar inputs to the right outputs. The formula shape means the model earns attention only when prediction survives examples it did not train on. The claim should be tested by this changed case: hold out a changed material, geometry, parameter range, or sensor condition.
- Weak answer warning: A weak answer says only that Deep Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.

### Partial Differential Equations Reader Check
- Setup: A reader is deciding whether Partial Differential Equations fits a scientific job in fluids, heat, waves, mechanics, chemistry, climate, and other changing fields.
- Strong answer: Observed: a field such as temperature, pressure, concentration, velocity, or displacement. Hidden: how every point in the field affects nearby points over time. The mathematical move is to write a local change rule that uses rates across space and time. The formula shape means the equation carries how a whole field changes, not just how one number changes. The claim should be tested by this changed case: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error.
- Weak answer warning: A weak answer says only that Partial Differential Equations is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.

### Scientific Machine Learning Reader Check
- Setup: A reader is deciding whether Scientific Machine Learning fits a scientific job in using data-driven models inside scientific workflows.
- Strong answer: Observed: data, equations, units, simulation outputs, and domain limits. Hidden: which parts of the scientific system are missing, noisy, or too costly to compute directly. The mathematical move is to combine learned prediction with scientific checks that name what the claim is allowed to mean. The formula shape means the model is judged by a scientific job, not by a score floating away from the job. The claim should be tested by this changed case: state the scientific quantity first, then test it under a changed case that matters in that domain.
- Weak answer warning: A weak answer says only that Scientific Machine Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.

### Optimization For Learning Reader Check
- Setup: A reader is deciding whether Optimization For Learning fits a scientific job in turning model fitting into a repeatable computation.
- Strong answer: Observed: a written score that says which model behavior is better or worse. Hidden: whether that score matches the scientific behavior the user actually cares about. The mathematical move is to change model settings to lower the written score. The formula shape means the model learns the score, so the score must include the scientific burden. The claim should be tested by this changed case: inspect what the score ignores, then check whether the ignored behavior fails after training.
- Weak answer warning: A weak answer says only that Optimization For Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.

### Generative Modeling Reader Check
- Setup: A reader is deciding whether Generative Modeling fits a scientific job in creating plausible scientific samples, fields, or candidate designs.
- Strong answer: Observed: examples of fields, molecules, flows, shapes, or other scientific objects. Hidden: the spread of possible valid objects beyond the examples. The mathematical move is to learn how to sample new candidates that resemble the training family. The formula shape means a generated object must still pass physics and usefulness checks. The claim should be tested by this changed case: measure constraints, rare cases, conservation, and downstream task performance on generated samples.
- Weak answer warning: A weak answer says only that Generative Modeling is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.

### Graphs And Geometric Learning Reader Check
- Setup: A reader is deciding whether Graphs And Geometric Learning fits a scientific job in systems made of interacting parts, meshes, molecules, or spatial relations.
- Strong answer: Observed: objects with parts and connections, such as meshes, molecules, or interacting components. Hidden: which neighboring and long-range interactions control the scientific quantity. The mathematical move is to let information move along the object connections instead of flattening the object into a plain row. The formula shape means the model keeps the structure of the scientific object visible. The claim should be tested by this changed case: change the mesh, rotate or move the object, or add missing interactions and inspect what breaks.
- Weak answer warning: A weak answer says only that Graphs And Geometric Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.

### Neural Differential Equations Reader Check
- Setup: A reader is deciding whether Neural Differential Equations fits a scientific job in changing systems where time evolution is part of the model.
- Strong answer: Observed: measurements of a system changing over time. Hidden: the rate rule that moves the present value into the future. The mathematical move is to learn the missing rate rule and place it inside a time-evolution calculation. The formula shape means learning supplies the unknown change rule while the time update carries the idea of continuous motion. The claim should be tested by this changed case: run longer than the training window and check whether small rate errors accumulate into drift.
- Weak answer warning: A weak answer says only that Neural Differential Equations is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.

### Attention For Scientific Fields Reader Check
- Setup: A reader is deciding whether Attention For Scientific Fields fits a scientific job in large scientific fields where distant parts may interact.
- Strong answer: Observed: large fields where one location may depend on other locations. Hidden: which distant parts matter for the local prediction. The mathematical move is to let the model choose which parts of the field exchange information. The formula shape means attention is a routing rule for information, not proof that the selected route is physically complete. The claim should be tested by this changed case: change the window size, inspect long-range effects, and compare behavior near boundaries or sharp structures.
- Weak answer warning: A weak answer says only that Attention For Scientific Fields is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.


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

### Many Examples, No Clear Rule
- Situation: You have many examples, but no trusted equation or readable law yet.
- Start with: Deep learning
- Why: The first useful move is to learn a flexible predictor, then test whether it carries the quantity that matters.
- Evidence needed: held-out examples, changed measurement tests, target-quantity error, and a named first failure

### Scientific Claim Needs Discipline
- Situation: A model is being called scientific, but the claim, evidence, and failure boundary are not yet separated.
- Start with: Scientific machine learning
- Why: The field-level job is to make the learned answer answerable to evidence, physical quantities, and changed cases.
- Evidence needed: source anchors, a named scientific quantity, domain-specific checks, and a changed-case rejection test

### Training Score Burden
- Situation: A model improves a written score, but the scientific decision may depend on something the score ignored.
- Start with: Optimization for learning
- Why: Training only improves what the objective asks it to improve, so the objective must match the scientific burden.
- Evidence needed: loss-term inspection, ignored-requirement tests, held-out edge cases, and the decision quantity after training

### Need Many Valid Possibilities
- Situation: The task needs many candidate fields, molecules, designs, or futures rather than one answer.
- Start with: Generative modeling
- Why: The useful product is a set of possible scientific objects that still obey the rules that matter.
- Evidence needed: constraint checks, rare-event checks, downstream-task tests, and examples of rejected samples

### Connected Object Matters
- Situation: The object is a molecule, mesh, graph, surface, or network where connections carry part of the scientific meaning.
- Start with: Graphs and geometric learning
- Why: Flattening the object can hide which parts influence which other parts.
- Evidence needed: mesh-change tests, symmetry checks, missing-interaction tests, and target-property error on changed objects

### Far Field Information Matters
- Situation: A local part of a scientific field depends on distant regions, but carrying every interaction is expensive.
- Start with: Attention for scientific fields
- Why: Attention gives a way to route selected information across a field while making the routing choice testable.
- Evidence needed: window-change tests, long-range interaction tests, boundary-stress cases, and error on the scientific quantity

### Field Rule Before Method
- Situation: A quantity changes across space, time, or both, and one number cannot describe the scientific state.
- Start with: Partial differential equations
- Why: The PDE names how local change, movement, sources, and boundaries must fit together before a learned method is trusted.
- Evidence needed: boundary tests, source-term checks, conservation or stability checks, and changed-grid or changed-scale cases


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
- Local files: scripts/build_physics_informed_ml_research_package.py, scripts/verify_remote_state.py, scripts/verify_ci_status.py, README.md, Makefile
- Checks: repo has a clear topic name, raw source material is preserved, generated pages are validated, commits are small enough to review, remote main hash matches local main after push, make review prints the strongest local review URLs, make ci-check verifies the current commit's GitHub Actions run after CI completes

### Cross-Channel Replication Playbook
- Purpose: Give another CLI an end-to-end operating plan for building the same kind of package from a different channel or playlist family.
- Local files: raw-material/playlists/, raw-material/metadata/, raw-material/transcripts/, analysis/, site/, exports/research-package.md
- Checks: source URLs are named, raw and clean transcripts are preserved, concept pages explain problem/domain/importance/failure, review entrypoints and coverage pages exist, validation commands pass


## Coverage Matrix
### Deep Learning
- Videos: 38
- Deep dive: yes
- Diagram: yes
- Reader check: yes
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
- Reader check: yes
- Evidence items: 6

### Operator Learning
- Videos: 33
- Deep dive: yes
- Diagram: yes
- Reader check: yes
- Evidence items: 6

### Scientific Machine Learning
- Videos: 33
- Deep dive: yes
- Diagram: yes
- Reader check: yes
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
- Deep dive: yes
- Diagram: yes
- Reader check: yes
- Evidence items: 6

### Generative Modeling
- Videos: 33
- Deep dive: yes
- Diagram: yes
- Reader check: yes
- Evidence items: 6

### Graphs And Geometric Learning
- Videos: 31
- Deep dive: yes
- Diagram: yes
- Reader check: yes
- Evidence items: 6

### Neural Differential Equations
- Videos: 40
- Deep dive: yes
- Diagram: yes
- Reader check: yes
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
- Deep dive: yes
- Diagram: yes
- Reader check: yes
- Evidence items: 6


## Review Queue
### P2 Attention For Scientific Fields
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Missing layers: none
- Reason: ready for hand polish
- Next action: Open the evidence packet, check the source-strength audit, then add or confirm anchors before widening the claim for Attention For Scientific Fields.
- Topic: topics/attention-for-scientific-fields.html
- Evidence packet: evidence-packets/attention-for-scientific-fields.html

### P2 Deep Learning
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Missing layers: none
- Reason: ready for hand polish
- Next action: Open the evidence packet, check the source-strength audit, then add or confirm anchors before widening the claim for Deep Learning.
- Topic: topics/deep-learning.html
- Evidence packet: evidence-packets/deep-learning.html

### P2 Foundation Models For PDEs
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Missing layers: none
- Reason: ready for hand polish
- Next action: Open the evidence packet, check the source-strength audit, then add or confirm anchors before widening the claim for Foundation Models For PDEs.
- Topic: topics/foundation-models-for-pdes.html
- Evidence packet: evidence-packets/foundation-models-for-pdes.html

### P2 Generative Modeling
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Missing layers: none
- Reason: ready for hand polish
- Next action: Open the evidence packet, check the source-strength audit, then add or confirm anchors before widening the claim for Generative Modeling.
- Topic: topics/generative-modeling.html
- Evidence packet: evidence-packets/generative-modeling.html

### P2 Graphs And Geometric Learning
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Missing layers: none
- Reason: ready for hand polish
- Next action: Open the evidence packet, check the source-strength audit, then add or confirm anchors before widening the claim for Graphs And Geometric Learning.
- Topic: topics/graphs-and-geometric-learning.html
- Evidence packet: evidence-packets/graphs-and-geometric-learning.html

### P2 Neural Differential Equations
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Missing layers: none
- Reason: ready for hand polish
- Next action: Open the evidence packet, check the source-strength audit, then add or confirm anchors before widening the claim for Neural Differential Equations.
- Topic: topics/neural-differential-equations.html
- Evidence packet: evidence-packets/neural-differential-equations.html

### P2 Operator Learning
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Missing layers: none
- Reason: ready for hand polish
- Next action: Open the evidence packet, check the source-strength audit, then add or confirm anchors before widening the claim for Operator Learning.
- Topic: topics/operator-learning.html
- Evidence packet: evidence-packets/operator-learning.html

### P2 Optimization For Learning
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Missing layers: none
- Reason: ready for hand polish
- Next action: Open the evidence packet, check the source-strength audit, then add or confirm anchors before widening the claim for Optimization For Learning.
- Topic: topics/optimization-for-learning.html
- Evidence packet: evidence-packets/optimization-for-learning.html

### P2 Partial Differential Equations
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Missing layers: none
- Reason: ready for hand polish
- Next action: Open the evidence packet, check the source-strength audit, then add or confirm anchors before widening the claim for Partial Differential Equations.
- Topic: topics/partial-differential-equations.html
- Evidence packet: evidence-packets/partial-differential-equations.html

### P2 Physics-Informed Neural Networks
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Missing layers: none
- Reason: ready for hand polish
- Next action: Open the evidence packet, check the source-strength audit, then add or confirm anchors before widening the claim for Physics-Informed Neural Networks.
- Topic: topics/physics-informed-neural-networks.html
- Evidence packet: evidence-packets/physics-informed-neural-networks.html

### P2 Scientific Machine Learning
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Missing layers: none
- Reason: ready for hand polish
- Next action: Open the evidence packet, check the source-strength audit, then add or confirm anchors before widening the claim for Scientific Machine Learning.
- Topic: topics/scientific-machine-learning.html
- Evidence packet: evidence-packets/scientific-machine-learning.html

### P2 Surrogate Modeling
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Missing layers: none
- Reason: ready for hand polish
- Next action: Open the evidence packet, check the source-strength audit, then add or confirm anchors before widening the claim for Surrogate Modeling.
- Topic: topics/surrogate-modeling.html
- Evidence packet: evidence-packets/surrogate-modeling.html

### P2 Symbolic Regression And Model Discovery
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Missing layers: none
- Reason: ready for hand polish
- Next action: Open the evidence packet, check the source-strength audit, then add or confirm anchors before widening the claim for Symbolic Regression And Model Discovery.
- Topic: topics/symbolic-regression.html
- Evidence packet: evidence-packets/symbolic-regression.html

### P2 Uncertainty And Generalization
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Missing layers: none
- Reason: ready for hand polish
- Next action: Open the evidence packet, check the source-strength audit, then add or confirm anchors before widening the claim for Uncertainty And Generalization.
- Topic: topics/uncertainty-and-generalization.html
- Evidence packet: evidence-packets/uncertainty-and-generalization.html


## Hand Polish Audit
### P2 Attention For Scientific Fields
- Status: ready for hand polish
- Supported claim: This page can claim that Attention For Scientific Fields is a route for this problem: a local patch of a field may depend on faraway information, but looking everywhere can be expensive
- Overclaim to avoid: Do not claim that Attention For Scientific Fields works across large scientific fields where distant parts may interact without a changed-case test tied to the target quantity.
- Stronger evidence needed: Use held-out measurements, trusted solves, changed boundaries, changed geometry, or changed regimes to test: change the window size, inspect long-range effects, and compare behavior near boundaries or sharp structures
- First rejection test: windowing or scaling choices can miss long-range effects that matter for the scientific quantity being predicted
- Done when: A reviewer can retell the page as problem, evidence, hidden quantity, mathematical move, source limit, and changed-case rejection without adding outside jargon.
- Topic: topics/attention-for-scientific-fields.html
- Evidence packet: evidence-packets/attention-for-scientific-fields.html

### P2 Deep Learning
- Status: ready for hand polish
- Supported claim: This page can claim that Deep Learning is a route for this problem: scientists often have examples of behavior but no short rule that predicts the next case
- Overclaim to avoid: Do not claim that Deep Learning works across scientific prediction from large measured or simulated data sets without a changed-case test tied to the target quantity.
- Stronger evidence needed: Use held-out measurements, trusted solves, changed boundaries, changed geometry, or changed regimes to test: hold out a changed material, geometry, parameter range, or sensor condition
- First rejection test: the model can fit familiar examples while failing on a new material, geometry, scale, or boundary condition
- Done when: A reviewer can retell the page as problem, evidence, hidden quantity, mathematical move, source limit, and changed-case rejection without adding outside jargon.
- Topic: topics/deep-learning.html
- Evidence packet: evidence-packets/deep-learning.html

### P2 Foundation Models For PDEs
- Status: ready for hand polish
- Supported claim: This page can claim that Foundation Models For PDEs is a route for this problem: one trained model may be asked to handle many related equations, grids, parameters, or physical settings
- Overclaim to avoid: Do not claim that Foundation Models For PDEs works across broad families of PDE problems and scientific fields without a changed-case test tied to the target quantity.
- Stronger evidence needed: Use held-out measurements, trusted solves, changed boundaries, changed geometry, or changed regimes to test: hold out a new equation family, boundary type, scale, or rare regime and compare against a trusted solver
- First rejection test: the model can look broad while missing rare regimes, new boundary conditions, or quantities not represented in training
- Done when: A reviewer can retell the page as problem, evidence, hidden quantity, mathematical move, source limit, and changed-case rejection without adding outside jargon.
- Topic: topics/foundation-models-for-pdes.html
- Evidence packet: evidence-packets/foundation-models-for-pdes.html

### P2 Generative Modeling
- Status: ready for hand polish
- Supported claim: This page can claim that Generative Modeling is a route for this problem: some tasks need many possible examples, not one predicted answer
- Overclaim to avoid: Do not claim that Generative Modeling works across creating plausible scientific samples, fields, or candidate designs without a changed-case test tied to the target quantity.
- Stronger evidence needed: Use held-out measurements, trusted solves, changed boundaries, changed geometry, or changed regimes to test: measure constraints, rare cases, conservation, and downstream task performance on generated samples
- First rejection test: generated samples can look realistic while breaking constraints, conservation, or rare-event behavior
- Done when: A reviewer can retell the page as problem, evidence, hidden quantity, mathematical move, source limit, and changed-case rejection without adding outside jargon.
- Topic: topics/generative-modeling.html
- Evidence packet: evidence-packets/generative-modeling.html

### P2 Graphs And Geometric Learning
- Status: ready for hand polish
- Supported claim: This page can claim that Graphs And Geometric Learning is a route for this problem: many scientific objects are not simple rows of numbers; their connections matter
- Overclaim to avoid: Do not claim that Graphs And Geometric Learning works across systems made of interacting parts, meshes, molecules, or spatial relations without a changed-case test tied to the target quantity.
- Stronger evidence needed: Use held-out measurements, trusted solves, changed boundaries, changed geometry, or changed regimes to test: change the mesh, rotate or move the object, or add missing interactions and inspect what breaks
- First rejection test: the graph can encode the wrong neighborhood, hide missing interactions, or fail when the mesh changes
- Done when: A reviewer can retell the page as problem, evidence, hidden quantity, mathematical move, source limit, and changed-case rejection without adding outside jargon.
- Topic: topics/graphs-and-geometric-learning.html
- Evidence packet: evidence-packets/graphs-and-geometric-learning.html

### P2 Neural Differential Equations
- Status: ready for hand polish
- Supported claim: This page can claim that Neural Differential Equations is a route for this problem: scientists may know that a system changes continuously but not know the exact rule for that change
- Overclaim to avoid: Do not claim that Neural Differential Equations works across changing systems where time evolution is part of the model without a changed-case test tied to the target quantity.
- Stronger evidence needed: Use held-out measurements, trusted solves, changed boundaries, changed geometry, or changed regimes to test: run longer than the training window and check whether small rate errors accumulate into drift
- First rejection test: small learned-rate errors can accumulate until long-time predictions drift away from the real system
- Done when: A reviewer can retell the page as problem, evidence, hidden quantity, mathematical move, source limit, and changed-case rejection without adding outside jargon.
- Topic: topics/neural-differential-equations.html
- Evidence packet: evidence-packets/neural-differential-equations.html

### P2 Operator Learning
- Status: ready for hand polish
- Supported claim: This page can claim that Operator Learning is a route for this problem: one simulation answer is not enough when engineers need the whole map from inputs to solution fields
- Overclaim to avoid: Do not claim that Operator Learning works across fast prediction for families of scientific simulations without a changed-case test tied to the target quantity.
- Stronger evidence needed: Use held-out measurements, trusted solves, changed boundaries, changed geometry, or changed regimes to test: change resolution, coefficients, boundary conditions, or forcing and check whether the predicted field still satisfies the scientific quantity being claimed
- First rejection test: the learned map can give plausible-looking fields that violate the equation or fail on a shifted input family
- Done when: A reviewer can retell the page as problem, evidence, hidden quantity, mathematical move, source limit, and changed-case rejection without adding outside jargon.
- Topic: topics/operator-learning.html
- Evidence packet: evidence-packets/operator-learning.html

### P2 Optimization For Learning
- Status: ready for hand polish
- Supported claim: This page can claim that Optimization For Learning is a route for this problem: learning needs a way to decide which model settings are better or worse
- Overclaim to avoid: Do not claim that Optimization For Learning works across turning model fitting into a repeatable computation without a changed-case test tied to the target quantity.
- Stronger evidence needed: Use held-out measurements, trusted solves, changed boundaries, changed geometry, or changed regimes to test: inspect what the score ignores, then check whether the ignored behavior fails after training
- First rejection test: a model can optimize the written score while missing the scientific behavior the score failed to name
- Done when: A reviewer can retell the page as problem, evidence, hidden quantity, mathematical move, source limit, and changed-case rejection without adding outside jargon.
- Topic: topics/optimization-for-learning.html
- Evidence packet: evidence-packets/optimization-for-learning.html

### P2 Partial Differential Equations
- Status: ready for hand polish
- Supported claim: This page can claim that Partial Differential Equations is a route for this problem: a quantity changes over space and time, so one number is not enough to describe the situation
- Overclaim to avoid: Do not claim that Partial Differential Equations works across fluids, heat, waves, mechanics, chemistry, climate, and other changing fields without a changed-case test tied to the target quantity.
- Stronger evidence needed: Use held-out measurements, trusted solves, changed boundaries, changed geometry, or changed regimes to test: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error
- First rejection test: a learned shortcut can ignore boundary conditions or conservation behavior that the PDE was carrying
- Done when: A reviewer can retell the page as problem, evidence, hidden quantity, mathematical move, source limit, and changed-case rejection without adding outside jargon.
- Topic: topics/partial-differential-equations.html
- Evidence packet: evidence-packets/partial-differential-equations.html

### P2 Physics-Informed Neural Networks
- Status: ready for hand polish
- Supported claim: This page can claim that Physics-Informed Neural Networks is a route for this problem: measurements may be sparse, but the answer must still respect a known physical equation
- Overclaim to avoid: Do not claim that Physics-Informed Neural Networks works across differential equations in science and engineering without a changed-case test tied to the target quantity.
- Stronger evidence needed: Use held-out measurements, trusted solves, changed boundaries, changed geometry, or changed regimes to test: move the training points, inspect sharp regions, and compare against a numerical solve or held-out measurements
- First rejection test: the equation penalty can look small while the solution is wrong in hard regions, sharp layers, or unseen boundary cases
- Done when: A reviewer can retell the page as problem, evidence, hidden quantity, mathematical move, source limit, and changed-case rejection without adding outside jargon.
- Topic: topics/physics-informed-neural-networks.html
- Evidence packet: evidence-packets/physics-informed-neural-networks.html

### P2 Scientific Machine Learning
- Status: ready for hand polish
- Supported claim: This page can claim that Scientific Machine Learning is a route for this problem: scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time
- Overclaim to avoid: Do not claim that Scientific Machine Learning works across using data-driven models inside scientific workflows without a changed-case test tied to the target quantity.
- Stronger evidence needed: Use held-out measurements, trusted solves, changed boundaries, changed geometry, or changed regimes to test: state the scientific quantity first, then test it under a changed case that matters in that domain
- First rejection test: the method becomes a generic fitting tool if the physical quantity, scientific claim, and validation case are not named
- Done when: A reviewer can retell the page as problem, evidence, hidden quantity, mathematical move, source limit, and changed-case rejection without adding outside jargon.
- Topic: topics/scientific-machine-learning.html
- Evidence packet: evidence-packets/scientific-machine-learning.html

### P2 Surrogate Modeling
- Status: ready for hand polish
- Supported claim: This page can claim that Surrogate Modeling is a route for this problem: a trusted simulator may be too slow to run for every design, control, or uncertainty question
- Overclaim to avoid: Do not claim that Surrogate Modeling works across expensive simulation and design loops without a changed-case test tied to the target quantity.
- Stronger evidence needed: Use held-out measurements, trusted solves, changed boundaries, changed geometry, or changed regimes to test: compare against the full solver on new cases near the edge of the intended use
- First rejection test: speed can hide missing physics when the surrogate is used beyond the regime where it was checked
- Done when: A reviewer can retell the page as problem, evidence, hidden quantity, mathematical move, source limit, and changed-case rejection without adding outside jargon.
- Topic: topics/surrogate-modeling.html
- Evidence packet: evidence-packets/surrogate-modeling.html

### P2 Symbolic Regression And Model Discovery
- Status: ready for hand polish
- Supported claim: This page can claim that Symbolic Regression And Model Discovery is a route for this problem: a scientist may need a readable equation, not only a model that predicts well
- Overclaim to avoid: Do not claim that Symbolic Regression And Model Discovery works across turning data into equations people can inspect without a changed-case test tied to the target quantity.
- Stronger evidence needed: Use held-out measurements, trusted solves, changed boundaries, changed geometry, or changed regimes to test: remove a needed variable, add noise, or test a new experiment and see whether the formula still predicts
- First rejection test: a neat formula can fit the training data while using the wrong variables or failing on a changed experiment
- Done when: A reviewer can retell the page as problem, evidence, hidden quantity, mathematical move, source limit, and changed-case rejection without adding outside jargon.
- Topic: topics/symbolic-regression.html
- Evidence packet: evidence-packets/symbolic-regression.html

### P2 Uncertainty And Generalization
- Status: ready for hand polish
- Supported claim: This page can claim that Uncertainty And Generalization is a route for this problem: a prediction is not enough unless the user knows when it should be believed
- Overclaim to avoid: Do not claim that Uncertainty And Generalization works across model use under new conditions without a changed-case test tied to the target quantity.
- Stronger evidence needed: Use held-out measurements, trusted solves, changed boundaries, changed geometry, or changed regimes to test: move one important condition outside the training range and measure the first failure
- First rejection test: training error can look good while the model fails under a new geometry, parameter range, sensor, or physical regime
- Done when: A reviewer can retell the page as problem, evidence, hidden quantity, mathematical move, source limit, and changed-case rejection without adding outside jargon.
- Topic: topics/uncertainty-and-generalization.html
- Evidence packet: evidence-packets/uncertainty-and-generalization.html


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
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in scientific prediction from large measured or simulated data sets, not only a lecture mention.
- Packet: evidence-packets/deep-learning.html

### Physics-Informed Neural Networks
- Problem: measurements may be sparse, but the answer must still respect a known physical equation
- Domain: differential equations in science and engineering
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in differential equations in science and engineering, not only a lecture mention.
- Packet: evidence-packets/physics-informed-neural-networks.html

### Partial Differential Equations
- Problem: a quantity changes over space and time, so one number is not enough to describe the situation
- Domain: fluids, heat, waves, mechanics, chemistry, climate, and other changing fields
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in fluids, heat, waves, mechanics, chemistry, climate, and other changing fields, not only a lecture mention.
- Packet: evidence-packets/partial-differential-equations.html

### Operator Learning
- Problem: one simulation answer is not enough when engineers need the whole map from inputs to solution fields
- Domain: fast prediction for families of scientific simulations
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in fast prediction for families of scientific simulations, not only a lecture mention.
- Packet: evidence-packets/operator-learning.html

### Scientific Machine Learning
- Problem: scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time
- Domain: using data-driven models inside scientific workflows
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in using data-driven models inside scientific workflows, not only a lecture mention.
- Packet: evidence-packets/scientific-machine-learning.html

### Surrogate Modeling
- Problem: a trusted simulator may be too slow to run for every design, control, or uncertainty question
- Domain: expensive simulation and design loops
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in expensive simulation and design loops, not only a lecture mention.
- Packet: evidence-packets/surrogate-modeling.html

### Uncertainty And Generalization
- Problem: a prediction is not enough unless the user knows when it should be believed
- Domain: model use under new conditions
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in model use under new conditions, not only a lecture mention.
- Packet: evidence-packets/uncertainty-and-generalization.html

### Optimization For Learning
- Problem: learning needs a way to decide which model settings are better or worse
- Domain: turning model fitting into a repeatable computation
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in turning model fitting into a repeatable computation, not only a lecture mention.
- Packet: evidence-packets/optimization-for-learning.html

### Generative Modeling
- Problem: some tasks need many possible examples, not one predicted answer
- Domain: creating plausible scientific samples, fields, or candidate designs
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in creating plausible scientific samples, fields, or candidate designs, not only a lecture mention.
- Packet: evidence-packets/generative-modeling.html

### Graphs And Geometric Learning
- Problem: many scientific objects are not simple rows of numbers; their connections matter
- Domain: systems made of interacting parts, meshes, molecules, or spatial relations
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in systems made of interacting parts, meshes, molecules, or spatial relations, not only a lecture mention.
- Packet: evidence-packets/graphs-and-geometric-learning.html

### Neural Differential Equations
- Problem: scientists may know that a system changes continuously but not know the exact rule for that change
- Domain: changing systems where time evolution is part of the model
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in changing systems where time evolution is part of the model, not only a lecture mention.
- Packet: evidence-packets/neural-differential-equations.html

### Symbolic Regression And Model Discovery
- Problem: a scientist may need a readable equation, not only a model that predicts well
- Domain: turning data into equations people can inspect
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in turning data into equations people can inspect, not only a lecture mention.
- Packet: evidence-packets/symbolic-regression.html

### Foundation Models For PDEs
- Problem: one trained model may be asked to handle many related equations, grids, parameters, or physical settings
- Domain: broad families of PDE problems and scientific fields
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in broad families of PDE problems and scientific fields, not only a lecture mention.
- Packet: evidence-packets/foundation-models-for-pdes.html

### Attention For Scientific Fields
- Problem: a local patch of a field may depend on faraway information, but looking everywhere can be expensive
- Domain: large scientific fields where distant parts may interact
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in large scientific fields where distant parts may interact, not only a lecture mention.
- Packet: evidence-packets/attention-for-scientific-fields.html


## Selected Source Anchors

### Deep Learning
- Source: ETH Zurich AISE 2025: Lecture 2 Introduction to Deep Learning
- Page: videos/eth-aise-2025-002-eth-zrich-aise-2025-lecture-2-introduction-to-deep-learning.html
- Claim anchored: Deep learning is the course foundation for fitting flexible models from examples before adding scientific constraints.
- Why this source: This is the 2025 introduction to deep learning in the local transcript set.
- Limit: The source anchors the basic model-fitting foundation; it does not prove a fitted model carries the scientific quantity needed in a new domain.

- Source: ETH Zurich AISE 2024: Introduction to Deep Learning Part 1
- Page: videos/eth-aise-2024-002-eth-zrich-aise-introduction-to-deep-learning-part-1.html
- Claim anchored: The 2024 deep-learning introduction anchors the shared vocabulary used before PINNs, operators, surrogates, and generative models.
- Why this source: This lecture starts the 2024 deep-learning block that later methods build on.
- Limit: The source supports the prerequisite role of deep learning; every later scientific claim still needs its own domain and changed-case test.


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


### Partial Differential Equations
- Source: ETH Zurich AISE 2024: Importance of PDEs in Science
- Page: videos/eth-aise-2024-004-eth-zrich-aise-importance-of-pdes-in-science.html
- Claim anchored: PDEs are the field language for quantities that change across space and time.
- Why this source: This lecture is the local source focused on why PDEs matter in scientific settings.
- Limit: The source anchors why PDEs matter; it does not solve any particular PDE or validate a learned approximation.

- Source: ETH Zurich AISE 2025: Lecture 3 Physics-Informed Neural Networks Introduction
- Page: videos/eth-aise-2025-003-eth-zrich-aise-2025-lecture-3-physics-informed-neural-networks-introduction.html
- Claim anchored: PINN lectures depend on PDE residuals because the equation is used as a check on the learned field.
- Why this source: This lecture places differential equations inside the physics-informed learning route.
- Limit: The source supports PDEs as a constraint source; it does not prove the equation is complete for every experiment.


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


### Scientific Machine Learning
- Source: ETH Zurich AISE 2025: Lecture 1 Course Introduction
- Page: videos/eth-aise-2025-001-eth-zrich-aise-2025-lecture-1-course-introduction.html
- Claim anchored: Scientific machine learning combines learned models with scientific quantities, equations, and validation checks.
- Why this source: This lecture introduces the 2025 course scope: AI in science and engineering.
- Limit: The source anchors the course-level field framing; it does not prove any one method works for a specific scientific job.

- Source: ETH Zurich AISE 2024: Course Introduction
- Page: videos/eth-aise-2024-001-eth-zrich-aise-course-introduction.html
- Claim anchored: The 2024 course introduction anchors the broad route from AI methods to science and engineering applications.
- Why this source: This is the 2024 starting point for the local playlist family.
- Limit: The source supports the field-level map; task-level claims still need evidence, domain limits, and changed-case tests.


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


### Optimization For Learning
- Source: ETH Zurich AISE 2024: Introduction to Deep Learning Part 2
- Page: videos/eth-aise-2024-003-eth-zrich-aise-introduction-to-deep-learning-part-2.html
- Claim anchored: Optimization is the mechanism that turns a written training objective into model settings.
- Why this source: This lecture continues the deep-learning setup where training and fitting are introduced.
- Limit: The source anchors optimization as training machinery; it does not prove the optimized score matches the scientific decision.

- Source: ETH Zurich AISE 2025: Lecture 3 Physics-Informed Neural Networks Introduction
- Page: videos/eth-aise-2025-003-eth-zrich-aise-2025-lecture-3-physics-informed-neural-networks-introduction.html
- Claim anchored: PINNs make the optimization burden visible because data, equation, and boundary errors are trained together.
- Why this source: This lecture anchors an example where the loss contains multiple scientific burdens.
- Limit: The source supports the need to inspect loss terms; it does not guarantee that optimizing those terms finds the right physical field.


### Generative Modeling
- Source: ETH Zurich AISE 2025: Lecture 11 Generative Models for PDEs GenCFD
- Page: videos/eth-aise-2025-011-eth-zrich-aise-2025-lecture-11-generative-models-for-pdes-gencfd.html
- Claim anchored: Generative models for PDEs are used when the task needs possible scientific fields, not only one predicted field.
- Why this source: This is the 2025 lecture dedicated to generative models for PDEs in the local source set.
- Limit: The source anchors the generative-model topic; generated fields still need conservation, constraint, and downstream-use checks.

- Source: ETH Zurich AISE 2024: Introduction to Diffusion Models
- Page: videos/eth-aise-2024-022-eth-zrich-aise-introduction-to-diffusion-models.html
- Claim anchored: Diffusion models are a neighboring generative route for creating samples rather than a single deterministic answer.
- Why this source: This lecture provides the 2024 generative-model background in the local transcript set.
- Limit: The source supports the generative route; it does not prove samples are valid scientific objects without domain checks.


### Graphs And Geometric Learning
- Source: ETH Zurich AISE 2025: Lecture 9 Operator Learning Graph-based Models
- Page: videos/eth-aise-2025-009-eth-zrich-aise-2025-lecture-9-operator-learning-graph-based-models.html
- Claim anchored: Graph-based operator models keep connections visible when scientific data live on meshes, graphs, or irregular geometry.
- Why this source: This lecture is the 2025 graph-based operator-learning treatment.
- Limit: The source anchors graph-based modeling; it does not prove the chosen graph contains every interaction that matters.

- Source: ETH Zurich AISE 2025: Lecture 13 AI in Chemistry Biology Part 1
- Page: videos/eth-aise-2025-013-eth-zrich-aise-2025-lecture-13-ai-in-chemistry-biology-part-1.html
- Claim anchored: Applications in chemistry and biology motivate graph and geometric representations because molecules and biological objects have structure.
- Why this source: This lecture anchors structured scientific objects in chemistry and biology applications.
- Limit: The source supports the domain motivation; property prediction still needs changed-molecule and held-out-family checks.


### Neural Differential Equations
- Source: ETH Zurich AISE 2024: Neural Differential Equations
- Page: videos/eth-aise-2024-021-eth-zrich-aise-neural-differential-equations.html
- Claim anchored: Neural differential equations learn or include a change rule inside a time-evolution calculation.
- Why this source: This is the local lecture dedicated to neural differential equations.
- Limit: The source anchors the concept; long-time behavior and changed initial conditions still need separate validation.

- Source: ETH Zurich AISE 2024: Symbolic Regression and Model Discovery
- Page: videos/eth-aise-2024-024-eth-zrich-aise-symbolic-regression-and-model-discovery.html
- Claim anchored: Model discovery and symbolic regression are neighboring ideas when the goal is to recover a readable or testable change rule.
- Why this source: This lecture anchors the related model-discovery route.
- Limit: The source supports the connection; it does not prove a learned differential equation is stable or physically complete.


### Attention For Scientific Fields
- Source: ETH Zurich AISE 2024: Attention as a Neural Operator
- Page: videos/eth-aise-2024-017-eth-zrich-aise-attention-as-a-neural-operator.html
- Claim anchored: Attention is treated as a neural-operator route for moving information across scientific fields.
- Why this source: This lecture directly connects attention to neural operators in the 2024 source set.
- Limit: The source anchors the attention-as-operator idea; the chosen attention pattern still needs checks for missed long-range effects.

- Source: ETH Zurich AISE 2024: Windowed Attention and Scaling Laws
- Page: videos/eth-aise-2024-018-eth-zrich-aise-windowed-attention-and-scaling-laws.html
- Claim anchored: Windowed attention and scaling choices matter because field models must decide which distant information is worth carrying.
- Why this source: This lecture follows the attention-as-operator treatment and focuses on windowing and scaling.
- Limit: The source supports the design pressure; it does not prove a specific window or attention pattern preserves the scientific quantity.


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
- Remote repository is created and main is pushed.
- For any later commit, run git push and compare git ls-remote origin main with git rev-parse main.
- Keep this handoff updated whenever the latest local commit changes.
- Optional later editorial work: replace selected source anchors with manually verified short lecture quotes.

### Remote Verification Commands
- Status: Configured origin is https://github.com/mehtama1234/physics-informed-machine-learning-concepts-research.git. The repository exists, main is pushed, and origin/main should match local main after each final push.
- `git status --short --branch`
- `git remote -v`
- `git rev-parse main`
- `git ls-remote --heads origin main`
- `make remote-check`
- `make ci-check`
- `python3 scripts/verify_remote_state.py`
- `python3 scripts/verify_ci_status.py`
- `git push -u origin main`

## Review Entrypoints

### Start The Review
- Purpose: Use these pages to see the whole argument before inspecting details.
- Review Handoff: handoff.html | What exists now, and what still needs hand-written depth?
- Find Pages By Question: review-search.html | Which page should I open for the question I have right now?
- Completion Audit: completion-audit.html | What is locally verified, and what is still outside the workspace?
- Editorial Roadmap: editorial-roadmap.html | What is the meaty next goal after the generated first pass?
- Meaty Goal: meaty-goal.html | What must be true before these writeups should count as done?
- Meaty Goal Coverage: meaty-goal-coverage.html | Which concepts still miss a required first-principles teaching section?
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
- Review Queue: review-queue.html
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
- Review Queue: review-queue.html
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

## Meaty End-To-End Goal
- Goal: Turn the Physics-Informed Machine Learning site from a structured first-pass atlas into a teaching-grade research package that explains the paper family from first principles.
- Target reader: A new reader who does not know the math, machine learning terms, benchmark language, causal language, optimization language, or systems language.
- Acceptance sentence: This concept exists because scientists need ___, but they only observe ___. The hidden thing is ___. The math does ___ because ___. It matters in ___ domain because ___. It fails when ___. I would test it by changing ___.

### Done Means
- The reader can start from a plain scientific problem before seeing a method name.
- The reader can name the real quantity being predicted, explained, controlled, designed, or discovered.
- The reader can name the available evidence: measurements, equations, simulations, boundary information, geometry, prior cases, or transcript support.
- The reader can name what is hidden, missing, or unknown.
- The reader can explain why the mathematical move follows from that missing piece.
- The reader can translate the formula shape into everyday language.
- The reader can say which domain the idea belongs to and why solving it matters there.
- The reader can say what the method keeps, what it ignores, and where it fails.
- The reader can name the changed case that would reject an overclaim.
- The reader can connect the concept to nearby concepts, examples, diagrams, and source anchors.

### Every Core Page Must Contain
- A concrete domain story that starts from a real scientific job.
- A first-principles derivation from observed evidence to hidden quantity to mathematical move.
- A plain formula explanation that says what every term carries.
- A worked example and a wrong-use example.
- A failure boundary and a changed-case rejection test.
- Transcript anchors that state what the source supports and what it does not prove.
- Links to nearby concepts, diagrams, derivations, examples, and reader checks.

### Not Done If
- The page starts with a method name but does not explain the world problem first.
- The page says a model learns patterns without naming the quantity, evidence, hidden part, and failure test.
- The page uses broad confidence words instead of a changed-case test.
- The page has transcript evidence but does not state what the evidence fails to prove.
- The page cannot be retold by a new reader in ordinary language.

## Meaty Goal Coverage Audit
### Deep Learning
- Common problem: scientists often have examples of behavior but no short rule that predicts the next case
- Missing items: none
- Present required parts: First Principles, Hand Teaching Note, Case Walkthrough, Concept Connections, Belief Evidence, Domain Fit, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Acceptance Sentence
- Topic: topics/deep-learning.html
- Evidence packet: evidence-packets/deep-learning.html
- Reader check: reader-checks/deep-learning-check.html

### Physics-Informed Neural Networks
- Common problem: measurements may be sparse, but the answer must still respect a known physical equation
- Missing items: none
- Present required parts: First Principles, Hand Teaching Note, Case Walkthrough, Concept Connections, Belief Evidence, Domain Fit, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Acceptance Sentence
- Topic: topics/physics-informed-neural-networks.html
- Evidence packet: evidence-packets/physics-informed-neural-networks.html
- Reader check: reader-checks/pinns-check.html

### Partial Differential Equations
- Common problem: a quantity changes over space and time, so one number is not enough to describe the situation
- Missing items: none
- Present required parts: First Principles, Hand Teaching Note, Case Walkthrough, Concept Connections, Belief Evidence, Domain Fit, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Acceptance Sentence
- Topic: topics/partial-differential-equations.html
- Evidence packet: evidence-packets/partial-differential-equations.html
- Reader check: reader-checks/partial-differential-equations-check.html

### Operator Learning
- Common problem: one simulation answer is not enough when engineers need the whole map from inputs to solution fields
- Missing items: none
- Present required parts: First Principles, Hand Teaching Note, Case Walkthrough, Concept Connections, Belief Evidence, Domain Fit, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Acceptance Sentence
- Topic: topics/operator-learning.html
- Evidence packet: evidence-packets/operator-learning.html
- Reader check: reader-checks/operator-learning-check.html

### Scientific Machine Learning
- Common problem: scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time
- Missing items: none
- Present required parts: First Principles, Hand Teaching Note, Case Walkthrough, Concept Connections, Belief Evidence, Domain Fit, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Acceptance Sentence
- Topic: topics/scientific-machine-learning.html
- Evidence packet: evidence-packets/scientific-machine-learning.html
- Reader check: reader-checks/scientific-machine-learning-check.html

### Surrogate Modeling
- Common problem: a trusted simulator may be too slow to run for every design, control, or uncertainty question
- Missing items: none
- Present required parts: First Principles, Hand Teaching Note, Case Walkthrough, Concept Connections, Belief Evidence, Domain Fit, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Acceptance Sentence
- Topic: topics/surrogate-modeling.html
- Evidence packet: evidence-packets/surrogate-modeling.html
- Reader check: reader-checks/surrogate-check.html

### Uncertainty And Generalization
- Common problem: a prediction is not enough unless the user knows when it should be believed
- Missing items: none
- Present required parts: First Principles, Hand Teaching Note, Case Walkthrough, Concept Connections, Belief Evidence, Domain Fit, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Acceptance Sentence
- Topic: topics/uncertainty-and-generalization.html
- Evidence packet: evidence-packets/uncertainty-and-generalization.html
- Reader check: reader-checks/uncertainty-check.html

### Optimization For Learning
- Common problem: learning needs a way to decide which model settings are better or worse
- Missing items: none
- Present required parts: First Principles, Hand Teaching Note, Case Walkthrough, Concept Connections, Belief Evidence, Domain Fit, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Acceptance Sentence
- Topic: topics/optimization-for-learning.html
- Evidence packet: evidence-packets/optimization-for-learning.html
- Reader check: reader-checks/optimization-for-learning-check.html

### Generative Modeling
- Common problem: some tasks need many possible examples, not one predicted answer
- Missing items: none
- Present required parts: First Principles, Hand Teaching Note, Case Walkthrough, Concept Connections, Belief Evidence, Domain Fit, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Acceptance Sentence
- Topic: topics/generative-modeling.html
- Evidence packet: evidence-packets/generative-modeling.html
- Reader check: reader-checks/generative-modeling-check.html

### Graphs And Geometric Learning
- Common problem: many scientific objects are not simple rows of numbers; their connections matter
- Missing items: none
- Present required parts: First Principles, Hand Teaching Note, Case Walkthrough, Concept Connections, Belief Evidence, Domain Fit, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Acceptance Sentence
- Topic: topics/graphs-and-geometric-learning.html
- Evidence packet: evidence-packets/graphs-and-geometric-learning.html
- Reader check: reader-checks/graphs-and-geometric-learning-check.html

### Neural Differential Equations
- Common problem: scientists may know that a system changes continuously but not know the exact rule for that change
- Missing items: none
- Present required parts: First Principles, Hand Teaching Note, Case Walkthrough, Concept Connections, Belief Evidence, Domain Fit, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Acceptance Sentence
- Topic: topics/neural-differential-equations.html
- Evidence packet: evidence-packets/neural-differential-equations.html
- Reader check: reader-checks/neural-differential-equations-check.html

### Symbolic Regression And Model Discovery
- Common problem: a scientist may need a readable equation, not only a model that predicts well
- Missing items: none
- Present required parts: First Principles, Hand Teaching Note, Case Walkthrough, Concept Connections, Belief Evidence, Domain Fit, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Acceptance Sentence
- Topic: topics/symbolic-regression.html
- Evidence packet: evidence-packets/symbolic-regression.html
- Reader check: reader-checks/symbolic-regression-check.html

### Foundation Models For PDEs
- Common problem: one trained model may be asked to handle many related equations, grids, parameters, or physical settings
- Missing items: none
- Present required parts: First Principles, Hand Teaching Note, Case Walkthrough, Concept Connections, Belief Evidence, Domain Fit, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Acceptance Sentence
- Topic: topics/foundation-models-for-pdes.html
- Evidence packet: evidence-packets/foundation-models-for-pdes.html
- Reader check: reader-checks/foundation-pde-check.html

### Attention For Scientific Fields
- Common problem: a local patch of a field may depend on faraway information, but looking everywhere can be expensive
- Missing items: none
- Present required parts: First Principles, Hand Teaching Note, Case Walkthrough, Concept Connections, Belief Evidence, Domain Fit, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Acceptance Sentence
- Topic: topics/attention-for-scientific-fields.html
- Evidence packet: evidence-packets/attention-for-scientific-fields.html
- Reader check: reader-checks/attention-for-scientific-fields-check.html


## Editorial Roadmap
### P0 Pin Down The Core Argument
- Status: locally completed
- Goal: Make the first review route say one thing clearly: physics-informed machine learning is about making learned answers answerable to data, physical rules, and changed scientific cases.
- Why it matters: Without this, readers see a pile of methods. With it, every concept becomes a different answer to the same scientific pressure.
- Current evidence: The home page, synthesis pages, and learning path now use the five-part route: real quantity, evidence, missing quantity, mathematical move, and changed-case test.
- Proof pages: index.html, synthesis/central-problem.html, learning-path/scientific-question-first.html
- Target pages: synthesis.html, learning-path.html, handoff.html, completion-audit.html
- Work: Rewrite the opening paragraphs so they start from the scientific problem before naming methods.; Make every route explain what is observed, what is hidden, what rule is kept, and what changed case can reject the claim.; Remove any sentence that sounds impressive but does not name evidence, domain, quantity, or failure test.
- Acceptance check: A new reader can say the field's common problem in one sentence before opening any topic page.

### P0 Add Source Anchors To Core Concepts
- Status: locally completed
- Goal: Turn the main topic pages and evidence packets into source-backed teaching pages, not only generated summaries.
- Why it matters: The package is transcript-backed only if the important claims point to lecture-specific support and state what that support does not prove.
- Current evidence: Core topic pages and evidence packets include selected source anchors with claim, source page, reason, and limit.
- Proof pages: topics/physics-informed-neural-networks.html, evidence-packets/foundation-models-for-pdes.html, evidence-packets/operator-learning.html
- Target pages: topics/physics-informed-neural-networks.html, topics/operator-learning.html, topics/uncertainty-and-generalization.html, topics/foundation-models-for-pdes.html, evidence-packets.html
- Work: Manually review the transcript excerpts for each core concept and choose the best source anchors.; Add a short source note beside each major claim: what the lecture supports, and what it does not settle.; Prefer concrete lecture moments over broad statements.
- Acceptance check: Each core concept has at least two reviewed transcript anchors and one clear limit statement.

### P0 Deepen The Hand Derivations
- Status: locally completed
- Goal: Make the math feel inevitable from the problem instead of appearing as a finished formula.
- Why it matters: The reader should see why the terms show up: data error comes from measured points, physics error comes from the equation, uncertainty comes from possible wrong answers, and operators come from learning a map between fields.
- Current evidence: Core derivation pages include Hand Derivation tables that explain each term, why it enters, and how to check it.
- Proof pages: derivations/physics-informed-neural-networks.html, derivations/operator-learning.html, derivations/foundation-models-for-pdes.html
- Target pages: derivations.html, derivations/physics-informed-neural-networks.html, derivations/operator-learning.html, derivations/foundation-models-for-pdes.html, formula-guide.html
- Work: Add one handwritten derivation from observed evidence to loss shape for PINNs.; Add one derivation showing why operator learning maps a whole input field to a whole output field.; Add one derivation showing what must be shared before a PDE model can transfer to a new equation case.; Keep each line in everyday language before adding symbols.
- Acceptance check: A reader who skips the formula can still explain why each term exists and what would make it fail.

### P1 Add Figures And Mathematical Sketches
- Status: locally completed
- Goal: Replace purely textual explanation where a picture would reveal the object being learned or checked.
- Why it matters: Some ideas are spatial: a PDE field, a boundary, a residual point, an input field, an output field, or a shifted test case. A sketch can make the hidden quantity visible.
- Current evidence: The diagrams index and core topic pages include mathematical sketches with input, output, kept rule, and failure case.
- Proof pages: diagrams.html, topics/operator-learning.html, topics/surrogate-modeling.html
- Target pages: diagrams.html, topics/physics-informed-neural-networks.html, topics/operator-learning.html, topics/surrogate-modeling.html, topics/uncertainty-and-generalization.html
- Work: Add one sketch for measured points plus equation-check points.; Add one sketch for input field to output field.; Add one sketch for a fast surrogate inside repeated scientific choices.; Add one sketch for a shifted case where the model should admit doubt.
- Acceptance check: Each sketch names input, output, kept rule, and failure case in the caption.

### P1 Strengthen Domain Examples
- Status: locally completed
- Goal: Make chemistry, materials, climate, fluids, and geometry pages show real scientific jobs rather than generic use cases.
- Why it matters: The math matters because a scientist needs a quantity for a decision: a molecule property, stress field, flow force, climate risk, or field on an irregular shape.
- Current evidence: Each domain guide includes a concrete scientific job with observed evidence, hidden quantity, decision, and changed-case test.
- Proof pages: domains/chemistry-and-biology.html, domains/materials-and-mechanics.html, domains/many-pde-tasks.html
- Target pages: domains.html, worked-examples.html, worked-examples/molecule-property-from-structure.html, worked-examples/material-stress-from-sparse-tests.html, worked-examples/climate-risk-under-shifted-conditions.html
- Work: Add one richer concrete example per domain.; Name the observed evidence, hidden quantity, decision, and changed-case test.; Tie each example back to one concept page, one derivation, and one evidence packet.
- Acceptance check: Each domain page contains a concrete scientific job that cannot be mistaken for a generic prediction task.

### P1 Sharpen Nearby Method Comparisons
- Status: locally completed
- Goal: Make the comparison pages teach what changes when two methods sound similar.
- Why it matters: Readers often confuse fitting data, obeying a rule, learning a solver shortcut, and building a cheap stand-in. The package should separate those by job and evidence.
- Current evidence: Each comparison page includes left-case, right-case, wrong-choice case, and evidence that exposes the wrong choice.
- Proof pages: comparisons/pinns-vs-neural-operators.html, comparisons/solvers-vs-learned-surrogates.html
- Target pages: comparisons.html, decision-guide.html, misconceptions.html, dependencies.html
- Work: For each comparison, add one situation where the left method is right and one where the right method is right.; Add one wrong-choice example and the evidence that would expose it.; Keep the language tied to the scientific job, not method labels.
- Acceptance check: A reader can choose between two nearby methods by naming the job, evidence, and failure case.

### P2 Finish Replication And Remote State
- Status: locally completed
- Goal: Make the package easy for another CLI to reproduce and push once the GitHub repository exists.
- Why it matters: Local validation proves the package files. The final handoff also needs a verified remote so another person can clone and continue.
- Current evidence: The GitHub repository exists, main is pushed, and git ls-remote origin main can be compared with git rev-parse main after each final push.
- Proof pages: completion-audit.html, handoff.html, provenance/cli-reproduction.html
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
- Evidence: summary reports 5 domain guides and 8 worked examples; domain guides include concrete scientific job cards and worked examples include end-to-end flow traces.

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
- Status: locally verified
- Evidence: origin is configured at https://github.com/mehtama1234/physics-informed-machine-learning-concepts-research.git; main has been pushed and can be verified with git ls-remote --heads origin main.

### Run the generated-site checks in GitHub Actions for pushed commits.
- Status: locally verified
- Evidence: the check workflow runs make check on push and pull request; make ci-check verifies the current commit's workflow run through the GitHub Actions API.

