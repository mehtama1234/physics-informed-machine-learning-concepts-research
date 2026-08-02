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
- sketch_count: 6
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
- review_entrypoint_count: 30
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

## Course Spine In Plain Words
- Whole course problem: move from partial evidence to a scientific answer without hiding what would make the answer fail.
- Evidence can be measurements, equations, solved cases, simulations, geometry, shape, topology, previous examples, or source support.
- Missing answers can be fields, future states, properties, design answers, readable rules, maps, or trust boundaries.
- First-principles route: name the decision, name the evidence, name the missing thing, choose the carrier, keep the boundary visible, and end with a changed case.
- Topology and shape matter because meshes, molecules, bridges, wings, coastlines, proteins, sensor networks, and fields have structure before a model sees them.
- Reader test: open any topic and say the real problem, evidence, missing answer, mathematical move, allowed claim, left-out part, and first changed case in everyday words.

## Topology And Shape In Plain Words
- Everyday meaning: ask what stays connected, what has a hole, what touches what, and what can bend without changing the question.
- First-principles reason: many scientific objects are not loose rows of numbers; their boundaries, connections, distances, and symmetries are evidence.
- Main failure: a model can flatten away the relation that carries the scientific quantity, then look good on old cases while failing on a changed shape.
- Shape check: change geometry, boundary, mesh order, missing connection, long-range link, or shape family and inspect the named quantity.

## Shape Transfer Practice
- See `site/shape-transfer-practice.html` for learner drills that move each topology or shape idea across engineering, materials or biology, and climate or field uses.

## Question To Topic Guide
- Everyday question: I have many examples, but I do not have a short rule. Where do I start? Open this topic: Deep Learning. First stop reason: scientists often have examples of behavior but no short rule that predicts the next case. First check: the model can fit familiar examples while failing on a new material, geometry, scale, or boundary condition. Mathematical move: adjust many weights until the model maps familiar inputs to the right outputs.
- Everyday question: I have a few measurements and a known equation. How do I make them work together? Open this topic: Physics-Informed Neural Networks. First stop reason: measurements may be sparse, but the answer must still respect a known physical equation. First check: the equation penalty can look small while the solution is wrong in hard regions, sharp layers, or unseen boundary cases. Mathematical move: fit a neural network while also measuring how badly its output violates the known equation.
- Everyday question: My quantity changes across space and time. What language describes that change? Open this topic: Partial Differential Equations. First stop reason: a quantity changes over space and time, so one number is not enough to describe the situation. First check: a learned shortcut can ignore boundary conditions or conservation behavior that the PDE was carrying. Mathematical move: write a local change rule that uses rates across space and time.
- Everyday question: I need the whole answer field for new inputs, not only one solved case. What carries that map? Open this topic: Operator Learning. First stop reason: one simulation answer is not enough when engineers need the whole map from inputs to solution fields. First check: the learned map can give plausible-looking fields that violate the equation or fail on a shifted input family. Mathematical move: learn the map from problem input to solution, not only one solution at a time.
- Everyday question: I need data, equations, units, and checks to live in one scientific claim. What is the broad home for that? Open this topic: Scientific Machine Learning. First stop reason: scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time. First check: the method becomes a generic fitting tool if the physical quantity, scientific claim, and validation case are not named. Mathematical move: combine learned prediction with scientific checks that name what the claim is allowed to mean.
- Everyday question: My trusted solver is too slow to run for every design or control question. What is the first shortcut to study? Open this topic: Surrogate Modeling. First stop reason: a trusted simulator may be too slow to run for every design, control, or uncertainty question. First check: speed can hide missing physics when the surrogate is used beyond the regime where it was checked. Mathematical move: train a cheaper stand-in for the expensive input-output behavior.
- Everyday question: I have a prediction, but I need to know when to believe it. What topic handles that? Open this topic: Uncertainty And Generalization. First stop reason: a prediction is not enough unless the user knows when it should be believed. First check: training error can look good while the model fails under a new geometry, parameter range, sensor, or physical regime. Mathematical move: separate fit on familiar examples from evidence on changed examples.
- Everyday question: The model is changing its settings. How do I know what it is being asked to improve? Open this topic: Optimization For Learning. First stop reason: learning needs a way to decide which model settings are better or worse. First check: a model can optimize the written score while missing the scientific behavior the score failed to name. Mathematical move: change model settings to lower the written score.
- Everyday question: I need several possible fields, molecules, shapes, or scenarios, not one answer. Where do I start? Open this topic: Generative Modeling. First stop reason: some tasks need many possible examples, not one predicted answer. First check: generated samples can look realistic while breaking constraints, conservation, or rare-event behavior. Mathematical move: learn how to sample new candidates that resemble the training family.
- Everyday question: My object has parts, neighbors, bonds, mesh points, or shape. Which topic keeps those relations visible? Open this topic: Graphs And Geometric Learning. First stop reason: many scientific objects are not simple rows of numbers; their connections matter. First check: the graph can encode the wrong neighborhood, hide missing interactions, or fail when the mesh changes. Mathematical move: let information move along the object connections instead of flattening the object into a plain row.
- Everyday question: A system changes over time, but the rate rule is partly unknown. What topic should I open? Open this topic: Neural Differential Equations. First stop reason: scientists may know that a system changes continuously but not know the exact rule for that change. First check: small learned-rate errors can accumulate until long-time predictions drift away from the real system. Mathematical move: learn the missing rate rule and place it inside a time-evolution calculation.
- Everyday question: I want a readable equation from measured variables. What topic is about that search? Open this topic: Symbolic Regression And Model Discovery. First stop reason: a scientist may need a readable equation, not only a model that predicts well. First check: a neat formula can fit the training data while using the wrong variables or failing on a changed experiment. Mathematical move: search for a readable equation that fits the data and survives a changed case.
- Everyday question: I want one field model to help across related PDE tasks. What should I read first? Open this topic: Foundation Models For PDEs. First stop reason: one trained model may be asked to handle many related equations, grids, parameters, or physical settings. First check: the model can look broad while missing rare regimes, new boundary conditions, or quantities not represented in training. Mathematical move: train one broad model to reuse structure across many related field-prediction tasks.
- Everyday question: Faraway parts of a field may affect the local answer. What topic explains that information route? Open this topic: Attention For Scientific Fields. First stop reason: a local patch of a field may depend on faraway information, but looking everywhere can be expensive. First check: windowing or scaling choices can miss long-range effects that matter for the scientific quantity being predicted. Mathematical move: let the model choose which parts of the field exchange information.

## Field Application Guide In Plain Words
### Engineering design
- Deep Learning: use: Sort old test runs so a designer can screen the next part before a costly build. Why: The learned pattern saves time only inside the kind of cases it has actually survived. Check: Test a new material, sensor, or part size before using the prediction for a build decision.
- Physics-Informed Neural Networks: use: Estimate heat, stress, flow, or pressure when tests are sparse but the physical law is known. Why: The design answer is useful only if the fitted field respects the law between measured points. Check: Inspect sharp regions, edge cases, and held-out sensors near the places where failure would matter.
- Partial Differential Equations: use: Write the rule for heat, stress, flow, pressure, or waves before choosing a learning method. Why: The equation states what must be true for the design quantity to be believable. Check: Change load, source, geometry, or scale and inspect the quantity used for the decision.
- Operator Learning: use: Give fast field estimates for repeated wing, device, part, or load queries. Why: The shortcut is useful only if it keeps the design quantity accurate across the tested family. Check: Compare lift, drag, stress, heat, or pressure against trusted solves near the design edge.
- Scientific Machine Learning: use: Use data and scientific checks together when a design decision has a cost. Why: The method is useful only if it names the decision and the failure condition. Check: Test near the build limit, load limit, safety limit, or operating limit.
- Surrogate Modeling: use: Screen many candidate parts, wings, devices, or loads before running the costly solve. Why: Speed matters only when the shortcut preserves the quantity that drives the design choice. Check: Test near peaks, boundaries, rare regimes, and cases where the decision changes.
- Uncertainty And Generalization: use: Attach a use range and warning boundary to a prediction before a design choice. Why: A confident answer is dangerous when the design is outside the checked range. Check: Move load, material, size, or boundary beyond training and measure the first failure.
- Optimization For Learning: use: Train toward the quantity that drives the design, not only average error. Why: The score decides what the model learns to care about. Check: Check rare loads, edge cases, constraints, and the final design quantity after training.
- Generative Modeling: use: Propose candidate parts, layouts, fields, or operating cases for later testing. Why: The generated candidate is useful only if it can pass the design checks. Check: Run constraints, full solves, stress tests, and use-case checks on generated candidates.
- Graphs And Geometric Learning: use: Model meshes, parts, sensor networks, or connected components without flattening away contact. Why: The design answer can depend on which parts touch, not only on the part list. Check: Change mesh resolution, contact regions, or boundary connections and compare the design quantity.
- Neural Differential Equations: use: Predict changing heat, motion, wear, control, or flow when the exact rate rule is unknown. Why: The rate rule matters because small errors can grow over time. Check: Test long-time drift, stability, conservation, and changed starting conditions.
- Symbolic Regression And Model Discovery: use: Find a readable equation that links design variables to the decision quantity. Why: The equation is useful when people can inspect, test, and reject it. Check: Run a changed design case and reject formulas that only fit old designs.
- Foundation Models For PDEs: use: Start from a broad PDE model for a new device or part, then verify the design quantity. Why: Breadth helps only when it reduces work without hiding a failed design case. Check: Compare with trusted solves on new designs near the intended use boundary.
- Attention For Scientific Fields: use: Route information across a part, surface, or field where distant regions interact. Why: The design quantity may depend on faraway pressure, heat, load, or flow behavior. Check: Stress long-range cases and compare the design quantity near hard regions.
### Materials, chemistry, and biology
- Deep Learning: use: Read images, spectra, molecules, or cell measurements when hand rules are incomplete. Why: The answer matters when it flags a property or risk that a person must inspect. Check: Hold out a lab, instrument, molecule family, or cell type and compare the measured property.
- Physics-Informed Neural Networks: use: Fill in missing concentration, strain, or reaction fields while keeping known balance rules visible. Why: The method helps when measurements are expensive and the known rule should constrain the answer. Check: Change material settings, boundary values, or reaction conditions and compare with measurements.
- Partial Differential Equations: use: Track diffusion, reaction, strain, growth, or transport through a material or tissue. Why: The field answer matters because local change can create a global effect. Check: Change a coefficient, source, boundary, or sample shape and compare with measurements.
- Operator Learning: use: Map a material setting, molecular field, or tissue condition to a response field. Why: The method helps when each new query would otherwise need a slow solve. Check: Hold out a new material range, molecule type, or biological condition and inspect the response.
- Scientific Machine Learning: use: Tie learned predictions to units, mechanisms, measurements, and domain limits. Why: The answer matters when it changes an experiment, a screening choice, or a safety claim. Check: Hold out a new lab setting, material range, molecule family, or measured condition.
- Surrogate Modeling: use: Use a cheaper stand-in for repeated material, molecule, or tissue simulations. Why: The stand-in helps when it stays inside the checked query range. Check: Compare with trusted simulations or measurements on new settings near the use boundary.
- Uncertainty And Generalization: use: Say when a measured property prediction should weaken under a new lab or sample condition. Why: The claim matters only if the user knows where belief should stop. Check: Hold out a new instrument, molecule family, tissue type, or material batch.
- Optimization For Learning: use: Set the training score so it respects measured properties, units, and known checks. Why: A low score is useful only if it includes the scientific burden. Check: Inspect what the score ignored, then test the ignored behavior on new samples.
- Generative Modeling: use: Suggest molecules, structures, images, or samples that should still obey known rules. Why: A sample matters when it can be measured, built, or screened for a real property. Check: Reject samples that break chemistry rules, material limits, or biological measurements.
- Graphs And Geometric Learning: use: Represent atoms, bonds, cells, proteins, grains, or interaction networks as connected objects. Why: The property often depends on neighbors and long-range interactions. Check: Hold out new structures, rotations, missing interactions, or graph sizes.
- Neural Differential Equations: use: Learn reaction, growth, motion, or change rules from measured time traces. Why: The model is useful when it explains how the next state follows from the present state. Check: Hold out time ranges, doses, reaction settings, or starting conditions.
- Symbolic Regression And Model Discovery: use: Search for compact laws from measured variables, ingredients, and properties. Why: A short equation matters only if it survives new measurements. Check: Add noise, hold out a condition, or test a missing variable.
- Foundation Models For PDEs: use: Transfer learned field behavior across related materials, tissues, or reaction settings. Why: The model matters when the new task shares the structure it actually learned. Check: Hold out a task family, material range, tissue setting, or coefficient regime.
- Attention For Scientific Fields: use: Let distant atoms, cells, residues, or regions influence a local prediction. Why: The method helps when the local property depends on nonlocal context. Check: Remove long-range context, change structure, or hold out larger objects.
### Climate, fluids, and fields
- Deep Learning: use: Learn repeated field patterns from stored simulations or measurements. Why: The model is useful only when the learned pattern still answers the field question people care about. Check: Change the region, forcing, boundary, or rare event and inspect where the field fails first.
- Physics-Informed Neural Networks: use: Recover a full field from sparse measurements without ignoring the governing equation. Why: The important claim is not a smooth picture; it is whether the field follows the physical rule. Check: Change source terms, boundaries, or sensor placement and compare against a solver or held-out data.
- Partial Differential Equations: use: Describe wind, heat, concentration, pressure, and water over space and time. Why: A single number cannot carry the decision when the whole field changes. Check: Check mass, energy, boundary behavior, stability, and measured error under a changed case.
- Operator Learning: use: Map forcing, boundary, or initial fields to future solution fields. Why: The value is speed across a named family, not proof across all possible fields. Check: Change forcing, scale, resolution, or rare regimes and compare with trusted simulations.
- Scientific Machine Learning: use: Use learned models only with clear field checks, physical checks, and use ranges. Why: A field prediction is useful when it survives the changed case that matters to the user. Check: Change region, season, boundary, forcing, or resolution and measure the decision quantity.
- Surrogate Modeling: use: Answer repeated field queries faster than running a full model each time. Why: The shortcut is useful only where the field behavior was checked against trusted runs. Check: Hold out storms, flow regimes, boundary cases, or regional shifts and compare key fields.
- Uncertainty And Generalization: use: Separate ordinary test success from success under changed climate, flow, or boundary conditions. Why: The field answer must include where it may be wrong, not only what it predicts. Check: Test a shifted region, rare event, changed forcing, or new sensor pattern.
- Optimization For Learning: use: Balance field error, physical checks, and decision costs during training. Why: The field can look good on average while failing where the decision is made. Check: Test boundaries, rare events, conserved quantities, and high-cost regions.
- Generative Modeling: use: Sample possible fields for stress tests, rare cases, or downstream solvers. Why: The samples are useful only if they carry the field behavior needed by the next task. Check: Measure conservation, rare-event rates, boundary behavior, and downstream task performance.
- Graphs And Geometric Learning: use: Carry information over irregular grids, sensor networks, coastlines, or mesh fields. Why: The field may live on a shape where plain rows erase the needed relation. Check: Change grid order, mesh detail, boundary regions, or long-range links.
- Neural Differential Equations: use: Learn missing pieces of a time-update rule for fields. Why: The field forecast depends on repeated updates, so small rate errors matter. Check: Run past the training window and inspect drift, conservation, and boundary behavior.
- Symbolic Regression And Model Discovery: use: Look for a readable relation inside measured or simulated field behavior. Why: The formula helps when it explains a quantity, not when it only draws a curve through old points. Check: Test a new region, forcing, scale, or event and compare the predicted quantity.
- Foundation Models For PDEs: use: Use one broad field model across related equation settings. Why: The useful claim is coverage over named tasks, not coverage over every possible PDE. Check: Compare against trusted solvers for new equation families, grids, and boundaries.
- Attention For Scientific Fields: use: Route information across fields where one region can affect another. Why: The field answer may need faraway signals without looking everywhere equally. Check: Change storms, fronts, boundaries, and long-range interactions and inspect the field.

## Importance Matrix
- Deep Learning: everyday problem: scientists often have examples of behavior but no short rule that predicts the next case Why it matters: it can learn useful patterns when hand-written rules are incomplete, but the result still needs tests outside the examples used for fitting Topology or shape link: Deep learning matters here only if changed shapes still get the right answer for the named task. First shape check: Hold out a new shape family, camera view, mesh order, or scale and measure the target error. Other fields: Engineering design: Sort old test runs so a designer can screen the next part before a costly build. Check: Test a new material, sensor, or part size before using the prediction for a build decision. Materials, chemistry, and biology: Read images, spectra, molecules, or cell measurements when hand rules are incomplete. Check: Hold out a lab, instrument, molecule family, or cell type and compare the measured property. Climate, fluids, and fields: Learn repeated field patterns from stored simulations or measurements. Check: Change the region, forcing, boundary, or rare event and inspect where the field fails first. First test: hold out a changed material, geometry, parameter range, or sensor condition
- Physics-Informed Neural Networks: everyday problem: measurements may be sparse, but the answer must still respect a known physical equation Why it matters: it lets known physics push the fit toward physically possible behavior instead of treating data points as the only evidence Topology or shape link: A PINN matters here when sparse points are not enough but an equation can still guide the missing field. First shape check: Move sensors, change the boundary, or bend the domain and compare the hidden field with trusted values. Other fields: Engineering design: Estimate heat, stress, flow, or pressure when tests are sparse but the physical law is known. Check: Inspect sharp regions, edge cases, and held-out sensors near the places where failure would matter. Materials, chemistry, and biology: Fill in missing concentration, strain, or reaction fields while keeping known balance rules visible. Check: Change material settings, boundary values, or reaction conditions and compare with measurements. Climate, fluids, and fields: Recover a full field from sparse measurements without ignoring the governing equation. Check: Change source terms, boundaries, or sensor placement and compare against a solver or held-out data. First test: move the training points, inspect sharp regions, and compare against a numerical solve or held-out measurements
- Partial Differential Equations: everyday problem: a quantity changes over space and time, so one number is not enough to describe the situation Why it matters: PDEs are the language many scientific models use before machine learning enters the story Topology or shape link: PDEs matter here because shape and boundary decide how local changes spread. First shape check: Change the boundary, cut a hole, refine the mesh, or bend the region and check conservation. Other fields: Engineering design: Write the rule for heat, stress, flow, pressure, or waves before choosing a learning method. Check: Change load, source, geometry, or scale and inspect the quantity used for the decision. Materials, chemistry, and biology: Track diffusion, reaction, strain, growth, or transport through a material or tissue. Check: Change a coefficient, source, boundary, or sample shape and compare with measurements. Climate, fluids, and fields: Describe wind, heat, concentration, pressure, and water over space and time. Check: Check mass, energy, boundary behavior, stability, and measured error under a changed case. First test: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error
- Operator Learning: everyday problem: one simulation answer is not enough when engineers need the whole map from inputs to solution fields Why it matters: it can replace many expensive solves with a fast approximation when the requested cases stay inside the tested family Topology or shape link: Operator learning matters when the question is about a family of field problems, not one solve. First shape check: Hold out a new geometry class, mesh resolution, boundary type, or coefficient range. Other fields: Engineering design: Give fast field estimates for repeated wing, device, part, or load queries. Check: Compare lift, drag, stress, heat, or pressure against trusted solves near the design edge. Materials, chemistry, and biology: Map a material setting, molecular field, or tissue condition to a response field. Check: Hold out a new material range, molecule type, or biological condition and inspect the response. Climate, fluids, and fields: Map forcing, boundary, or initial fields to future solution fields. Check: Change forcing, scale, resolution, or rare regimes and compare with trusted simulations. First test: change resolution, coefficients, boundary conditions, or forcing and check whether the predicted field still satisfies the scientific quantity being claimed
- Scientific Machine Learning: everyday problem: scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time Why it matters: it connects flexible prediction to the checks scientists already need: units, conservation, boundaries, uncertainty, and failure cases Topology or shape link: Scientific machine learning matters when the target is a real quantity, not only a fitted score. First shape check: Change shape, mesh, boundary, or sensor layout and inspect the scientific quantity. Other fields: Engineering design: Use data and scientific checks together when a design decision has a cost. Check: Test near the build limit, load limit, safety limit, or operating limit. Materials, chemistry, and biology: Tie learned predictions to units, mechanisms, measurements, and domain limits. Check: Hold out a new lab setting, material range, molecule family, or measured condition. Climate, fluids, and fields: Use learned models only with clear field checks, physical checks, and use ranges. Check: Change region, season, boundary, forcing, or resolution and measure the decision quantity. First test: state the scientific quantity first, then test it under a changed case that matters in that domain
- Surrogate Modeling: everyday problem: a trusted simulator may be too slow to run for every design, control, or uncertainty question Why it matters: it makes repeated scientific decisions possible when full simulation cost would stop the workflow Topology or shape link: A surrogate matters here when shape changes are common and full solves are too slow. First shape check: Change holes, edges, mesh detail, or shape class and compare with the full solver. Other fields: Engineering design: Screen many candidate parts, wings, devices, or loads before running the costly solve. Check: Test near peaks, boundaries, rare regimes, and cases where the decision changes. Materials, chemistry, and biology: Use a cheaper stand-in for repeated material, molecule, or tissue simulations. Check: Compare with trusted simulations or measurements on new settings near the use boundary. Climate, fluids, and fields: Answer repeated field queries faster than running a full model each time. Check: Hold out storms, flow regimes, boundary cases, or regional shifts and compare key fields. First test: compare against the full solver on new cases near the edge of the intended use
- Uncertainty And Generalization: everyday problem: a prediction is not enough unless the user knows when it should be believed Why it matters: scientific models are used to make decisions, so the cost of being confidently wrong can be high Topology or shape link: Uncertainty matters here because a prediction can look good on familiar shapes and fail on a new one. First shape check: Hold out a new shape family, missing connection, or mesh resolution and measure the error. Other fields: Engineering design: Attach a use range and warning boundary to a prediction before a design choice. Check: Move load, material, size, or boundary beyond training and measure the first failure. Materials, chemistry, and biology: Say when a measured property prediction should weaken under a new lab or sample condition. Check: Hold out a new instrument, molecule family, tissue type, or material batch. Climate, fluids, and fields: Separate ordinary test success from success under changed climate, flow, or boundary conditions. Check: Test a shifted region, rare event, changed forcing, or new sensor pattern. First test: move one important condition outside the training range and measure the first failure
- Optimization For Learning: everyday problem: learning needs a way to decide which model settings are better or worse Why it matters: the model only learns what the training score asks it to improve Topology or shape link: Optimization matters here because the model will chase the score even when the score misses the real shape question. First shape check: Inspect whether the trained answer breaks after relabeling, mesh change, or boundary change. Other fields: Engineering design: Train toward the quantity that drives the design, not only average error. Check: Check rare loads, edge cases, constraints, and the final design quantity after training. Materials, chemistry, and biology: Set the training score so it respects measured properties, units, and known checks. Check: Inspect what the score ignored, then test the ignored behavior on new samples. Climate, fluids, and fields: Balance field error, physical checks, and decision costs during training. Check: Test boundaries, rare events, conserved quantities, and high-cost regions. First test: inspect what the score ignores, then check whether the ignored behavior fails after training
- Generative Modeling: everyday problem: some tasks need many possible examples, not one predicted answer Why it matters: it can explore candidate fields, shapes, or scenarios when direct enumeration is impossible Topology or shape link: Generative modeling matters here only if the samples are valid objects rather than plausible pictures. First shape check: Test connected parts, forbidden holes, mesh validity, and downstream use. Other fields: Engineering design: Propose candidate parts, layouts, fields, or operating cases for later testing. Check: Run constraints, full solves, stress tests, and use-case checks on generated candidates. Materials, chemistry, and biology: Suggest molecules, structures, images, or samples that should still obey known rules. Check: Reject samples that break chemistry rules, material limits, or biological measurements. Climate, fluids, and fields: Sample possible fields for stress tests, rare cases, or downstream solvers. Check: Measure conservation, rare-event rates, boundary behavior, and downstream task performance. First test: measure constraints, rare cases, conservation, and downstream task performance on generated samples
- Graphs And Geometric Learning: everyday problem: many scientific objects are not simple rows of numbers; their connections matter Why it matters: it lets the model respect the structure of the object instead of flattening away important relations Topology or shape link: Graphs and geometric learning matters here because the connection pattern is part of the evidence. First shape check: Relabel nodes, rotate the object, refine the mesh, or add a missing edge and inspect the target. Other fields: Engineering design: Model meshes, parts, sensor networks, or connected components without flattening away contact. Check: Change mesh resolution, contact regions, or boundary connections and compare the design quantity. Materials, chemistry, and biology: Represent atoms, bonds, cells, proteins, grains, or interaction networks as connected objects. Check: Hold out new structures, rotations, missing interactions, or graph sizes. Climate, fluids, and fields: Carry information over irregular grids, sensor networks, coastlines, or mesh fields. Check: Change grid order, mesh detail, boundary regions, or long-range links. First test: change the mesh, rotate or move the object, or add missing interactions and inspect what breaks
- Neural Differential Equations: everyday problem: scientists may know that a system changes continuously but not know the exact rule for that change Why it matters: it lets learning focus on the missing change rule while the time update still carries the idea of continuous evolution Topology or shape link: Neural differential equations matter here when the missing part is the rule of change. First shape check: Change the starting state, shape, or connection pattern and run longer than the training window. Other fields: Engineering design: Predict changing heat, motion, wear, control, or flow when the exact rate rule is unknown. Check: Test long-time drift, stability, conservation, and changed starting conditions. Materials, chemistry, and biology: Learn reaction, growth, motion, or change rules from measured time traces. Check: Hold out time ranges, doses, reaction settings, or starting conditions. Climate, fluids, and fields: Learn missing pieces of a time-update rule for fields. Check: Run past the training window and inspect drift, conservation, and boundary behavior. First test: run longer than the training window and check whether small rate errors accumulate into drift
- Symbolic Regression And Model Discovery: everyday problem: a scientist may need a readable equation, not only a model that predicts well Why it matters: a short equation can be tested, criticized, and reused more easily than a large fitted model Topology or shape link: Symbolic regression matters here only if the readable formula keeps the real cause visible. First shape check: Remove a shape measure, change the mesh, or add a missing variable and test the formula. Other fields: Engineering design: Find a readable equation that links design variables to the decision quantity. Check: Run a changed design case and reject formulas that only fit old designs. Materials, chemistry, and biology: Search for compact laws from measured variables, ingredients, and properties. Check: Add noise, hold out a condition, or test a missing variable. Climate, fluids, and fields: Look for a readable relation inside measured or simulated field behavior. Check: Test a new region, forcing, scale, or event and compare the predicted quantity. First test: remove a needed variable, add noise, or test a new experiment and see whether the formula still predicts
- Foundation Models For PDEs: everyday problem: one trained model may be asked to handle many related equations, grids, parameters, or physical settings Why it matters: a broad model could reduce repeated training cost if it keeps the physical features that matter across tasks Topology or shape link: Foundation PDE models matter here only if shared structure carries to the new shape family. First shape check: Hold out whole geometry families, boundary types, scales, or rare regimes. Other fields: Engineering design: Start from a broad PDE model for a new device or part, then verify the design quantity. Check: Compare with trusted solves on new designs near the intended use boundary. Materials, chemistry, and biology: Transfer learned field behavior across related materials, tissues, or reaction settings. Check: Hold out a task family, material range, tissue setting, or coefficient regime. Climate, fluids, and fields: Use one broad field model across related equation settings. Check: Compare against trusted solvers for new equation families, grids, and boundaries. First test: hold out a new equation family, boundary type, scale, or rare regime and compare against a trusted solver
- Attention For Scientific Fields: everyday problem: a local patch of a field may depend on faraway information, but looking everywhere can be expensive Why it matters: it gives the model a way to move information across a field without treating every location as isolated Topology or shape link: Attention matters here when faraway structure changes the local answer. First shape check: Change window size, long-range links, boundary regions, or point order. Other fields: Engineering design: Route information across a part, surface, or field where distant regions interact. Check: Stress long-range cases and compare the design quantity near hard regions. Materials, chemistry, and biology: Let distant atoms, cells, residues, or regions influence a local prediction. Check: Remove long-range context, change structure, or hold out larger objects. Climate, fluids, and fields: Route information across fields where one region can affect another. Check: Change storms, fronts, boundaries, and long-range interactions and inspect the field. First test: change the window size, inspect long-range effects, and compare behavior near boundaries or sharp structures

## End-To-End Course Walkthrough
- One scientific job: move from sparse measurements, old simulations, a shaped domain, and a real decision to a bounded scientific claim.
- Plain route: name the evidence, name the hidden answer, choose topic moves that carry the answer, keep shape and field checks visible, and end with a changed case.
- Final say-it-back test: state the scientific job, evidence, hidden answer, topic route, shape or topology issue, field use, and changed case without hiding behind a method name.

## Plain Capstone
- See `site/plain-capstone.html` for final learner prompts that prove each topic from everyday need to bounded field claim.

## Example Route Guide
- Heat Equation From Few Measurements: job: What is the temperature everywhere if sensors only report a few places? Observed: sensor readings, starting temperature, boundary temperature, and the rule that heat flows from hot regions toward cold regions Hidden: temperature at every unsensed point and later time Route: partial differential equations -> physics informed neural networks -> scientific machine learning -> uncertainty and generalization. First failure: the fitted field matches sensor points but gives the wrong temperature between them or after the starting time
- Fast Fluid Field Surrogate: job: How can engineers test many shapes without running a full simulation every time? Observed: many prior simulations connecting shape, conditions, and resulting velocity or pressure fields Hidden: the flow field for a new shape or new condition Route: surrogate modeling -> operator learning -> attention for scientific fields. First failure: the shortcut is fast but misses a force, vortex, or boundary effect that changes the engineering choice
- Discovering A Small Law From Motion: job: Can data reveal a short rule for how the system moves? Observed: measurements of position, speed, concentration, or another changing quantity Hidden: the rate rule that causes the next moment Route: symbolic regression -> neural differential equations -> optimization for learning. First failure: the rule fits the original trace but breaks when the starting condition, forcing, or measured setting changes
- Molecule Property From Structure: job: Can a model predict a useful molecular property without flattening away the structure that causes it? Observed: molecular graphs, atom types, bond patterns, shape information, and measured properties from experiments or trusted calculations Hidden: which structural relations control the property for a new molecule Route: graphs and geometric learning -> generative modeling -> deep learning -> uncertainty and generalization. First failure: the model works on familiar molecules but fails on a new scaffold, rare atom type, or changed assay
- Material Stress From Sparse Tests: job: How can a model estimate stress inside a material when only a few tests or simulations are available? Observed: sample geometry, load conditions, a few measured displacements or strains, and known mechanical balance laws Hidden: the internal stress field and the weak region where failure may begin Route: partial differential equations -> physics informed neural networks -> surrogate modeling. First failure: the model has low average error but misses the local stress concentration that drives failure
- Mesh Field On Irregular Geometry: job: How can a model predict a field when the points are connected in an uneven shape instead of a neat grid? Observed: mesh points, connections, boundary labels, local features, and solution fields from prior solves Hidden: how information should move across the irregular geometry for a new case Route: graphs and geometric learning -> operator learning -> attention for scientific fields. First failure: renumbering, refining, rotating, or changing the boundary makes the field answer change for the wrong reason
- Foundation PDE Model On A New Equation: job: When can a model trained on many PDE examples help with a new equation family? Observed: many prior equation tasks, grids, parameters, boundary types, and solution fields Hidden: which shared structure carries to the new equation and which parts do not Route: foundation models for pdes -> operator learning -> uncertainty and generalization. First failure: the model looks broad but fails on the held-out equation family, boundary type, scale, or quantity
- Climate Risk Under Shifted Conditions: job: How should a model report risk when the future case differs from familiar examples? Observed: historical fields, simulation ensembles, forcing conditions, regional measurements, and known physical constraints Hidden: how wrong the prediction may be under a changed climate, rare event, or new regional pattern Route: uncertainty and generalization -> surrogate modeling -> partial differential equations. First failure: the model reports confident risk while rare events, changed forcing, or the target region were not tested

## No-Jargon Concept Guide
- Deep Learning: job: scientists often have examples of behavior but no short rule that predicts the next case Evidence: many input-output examples from experiments, simulations, or measurements Hidden answer: the exact rule that connects the input to the output Move: adjust many weights until the model maps familiar inputs to the right outputs Reject first by: hold out a changed material, geometry, parameter range, or sensor condition
- Physics-Informed Neural Networks: job: measurements may be sparse, but the answer must still respect a known physical equation Evidence: some measured values, boundary values, starting values, and a known differential equation Hidden answer: the full field value at every point in space and time Move: fit a neural network while also measuring how badly its output violates the known equation Reject first by: move the training points, inspect sharp regions, and compare against a numerical solve or held-out measurements
- Partial Differential Equations: job: a quantity changes over space and time, so one number is not enough to describe the situation Evidence: a field such as temperature, pressure, concentration, velocity, or displacement Hidden answer: how every point in the field affects nearby points over time Move: write a local change rule that uses rates across space and time Reject first by: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error
- Operator Learning: job: one simulation answer is not enough when engineers need the whole map from inputs to solution fields Evidence: many example inputs and their full solution fields Hidden answer: the rule that maps a new input field to its new solution field Move: learn the map from problem input to solution, not only one solution at a time Reject first by: change resolution, coefficients, boundary conditions, or forcing and check whether the predicted field still satisfies the scientific quantity being claimed
- Scientific Machine Learning: job: scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time Evidence: data, equations, units, simulation outputs, and domain limits Hidden answer: which parts of the scientific system are missing, noisy, or too costly to compute directly Move: combine learned prediction with scientific checks that name what the claim is allowed to mean Reject first by: state the scientific quantity first, then test it under a changed case that matters in that domain
- Surrogate Modeling: job: a trusted simulator may be too slow to run for every design, control, or uncertainty question Evidence: expensive solver inputs and outputs for a limited set of cases Hidden answer: the solver answer for every new query someone wants to ask Move: train a cheaper stand-in for the expensive input-output behavior Reject first by: compare against the full solver on new cases near the edge of the intended use
- Uncertainty And Generalization: job: a prediction is not enough unless the user knows when it should be believed Evidence: training cases, validation cases, prediction errors, and known shifts between cases Hidden answer: how wrong the model may be on a case unlike the ones it learned from Move: separate fit on familiar examples from evidence on changed examples Reject first by: move one important condition outside the training range and measure the first failure
- Optimization For Learning: job: learning needs a way to decide which model settings are better or worse Evidence: a written score that says which model behavior is better or worse Hidden answer: whether that score matches the scientific behavior the user actually cares about Move: change model settings to lower the written score Reject first by: inspect what the score ignores, then check whether the ignored behavior fails after training
- Generative Modeling: job: some tasks need many possible examples, not one predicted answer Evidence: examples of fields, molecules, flows, shapes, or other scientific objects Hidden answer: the spread of possible valid objects beyond the examples Move: learn how to sample new candidates that resemble the training family Reject first by: measure constraints, rare cases, conservation, and downstream task performance on generated samples
- Graphs And Geometric Learning: job: many scientific objects are not simple rows of numbers; their connections matter Evidence: objects with parts and connections, such as meshes, molecules, or interacting components Hidden answer: which neighboring and long-range interactions control the scientific quantity Move: let information move along the object connections instead of flattening the object into a plain row Reject first by: change the mesh, rotate or move the object, or add missing interactions and inspect what breaks
- Neural Differential Equations: job: scientists may know that a system changes continuously but not know the exact rule for that change Evidence: measurements of a system changing over time Hidden answer: the rate rule that moves the present value into the future Move: learn the missing rate rule and place it inside a time-evolution calculation Reject first by: run longer than the training window and check whether small rate errors accumulate into drift
- Symbolic Regression And Model Discovery: job: a scientist may need a readable equation, not only a model that predicts well Evidence: measured variables and candidate mathematical ingredients Hidden answer: which short formula, if any, actually explains the measured change Move: search for a readable equation that fits the data and survives a changed case Reject first by: remove a needed variable, add noise, or test a new experiment and see whether the formula still predicts
- Foundation Models For PDEs: job: one trained model may be asked to handle many related equations, grids, parameters, or physical settings Evidence: many PDE problem instances across equations, grids, parameters, or physical settings Hidden answer: which shared structure carries from one scientific task to another Move: train one broad model to reuse structure across many related field-prediction tasks Reject first by: hold out a new equation family, boundary type, scale, or rare regime and compare against a trusted solver
- Attention For Scientific Fields: job: a local patch of a field may depend on faraway information, but looking everywhere can be expensive Evidence: large fields where one location may depend on other locations Hidden answer: which distant parts matter for the local prediction Move: let the model choose which parts of the field exchange information Reject first by: change the window size, inspect long-range effects, and compare behavior near boundaries or sharp structures

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

#### Route Burden Table
- Step 1: What is the thing we are trying to know? Evidence needed: a named field such as temperature, pressure, velocity, stress, or concentration Mistake it catches: treating a field problem like a single-number prediction
- Step 2: What keeps the empty places from being arbitrary? Evidence needed: the equation, boundary data, starting data, and units for the physical case Mistake it catches: using physics words without naming the rule that can reject an answer
- Step 3: What ties the answer to the real case? Evidence needed: sensor values, measurements, or trusted simulation values at known places Mistake it catches: letting the fitted field drift away from observed evidence
- Step 4: What checks the places nobody measured? Evidence needed: equation-error checks between measurements and near boundaries or sharp regions Mistake it catches: matching data points while breaking the rule between them
- Step 5: What would make us stop trusting it? Evidence needed: a changed boundary, source, scale, or hard region held back from fitting Mistake it catches: calling one polished fit a scientific answer before it survives a changed case

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

#### Route Burden Table
- Step 1: What collection teaches the map? Evidence needed: paired input fields and output fields from trusted solves or measurements Mistake it catches: trying to learn a field-to-field map from isolated examples with no named family
- Step 2: What is this model allowed to answer? Evidence needed: the equation types, boundaries, geometries, grids, and parameter ranges included Mistake it catches: using the model on a new family because the output looks smooth
- Step 3: What is being learned? Evidence needed: a map from a new input field to the full output field, not one scalar score Mistake it catches: confusing a single solved case with the reusable object scientists need
- Step 4: What structure must survive inside the field? Evidence needed: checks for far interactions, local detail, boundary effects, and resolution changes Mistake it catches: choosing an architecture that erases the relation the field depends on
- Step 5: What rejects the claim? Evidence needed: held-out fields, changed resolution, and physical quantities checked after prediction Mistake it catches: trusting visual similarity while the physical quantity is wrong

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

#### Route Burden Table
- Step 1: What changed in the system? Evidence needed: measurements over time, across conditions, or across controlled experiments Mistake it catches: searching for a law before naming the behavior the law must explain
- Step 2: What could possibly explain that change? Evidence needed: measured variables, units, candidate terms, and known excluded variables Mistake it catches: letting an unmeasured cause hide inside a neat formula
- Step 3: What candidate rule is being proposed? Evidence needed: a short formula, a learned rate rule, or a named missing term Mistake it catches: settling for next-step prediction when the job asks for a law
- Step 4: Does the rule survive a new experiment? Evidence needed: changed starts, changed forcing, noise checks, and held-out trajectories Mistake it catches: mistaking one fitted trace for a reusable mechanism
- Step 5: What did the search never have a chance to see? Evidence needed: a list of missing variables, forbidden terms, and experiments not run Mistake it catches: claiming discovery when the search space could not express the true cause

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

#### Route Burden Table
- Step 1: What trusted source is too slow to call every time? Evidence needed: the solver, experiment, or workflow used as the check Mistake it catches: building a fast answer with no source of truth to compare against
- Step 2: Which repeated questions justify the shortcut? Evidence needed: a named query family, such as shape range, load range, or parameter sweep Mistake it catches: using the stand-in for any question because it is fast
- Step 3: What is the stand-in allowed to imitate? Evidence needed: training examples tied to the same inputs, outputs, and decision quantity Mistake it catches: optimizing a neat average while missing the quantity that drives the decision
- Step 4: Where is the edge of its use range? Evidence needed: comparisons against the trusted source near boundaries, rare cases, and hard regions Mistake it catches: reporting speed while hiding where the shortcut first fails
- Step 5: How is the limit shown with the answer? Evidence needed: reported use range, rejected cases, and a rule for when to return to the trusted source Mistake it catches: letting a fast answer travel farther than the evidence does

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
- Question: How should a model report risk when the future case differs from familiar examples?
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
- Do not use when: Do not treat it as an automatic solution for hard PDEs; if boundary data, scales, or sharp regions are poorly handled, the equation penalty can mislead.
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
- Do not use when: Do not trust long-time behavior because short training windows fit well; long runs need their own checks.
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
- Do not use when: Do not call a model scientific because the data came from science; the physical quantity, rule, and failure test must be explicit.
- Plain formula: measurements + known rule + learned missing part -> checked scientific answer
- Why it matters: It turns machine learning from a general prediction tool into a disciplined way to answer a scientific question with stated evidence.

### Optimization For Learning
- One sentence: Optimization is the process of changing a model until a written error score gets smaller.
- Use when: Use it whenever a model has adjustable parts and there is a clear score saying what counts as a better answer.
- Do not use when: Do not mistake a lower training score for a better scientific model if the score omits boundaries, rare cases, units, or the decision quantity.
- Plain formula: current model -> error score -> change model -> check again
- Why it matters: The training score is the contract the model follows; if the contract is wrong, the learned answer can be wrong in a polished way.

### Generative Modeling
- One sentence: Generative modeling learns how to make possible examples, rather than only score one existing example.
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
- Plain problem: Some scientific jobs need many possible fields, designs, or futures, rather than a single average answer.
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
- Smallest useful formula: The smallest useful formula must start from some measured values, boundary values, starting values, and a known differential equation, carry the answer toward the full field value at every point in space and time, and include a check that can fail: move the training points, inspect sharp regions, and compare against a numerical solve or held-out measurements.
- First wrong simplification: The first wrong shortcut is to keep the part that gives an answer while dropping the part that checks it. That would hide this failure: move the training points, inspect sharp regions, and compare against a numerical solve or held-out measurements.
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
- Smallest useful formula: The smallest useful formula must start from a field such as temperature, pressure, concentration, velocity, or displacement, carry the answer toward how every point in the field affects nearby points over time, and include a check that can fail: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error.
- First wrong simplification: The first wrong shortcut is to keep the part that gives an answer while dropping the part that checks it. That would hide this failure: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error.
- Failure test: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error
- Page: derivations/partial-differential-equations.html

#### Hand Derivation For Partial Differential Equations
- Start: Start with a quantity spread across space, such as temperature, pressure, concentration, velocity, or displacement. One value cannot describe it because each location is tied to nearby locations, sources, and boundaries.
- field value: The object being described is a value at many places, not one number for the whole system. Check: If the field is reduced to independent points, movement, flow, stress, or diffusion can be lost.
- change rates: The equation must say how the field changes in time or across space, because that is where the physical rule lives. Check: If the rates are wrong, the equation can look neat while giving the wrong evolution.
- sources and boundaries: A field can obey the same local rule but behave differently when heat, force, material, or edge conditions change. Check: If sources or boundaries are vague, the equation may describe a different physical problem.
- Final line: A PDE is a compact way to say how a field, its local changes, its sources, and its boundaries must agree.

### Operator Learning
- Problem: one simulation answer is not enough when engineers need the whole map from inputs to solution fields
- Observed: many example inputs and their full solution fields
- Hidden: the rule that maps a new input field to its new solution field
- Plain formula: input field -> learned field-to-field map -> output field
- Smallest useful formula: The smallest useful formula must start from many example inputs and their full solution fields, carry the answer toward the rule that maps a new input field to its new solution field, and include a check that can fail: change resolution, coefficients, boundary conditions, or forcing and check whether the predicted field still satisfies the scientific quantity being claimed.
- First wrong simplification: The first wrong shortcut is to keep the part that gives an answer while dropping the part that checks it. That would hide this failure: change resolution, coefficients, boundary conditions, or forcing and check whether the predicted field still satisfies the scientific quantity being claimed.
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
- Smallest useful formula: The smallest useful formula must start from expensive solver inputs and outputs for a limited set of cases, carry the answer toward the solver answer for every new query someone wants to ask, and include a check that can fail: compare against the full solver on new cases near the edge of the intended use.
- First wrong simplification: The first wrong shortcut is to keep the part that gives an answer while dropping the part that checks it. That would hide this failure: compare against the full solver on new cases near the edge of the intended use.
- Failure test: compare against the full solver on new cases near the edge of the intended use
- Page: derivations/surrogate-modeling.html

#### Hand Derivation For Surrogate Modeling
- Start: Start with a trusted source that is too slow for repeated use. The scientist still needs many answers for design, search, or risk checks.
- trusted source: The stand-in needs something to imitate and something to be checked against. Check: If the trusted source is not named, the surrogate has no clear reference point.
- cheap stand-in: The learned model replaces repeated expensive calls inside a named use range. Check: If the use range is missing, speed can hide bad answers.
- edge check: Errors often matter most near the edge of the range where decisions are tempting and evidence is thin. Check: If only average error is reported, the decision quantity may still be wrong.
- Final line: A surrogate derivation is about earning a cheaper answer while keeping the trusted source in view, rather than only fitting a curve.

### Uncertainty And Generalization
- Problem: a prediction is not enough unless the user knows when it should be believed
- Observed: training cases, validation cases, prediction errors, and known shifts between cases
- Hidden: how wrong the model may be on a case unlike the ones it learned from
- Plain formula: prediction + tested use range + failure evidence
- Smallest useful formula: The smallest useful formula must start from training cases, validation cases, prediction errors, and known shifts between cases, carry the answer toward how wrong the model may be on a case unlike the ones it learned from, and include a check that can fail: move one important condition outside the training range and measure the first failure.
- First wrong simplification: The first wrong shortcut is to keep the part that gives an answer while dropping the part that checks it. That would hide this failure: move one important condition outside the training range and measure the first failure.
- Failure test: move one important condition outside the training range and measure the first failure
- Page: derivations/uncertainty-and-generalization.html

#### Hand Derivation For Uncertainty And Generalization
- Start: Start with a model trained on old cases and a new case that may differ. The missing quantity is not only the prediction; it is how much trust the prediction deserves.
- prediction: The model gives an answer for the quantity the scientist asked for. Check: A prediction without a use range is incomplete.
- tested use range: The reader needs to know which cases actually support the answer. Check: If the test cases look like the training cases, changed-case trust is still unproved.
- failure evidence: Knowing where the model breaks is part of knowing where it can be used. Check: If no failure case is named, confidence is a number without a boundary.
- Final line: The mathematical shape joins answer and boundary: report the prediction together with the evidence that says where belief should weaken.

### Neural Differential Equations
- Problem: scientists may know that a system changes continuously but not know the exact rule for that change
- Observed: measurements of a system changing over time
- Hidden: the rate rule that moves the present value into the future
- Plain formula: current state -> learned change rate -> next state
- Smallest useful formula: The smallest useful formula must start from measurements of a system changing over time, carry the answer toward the rate rule that moves the present value into the future, and include a check that can fail: run longer than the training window and check whether small rate errors accumulate into drift.
- First wrong simplification: The first wrong shortcut is to keep the part that gives an answer while dropping the part that checks it. That would hide this failure: run longer than the training window and check whether small rate errors accumulate into drift.
- Failure test: run longer than the training window and check whether small rate errors accumulate into drift
- Page: derivations/neural-differential-equations.html

#### Hand Derivation For Neural Differential Equations
- Start: Start with a system observed over time and an incomplete rule for how it changes. The missing object is the rate that moves the present state forward.
- state: The state is the information carried from the present into the next moment. Check: If the state leaves out an important variable, the learned rate may compensate in a false way.
- learned rate: The unknown change rule is placed where a differential equation needs a rate. Check: If the rate is only right over a short window, long-time behavior can drift.
- time solver: The rate has to be accumulated through time to produce a path. Check: If the solver amplifies small rate errors, the path can look right at first and then fail.
- Final line: A neural differential equation learns a missing rate, then exposes that rate to the discipline of time evolution.

### Symbolic Regression And Model Discovery
- Problem: a scientist may need a readable equation, not only a model that predicts well
- Observed: measured variables and candidate mathematical ingredients
- Hidden: which short formula, if any, actually explains the measured change
- Plain formula: candidate ingredients -> searched formulas -> tested small law
- Smallest useful formula: The smallest useful formula must start from measured variables and candidate mathematical ingredients, carry the answer toward which short formula, if any, actually explains the measured change, and include a check that can fail: remove a needed variable, add noise, or test a new experiment and see whether the formula still predicts.
- First wrong simplification: The first wrong shortcut is to keep the part that gives an answer while dropping the part that checks it. That would hide this failure: remove a needed variable, add noise, or test a new experiment and see whether the formula still predicts.
- Failure test: remove a needed variable, add noise, or test a new experiment and see whether the formula still predicts
- Page: derivations/symbolic-regression.html

#### Hand Derivation For Symbolic Regression And Model Discovery
- Start: Start with measured variables and a need for a readable law. The unknown object is the relation among the variables, rather than only the next predicted value.
- candidate ingredients: The search can only build formulas from measured variables and allowed operations. Check: If an important variable is missing, the best formula may still be false.
- searched formulas: Many possible short laws are tried because the correct relation is not known ahead of time. Check: If size is not controlled, the formula may only memorize noise.
- changed experiment: A readable formula becomes a scientific candidate only if it survives a new situation. Check: If it is tested only where it was found, it is not yet a law.
- Final line: The derivation is a search with a burden: the result must be short enough to inspect and strong enough to survive a new experiment.

### Foundation Models For PDEs
- Problem: one trained model may be asked to handle many related equations, grids, parameters, or physical settings
- Observed: many PDE problem instances across equations, grids, parameters, or physical settings
- Hidden: which shared structure carries from one scientific task to another
- Plain formula: many PDE tasks -> shared learned structure -> new task prediction
- Smallest useful formula: The smallest useful formula must start from many PDE problem instances across equations, grids, parameters, or physical settings, carry the answer toward which shared structure carries from one scientific task to another, and include a check that can fail: hold out a new equation family, boundary type, scale, or rare regime and compare against a trusted solver.
- First wrong simplification: The first wrong shortcut is to keep the part that gives an answer while dropping the part that checks it. That would hide this failure: hold out a new equation family, boundary type, scale, or rare regime and compare against a trusted solver.
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
- Smallest useful formula: The smallest useful formula must start from many input-output examples from experiments, simulations, or measurements, carry the answer toward the exact rule that connects the input to the output, and include a check that can fail: hold out a changed material, geometry, parameter range, or sensor condition.
- First wrong simplification: The first wrong shortcut is to keep the part that gives an answer while dropping the part that checks it. That would hide this failure: hold out a changed material, geometry, parameter range, or sensor condition.
- Failure test: hold out a changed material, geometry, parameter range, or sensor condition
- Page: derivations/deep-learning.html

#### Hand Derivation For Deep Learning
- Start: Start with many examples and no short hand-written rule. The model needs adjustable parts because the useful relation is not known before training.
- examples: Examples are the evidence the model is allowed to learn from. Check: If the examples miss the important case, the learned pattern may fail exactly where it is needed.
- adjustable weights: The weights give the model room to shape a relation that was not written down by hand. Check: If the model has room to fit noise, a low training error is not enough.
- held-out test: The claim is about a new case, so some evidence must be kept aside from fitting. Check: If the test looks too much like training, the model may only be repeating familiar cases.
- Final line: Deep learning trades a hand-written rule for an adjustable rule, so the proof burden moves to examples, tests, and the boundary of use.

### Scientific Machine Learning
- Problem: scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time
- Observed: data, equations, units, simulation outputs, and domain limits
- Hidden: which parts of the scientific system are missing, noisy, or too costly to compute directly
- Plain formula: measurements + known rule + learned missing part -> checked scientific answer
- Smallest useful formula: The smallest useful formula must start from data, equations, units, simulation outputs, and domain limits, carry the answer toward which parts of the scientific system are missing, noisy, or too costly to compute directly, and include a check that can fail: state the scientific quantity first, then test it under a changed case that matters in that domain.
- First wrong simplification: The first wrong shortcut is to keep the part that gives an answer while dropping the part that checks it. That would hide this failure: state the scientific quantity first, then test it under a changed case that matters in that domain.
- Failure test: state the scientific quantity first, then test it under a changed case that matters in that domain
- Page: derivations/scientific-machine-learning.html

#### Hand Derivation For Scientific Machine Learning
- Start: Start with a scientific question where data, equations, simulations, and uncertainty each carry part of the answer. No single piece is enough by itself.
- measured evidence: Measurements tie the answer to the world rather than only to a modeler's preference. Check: If measurements are ignored, the result may satisfy a rule but miss the experiment.
- scientific rule: Known physics or chemistry can reject answers that fit data points but break the system between them. Check: If the rule is wrong or incomplete, adding it can make the answer confidently wrong.
- changed-case validation: The scientific claim matters in a use case that can differ from the examples used to build it. Check: If no changed case is named, the page has not separated evidence from hope.
- Final line: Scientific machine learning is the discipline of saying which evidence is carried, which rule is kept, and which changed case can reject the claim.

### Optimization For Learning
- Problem: learning needs a way to decide which model settings are better or worse
- Observed: a written score that says which model behavior is better or worse
- Hidden: whether that score matches the scientific behavior the user actually cares about
- Plain formula: current model -> error score -> change model -> check again
- Smallest useful formula: The smallest useful formula must start from a written score that says which model behavior is better or worse, carry the answer toward whether that score matches the scientific behavior the user actually cares about, and include a check that can fail: inspect what the score ignores, then check whether the ignored behavior fails after training.
- First wrong simplification: The first wrong shortcut is to keep the part that gives an answer while dropping the part that checks it. That would hide this failure: inspect what the score ignores, then check whether the ignored behavior fails after training.
- Failure test: inspect what the score ignores, then check whether the ignored behavior fails after training
- Page: derivations/optimization-for-learning.html

#### Hand Derivation For Optimization For Learning
- Start: Start with a model that can be adjusted and a score that says which answers look better. Training is the repeated act of changing the model to reduce that score.
- adjustable model parts: Something must be changeable, or there is nothing for training to improve. Check: If the adjustable parts cannot express the needed behavior, optimization cannot invent it.
- training score: The score tells the optimizer what better means. Check: If the score ignores the scientific quantity, training can improve the score while harming the job.
- update rule: The model needs a way to use local score information to choose the next setting. Check: If the updates stall or chase the wrong term, the final model may reflect optimization failure rather than scientific truth.
- Final line: Optimization is not proof; it is a way to obey a written score, so the score must match the scientific burden.

### Generative Modeling
- Problem: some tasks need many possible examples, not one predicted answer
- Observed: examples of fields, molecules, flows, shapes, or other scientific objects
- Hidden: the spread of possible valid objects beyond the examples
- Plain formula: known conditions + variation -> candidate example -> realism and rule checks
- Smallest useful formula: The smallest useful formula must start from examples of fields, molecules, flows, shapes, or other scientific objects, carry the answer toward the spread of possible valid objects beyond the examples, and include a check that can fail: measure constraints, rare cases, conservation, and downstream task performance on generated samples.
- First wrong simplification: The first wrong shortcut is to keep the part that gives an answer while dropping the part that checks it. That would hide this failure: measure constraints, rare cases, conservation, and downstream task performance on generated samples.
- Failure test: measure constraints, rare cases, conservation, and downstream task performance on generated samples
- Page: derivations/generative-modeling.html

#### Hand Derivation For Generative Modeling
- Start: Start with a task that needs many possible fields, designs, molecules, or futures. One average answer can hide the variety the scientist must inspect.
- source of variation: The model needs a way to produce different candidates instead of the same answer every time. Check: If variation is only visual noise, the samples may not represent real possibilities.
- conditioning information: The candidates must answer the actual prompt, boundary, geometry, property, or physical setting. Check: If the condition is ignored, plausible samples can be useless for the scientific job.
- constraint check: A generated object is only usable if it satisfies the rule or property the domain requires. Check: If samples are judged only by appearance, invalid candidates can look convincing.
- Final line: Generative modeling is useful when many candidates matter, but each candidate still has to answer to the domain rule.

### Graphs And Geometric Learning
- Problem: many scientific objects are not simple rows of numbers; their connections matter
- Observed: objects with parts and connections, such as meshes, molecules, or interacting components
- Hidden: which neighboring and long-range interactions control the scientific quantity
- Plain formula: connected shape + local values -> relation-aware updates -> field or object answer
- Smallest useful formula: The smallest useful formula must start from objects with parts and connections, such as meshes, molecules, or interacting components, carry the answer toward which neighboring and long-range interactions control the scientific quantity, and include a check that can fail: change the mesh, rotate or move the object, or add missing interactions and inspect what breaks.
- First wrong simplification: The first wrong shortcut is to keep the part that gives an answer while dropping the part that checks it. That would hide this failure: change the mesh, rotate or move the object, or add missing interactions and inspect what breaks.
- Failure test: change the mesh, rotate or move the object, or add missing interactions and inspect what breaks
- Page: derivations/graphs-and-geometric-learning.html

#### Hand Derivation For Graphs And Geometric Learning
- Start: Start with an object whose parts and connections matter: a molecule, mesh, material, body, or network. The arrangement is part of the evidence.
- parts: The model needs the pieces whose values, features, or positions carry the scientific quantity. Check: If important parts are missing, the graph cannot recover their influence.
- connections: Connections say which parts can directly affect one another. Check: If the graph connects the wrong neighbors, the model can learn the wrong interaction pattern.
- geometry or symmetry check: The answer should not change for reasons that are only artifacts of mesh order, rotation, or labeling. Check: If relabeling, rotation, or mesh changes break the result, the model may be learning bookkeeping instead of structure.
- Final line: Graph and geometric learning starts from the fact that the scientific object is connected, rather than only listed.

### Attention For Scientific Fields
- Problem: a local patch of a field may depend on faraway information, but looking everywhere can be expensive
- Observed: large fields where one location may depend on other locations
- Hidden: which distant parts matter for the local prediction
- Plain formula: current field part + relevant other parts -> weighted information -> updated field part
- Smallest useful formula: The smallest useful formula must start from large fields where one location may depend on other locations, carry the answer toward which distant parts matter for the local prediction, and include a check that can fail: change the window size, inspect long-range effects, and compare behavior near boundaries or sharp structures.
- First wrong simplification: The first wrong shortcut is to keep the part that gives an answer while dropping the part that checks it. That would hide this failure: change the window size, inspect long-range effects, and compare behavior near boundaries or sharp structures.
- Failure test: change the window size, inspect long-range effects, and compare behavior near boundaries or sharp structures
- Page: derivations/attention-for-scientific-fields.html

#### Hand Derivation For Attention For Scientific Fields
- Start: Start with a field where a local prediction may depend on distant parts: a boundary, forcing pattern, large structure, or rare event.
- query location: The model needs to know which local place is asking for information. Check: If the query is poorly tied to the target quantity, attention can gather irrelevant signals.
- candidate source locations: The useful information may live far from the query location. Check: If distant or boundary information is excluded, the local answer may miss the real cause.
- weighted gathering: The model needs a way to combine the parts judged relevant for the local prediction. Check: If the gathered pattern fails boundary or long-range tests, the attention pattern is not scientific evidence.
- Final line: Attention is a gathering rule for field information; it becomes scientific only when the gathered information survives changed-case checks.


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
- Why tempting: The shortcut is tempting because it keeps the visible result for Physics-Informed Neural Networks while skipping the evidence boundary: move the training points, inspect sharp regions, and compare against a numerical solve or held-out measurements.
- Correction: A PINN is a fitted field that must answer to both measured values and a known physical rule.
- Repair sentence: Say instead: A PINN is a fitted field that must answer to both measured values and a known physical rule. It should be trusted only after this check: move the training points, inspect sharp regions, and compare against a numerical solve or held-out measurements.
- First-principles test: move the training points, inspect sharp regions, and compare against a numerical solve or held-out measurements
- Wrong turns: A weak answer says only that the neural network fits data.; The page reports only training error.; The hard region has few check points.; The equation is known to be incomplete for the experiment.; No comparison is made against held-out measurements or a trusted solver.

### Partial Differential Equations
- Why tempting: The shortcut is tempting because it keeps the visible result for Partial Differential Equations while skipping the evidence boundary: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error.
- Correction: A PDE is a rule for how a whole field changes across space and time.
- Repair sentence: Say instead: A PDE is a rule for how a whole field changes across space and time. It should be trusted only after this check: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error.
- First-principles test: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error
- Wrong turns: A weak answer says only that Partial Differential Equations is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.; The boundary condition is vague.; The learned answer ignores conservation.; The grid or resolution changes the conclusion.; Small visual error hides a large error in the quantity people care about.

### Operator Learning
- Why tempting: The shortcut is tempting because it keeps the visible result for Operator Learning while skipping the evidence boundary: change resolution, coefficients, boundary conditions, or forcing and check whether the predicted field still satisfies the scientific quantity being claimed.
- Correction: Operator learning tries to learn the machine that turns one field into another field.
- Repair sentence: Say instead: Operator learning tries to learn the machine that turns one field into another field. It should be trusted only after this check: change resolution, coefficients, boundary conditions, or forcing and check whether the predicted field still satisfies the scientific quantity being claimed.
- First-principles test: change resolution, coefficients, boundary conditions, or forcing and check whether the predicted field still satisfies the scientific quantity being claimed
- Wrong turns: A weak answer says only that the model is fast.; The training family is not named.; Only one resolution is tested.; The output looks plausible but physical quantities are not checked.; The model is used on a new boundary type without evidence.

### Surrogate Modeling
- Why tempting: The shortcut is tempting because it keeps the visible result for Surrogate Modeling while skipping the evidence boundary: compare against the full solver on new cases near the edge of the intended use.
- Correction: A surrogate is a faster stand-in for a slower trusted process.
- Repair sentence: Say instead: A surrogate is a faster stand-in for a slower trusted process. It should be trusted only after this check: compare against the full solver on new cases near the edge of the intended use.
- First-principles test: compare against the full solver on new cases near the edge of the intended use
- Wrong turns: A weak answer treats speed as trust.; The surrogate is described without its use range.; The edge cases are not tested.; The output metric ignores the decision people actually make.; The full solver is never used again for spot checks.

### Uncertainty And Generalization
- Why tempting: The shortcut is tempting because it keeps the visible result for Uncertainty And Generalization while skipping the evidence boundary: move one important condition outside the training range and measure the first failure.
- Correction: This topic asks when a prediction should be believed on a case the model did not learn from.
- Repair sentence: Say instead: This topic asks when a prediction should be believed on a case the model did not learn from. It should be trusted only after this check: move one important condition outside the training range and measure the first failure.
- First-principles test: move one important condition outside the training range and measure the first failure
- Wrong turns: A weak answer reports one score without saying what changed.; Only familiar cases are reported.; The test set differs from training only in name.; Rare regimes are averaged away.; No one states what condition would make the model unusable.

### Neural Differential Equations
- Why tempting: The shortcut is tempting because it keeps the visible result for Neural Differential Equations while skipping the evidence boundary: run longer than the training window and check whether small rate errors accumulate into drift.
- Correction: A neural differential equation learns the missing rule for how a system changes.
- Repair sentence: Say instead: A neural differential equation learns the missing rule for how a system changes. It should be trusted only after this check: run longer than the training window and check whether small rate errors accumulate into drift.
- First-principles test: run longer than the training window and check whether small rate errors accumulate into drift
- Wrong turns: A weak answer says only that Neural Differential Equations is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.; The model is tested only over short times.; Small rate errors accumulate unnoticed.; Known conservation or stability behavior is not checked.; The learned rate fits noise instead of mechanism.

### Symbolic Regression And Model Discovery
- Why tempting: The shortcut is tempting because it keeps the visible result for Symbolic Regression And Model Discovery while skipping the evidence boundary: remove a needed variable, add noise, or test a new experiment and see whether the formula still predicts.
- Correction: Symbolic regression searches for a short formula that explains measured behavior.
- Repair sentence: Say instead: Symbolic regression searches for a short formula that explains measured behavior. It should be trusted only after this check: remove a needed variable, add noise, or test a new experiment and see whether the formula still predicts.
- First-principles test: remove a needed variable, add noise, or test a new experiment and see whether the formula still predicts
- Wrong turns: A weak answer trusts a neat formula because it fits the original data.; Important variables were never measured.; The formula is selected only on the original data.; Noise creates a fake term.; The search space could not express the real mechanism.

### Foundation Models For PDEs
- Why tempting: The shortcut is tempting because it keeps the visible result for Foundation Models For PDEs while skipping the evidence boundary: hold out a new equation family, boundary type, scale, or rare regime and compare against a trusted solver.
- Correction: A PDE foundation model tries to reuse structure across many related field-prediction tasks.
- Repair sentence: Say instead: A PDE foundation model tries to reuse structure across many related field-prediction tasks. It should be trusted only after this check: hold out a new equation family, boundary type, scale, or rare regime and compare against a trusted solver.
- First-principles test: hold out a new equation family, boundary type, scale, or rare regime and compare against a trusted solver
- Wrong turns: A weak answer treats broad training size as proof of broad scientific trust.; The held-out test is too similar to training.; Rare regimes are missing.; New boundaries or quantities are assumed rather than tested.; Scale is treated as a substitute for scientific validation.

### Deep Learning
- Why tempting: The shortcut is tempting because it keeps the visible result for Deep Learning while skipping the evidence boundary: hold out a changed material, geometry, parameter range, or sensor condition.
- Correction: Deep learning fits a flexible rule from examples when the useful pattern is hard to write by hand.
- Repair sentence: Say instead: Deep learning fits a flexible rule from examples when the useful pattern is hard to write by hand. It should be trusted only after this check: hold out a changed material, geometry, parameter range, or sensor condition.
- First-principles test: hold out a changed material, geometry, parameter range, or sensor condition
- Wrong turns: A weak answer says only that Deep Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.; The page talks about accuracy without naming the test cases.; The model is used after the data source or physical scale changes.; The important scientific quantity is not the quantity being checked.; No one asks what pattern the examples could not possibly teach.

### Scientific Machine Learning
- Why tempting: The shortcut is tempting because it keeps the visible result for Scientific Machine Learning while skipping the evidence boundary: state the scientific quantity first, then test it under a changed case that matters in that domain.
- Correction: Scientific machine learning uses data and scientific rules together so the answer is useful for a named scientific question.
- Repair sentence: Say instead: Scientific machine learning uses data and scientific rules together so the answer is useful for a named scientific question. It should be trusted only after this check: state the scientific quantity first, then test it under a changed case that matters in that domain.
- First-principles test: state the scientific quantity first, then test it under a changed case that matters in that domain
- Wrong turns: A weak answer says only that Scientific Machine Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.; The target quantity is vague.; The known rule is mentioned but not actually checked.; The learned part can violate conservation, boundaries, or units without penalty.; The result is not compared against a changed experiment or trusted solve.

### Optimization For Learning
- Why tempting: The shortcut is tempting because it keeps the visible result for Optimization For Learning while skipping the evidence boundary: inspect what the score ignores, then check whether the ignored behavior fails after training.
- Correction: Optimization is the process of changing a model until a written error score gets smaller.
- Repair sentence: Say instead: Optimization is the process of changing a model until a written error score gets smaller. It should be trusted only after this check: inspect what the score ignores, then check whether the ignored behavior fails after training.
- First-principles test: inspect what the score ignores, then check whether the ignored behavior fails after training
- Wrong turns: A weak answer says only that Optimization For Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.; The loss terms are listed but their relative weight is not justified.; Only the final score is reported.; A hard constraint is treated as a soft suggestion without checking the damage.; Training succeeds while the physical test fails.

### Generative Modeling
- Why tempting: The shortcut is tempting because it keeps the visible result for Generative Modeling while skipping the evidence boundary: measure constraints, rare cases, conservation, and downstream task performance on generated samples.
- Correction: Generative modeling learns how to make possible examples, rather than only score one existing example.
- Repair sentence: Say instead: Generative modeling learns how to make possible examples, rather than only score one existing example. It should be trusted only after this check: measure constraints, rare cases, conservation, and downstream task performance on generated samples.
- First-principles test: measure constraints, rare cases, conservation, and downstream task performance on generated samples
- Wrong turns: A weak answer says only that Generative Modeling is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.; Samples look realistic but violate a known equation or boundary.; Diversity is reported without saying whether the candidates are valid.; The model creates cases outside the evidence family.; The generated object is used as data without marking it as generated.

### Graphs And Geometric Learning
- Why tempting: The shortcut is tempting because it keeps the visible result for Graphs And Geometric Learning while skipping the evidence boundary: change the mesh, rotate or move the object, or add missing interactions and inspect what breaks.
- Correction: Graph and geometric learning keeps the connections and shape of the object visible to the model.
- Repair sentence: Say instead: Graph and geometric learning keeps the connections and shape of the object visible to the model. It should be trusted only after this check: change the mesh, rotate or move the object, or add missing interactions and inspect what breaks.
- First-principles test: change the mesh, rotate or move the object, or add missing interactions and inspect what breaks
- Wrong turns: A weak answer says only that Graphs And Geometric Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.; Mesh order changes the answer when the geometry did not change.; The model ignores boundaries or long-distance connections that matter physically.; It is tested only on one mesh resolution.; A rotated or refined shape breaks the result without explanation.

### Attention For Scientific Fields
- Why tempting: The shortcut is tempting because it keeps the visible result for Attention For Scientific Fields while skipping the evidence boundary: change the window size, inspect long-range effects, and compare behavior near boundaries or sharp structures.
- Correction: Attention lets a model decide which other parts of a field matter for the point or region being predicted.
- Repair sentence: Say instead: Attention lets a model decide which other parts of a field matter for the point or region being predicted. It should be trusted only after this check: change the window size, inspect long-range effects, and compare behavior near boundaries or sharp structures.
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

### Symbolic Regression: Measurements To A Readable Law
- Input: measurements of a changing system and a chosen set of possible variables
- Output: a short candidate law that a person can inspect
- Kept rule: the search is allowed to combine only named measured quantities, so the result must explain what those measurements can actually support
- Failure case: the law looks simple but leaves out an unmeasured cause, fits noise, or fails in a new experiment
- Caption: Input: measured behavior and candidate variables. Output: readable law. Kept rule: every term must come from evidence the experiment carried. Failure case: simple formula that breaks when the system is changed.

### Foundation PDE Models: Old Tasks To A New Equation Case
- Input: many solved PDE tasks plus one new PDE case
- Output: a proposed solution or useful starting point for the new case
- Kept rule: the old tasks must share enough field structure with the new case to carry useful evidence
- Failure case: the new equation, boundary, scale, or target quantity is outside what the old tasks taught
- Caption: Input: many solved PDE tasks and a new case. Output: new field answer or starting point. Kept rule: shared field structure must be real, not assumed. Failure case: broad model fails on the held-out equation family.


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

#### What Each Concept Must Carry In This Domain
- Partial Differential Equations: handles a quantity changes over space and time, so one number is not enough to describe the situation Evidence it uses: a field such as temperature, pressure, concentration, velocity, or displacement Carries: a field, its rates of change, and the boundary or starting information needed to evolve it Failure: a learned shortcut can ignore boundary conditions or conservation behavior that the PDE was carrying. In this domain, reject it if this changed-case test fails: move the heat source or change the boundary temperature and compare against held-out sensors or a trusted solve.
- Physics-Informed Neural Networks: handles measurements may be sparse, but the answer must still respect a known physical equation Evidence it uses: some measured values, boundary values, starting values, and a known differential equation Carries: a neural network prediction plus a penalty for violating the known equation Failure: the equation penalty can look small while the solution is wrong in hard regions, sharp layers, or unseen boundary cases. In this domain, reject it if this changed-case test fails: move the heat source or change the boundary temperature and compare against held-out sensors or a trusted solve.
- Uncertainty And Generalization: handles a prediction is not enough unless the user knows when it should be believed Evidence it uses: training cases, validation cases, prediction errors, and known shifts between cases Carries: error checks, changed-case tests, and limits on where the model was trained Failure: training error can look good while the model fails under a new geometry, parameter range, sensor, or physical regime. In this domain, reject it if this changed-case test fails: move the heat source or change the boundary temperature and compare against held-out sensors or a trusted solve.

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

#### What Each Concept Must Carry In This Domain
- Operator Learning: handles one simulation answer is not enough when engineers need the whole map from inputs to solution fields Evidence it uses: many example inputs and their full solution fields Carries: a learned map from a forcing, coefficient, shape, or starting field to a solution field Failure: the learned map can give plausible-looking fields that violate the equation or fail on a shifted input family. In this domain, reject it if this changed-case test fails: hold out a new geometry or flow regime and check drag, lift, boundary behavior, and vortices.
- Surrogate Modeling: handles a trusted simulator may be too slow to run for every design, control, or uncertainty question Evidence it uses: expensive solver inputs and outputs for a limited set of cases Carries: the input-output behavior needed for a specified family of queries Failure: speed can hide missing physics when the surrogate is used beyond the regime where it was checked. In this domain, reject it if this changed-case test fails: hold out a new geometry or flow regime and check drag, lift, boundary behavior, and vortices.
- Attention For Scientific Fields: handles a local patch of a field may depend on faraway information, but looking everywhere can be expensive Evidence it uses: large fields where one location may depend on other locations Carries: selected interactions between parts of the input field Failure: windowing or scaling choices can miss long-range effects that matter for the scientific quantity being predicted. In this domain, reject it if this changed-case test fails: hold out a new geometry or flow regime and check drag, lift, boundary behavior, and vortices.
- Uncertainty And Generalization: handles a prediction is not enough unless the user knows when it should be believed Evidence it uses: training cases, validation cases, prediction errors, and known shifts between cases Carries: error checks, changed-case tests, and limits on where the model was trained Failure: training error can look good while the model fails under a new geometry, parameter range, sensor, or physical regime. In this domain, reject it if this changed-case test fails: hold out a new geometry or flow regime and check drag, lift, boundary behavior, and vortices.

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

#### What Each Concept Must Carry In This Domain
- Partial Differential Equations: handles a quantity changes over space and time, so one number is not enough to describe the situation Evidence it uses: a field such as temperature, pressure, concentration, velocity, or displacement Carries: a field, its rates of change, and the boundary or starting information needed to evolve it Failure: a learned shortcut can ignore boundary conditions or conservation behavior that the PDE was carrying. In this domain, reject it if this changed-case test fails: change the load path, defect, mesh, or boundary and check stress near failure regions.
- Surrogate Modeling: handles a trusted simulator may be too slow to run for every design, control, or uncertainty question Evidence it uses: expensive solver inputs and outputs for a limited set of cases Carries: the input-output behavior needed for a specified family of queries Failure: speed can hide missing physics when the surrogate is used beyond the regime where it was checked. In this domain, reject it if this changed-case test fails: change the load path, defect, mesh, or boundary and check stress near failure regions.
- Graphs And Geometric Learning: handles many scientific objects are not simple rows of numbers; their connections matter Evidence it uses: objects with parts and connections, such as meshes, molecules, or interacting components Carries: nodes, edges, spatial relations, and symmetry rules that should not change the answer Failure: the graph can encode the wrong neighborhood, hide missing interactions, or fail when the mesh changes. In this domain, reject it if this changed-case test fails: change the load path, defect, mesh, or boundary and check stress near failure regions.
- Uncertainty And Generalization: handles a prediction is not enough unless the user knows when it should be believed Evidence it uses: training cases, validation cases, prediction errors, and known shifts between cases Carries: error checks, changed-case tests, and limits on where the model was trained Failure: training error can look good while the model fails under a new geometry, parameter range, sensor, or physical regime. In this domain, reject it if this changed-case test fails: change the load path, defect, mesh, or boundary and check stress near failure regions.

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

#### What Each Concept Must Carry In This Domain
- Graphs And Geometric Learning: handles many scientific objects are not simple rows of numbers; their connections matter Evidence it uses: objects with parts and connections, such as meshes, molecules, or interacting components Carries: nodes, edges, spatial relations, and symmetry rules that should not change the answer Failure: the graph can encode the wrong neighborhood, hide missing interactions, or fail when the mesh changes. In this domain, reject it if this changed-case test fails: test on a new scaffold, rare atom type, changed assay, or biological condition outside the familiar set.
- Generative Modeling: handles some tasks need many possible examples, not one predicted answer Evidence it uses: examples of fields, molecules, flows, shapes, or other scientific objects Carries: a learned rule for sampling outputs that resemble the training family Failure: generated samples can look realistic while breaking constraints, conservation, or rare-event behavior. In this domain, reject it if this changed-case test fails: test on a new scaffold, rare atom type, changed assay, or biological condition outside the familiar set.
- Symbolic Regression And Model Discovery: handles a scientist may need a readable equation, not only a model that predicts well Evidence it uses: measured variables and candidate mathematical ingredients Carries: candidate formulas that can be written, checked, and compared Failure: a neat formula can fit the training data while using the wrong variables or failing on a changed experiment. In this domain, reject it if this changed-case test fails: test on a new scaffold, rare atom type, changed assay, or biological condition outside the familiar set.
- Uncertainty And Generalization: handles a prediction is not enough unless the user knows when it should be believed Evidence it uses: training cases, validation cases, prediction errors, and known shifts between cases Carries: error checks, changed-case tests, and limits on where the model was trained Failure: training error can look good while the model fails under a new geometry, parameter range, sensor, or physical regime. In this domain, reject it if this changed-case test fails: test on a new scaffold, rare atom type, changed assay, or biological condition outside the familiar set.

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

#### What Each Concept Must Carry In This Domain
- Foundation Models For PDEs: handles one trained model may be asked to handle many related equations, grids, parameters, or physical settings Evidence it uses: many PDE problem instances across equations, grids, parameters, or physical settings Carries: shared structure across many scientific problem instances Failure: the model can look broad while missing rare regimes, new boundary conditions, or quantities not represented in training. In this domain, reject it if this changed-case test fails: withhold a full equation family, boundary type, scale, or quantity and compare against trusted solves.
- Operator Learning: handles one simulation answer is not enough when engineers need the whole map from inputs to solution fields Evidence it uses: many example inputs and their full solution fields Carries: a learned map from a forcing, coefficient, shape, or starting field to a solution field Failure: the learned map can give plausible-looking fields that violate the equation or fail on a shifted input family. In this domain, reject it if this changed-case test fails: withhold a full equation family, boundary type, scale, or quantity and compare against trusted solves.
- Attention For Scientific Fields: handles a local patch of a field may depend on faraway information, but looking everywhere can be expensive Evidence it uses: large fields where one location may depend on other locations Carries: selected interactions between parts of the input field Failure: windowing or scaling choices can miss long-range effects that matter for the scientific quantity being predicted. In this domain, reject it if this changed-case test fails: withhold a full equation family, boundary type, scale, or quantity and compare against trusted solves.
- Uncertainty And Generalization: handles a prediction is not enough unless the user knows when it should be believed Evidence it uses: training cases, validation cases, prediction errors, and known shifts between cases Carries: error checks, changed-case tests, and limits on where the model was trained Failure: training error can look good while the model fails under a new geometry, parameter range, sensor, or physical regime. In this domain, reject it if this changed-case test fails: withhold a full equation family, boundary type, scale, or quantity and compare against trusted solves.

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

#### What Each Concept Must Carry In This Domain
- Deep Learning: handles scientists often have examples of behavior but no short rule that predicts the next case Evidence it uses: many input-output examples from experiments, simulations, or measurements Carries: many adjustable weights that turn inputs into predictions Failure: the model can fit familiar examples while failing on a new material, geometry, scale, or boundary condition. In this domain, reject it if this changed-case test fails: hold out a new source, scale, sensor condition, or rare case and check the quantity used for decisions.
- Uncertainty And Generalization: handles a prediction is not enough unless the user knows when it should be believed Evidence it uses: training cases, validation cases, prediction errors, and known shifts between cases Carries: error checks, changed-case tests, and limits on where the model was trained Failure: training error can look good while the model fails under a new geometry, parameter range, sensor, or physical regime. In this domain, reject it if this changed-case test fails: hold out a new source, scale, sensor condition, or rare case and check the quantity used for decisions.
- Surrogate Modeling: handles a trusted simulator may be too slow to run for every design, control, or uncertainty question Evidence it uses: expensive solver inputs and outputs for a limited set of cases Carries: the input-output behavior needed for a specified family of queries Failure: speed can hide missing physics when the surrogate is used beyond the regime where it was checked. In this domain, reject it if this changed-case test fails: hold out a new source, scale, sensor condition, or rare case and check the quantity used for decisions.

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

#### What Each Concept Must Carry In This Domain
- Scientific Machine Learning: handles scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time Evidence it uses: data, equations, units, simulation outputs, and domain limits Carries: data evidence, scientific structure, and validation against changed cases Failure: the method becomes a generic fitting tool if the physical quantity, scientific claim, and validation case are not named. In this domain, reject it if this changed-case test fails: change the experiment, boundary, scale, or measured variable and verify the scientific target directly.
- Physics-Informed Neural Networks: handles measurements may be sparse, but the answer must still respect a known physical equation Evidence it uses: some measured values, boundary values, starting values, and a known differential equation Carries: a neural network prediction plus a penalty for violating the known equation Failure: the equation penalty can look small while the solution is wrong in hard regions, sharp layers, or unseen boundary cases. In this domain, reject it if this changed-case test fails: change the experiment, boundary, scale, or measured variable and verify the scientific target directly.
- Symbolic Regression And Model Discovery: handles a scientist may need a readable equation, not only a model that predicts well Evidence it uses: measured variables and candidate mathematical ingredients Carries: candidate formulas that can be written, checked, and compared Failure: a neat formula can fit the training data while using the wrong variables or failing on a changed experiment. In this domain, reject it if this changed-case test fails: change the experiment, boundary, scale, or measured variable and verify the scientific target directly.
- Uncertainty And Generalization: handles a prediction is not enough unless the user knows when it should be believed Evidence it uses: training cases, validation cases, prediction errors, and known shifts between cases Carries: error checks, changed-case tests, and limits on where the model was trained Failure: training error can look good while the model fails under a new geometry, parameter range, sensor, or physical regime. In this domain, reject it if this changed-case test fails: change the experiment, boundary, scale, or measured variable and verify the scientific target directly.

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

#### What Each Concept Must Carry In This Domain
- Neural Differential Equations: handles scientists may know that a system changes continuously but not know the exact rule for that change Evidence it uses: measurements of a system changing over time Carries: a learned rate rule inside a time-stepping calculation Failure: small learned-rate errors can accumulate until long-time predictions drift away from the real system. In this domain, reject it if this changed-case test fails: start from a new condition, run longer than the training window, and check drift, stability, and conserved quantities.
- Symbolic Regression And Model Discovery: handles a scientist may need a readable equation, not only a model that predicts well Evidence it uses: measured variables and candidate mathematical ingredients Carries: candidate formulas that can be written, checked, and compared Failure: a neat formula can fit the training data while using the wrong variables or failing on a changed experiment. In this domain, reject it if this changed-case test fails: start from a new condition, run longer than the training window, and check drift, stability, and conserved quantities.
- Optimization For Learning: handles learning needs a way to decide which model settings are better or worse Evidence it uses: a written score that says which model behavior is better or worse Carries: a written score that compares model output against data, physics penalties, or design goals Failure: a model can optimize the written score while missing the scientific behavior the score failed to name. In this domain, reject it if this changed-case test fails: start from a new condition, run longer than the training window, and check drift, stability, and conserved quantities.
- Uncertainty And Generalization: handles a prediction is not enough unless the user knows when it should be believed Evidence it uses: training cases, validation cases, prediction errors, and known shifts between cases Carries: error checks, changed-case tests, and limits on where the model was trained Failure: training error can look good while the model fails under a new geometry, parameter range, sensor, or physical regime. In this domain, reject it if this changed-case test fails: start from a new condition, run longer than the training window, and check drift, stability, and conserved quantities.

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

#### What Each Concept Must Carry In This Domain
- Optimization For Learning: handles learning needs a way to decide which model settings are better or worse Evidence it uses: a written score that says which model behavior is better or worse Carries: a written score that compares model output against data, physics penalties, or design goals Failure: a model can optimize the written score while missing the scientific behavior the score failed to name. In this domain, reject it if this changed-case test fails: change the weights, hold out hard regions, and check the physical or decision quantity directly.
- Physics-Informed Neural Networks: handles measurements may be sparse, but the answer must still respect a known physical equation Evidence it uses: some measured values, boundary values, starting values, and a known differential equation Carries: a neural network prediction plus a penalty for violating the known equation Failure: the equation penalty can look small while the solution is wrong in hard regions, sharp layers, or unseen boundary cases. In this domain, reject it if this changed-case test fails: change the weights, hold out hard regions, and check the physical or decision quantity directly.
- Deep Learning: handles scientists often have examples of behavior but no short rule that predicts the next case Evidence it uses: many input-output examples from experiments, simulations, or measurements Carries: many adjustable weights that turn inputs into predictions Failure: the model can fit familiar examples while failing on a new material, geometry, scale, or boundary condition. In this domain, reject it if this changed-case test fails: change the weights, hold out hard regions, and check the physical or decision quantity directly.
- Scientific Machine Learning: handles scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time Evidence it uses: data, equations, units, simulation outputs, and domain limits Carries: data evidence, scientific structure, and validation against changed cases Failure: the method becomes a generic fitting tool if the physical quantity, scientific claim, and validation case are not named. In this domain, reject it if this changed-case test fails: change the weights, hold out hard regions, and check the physical or decision quantity directly.


## Reader Checks
### PINNs Reader Check
- Setup: A wall has only a few temperature sensors, but the heat equation is trusted.
- Strong answer: Observed: sensor values, starting or boundary values, and the heat equation. Hidden: the full temperature field. The equation residual checks unsensed locations. The score needs data error, equation error, and boundary or starting error. A changed boundary, source, or held-out sensor should test the claim.
- Weak answer warning: A weak answer says only that the neural network fits data.
- Acceptance sentence: A reader passes only if they can say, in ordinary language, Observed: sensor values, starting or boundary values, and the heat equation. Hidden: the full temperature field. The equation residual checks unsensed locations. The score needs data error, equation error, and boundary or starting error. A changed boundary, source, or held-out sensor should test the claim.

#### First-Principles Scoring Rubric
- Observed evidence: pass if Names what is actually known before the method is chosen. Fail if Starts with the method name.
- Hidden quantity: pass if Names the field, rule, answer, or use range still missing. Fail if Treats the prediction as if it were already known.
- Mathematical move: pass if Explains what the math carries from evidence to missing quantity. Fail if Uses a label without saying what job the math does.
- Changed-case rejection: pass if Names a changed case that could make the claim fail. Fail if Reports a score without a failure condition.
- Forbidden shortcut: pass if Avoids this weak answer: A weak answer says only that the neural network fits data. Fail if A weak answer says only that the neural network fits data.

### Operator Learning Reader Check
- Setup: You have many solved PDE examples and want fast predictions for new input fields.
- Strong answer: The input is a whole field or function, and the output is a whole solution field. The equation, boundary, grid, parameter, and geometry family must be named. The method learns a map between fields, not one field. A new boundary, resolution, parameter range, or equation family should test the claim.
- Weak answer warning: A weak answer says only that the model is fast.
- Acceptance sentence: A reader passes only if they can say, in ordinary language, The input is a whole field or function, and the output is a whole solution field. The equation, boundary, grid, parameter, and geometry family must be named. The method learns a map between fields, not one field. A new boundary, resolution, parameter range, or equation family should test the claim.

#### First-Principles Scoring Rubric
- Observed evidence: pass if Names what is actually known before the method is chosen. Fail if Starts with the method name.
- Hidden quantity: pass if Names the field, rule, answer, or use range still missing. Fail if Treats the prediction as if it were already known.
- Mathematical move: pass if Explains what the math carries from evidence to missing quantity. Fail if Uses a label without saying what job the math does.
- Changed-case rejection: pass if Names a changed case that could make the claim fail. Fail if Reports a score without a failure condition.
- Forbidden shortcut: pass if Avoids this weak answer: A weak answer says only that the model is fast. Fail if A weak answer says only that the model is fast.

### Surrogate Reader Check
- Setup: A trusted simulation is too slow for a design loop.
- Strong answer: The surrogate replaces a named solver or experiment only inside a named query family. Inputs and outputs must match the decision. The stand-in should be checked near the edge of intended use, and the full solver should return when the query leaves that range or when errors affect the decision quantity.
- Weak answer warning: A weak answer treats speed as trust.
- Acceptance sentence: A reader passes only if they can say, in ordinary language, The surrogate replaces a named solver or experiment only inside a named query family. Inputs and outputs must match the decision. The stand-in should be checked near the edge of intended use, and the full solver should return when the query leaves that range or when errors affect the decision quantity.

#### First-Principles Scoring Rubric
- Observed evidence: pass if Names what is actually known before the method is chosen. Fail if Starts with the method name.
- Hidden quantity: pass if Names the field, rule, answer, or use range still missing. Fail if Treats the prediction as if it were already known.
- Mathematical move: pass if Explains what the math carries from evidence to missing quantity. Fail if Uses a label without saying what job the math does.
- Changed-case rejection: pass if Names a changed case that could make the claim fail. Fail if Reports a score without a failure condition.
- Forbidden shortcut: pass if Avoids this weak answer: A weak answer treats speed as trust. Fail if A weak answer treats speed as trust.

### Uncertainty Reader Check
- Setup: A model works on familiar examples and is now proposed for a new scientific setting.
- Strong answer: The answer names the actual shift, such as geometry, parameter range, sensor, scale, boundary, or regime. It measures the error that matters for the scientific decision, states the use range, and names a condition that would stop use.
- Weak answer warning: A weak answer reports one score without saying what changed.
- Acceptance sentence: A reader passes only if they can say, in ordinary language, The answer names the actual shift, such as geometry, parameter range, sensor, scale, boundary, or regime. It measures the error that matters for the scientific decision, states the use range, and names a condition that would stop use.

#### First-Principles Scoring Rubric
- Observed evidence: pass if Names what is actually known before the method is chosen. Fail if Starts with the method name.
- Hidden quantity: pass if Names the field, rule, answer, or use range still missing. Fail if Treats the prediction as if it were already known.
- Mathematical move: pass if Explains what the math carries from evidence to missing quantity. Fail if Uses a label without saying what job the math does.
- Changed-case rejection: pass if Names a changed case that could make the claim fail. Fail if Reports a score without a failure condition.
- Forbidden shortcut: pass if Avoids this weak answer: A weak answer reports one score without saying what changed. Fail if A weak answer reports one score without saying what changed.

### Symbolic Regression Reader Check
- Setup: Measurements suggest there may be a short law behind a changing system.
- Strong answer: The answer lists measured variables, allowed operations or ingredients, and the formula's claim about the system. It names at least one missing variable or untested regime and demands a changed experiment before calling the formula useful.
- Weak answer warning: A weak answer trusts a neat formula because it fits the original data.
- Acceptance sentence: A reader passes only if they can say, in ordinary language, The answer lists measured variables, allowed operations or ingredients, and the formula's claim about the system. It names at least one missing variable or untested regime and demands a changed experiment before calling the formula useful.

#### First-Principles Scoring Rubric
- Observed evidence: pass if Names what is actually known before the method is chosen. Fail if Starts with the method name.
- Hidden quantity: pass if Names the field, rule, answer, or use range still missing. Fail if Treats the prediction as if it were already known.
- Mathematical move: pass if Explains what the math carries from evidence to missing quantity. Fail if Uses a label without saying what job the math does.
- Changed-case rejection: pass if Names a changed case that could make the claim fail. Fail if Reports a score without a failure condition.
- Forbidden shortcut: pass if Avoids this weak answer: A weak answer trusts a neat formula because it fits the original data. Fail if A weak answer trusts a neat formula because it fits the original data.

### Foundation PDE Model Reader Check
- Setup: One broad model is trained across many PDE tasks.
- Strong answer: The answer names included and held-out task families, the shared structure being claimed, and a trusted solver or measurement for checking. It rejects broad claims when new equations, boundaries, scales, or rare regimes were not tested.
- Weak answer warning: A weak answer treats broad training size as proof of broad scientific trust.
- Acceptance sentence: A reader passes only if they can say, in ordinary language, The answer names included and held-out task families, the shared structure being claimed, and a trusted solver or measurement for checking. It rejects broad claims when new equations, boundaries, scales, or rare regimes were not tested.

#### First-Principles Scoring Rubric
- Observed evidence: pass if Names what is actually known before the method is chosen. Fail if Starts with the method name.
- Hidden quantity: pass if Names the field, rule, answer, or use range still missing. Fail if Treats the prediction as if it were already known.
- Mathematical move: pass if Explains what the math carries from evidence to missing quantity. Fail if Uses a label without saying what job the math does.
- Changed-case rejection: pass if Names a changed case that could make the claim fail. Fail if Reports a score without a failure condition.
- Forbidden shortcut: pass if Avoids this weak answer: A weak answer treats broad training size as proof of broad scientific trust. Fail if A weak answer treats broad training size as proof of broad scientific trust.

### Deep Learning Reader Check
- Setup: A reader is deciding whether Deep Learning fits a scientific job in scientific prediction from large measured or simulated data sets.
- Strong answer: Observed: many input-output examples from experiments, simulations, or measurements. Hidden: the exact rule that connects the input to the output. The mathematical move is to adjust many weights until the model maps familiar inputs to the right outputs. The formula shape means the model earns attention only when prediction survives examples it did not train on. The claim should be tested by this changed case: hold out a changed material, geometry, parameter range, or sensor condition.
- Weak answer warning: A weak answer says only that Deep Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.
- Acceptance sentence: A reader passes only if they can say, in ordinary language, Observed: many input-output examples from experiments, simulations, or measurements. Hidden: the exact rule that connects the input to the output. The mathematical move is to adjust many weights until the model maps familiar inputs to the right outputs. The formula shape means the model earns attention only when prediction survives examples it did not train on. The claim should be tested by this changed case: hold out a changed material, geometry, parameter range, or sensor condition.

#### First-Principles Scoring Rubric
- Observed evidence: pass if Names what is actually known before the method is chosen. Fail if Starts with the method name.
- Hidden quantity: pass if Names the field, rule, answer, or use range still missing. Fail if Treats the prediction as if it were already known.
- Mathematical move: pass if Explains what the math carries from evidence to missing quantity. Fail if Uses a label without saying what job the math does.
- Changed-case rejection: pass if Names a changed case that could make the claim fail. Fail if Reports a score without a failure condition.
- Forbidden shortcut: pass if Avoids this weak answer: A weak answer says only that Deep Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test. Fail if A weak answer says only that Deep Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.

### Partial Differential Equations Reader Check
- Setup: A reader is deciding whether Partial Differential Equations fits a scientific job in fluids, heat, waves, mechanics, chemistry, climate, and other changing fields.
- Strong answer: Observed: a field such as temperature, pressure, concentration, velocity, or displacement. Hidden: how every point in the field affects nearby points over time. The mathematical move is to write a local change rule that uses rates across space and time. The formula shape means the equation carries how a whole field changes, rather than only how one number changes. The claim should be tested by this changed case: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error.
- Weak answer warning: A weak answer says only that Partial Differential Equations is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.
- Acceptance sentence: A reader passes only if they can say, in ordinary language, Observed: a field such as temperature, pressure, concentration, velocity, or displacement. Hidden: how every point in the field affects nearby points over time. The mathematical move is to write a local change rule that uses rates across space and time. The formula shape means the equation carries how a whole field changes, rather than only how one number changes. The claim should be tested by this changed case: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error.

#### First-Principles Scoring Rubric
- Observed evidence: pass if Names what is actually known before the method is chosen. Fail if Starts with the method name.
- Hidden quantity: pass if Names the field, rule, answer, or use range still missing. Fail if Treats the prediction as if it were already known.
- Mathematical move: pass if Explains what the math carries from evidence to missing quantity. Fail if Uses a label without saying what job the math does.
- Changed-case rejection: pass if Names a changed case that could make the claim fail. Fail if Reports a score without a failure condition.
- Forbidden shortcut: pass if Avoids this weak answer: A weak answer says only that Partial Differential Equations is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test. Fail if A weak answer says only that Partial Differential Equations is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.

### Scientific Machine Learning Reader Check
- Setup: A reader is deciding whether Scientific Machine Learning fits a scientific job in using data-driven models inside scientific workflows.
- Strong answer: Observed: data, equations, units, simulation outputs, and domain limits. Hidden: which parts of the scientific system are missing, noisy, or too costly to compute directly. The mathematical move is to combine learned prediction with scientific checks that name what the claim is allowed to mean. The formula shape means the model is judged by a scientific job, not by a score floating away from the job. The claim should be tested by this changed case: state the scientific quantity first, then test it under a changed case that matters in that domain.
- Weak answer warning: A weak answer says only that Scientific Machine Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.
- Acceptance sentence: A reader passes only if they can say, in ordinary language, Observed: data, equations, units, simulation outputs, and domain limits. Hidden: which parts of the scientific system are missing, noisy, or too costly to compute directly. The mathematical move is to combine learned prediction with scientific checks that name what the claim is allowed to mean. The formula shape means the model is judged by a scientific job, not by a score floating away from the job. The claim should be tested by this changed case: state the scientific quantity first, then test it under a changed case that matters in that domain.

#### First-Principles Scoring Rubric
- Observed evidence: pass if Names what is actually known before the method is chosen. Fail if Starts with the method name.
- Hidden quantity: pass if Names the field, rule, answer, or use range still missing. Fail if Treats the prediction as if it were already known.
- Mathematical move: pass if Explains what the math carries from evidence to missing quantity. Fail if Uses a label without saying what job the math does.
- Changed-case rejection: pass if Names a changed case that could make the claim fail. Fail if Reports a score without a failure condition.
- Forbidden shortcut: pass if Avoids this weak answer: A weak answer says only that Scientific Machine Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test. Fail if A weak answer says only that Scientific Machine Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.

### Optimization For Learning Reader Check
- Setup: A reader is deciding whether Optimization For Learning fits a scientific job in turning model fitting into a repeatable computation.
- Strong answer: Observed: a written score that says which model behavior is better or worse. Hidden: whether that score matches the scientific behavior the user actually cares about. The mathematical move is to change model settings to lower the written score. The formula shape means the model learns the score, so the score must include the scientific burden. The claim should be tested by this changed case: inspect what the score ignores, then check whether the ignored behavior fails after training.
- Weak answer warning: A weak answer says only that Optimization For Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.
- Acceptance sentence: A reader passes only if they can say, in ordinary language, Observed: a written score that says which model behavior is better or worse. Hidden: whether that score matches the scientific behavior the user actually cares about. The mathematical move is to change model settings to lower the written score. The formula shape means the model learns the score, so the score must include the scientific burden. The claim should be tested by this changed case: inspect what the score ignores, then check whether the ignored behavior fails after training.

#### First-Principles Scoring Rubric
- Observed evidence: pass if Names what is actually known before the method is chosen. Fail if Starts with the method name.
- Hidden quantity: pass if Names the field, rule, answer, or use range still missing. Fail if Treats the prediction as if it were already known.
- Mathematical move: pass if Explains what the math carries from evidence to missing quantity. Fail if Uses a label without saying what job the math does.
- Changed-case rejection: pass if Names a changed case that could make the claim fail. Fail if Reports a score without a failure condition.
- Forbidden shortcut: pass if Avoids this weak answer: A weak answer says only that Optimization For Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test. Fail if A weak answer says only that Optimization For Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.

### Generative Modeling Reader Check
- Setup: A reader is deciding whether Generative Modeling fits a scientific job in creating plausible scientific samples, fields, or candidate designs.
- Strong answer: Observed: examples of fields, molecules, flows, shapes, or other scientific objects. Hidden: the spread of possible valid objects beyond the examples. The mathematical move is to learn how to sample new candidates that resemble the training family. The formula shape means a generated object must still pass physics and usefulness checks. The claim should be tested by this changed case: measure constraints, rare cases, conservation, and downstream task performance on generated samples.
- Weak answer warning: A weak answer says only that Generative Modeling is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.
- Acceptance sentence: A reader passes only if they can say, in ordinary language, Observed: examples of fields, molecules, flows, shapes, or other scientific objects. Hidden: the spread of possible valid objects beyond the examples. The mathematical move is to learn how to sample new candidates that resemble the training family. The formula shape means a generated object must still pass physics and usefulness checks. The claim should be tested by this changed case: measure constraints, rare cases, conservation, and downstream task performance on generated samples.

#### First-Principles Scoring Rubric
- Observed evidence: pass if Names what is actually known before the method is chosen. Fail if Starts with the method name.
- Hidden quantity: pass if Names the field, rule, answer, or use range still missing. Fail if Treats the prediction as if it were already known.
- Mathematical move: pass if Explains what the math carries from evidence to missing quantity. Fail if Uses a label without saying what job the math does.
- Changed-case rejection: pass if Names a changed case that could make the claim fail. Fail if Reports a score without a failure condition.
- Forbidden shortcut: pass if Avoids this weak answer: A weak answer says only that Generative Modeling is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test. Fail if A weak answer says only that Generative Modeling is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.

### Graphs And Geometric Learning Reader Check
- Setup: A reader is deciding whether Graphs And Geometric Learning fits a scientific job in systems made of interacting parts, meshes, molecules, or spatial relations.
- Strong answer: Observed: objects with parts and connections, such as meshes, molecules, or interacting components. Hidden: which neighboring and long-range interactions control the scientific quantity. The mathematical move is to let information move along the object connections instead of flattening the object into a plain row. The formula shape means the model keeps the structure of the scientific object visible. The claim should be tested by this changed case: change the mesh, rotate or move the object, or add missing interactions and inspect what breaks.
- Weak answer warning: A weak answer says only that Graphs And Geometric Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.
- Acceptance sentence: A reader passes only if they can say, in ordinary language, Observed: objects with parts and connections, such as meshes, molecules, or interacting components. Hidden: which neighboring and long-range interactions control the scientific quantity. The mathematical move is to let information move along the object connections instead of flattening the object into a plain row. The formula shape means the model keeps the structure of the scientific object visible. The claim should be tested by this changed case: change the mesh, rotate or move the object, or add missing interactions and inspect what breaks.

#### First-Principles Scoring Rubric
- Observed evidence: pass if Names what is actually known before the method is chosen. Fail if Starts with the method name.
- Hidden quantity: pass if Names the field, rule, answer, or use range still missing. Fail if Treats the prediction as if it were already known.
- Mathematical move: pass if Explains what the math carries from evidence to missing quantity. Fail if Uses a label without saying what job the math does.
- Changed-case rejection: pass if Names a changed case that could make the claim fail. Fail if Reports a score without a failure condition.
- Forbidden shortcut: pass if Avoids this weak answer: A weak answer says only that Graphs And Geometric Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test. Fail if A weak answer says only that Graphs And Geometric Learning is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.

### Neural Differential Equations Reader Check
- Setup: A reader is deciding whether Neural Differential Equations fits a scientific job in changing systems where time evolution is part of the model.
- Strong answer: Observed: measurements of a system changing over time. Hidden: the rate rule that moves the present value into the future. The mathematical move is to learn the missing rate rule and place it inside a time-evolution calculation. The formula shape means learning supplies the unknown change rule while the time update carries the idea of continuous motion. The claim should be tested by this changed case: run longer than the training window and check whether small rate errors accumulate into drift.
- Weak answer warning: A weak answer says only that Neural Differential Equations is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.
- Acceptance sentence: A reader passes only if they can say, in ordinary language, Observed: measurements of a system changing over time. Hidden: the rate rule that moves the present value into the future. The mathematical move is to learn the missing rate rule and place it inside a time-evolution calculation. The formula shape means learning supplies the unknown change rule while the time update carries the idea of continuous motion. The claim should be tested by this changed case: run longer than the training window and check whether small rate errors accumulate into drift.

#### First-Principles Scoring Rubric
- Observed evidence: pass if Names what is actually known before the method is chosen. Fail if Starts with the method name.
- Hidden quantity: pass if Names the field, rule, answer, or use range still missing. Fail if Treats the prediction as if it were already known.
- Mathematical move: pass if Explains what the math carries from evidence to missing quantity. Fail if Uses a label without saying what job the math does.
- Changed-case rejection: pass if Names a changed case that could make the claim fail. Fail if Reports a score without a failure condition.
- Forbidden shortcut: pass if Avoids this weak answer: A weak answer says only that Neural Differential Equations is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test. Fail if A weak answer says only that Neural Differential Equations is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.

### Attention For Scientific Fields Reader Check
- Setup: A reader is deciding whether Attention For Scientific Fields fits a scientific job in large scientific fields where distant parts may interact.
- Strong answer: Observed: large fields where one location may depend on other locations. Hidden: which distant parts matter for the local prediction. The mathematical move is to let the model choose which parts of the field exchange information. The formula shape means attention is a routing rule for information, not proof that the selected route is physically complete. The claim should be tested by this changed case: change the window size, inspect long-range effects, and compare behavior near boundaries or sharp structures.
- Weak answer warning: A weak answer says only that Attention For Scientific Fields is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.
- Acceptance sentence: A reader passes only if they can say, in ordinary language, Observed: large fields where one location may depend on other locations. Hidden: which distant parts matter for the local prediction. The mathematical move is to let the model choose which parts of the field exchange information. The formula shape means attention is a routing rule for information, not proof that the selected route is physically complete. The claim should be tested by this changed case: change the window size, inspect long-range effects, and compare behavior near boundaries or sharp structures.

#### First-Principles Scoring Rubric
- Observed evidence: pass if Names what is actually known before the method is chosen. Fail if Starts with the method name.
- Hidden quantity: pass if Names the field, rule, answer, or use range still missing. Fail if Treats the prediction as if it were already known.
- Mathematical move: pass if Explains what the math carries from evidence to missing quantity. Fail if Uses a label without saying what job the math does.
- Changed-case rejection: pass if Names a changed case that could make the claim fail. Fail if Reports a score without a failure condition.
- Forbidden shortcut: pass if Avoids this weak answer: A weak answer says only that Attention For Scientific Fields is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test. Fail if A weak answer says only that Attention For Scientific Fields is useful without naming the observed evidence, hidden quantity, mathematical move, and changed-case test.


## Plain Explanation Practice
- See `site/plain-explanation-practice.html` for learner drills that turn each topic into a plain spoken paragraph from everyday need to tested claim.

## Decision Guide
### Sparse Data, Known Equation
- Situation: You have few measurements, but a trusted equation and boundary or starting information exist.
- Start with: Physics-informed neural networks
- Why: The equation can check the fitted field where measurements are missing.
- Decision shortage: measurements may be sparse, but the answer must still respect a known physical equation
- Observed evidence: some measured values, boundary values, starting values, and a known differential equation
- Hidden need: the full field value at every point in space and time
- Why this starting point earns its place: fit a neural network while also measuring how badly its output violates the known equation
- What the choice carries: the model is not allowed to match points while freely breaking the equation between those points
- First rejection test: move the training points, inspect sharp regions, and compare against a numerical solve or held-out measurements
- Evidence needed: held-out measurements, boundary checks, equation residual checks, and comparison against a trusted solve when possible

### Many Related Simulations
- Situation: You have many solved examples and need fast answers for new inputs from the same family.
- Start with: Operator learning
- Why: The useful object is the map from input fields to output fields, not one solved field.
- Decision shortage: one simulation answer is not enough when engineers need the whole map from inputs to solution fields
- Observed evidence: many example inputs and their full solution fields
- Hidden need: the rule that maps a new input field to its new solution field
- Why this starting point earns its place: learn the map from problem input to solution, not only one solution at a time
- What the choice carries: the learned object is a shortcut for a family of solves, so the family must be named
- First rejection test: change resolution, coefficients, boundary conditions, or forcing and check whether the predicted field still satisfies the scientific quantity being claimed
- Evidence needed: held-out fields, changed resolution tests, boundary tests, and checks on the scientific output quantity

### Expensive Repeated Decisions
- Situation: A trusted solver or experiment is too slow for design, search, control, or uncertainty sweeps.
- Start with: Surrogate modeling
- Why: A fast stand-in can answer repeated questions if its use range is stated and checked.
- Decision shortage: a trusted simulator may be too slow to run for every design, control, or uncertainty question
- Observed evidence: expensive solver inputs and outputs for a limited set of cases
- Hidden need: the solver answer for every new query someone wants to ask
- Why this starting point earns its place: train a cheaper stand-in for the expensive input-output behavior
- What the choice carries: speed is useful only inside the query family where the stand-in was checked
- First rejection test: compare against the full solver on new cases near the edge of the intended use
- Evidence needed: full-solver comparisons near the edge of use, decision-metric error, and a stated use range

### Need A Readable Law
- Situation: Prediction is not enough; the output should be a formula or mechanism people can inspect.
- Start with: Symbolic regression or neural differential equations
- Why: The scientific product is a candidate rule, not only a number returned by a fitted model.
- Decision shortage: a scientist may need a readable equation, not only a model that predicts well
- Observed evidence: measured variables and candidate mathematical ingredients
- Hidden need: which short formula, if any, actually explains the measured change
- Why this starting point earns its place: search for a readable equation that fits the data and survives a changed case
- What the choice carries: a compact equation is a claim about structure, rather than only a curve through points
- First rejection test: remove a needed variable, add noise, or test a new experiment and see whether the formula still predicts
- Evidence needed: changed-experiment tests, missing-variable checks, noise checks, and scientific inspection of the selected rule

### New Setting Risk
- Situation: A model trained in one setting is being used in another setting.
- Start with: Uncertainty and generalization checks
- Why: The main question is whether the prediction should be believed under the change.
- Decision shortage: a prediction is not enough unless the user knows when it should be believed
- Observed evidence: training cases, validation cases, prediction errors, and known shifts between cases
- Hidden need: how wrong the model may be on a case unlike the ones it learned from
- Why this starting point earns its place: separate fit on familiar examples from evidence on changed examples
- What the choice carries: a prediction without a use range is not yet a scientific claim
- First rejection test: move one important condition outside the training range and measure the first failure
- Evidence needed: changed-case tests, use-range statements, error on the decision quantity, and first-failure examples

### Broad PDE Coverage
- Situation: One model is proposed for many equations, grids, parameters, or scientific tasks.
- Start with: Foundation models for PDEs
- Why: The claim is about shared structure across tasks, so whole task families must be tested.
- Decision shortage: one trained model may be asked to handle many related equations, grids, parameters, or physical settings
- Observed evidence: many PDE problem instances across equations, grids, parameters, or physical settings
- Hidden need: which shared structure carries from one scientific task to another
- Why this starting point earns its place: train one broad model to reuse structure across many related field-prediction tasks
- What the choice carries: breadth is useful only if the new task shares the structure the model actually learned
- First rejection test: hold out a new equation family, boundary type, scale, or rare regime and compare against a trusted solver
- Evidence needed: held-out task-family tests, trusted-solver comparisons, boundary and scale tests, and failure reports

### Many Examples, No Clear Rule
- Situation: You have many examples, but no trusted equation or readable law yet.
- Start with: Deep learning
- Why: The first useful move is to learn a flexible predictor, then test whether it carries the quantity that matters.
- Decision shortage: scientists often have examples of behavior but no short rule that predicts the next case
- Observed evidence: many input-output examples from experiments, simulations, or measurements
- Hidden need: the exact rule that connects the input to the output
- Why this starting point earns its place: adjust many weights until the model maps familiar inputs to the right outputs
- What the choice carries: the model earns attention only when prediction survives examples it did not train on
- First rejection test: hold out a changed material, geometry, parameter range, or sensor condition
- Evidence needed: held-out examples, changed measurement tests, target-quantity error, and a named first failure

### Scientific Claim Needs Discipline
- Situation: A model is being called scientific, but the claim, evidence, and failure boundary are not yet separated.
- Start with: Scientific machine learning
- Why: The field-level job is to make the learned answer answerable to evidence, physical quantities, and changed cases.
- Decision shortage: scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time
- Observed evidence: data, equations, units, simulation outputs, and domain limits
- Hidden need: which parts of the scientific system are missing, noisy, or too costly to compute directly
- Why this starting point earns its place: combine learned prediction with scientific checks that name what the claim is allowed to mean
- What the choice carries: the model is judged by a scientific job, not by a score floating away from the job
- First rejection test: state the scientific quantity first, then test it under a changed case that matters in that domain
- Evidence needed: source anchors, a named scientific quantity, domain-specific checks, and a changed-case rejection test

### Training Score Burden
- Situation: A model improves a written score, but the scientific decision may depend on something the score ignored.
- Start with: Optimization for learning
- Why: Training only improves what the objective asks it to improve, so the objective must match the scientific burden.
- Decision shortage: learning needs a way to decide which model settings are better or worse
- Observed evidence: a written score that says which model behavior is better or worse
- Hidden need: whether that score matches the scientific behavior the user actually cares about
- Why this starting point earns its place: change model settings to lower the written score
- What the choice carries: the model learns the score, so the score must include the scientific burden
- First rejection test: inspect what the score ignores, then check whether the ignored behavior fails after training
- Evidence needed: loss-term inspection, ignored-requirement tests, held-out edge cases, and the decision quantity after training

### Need Many Valid Possibilities
- Situation: The task needs many candidate fields, molecules, designs, or futures rather than one answer.
- Start with: Generative modeling
- Why: The useful product is a set of possible scientific objects that still obey the rules that matter.
- Decision shortage: some tasks need many possible examples, not one predicted answer
- Observed evidence: examples of fields, molecules, flows, shapes, or other scientific objects
- Hidden need: the spread of possible valid objects beyond the examples
- Why this starting point earns its place: learn how to sample new candidates that resemble the training family
- What the choice carries: a generated object must still pass physics and usefulness checks
- First rejection test: measure constraints, rare cases, conservation, and downstream task performance on generated samples
- Evidence needed: constraint checks, rare-event checks, downstream-task tests, and examples of rejected samples

### Connected Object Matters
- Situation: The object is a molecule, mesh, graph, surface, or network where connections carry part of the scientific meaning.
- Start with: Graphs and geometric learning
- Why: Flattening the object can hide which parts influence which other parts.
- Decision shortage: many scientific objects are not simple rows of numbers; their connections matter
- Observed evidence: objects with parts and connections, such as meshes, molecules, or interacting components
- Hidden need: which neighboring and long-range interactions control the scientific quantity
- Why this starting point earns its place: let information move along the object connections instead of flattening the object into a plain row
- What the choice carries: the model keeps the structure of the scientific object visible
- First rejection test: change the mesh, rotate or move the object, or add missing interactions and inspect what breaks
- Evidence needed: mesh-change tests, symmetry checks, missing-interaction tests, and target-property error on changed objects

### Far Field Information Matters
- Situation: A local part of a scientific field depends on distant regions, but carrying every interaction is expensive.
- Start with: Attention for scientific fields
- Why: Attention gives a way to route selected information across a field while making the routing choice testable.
- Decision shortage: a local patch of a field may depend on faraway information, but looking everywhere can be expensive
- Observed evidence: large fields where one location may depend on other locations
- Hidden need: which distant parts matter for the local prediction
- Why this starting point earns its place: let the model choose which parts of the field exchange information
- What the choice carries: attention is a routing rule for information, not proof that the selected route is physically complete
- First rejection test: change the window size, inspect long-range effects, and compare behavior near boundaries or sharp structures
- Evidence needed: window-change tests, long-range interaction tests, boundary-stress cases, and error on the scientific quantity

### Field Rule Before Method
- Situation: A quantity changes across space, time, or both, and one number cannot describe the scientific state.
- Start with: Partial differential equations
- Why: The PDE names how local change, movement, sources, and boundaries must fit together before a learned method is trusted.
- Decision shortage: a quantity changes over space and time, so one number is not enough to describe the situation
- Observed evidence: a field such as temperature, pressure, concentration, velocity, or displacement
- Hidden need: how every point in the field affects nearby points over time
- Why this starting point earns its place: write a local change rule that uses rates across space and time
- What the choice carries: the equation carries how a whole field changes, rather than only how one number changes
- First rejection test: change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error
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
- Confusion prevented: Without the dependencies, a reader may think a PINN is a neural network with physics language attached, rather than a fit constrained by data, equations, and boundaries.

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
- Transcript can support: The transcript can support that Deep Learning is taught as a way to address this shortage: scientists often have examples of behavior but no short rule that predicts the next case
- Transcript cannot support: The transcript cannot prove that Deep Learning will work on every new case in scientific prediction from large measured or simulated data sets; that has to be tested on the target quantity.
- Stronger validation needed: Run the idea on a changed case in scientific prediction from large measured or simulated data sets and compare the predicted quantity with trusted measurements, trusted solves, or a known conservation check.
- First overclaim to reject: Reject any sentence saying Deep Learning is generally reliable before it survives this test: the model can fit familiar examples while failing on a new material, geometry, scale, or boundary condition
- Reviewer action: Start from the selected source anchors, then ask whether the page's claim is no wider than this hidden need: the exact rule that connects the input to the output
- Packet: evidence-packets/deep-learning.html

### Physics-Informed Neural Networks
- Problem: measurements may be sparse, but the answer must still respect a known physical equation
- Domain: differential equations in science and engineering
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in differential equations in science and engineering, not only a lecture mention.
- Transcript can support: The transcript can support that Physics-Informed Neural Networks is taught as a way to address this shortage: measurements may be sparse, but the answer must still respect a known physical equation
- Transcript cannot support: The transcript cannot prove that Physics-Informed Neural Networks will work on every new case in differential equations in science and engineering; that has to be tested on the target quantity.
- Stronger validation needed: Run the idea on a changed case in differential equations in science and engineering and compare the predicted quantity with trusted measurements, trusted solves, or a known conservation check.
- First overclaim to reject: Reject any sentence saying Physics-Informed Neural Networks is generally reliable before it survives this test: the equation penalty can look small while the solution is wrong in hard regions, sharp layers, or unseen boundary cases
- Reviewer action: Start from the selected source anchors, then ask whether the page's claim is no wider than this hidden need: the full field value at every point in space and time
- Packet: evidence-packets/physics-informed-neural-networks.html

### Partial Differential Equations
- Problem: a quantity changes over space and time, so one number is not enough to describe the situation
- Domain: fluids, heat, waves, mechanics, chemistry, climate, and other changing fields
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in fluids, heat, waves, mechanics, chemistry, climate, and other changing fields, not only a lecture mention.
- Transcript can support: The transcript can support that Partial Differential Equations is taught as a way to address this shortage: a quantity changes over space and time, so one number is not enough to describe the situation
- Transcript cannot support: The transcript cannot prove that Partial Differential Equations will work on every new case in fluids, heat, waves, mechanics, chemistry, climate, and other changing fields; that has to be tested on the target quantity.
- Stronger validation needed: Run the idea on a changed case in fluids, heat, waves, mechanics, chemistry, climate, and other changing fields and compare the predicted quantity with trusted measurements, trusted solves, or a known conservation check.
- First overclaim to reject: Reject any sentence saying Partial Differential Equations is generally reliable before it survives this test: a learned shortcut can ignore boundary conditions or conservation behavior that the PDE was carrying
- Reviewer action: Start from the selected source anchors, then ask whether the page's claim is no wider than this hidden need: how every point in the field affects nearby points over time
- Packet: evidence-packets/partial-differential-equations.html

### Operator Learning
- Problem: one simulation answer is not enough when engineers need the whole map from inputs to solution fields
- Domain: fast prediction for families of scientific simulations
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in fast prediction for families of scientific simulations, not only a lecture mention.
- Transcript can support: The transcript can support that Operator Learning is taught as a way to address this shortage: one simulation answer is not enough when engineers need the whole map from inputs to solution fields
- Transcript cannot support: The transcript cannot prove that Operator Learning will work on every new case in fast prediction for families of scientific simulations; that has to be tested on the target quantity.
- Stronger validation needed: Run the idea on a changed case in fast prediction for families of scientific simulations and compare the predicted quantity with trusted measurements, trusted solves, or a known conservation check.
- First overclaim to reject: Reject any sentence saying Operator Learning is generally reliable before it survives this test: the learned map can give plausible-looking fields that violate the equation or fail on a shifted input family
- Reviewer action: Start from the selected source anchors, then ask whether the page's claim is no wider than this hidden need: the rule that maps a new input field to its new solution field
- Packet: evidence-packets/operator-learning.html

### Scientific Machine Learning
- Problem: scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time
- Domain: using data-driven models inside scientific workflows
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in using data-driven models inside scientific workflows, not only a lecture mention.
- Transcript can support: The transcript can support that Scientific Machine Learning is taught as a way to address this shortage: scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time
- Transcript cannot support: The transcript cannot prove that Scientific Machine Learning will work on every new case in using data-driven models inside scientific workflows; that has to be tested on the target quantity.
- Stronger validation needed: Run the idea on a changed case in using data-driven models inside scientific workflows and compare the predicted quantity with trusted measurements, trusted solves, or a known conservation check.
- First overclaim to reject: Reject any sentence saying Scientific Machine Learning is generally reliable before it survives this test: the method becomes a generic fitting tool if the physical quantity, scientific claim, and validation case are not named
- Reviewer action: Start from the selected source anchors, then ask whether the page's claim is no wider than this hidden need: which parts of the scientific system are missing, noisy, or too costly to compute directly
- Packet: evidence-packets/scientific-machine-learning.html

### Surrogate Modeling
- Problem: a trusted simulator may be too slow to run for every design, control, or uncertainty question
- Domain: expensive simulation and design loops
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in expensive simulation and design loops, not only a lecture mention.
- Transcript can support: The transcript can support that Surrogate Modeling is taught as a way to address this shortage: a trusted simulator may be too slow to run for every design, control, or uncertainty question
- Transcript cannot support: The transcript cannot prove that Surrogate Modeling will work on every new case in expensive simulation and design loops; that has to be tested on the target quantity.
- Stronger validation needed: Run the idea on a changed case in expensive simulation and design loops and compare the predicted quantity with trusted measurements, trusted solves, or a known conservation check.
- First overclaim to reject: Reject any sentence saying Surrogate Modeling is generally reliable before it survives this test: speed can hide missing physics when the surrogate is used beyond the regime where it was checked
- Reviewer action: Start from the selected source anchors, then ask whether the page's claim is no wider than this hidden need: the solver answer for every new query someone wants to ask
- Packet: evidence-packets/surrogate-modeling.html

### Uncertainty And Generalization
- Problem: a prediction is not enough unless the user knows when it should be believed
- Domain: model use under new conditions
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in model use under new conditions, not only a lecture mention.
- Transcript can support: The transcript can support that Uncertainty And Generalization is taught as a way to address this shortage: a prediction is not enough unless the user knows when it should be believed
- Transcript cannot support: The transcript cannot prove that Uncertainty And Generalization will work on every new case in model use under new conditions; that has to be tested on the target quantity.
- Stronger validation needed: Run the idea on a changed case in model use under new conditions and compare the predicted quantity with trusted measurements, trusted solves, or a known conservation check.
- First overclaim to reject: Reject any sentence saying Uncertainty And Generalization is generally reliable before it survives this test: training error can look good while the model fails under a new geometry, parameter range, sensor, or physical regime
- Reviewer action: Start from the selected source anchors, then ask whether the page's claim is no wider than this hidden need: how wrong the model may be on a case unlike the ones it learned from
- Packet: evidence-packets/uncertainty-and-generalization.html

### Optimization For Learning
- Problem: learning needs a way to decide which model settings are better or worse
- Domain: turning model fitting into a repeatable computation
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in turning model fitting into a repeatable computation, not only a lecture mention.
- Transcript can support: The transcript can support that Optimization For Learning is taught as a way to address this shortage: learning needs a way to decide which model settings are better or worse
- Transcript cannot support: The transcript cannot prove that Optimization For Learning will work on every new case in turning model fitting into a repeatable computation; that has to be tested on the target quantity.
- Stronger validation needed: Run the idea on a changed case in turning model fitting into a repeatable computation and compare the predicted quantity with trusted measurements, trusted solves, or a known conservation check.
- First overclaim to reject: Reject any sentence saying Optimization For Learning is generally reliable before it survives this test: a model can optimize the written score while missing the scientific behavior the score failed to name
- Reviewer action: Start from the selected source anchors, then ask whether the page's claim is no wider than this hidden need: whether that score matches the scientific behavior the user actually cares about
- Packet: evidence-packets/optimization-for-learning.html

### Generative Modeling
- Problem: some tasks need many possible examples, not one predicted answer
- Domain: creating plausible scientific samples, fields, or candidate designs
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in creating plausible scientific samples, fields, or candidate designs, not only a lecture mention.
- Transcript can support: The transcript can support that Generative Modeling is taught as a way to address this shortage: some tasks need many possible examples, not one predicted answer
- Transcript cannot support: The transcript cannot prove that Generative Modeling will work on every new case in creating plausible scientific samples, fields, or candidate designs; that has to be tested on the target quantity.
- Stronger validation needed: Run the idea on a changed case in creating plausible scientific samples, fields, or candidate designs and compare the predicted quantity with trusted measurements, trusted solves, or a known conservation check.
- First overclaim to reject: Reject any sentence saying Generative Modeling is generally reliable before it survives this test: generated samples can look realistic while breaking constraints, conservation, or rare-event behavior
- Reviewer action: Start from the selected source anchors, then ask whether the page's claim is no wider than this hidden need: the spread of possible valid objects beyond the examples
- Packet: evidence-packets/generative-modeling.html

### Graphs And Geometric Learning
- Problem: many scientific objects are not simple rows of numbers; their connections matter
- Domain: systems made of interacting parts, meshes, molecules, or spatial relations
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in systems made of interacting parts, meshes, molecules, or spatial relations, not only a lecture mention.
- Transcript can support: The transcript can support that Graphs And Geometric Learning is taught as a way to address this shortage: many scientific objects are not simple rows of numbers; their connections matter
- Transcript cannot support: The transcript cannot prove that Graphs And Geometric Learning will work on every new case in systems made of interacting parts, meshes, molecules, or spatial relations; that has to be tested on the target quantity.
- Stronger validation needed: Run the idea on a changed case in systems made of interacting parts, meshes, molecules, or spatial relations and compare the predicted quantity with trusted measurements, trusted solves, or a known conservation check.
- First overclaim to reject: Reject any sentence saying Graphs And Geometric Learning is generally reliable before it survives this test: the graph can encode the wrong neighborhood, hide missing interactions, or fail when the mesh changes
- Reviewer action: Start from the selected source anchors, then ask whether the page's claim is no wider than this hidden need: which neighboring and long-range interactions control the scientific quantity
- Packet: evidence-packets/graphs-and-geometric-learning.html

### Neural Differential Equations
- Problem: scientists may know that a system changes continuously but not know the exact rule for that change
- Domain: changing systems where time evolution is part of the model
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in changing systems where time evolution is part of the model, not only a lecture mention.
- Transcript can support: The transcript can support that Neural Differential Equations is taught as a way to address this shortage: scientists may know that a system changes continuously but not know the exact rule for that change
- Transcript cannot support: The transcript cannot prove that Neural Differential Equations will work on every new case in changing systems where time evolution is part of the model; that has to be tested on the target quantity.
- Stronger validation needed: Run the idea on a changed case in changing systems where time evolution is part of the model and compare the predicted quantity with trusted measurements, trusted solves, or a known conservation check.
- First overclaim to reject: Reject any sentence saying Neural Differential Equations is generally reliable before it survives this test: small learned-rate errors can accumulate until long-time predictions drift away from the real system
- Reviewer action: Start from the selected source anchors, then ask whether the page's claim is no wider than this hidden need: the rate rule that moves the present value into the future
- Packet: evidence-packets/neural-differential-equations.html

### Symbolic Regression And Model Discovery
- Problem: a scientist may need a readable equation, not only a model that predicts well
- Domain: turning data into equations people can inspect
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in turning data into equations people can inspect, not only a lecture mention.
- Transcript can support: The transcript can support that Symbolic Regression And Model Discovery is taught as a way to address this shortage: a scientist may need a readable equation, not only a model that predicts well
- Transcript cannot support: The transcript cannot prove that Symbolic Regression And Model Discovery will work on every new case in turning data into equations people can inspect; that has to be tested on the target quantity.
- Stronger validation needed: Run the idea on a changed case in turning data into equations people can inspect and compare the predicted quantity with trusted measurements, trusted solves, or a known conservation check.
- First overclaim to reject: Reject any sentence saying Symbolic Regression And Model Discovery is generally reliable before it survives this test: a neat formula can fit the training data while using the wrong variables or failing on a changed experiment
- Reviewer action: Start from the selected source anchors, then ask whether the page's claim is no wider than this hidden need: which short formula, if any, actually explains the measured change
- Packet: evidence-packets/symbolic-regression.html

### Foundation Models For PDEs
- Problem: one trained model may be asked to handle many related equations, grids, parameters, or physical settings
- Domain: broad families of PDE problems and scientific fields
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in broad families of PDE problems and scientific fields, not only a lecture mention.
- Transcript can support: The transcript can support that Foundation Models For PDEs is taught as a way to address this shortage: one trained model may be asked to handle many related equations, grids, parameters, or physical settings
- Transcript cannot support: The transcript cannot prove that Foundation Models For PDEs will work on every new case in broad families of PDE problems and scientific fields; that has to be tested on the target quantity.
- Stronger validation needed: Run the idea on a changed case in broad families of PDE problems and scientific fields and compare the predicted quantity with trusted measurements, trusted solves, or a known conservation check.
- First overclaim to reject: Reject any sentence saying Foundation Models For PDEs is generally reliable before it survives this test: the model can look broad while missing rare regimes, new boundary conditions, or quantities not represented in training
- Reviewer action: Start from the selected source anchors, then ask whether the page's claim is no wider than this hidden need: which shared structure carries from one scientific task to another
- Packet: evidence-packets/foundation-models-for-pdes.html

### Attention For Scientific Fields
- Problem: a local patch of a field may depend on faraway information, but looking everywhere can be expensive
- Domain: large scientific fields where distant parts may interact
- Evidence anchors: 6
- Reviewed source anchors: 2
- Broad transcript mentions: 4
- Stronger proof needed: To trust the method, add evidence from a changed-case test in large scientific fields where distant parts may interact, not only a lecture mention.
- Transcript can support: The transcript can support that Attention For Scientific Fields is taught as a way to address this shortage: a local patch of a field may depend on faraway information, but looking everywhere can be expensive
- Transcript cannot support: The transcript cannot prove that Attention For Scientific Fields will work on every new case in large scientific fields where distant parts may interact; that has to be tested on the target quantity.
- Stronger validation needed: Run the idea on a changed case in large scientific fields where distant parts may interact and compare the predicted quantity with trusted measurements, trusted solves, or a known conservation check.
- First overclaim to reject: Reject any sentence saying Attention For Scientific Fields is generally reliable before it survives this test: windowing or scaling choices can miss long-range effects that matter for the scientific quantity being predicted
- Reviewer action: Start from the selected source anchors, then ask whether the page's claim is no wider than this hidden need: which distant parts matter for the local prediction
- Packet: evidence-packets/attention-for-scientific-fields.html


## Selected Source Anchors

### Deep Learning
- Source: ETH Zurich AISE 2025: Lecture 2 Introduction to Deep Learning
- Page: videos/eth-aise-2025-002-eth-zrich-aise-2025-lecture-2-introduction-to-deep-learning.html
- Claim anchored: Deep learning is the course foundation for fitting flexible models from examples before adding scientific constraints.
- Why this source: This is the 2025 introduction to deep learning in the local transcript set.
- Transcript excerpt to inspect: stopped in the last lecture are neural networks because this is sort of the key point or the key sort of foundation
- Limit: The source anchors the basic model-fitting foundation; it does not prove a fitted model carries the scientific quantity needed in a new domain.

- Source: ETH Zurich AISE 2024: Introduction to Deep Learning Part 1
- Page: videos/eth-aise-2024-002-eth-zrich-aise-introduction-to-deep-learning-part-1.html
- Claim anchored: The 2024 deep-learning introduction anchors the shared vocabulary used before PINNs, operators, surrogates, and generative models.
- Why this source: This lecture starts the 2024 deep-learning block that later methods build on.
- Transcript excerpt to inspect: going to be covering an introduction to deep learning and so this is uh the first part of two lectures on this
- Limit: The source supports the prerequisite role of deep learning; every later scientific claim still needs its own domain and changed-case test.


### Physics Informed Neural Networks
- Source: ETH Zurich AISE 2025: Lecture 3 Physics-Informed Neural Networks Introduction
- Page: videos/eth-aise-2025-003-eth-zrich-aise-2025-lecture-3-physics-informed-neural-networks-introduction.html
- Claim anchored: PINNs are introduced as learned fields checked against both measured data and physical equations.
- Why this source: This is the 2025 introductory PINNs lecture in the local transcript set.
- Transcript excerpt to inspect: which is that we want to learn physics modeled by PTE from data using neural networks So these are the four sort
- Limit: The source supports the course placement and core idea; it does not prove performance on every PDE or boundary setting.

- Source: ETH Zurich AISE 2025: Lecture 4 PINNs Theoretical Insights
- Page: videos/eth-aise-2025-004-eth-zrich-aise-2025-lecture-4-pinns-theoretical-insights.html
- Claim anchored: PINNs need theory and failure checks because satisfying a written training score is not the same as proving the field is right everywhere.
- Why this source: This lecture is the 2025 theory follow-up for PINNs.
- Transcript excerpt to inspect: is good news right that we have a theory which tries to explain that if you have a small training error the
- Limit: The source anchors the need for theoretical care; the page still needs task-specific validation for any scientific claim.


### Partial Differential Equations
- Source: ETH Zurich AISE 2024: Importance of PDEs in Science
- Page: videos/eth-aise-2024-004-eth-zrich-aise-importance-of-pdes-in-science.html
- Claim anchored: PDEs are the field language for quantities that change across space and time.
- Why this source: This lecture is the local source focused on why PDEs matter in scientific settings.
- Transcript excerpt to inspect: how things change right how things change in time is given by the temporal derivative how things change in space is given
- Limit: The source anchors why PDEs matter; it does not solve any particular PDE or validate a learned approximation.

- Source: ETH Zurich AISE 2025: Lecture 3 Physics-Informed Neural Networks Introduction
- Page: videos/eth-aise-2025-003-eth-zrich-aise-2025-lecture-3-physics-informed-neural-networks-introduction.html
- Claim anchored: PINN lectures depend on PDE residuals because the equation is used as a check on the learned field.
- Why this source: This lecture places differential equations inside the physics-informed learning route.
- Transcript excerpt to inspect: what I have written down here So can neural networks this is our main objective Can they be used to solve PTE
- Limit: The source supports PDEs as a constraint source; it does not prove the equation is complete for every experiment.


### Operator Learning
- Source: ETH Zurich AISE 2025: Lecture 5 Operator Learning Introduction
- Page: videos/eth-aise-2025-005-eth-zrich-aise-2025-lecture-5-operator-learning-introduction.html
- Claim anchored: Operator learning is about learning maps from whole input fields or functions to whole output fields or functions.
- Why this source: This is the 2025 introduction to the operator-learning block.
- Transcript excerpt to inspect: and it moves things from the input space to the output space Why is it an operator It's an operator because this
- Limit: The source supports the object being learned; it does not prove the learned map works outside the named input family.

- Source: ETH Zurich AISE 2025: Lecture 6 Operator Learning FNO
- Page: videos/eth-aise-2025-006-eth-zrich-aise-2025-lecture-6-operator-learning-fno.html
- Claim anchored: Fourier neural operators are one route for learning field-to-field maps in PDE settings.
- Why this source: This lecture is the 2025 FNO treatment inside the operator-learning sequence.
- Transcript excerpt to inspect: essentially just like neural networks are universal oper universal approximators of functions neural operators particularly fia neural operator is a universal approximator
- Limit: The source anchors the method family; reliability still depends on the training range, resolution, geometry, and target quantity.


### Scientific Machine Learning
- Source: ETH Zurich AISE 2025: Lecture 1 Course Introduction
- Page: videos/eth-aise-2025-001-eth-zrich-aise-2025-lecture-1-course-introduction.html
- Claim anchored: Scientific machine learning combines learned models with scientific quantities, equations, and validation checks.
- Why this source: This lecture introduces the 2025 course scope: AI in science and engineering.
- Transcript excerpt to inspect: some natural phenomena to find the differential equations for processes that produce the phenomena So this has been what Newton introduced with
- Limit: The source anchors the course-level field framing; it does not prove any one method works for a specific scientific job.

- Source: ETH Zurich AISE 2024: Course Introduction
- Page: videos/eth-aise-2024-001-eth-zrich-aise-course-introduction.html
- Claim anchored: The 2024 course introduction anchors the broad route from AI methods to science and engineering applications.
- Why this source: This is the 2024 starting point for the local playlist family.
- Transcript excerpt to inspect: Okay good morning everyone Welcome to the first lecture of AI in the science and engineering My name is Sid Mishra and
- Limit: The source supports the field-level map; task-level claims still need evidence, domain limits, and changed-case tests.


### Surrogate Modeling
- Source: ETH Zurich AISE 2024: Introduction to Hybrid Workflows Part 1
- Page: videos/eth-aise-2024-019-eth-zrich-aise-introduction-to-hybrid-workflows-part-1.html
- Claim anchored: Surrogates are useful when repeated scientific choices need answers faster than a trusted simulation or experiment can provide them.
- Why this source: This lecture starts the local hybrid-workflow block where learned components are placed next to trusted scientific tools.
- Transcript excerpt to inspect: can be very expensive but once you've trained your operator these are often orders of magnitude faster than traditional simulation it's what
- Limit: The source supports the need for faster learned components; it does not prove a surrogate is valid outside checked cases.

- Source: ETH Zurich AISE 2024: Introduction to Hybrid Workflows Part 2
- Page: videos/eth-aise-2024-020-eth-zrich-aise-introduction-to-hybrid-workflows-part-2.html
- Claim anchored: A learned stand-in remains tied to the trusted source and must be checked where it will be used.
- Why this source: This lecture continues the hybrid-workflow treatment in the local transcript set.
- Transcript excerpt to inspect: up methods that we've talked about Okay so I'm going to move on to now the second part of hybrid workflows Um
- Limit: The source supports the review route; task-level error checks are still needed before using any stand-in for a decision.


### Uncertainty And Generalization
- Source: ETH Zurich AISE 2024: Windowed Attention and Scaling Laws
- Page: videos/eth-aise-2024-018-eth-zrich-aise-windowed-attention-and-scaling-laws.html
- Claim anchored: Trust depends on changed-case behavior, not only on matching familiar examples.
- Why this source: This source sits in the sequence where model behavior is discussed beyond a single training case.
- Transcript excerpt to inspect: of the basic idea here and now you can imagine that uh attention is only happening at the level of the windows
- Limit: The source anchors the need to discuss scale and changed behavior; it does not certify uncertainty estimates for a specific domain.

- Source: ETH Zurich AISE 2025: Lecture 12 Foundation Models for PDEs Poseidon
- Page: videos/eth-aise-2025-012-eth-zrich-aise-2025-lecture-12-foundation-models-for-pdes-poseidon.html
- Claim anchored: Foundation and operator-style PDE models need evaluation on held-out scientific cases before broad use.
- Why this source: This lecture anchors the broad PDE-model part of the 2025 playlist.
- Transcript excerpt to inspect: are millions of books right which are of different types for instance So now uh each time you need the PDEs and
- Limit: The source supports the need for held-out case checks; it does not prove broad transfer for every equation family.


### Optimization For Learning
- Source: ETH Zurich AISE 2024: Introduction to Deep Learning Part 2
- Page: videos/eth-aise-2024-003-eth-zrich-aise-introduction-to-deep-learning-part-2.html
- Claim anchored: Optimization is the mechanism that turns a written training objective into model settings.
- Why this source: This lecture continues the deep-learning setup where training and fitting are introduced.
- Transcript excerpt to inspect: so the first introduction to deep learning um and my take-home message for you that I try to impress on you is
- Limit: The source anchors optimization as training machinery; it does not prove the optimized score matches the scientific decision.

- Source: ETH Zurich AISE 2025: Lecture 3 Physics-Informed Neural Networks Introduction
- Page: videos/eth-aise-2025-003-eth-zrich-aise-2025-lecture-3-physics-informed-neural-networks-introduction.html
- Claim anchored: PINNs make the optimization burden visible because data, equation, and boundary errors are trained together.
- Why this source: This lecture anchors an example where the loss contains multiple scientific burdens.
- Transcript excerpt to inspect: which is that we want to learn physics modeled by PTE from data using neural networks So these are the four sort
- Limit: The source supports the need to inspect loss terms; it does not guarantee that optimizing those terms finds the right physical field.


### Generative Modeling
- Source: ETH Zurich AISE 2025: Lecture 11 Generative Models for PDEs GenCFD
- Page: videos/eth-aise-2025-011-eth-zrich-aise-2025-lecture-11-generative-models-for-pdes-gencfd.html
- Claim anchored: Generative models for PDEs are used when the task needs possible scientific fields, not only one predicted field.
- Why this source: This is the 2025 lecture dedicated to generative models for PDEs in the local source set.
- Transcript excerpt to inspect: that you should try to make the gradients as close to one as possible because when you put different layers together powers
- Limit: The source anchors the generative-model topic; generated fields still need conservation, constraint, and downstream-use checks.

- Source: ETH Zurich AISE 2024: Introduction to Diffusion Models
- Page: videos/eth-aise-2024-022-eth-zrich-aise-introduction-to-diffusion-models.html
- Claim anchored: Diffusion models are a neighboring generative route for creating samples rather than a single deterministic answer.
- Why this source: This lecture provides the 2024 generative-model background in the local transcript set.
- Transcript excerpt to inspect: the generative model that's doing the best so far or is the most popular at the moment are these diffusion models um
- Limit: The source supports the generative route; it does not prove samples are valid scientific objects without domain checks.


### Graphs And Geometric Learning
- Source: ETH Zurich AISE 2025: Lecture 9 Operator Learning Graph-based Models
- Page: videos/eth-aise-2025-009-eth-zrich-aise-2025-lecture-9-operator-learning-graph-based-models.html
- Claim anchored: Graph-based operator models keep connections visible when scientific data live on meshes, graphs, or irregular geometry.
- Why this source: This lecture is the 2025 graph-based operator-learning treatment.
- Transcript excerpt to inspect: operators of PDS from data And to do that we are going to use operator learning and we have seen lots and
- Limit: The source anchors graph-based modeling; it does not prove the chosen graph contains every interaction that matters.

- Source: ETH Zurich AISE 2025: Lecture 13 AI in Chemistry Biology Part 1
- Page: videos/eth-aise-2025-013-eth-zrich-aise-2025-lecture-13-ai-in-chemistry-biology-part-1.html
- Claim anchored: Applications in chemistry and biology motivate graph and geometric representations because molecules and biological objects have structure.
- Why this source: This lecture anchors structured scientific objects in chemistry and biology applications.
- Transcript excerpt to inspect: as well and I will talk today about some applications of AI in chemistry and biology Um this is a super dynamic
- Limit: The source supports the domain motivation; property prediction still needs changed-molecule and held-out-family checks.


### Neural Differential Equations
- Source: ETH Zurich AISE 2024: Neural Differential Equations
- Page: videos/eth-aise-2024-021-eth-zrich-aise-neural-differential-equations.html
- Claim anchored: Neural differential equations learn or include a change rule inside a time-evolution calculation.
- Why this source: This is the local lecture dedicated to neural differential equations.
- Transcript excerpt to inspect: can actually just use neural differential equations to solve machine learning tasks rather than just to learn these underlying dynamics We can
- Limit: The source anchors the concept; long-time behavior and changed initial conditions still need separate validation.

- Source: ETH Zurich AISE 2024: Symbolic Regression and Model Discovery
- Page: videos/eth-aise-2024-024-eth-zrich-aise-symbolic-regression-and-model-discovery.html
- Claim anchored: Model discovery and symbolic regression are neighboring ideas when the goal is to recover a readable or testable change rule.
- Why this source: This lecture anchors the related model-discovery route.
- Transcript excerpt to inspect: guest lectures next week and so what we're going to talk about is um symbolic regression and model Discovery uh
- Limit: The source supports the connection; it does not prove a learned differential equation is stable or physically complete.


### Symbolic Regression
- Source: ETH Zurich AISE 2024: Symbolic Regression and Model Discovery
- Page: videos/eth-aise-2024-024-eth-zrich-aise-symbolic-regression-and-model-discovery.html
- Claim anchored: Symbolic regression aims for a readable candidate law, rather than only a fitted prediction.
- Why this source: This is the local lecture dedicated to symbolic regression and model discovery.
- Transcript excerpt to inspect: guest lectures next week and so what we're going to talk about is um symbolic regression and model Discovery uh
- Limit: The source supports the concept and goal; a discovered law still needs a new-experiment test and measured variables that cover the real cause.

- Source: ETH Zurich AISE 2024: Neural Differential Equations
- Page: videos/eth-aise-2024-021-eth-zrich-aise-neural-differential-equations.html
- Claim anchored: Neural differential equations are a related route when the unknown object is the rate or rule of change.
- Why this source: This lecture anchors the neighboring model-discovery route in the source set.
- Transcript excerpt to inspect: time when you solve the differential equation Cool So uh summary of neural differential equations So this is the key idea Use
- Limit: The source supports the relation between learned dynamics and model discovery; it does not prove interpretability by itself.


### Foundation Models For Pdes
- Source: ETH Zurich AISE 2025: Lecture 12 Foundation Models for PDEs Poseidon
- Page: videos/eth-aise-2025-012-eth-zrich-aise-2025-lecture-12-foundation-models-for-pdes-poseidon.html
- Claim anchored: Foundation PDE models try to carry structure from many PDE tasks into a new PDE case.
- Why this source: This lecture is the 2025 source page for foundation models for PDEs.
- Transcript excerpt to inspect: foundation model what you do for down for downstream tasks or fine-tuning FT so you zero which is from the
- Limit: The source anchors the ambition and lecture treatment; the page must still state which new PDE case was held out and what failed.

- Source: ETH Zurich AISE 2025: Lecture 5 Operator Learning Introduction
- Page: videos/eth-aise-2025-005-eth-zrich-aise-2025-lecture-5-operator-learning-introduction.html
- Claim anchored: Broad PDE models build on operator-learning ideas because both care about maps between fields across many cases.
- Why this source: This lecture anchors the operator-learning prerequisite for later broad PDE models.
- Transcript excerpt to inspect: So when an operator is ill or a matrix is ill conditioned then you have to do something called preconditioning and many
- Limit: The source supports the dependency; it does not imply that a broad model works on every PDE family.


### Attention For Scientific Fields
- Source: ETH Zurich AISE 2024: Attention as a Neural Operator
- Page: videos/eth-aise-2024-017-eth-zrich-aise-attention-as-a-neural-operator.html
- Claim anchored: Attention is treated as a neural-operator route for moving information across scientific fields.
- Why this source: This lecture directly connects attention to neural operators in the 2024 source set.
- Transcript excerpt to inspect: the last lecture was to use Transformers so let me use this so use Transformers to do operator learning right so I'm
- Limit: The source anchors the attention-as-operator idea; the chosen attention pattern still needs checks for missed long-range effects.

- Source: ETH Zurich AISE 2024: Windowed Attention and Scaling Laws
- Page: videos/eth-aise-2024-018-eth-zrich-aise-windowed-attention-and-scaling-laws.html
- Claim anchored: Windowed attention and scaling choices matter because field models must decide which distant information is worth carrying.
- Why this source: This lecture follows the attention-as-operator treatment and focuses on windowing and scaling.
- Transcript excerpt to inspect: the risk now is that all this nice things about attention This Global mixing This Global Information propagation that goes out of
- Limit: The source supports the design pressure; it does not prove a specific window or attention pattern preserves the scientific quantity.


## Editorial Quality Rubric
### First Principles
- Standard: The page starts from the real problem, observed evidence, hidden quantity, and scientific job before naming a method.
- Strong page: A reader can say what exists in the world, what is measured, what is missing, and why the method is needed.
- Weak page: The page starts by naming a method and assumes the reader already knows why it matters.
- Check: Look for sections that name the common problem, domain, observed quantity, hidden quantity, and changed-case test.
- Forbidden shortcut: Do not open with a method name as if the problem is already obvious.
- Replacement test: The first paragraph must let a reader fill in: the world has ___, we observe ___, we need ___, so the method must carry ___.

### Plain Language
- Standard: The page translates technical terms into everyday meaning without hiding the mathematical idea.
- Strong page: Terms such as field, residual, operator, loss, and generalization are tied to concrete jobs.
- Weak page: The page uses method names, benchmark language, or vague praise instead of explaining the idea.
- Check: Look for glossary links, everyday anchors, concrete domain stories, and plain formulas.
- Forbidden shortcut: Do not use restricted praise words from the wording scan as a substitute for explanation.
- Replacement test: Replace each praise word with the quantity it helps carry, the evidence it uses, and the failure case it still cannot rule out.

### Domain Grounding
- Standard: The page says where the concept matters in science or engineering and what quantity is being predicted or explained.
- Strong page: The domain, real quantity, and domain-specific failure test are visible.
- Weak page: The page describes a general model but never says what scientific object or quantity it serves.
- Check: Look for domain guide links, worked examples, and concrete anchor pages.
- Forbidden shortcut: Do not say a method is useful in science without naming the scientific quantity and the decision that uses it.
- Replacement test: The page must name the domain object, the measured evidence, the hidden quantity, and the changed domain case that would reject the claim.

### Failure Boundary
- Standard: The page states what the concept does not prove and what changed case could reject the claim.
- Strong page: A reader sees the use range, red flags, and first failure test.
- Weak page: The page says the method works without stating where it breaks.
- Check: Look for failure boundary, red flags, reader checks, and decision guide evidence requirements.
- Forbidden shortcut: Do not end with confidence, accuracy, or usefulness without a rejection test.
- Replacement test: The page must say: trust this only inside ___, and reject it first when ___ changes.

### Evidence Discipline
- Standard: The page separates transcript support from scientific proof.
- Strong page: Transcript evidence is shown as support that a concept appears, while validation claims require explicit tests.
- Weak page: The page treats a lecture mention as proof that a method works broadly.
- Check: Look for transcript evidence, support type, and explicit evidence limits.
- Forbidden shortcut: Do not treat a source mention as proof that a method works on a new scientific case.
- Replacement test: Every source-backed claim must state what the transcript supports and what experiment, solve, or changed case would still be needed.

### Connected Map
- Standard: The page connects the concept to nearby concepts, families, diagrams, decisions, or checks.
- Strong page: A reader can move from the concept to a route, comparison, diagram, or decision case.
- Weak page: The page is isolated and does not show how the idea fits into the field.
- Check: Look for concept links, families, comparisons, visual maps, and coverage matrix entries.
- Forbidden shortcut: Do not leave a concept as a standalone definition.
- Replacement test: The page must point to at least one prerequisite, one neighboring method choice, one example, and one check that could reject the claim.


## Wording Audit
- See `site/wording-audit.html` for hard-stop terms, review terms, current page hits, and replacement tests.

## Plain Essay Review
- See `site/plain-essay-review.html` for teacher-facing checks that each long topic essay starts from an everyday need, follows first principles, explains topology or shape, names field uses, and ends with a changed-case test.

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

### Verified Project State
- Remote repository exists at https://github.com/mehtama1234/physics-informed-machine-learning-concepts-research.git.
- Local main is configured to track origin/main.
- The package has 40 transcript-backed video pages, 14 concept pages, and the generated review layers listed below.
- Before calling any later pass finished, compare local main with origin/main and verify the GitHub Actions result for the current commit.

### Remaining Editorial Work
- Replace selected source anchors with manually verified short lecture quotes where a page needs stronger evidence than the selected transcript excerpt.
- Optionally replace generated sketch cards with hand-drawn figures if a page needs spatial detail beyond input, output, kept rule, and failure case.
- Keep future commits tied to the first-principles standard: real quantity, observed evidence, hidden quantity, mathematical move, domain use, failure test.
- After any later content change, run git push, make remote-check, and make ci-check before handing the repo to another reviewer.

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
- Wording Audit: wording-audit.html | Which words still need a reviewer to confirm they carry evidence, quantity, domain, and failure test?
- Provenance: provenance.html | Could another CLI rebuild this package from the same sources?
- Cross-Channel Playbook: provenance/cross-channel-playbook.html | What exact source, concept, evidence, page, and validation steps should the next build follow?

## Find Pages By Question

### I need the big picture first.
- Look for: central problem, field map, learning order, and completion state
- Open first: Completion Audit (completion-audit.html)
- Prove before moving on: The pages Completion Audit, Editorial Roadmap, Field Synthesis must answer this intent with central problem, field map, learning order, and completion state.
- Reject the route if: The route names pages but never reaches a source, quantity, formula shape, changed-case test, or acceptance check.
- Completion Audit: completion-audit.html
- Editorial Roadmap: editorial-roadmap.html
- Field Synthesis: synthesis.html
- Learning Path: learning-path.html
- Review Handoff: handoff.html

### I need to know the next serious goal.
- Look for: priorities, hand-written depth tasks, target pages, and acceptance checks
- Open first: Review Queue (review-queue.html)
- Prove before moving on: The pages Review Queue, Editorial Roadmap, Review Entrypoints must answer this intent with priorities, hand-written depth tasks, target pages, and acceptance checks.
- Reject the route if: The route names pages but never reaches a source, quantity, formula shape, changed-case test, or acceptance check.
- Review Queue: review-queue.html
- Editorial Roadmap: editorial-roadmap.html
- Review Entrypoints: review-entrypoints.html
- Quality Rubric: quality.html
- Core Derivations: derivations.html

### I need to understand a concept from first principles.
- Look for: problem, observed evidence, hidden quantity, formula shape, and failure test
- Open first: Topic Atlas (concept-atlas.html)
- Prove before moving on: The pages Topic Atlas, Concept Ladder, Dependency Map must answer this intent with problem, observed evidence, hidden quantity, formula shape, and failure test.
- Reject the route if: The route names pages but never reaches a source, quantity, formula shape, changed-case test, or acceptance check.
- Topic Atlas: concept-atlas.html
- Concept Ladder: concept-ladder.html
- Dependency Map: dependencies.html
- Formula Guide: formula-guide.html
- Misconception Map: misconceptions.html

### I need transcript support for a claim.
- Look for: source video, transcript excerpt, support limit, and review links
- Open first: Review Queue (review-queue.html)
- Prove before moving on: The pages Review Queue, Evidence Packets, Evidence Ledger must answer this intent with source video, transcript excerpt, support limit, and review links.
- Reject the route if: The route names pages but never reaches a source, quantity, formula shape, changed-case test, or acceptance check.
- Review Queue: review-queue.html
- Evidence Packets: evidence-packets.html
- Evidence Ledger: evidence-ledger.html
- Transcripts: transcripts.html
- Coverage Matrix: coverage.html

### I need to choose a method for a scientific job.
- Look for: domain, quantity, method route, use range, and required evidence
- Open first: Decision Guide (decision-guide.html)
- Prove before moving on: The pages Decision Guide, Domain Guides, Worked Examples must answer this intent with domain, quantity, method route, use range, and required evidence.
- Reject the route if: The route names pages but never reaches a source, quantity, formula shape, changed-case test, or acceptance check.
- Decision Guide: decision-guide.html
- Domain Guides: domains.html
- Worked Examples: worked-examples.html
- Comparisons: comparisons.html

### I need to audit quality.
- Look for: topic quality gates, forbidden shortcuts, replacement tests, failure boundary, evidence discipline, and connected map
- Open first: Topic Atlas (concept-atlas.html)
- Prove before moving on: The pages Topic Atlas, Quality Rubric, Reader Checks must answer this intent with topic quality gates, forbidden shortcuts, replacement tests, failure boundary, evidence discipline, and connected map.
- Reject the route if: The route names pages but never reaches a source, quantity, formula shape, changed-case test, or acceptance check.
- Topic Atlas: concept-atlas.html
- Quality Rubric: quality.html
- Reader Checks: reader-checks.html
- Misconception Map: misconceptions.html
- Completion Audit: completion-audit.html

### I need another CLI to reproduce this for a different channel.
- Look for: source capture, transcript extraction, analysis build, site generation, and review gates
- Open first: Cross-Channel Playbook (provenance/cross-channel-playbook.html)
- Prove before moving on: The pages Cross-Channel Playbook, CLI Reproduction Checklist, Transcript Extraction must answer this intent with source capture, transcript extraction, analysis build, site generation, and review gates.
- Reject the route if: The route names pages but never reaches a source, quantity, formula shape, changed-case test, or acceptance check.
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
- Present required parts: First Principles, Big Picture Claim Chain, End-To-End Use Protocol, Before The Math Slow Walk, Teach From Zero, Application Claim Ladder, Plain Question To Answer Script, Know And Still Test, Failure Consequence, Slow Problem Shape Bridge, Plain Big Picture Essay, Slow Importance Essay, Long Everyday Importance Essay, From Scratch Story, No-Jargon Translation, Plain Retell Drill, Field Transfer Check, Wrong Path Repair, Course Bridge, Use Or Refuse Gate, Final Learner Proof, Next-Day Memory Check, Nearby Topic Comparison, Math Shape Rehearsal, Source-To-Claim Boundary, Field Mini Cases, Hand Teaching Note, Case Walkthrough, Course Role, Concept Connections, Belief Evidence, Domain Fit, Shape Follows, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Reader Answer Parts, Say It Back Check, Misread Repair Drill, Plain-Language Audit, Acceptance Sentence
- Topic: topics/deep-learning.html
- Evidence packet: evidence-packets/deep-learning.html
- Reader check: reader-checks/deep-learning-check.html

### Physics-Informed Neural Networks
- Common problem: measurements may be sparse, but the answer must still respect a known physical equation
- Missing items: none
- Present required parts: First Principles, Big Picture Claim Chain, End-To-End Use Protocol, Before The Math Slow Walk, Teach From Zero, Application Claim Ladder, Plain Question To Answer Script, Know And Still Test, Failure Consequence, Slow Problem Shape Bridge, Plain Big Picture Essay, Slow Importance Essay, Long Everyday Importance Essay, From Scratch Story, No-Jargon Translation, Plain Retell Drill, Field Transfer Check, Wrong Path Repair, Course Bridge, Use Or Refuse Gate, Final Learner Proof, Next-Day Memory Check, Nearby Topic Comparison, Math Shape Rehearsal, Source-To-Claim Boundary, Field Mini Cases, Hand Teaching Note, Case Walkthrough, Course Role, Concept Connections, Belief Evidence, Domain Fit, Shape Follows, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Reader Answer Parts, Say It Back Check, Misread Repair Drill, Plain-Language Audit, Acceptance Sentence
- Topic: topics/physics-informed-neural-networks.html
- Evidence packet: evidence-packets/physics-informed-neural-networks.html
- Reader check: reader-checks/pinns-check.html

### Partial Differential Equations
- Common problem: a quantity changes over space and time, so one number is not enough to describe the situation
- Missing items: none
- Present required parts: First Principles, Big Picture Claim Chain, End-To-End Use Protocol, Before The Math Slow Walk, Teach From Zero, Application Claim Ladder, Plain Question To Answer Script, Know And Still Test, Failure Consequence, Slow Problem Shape Bridge, Plain Big Picture Essay, Slow Importance Essay, Long Everyday Importance Essay, From Scratch Story, No-Jargon Translation, Plain Retell Drill, Field Transfer Check, Wrong Path Repair, Course Bridge, Use Or Refuse Gate, Final Learner Proof, Next-Day Memory Check, Nearby Topic Comparison, Math Shape Rehearsal, Source-To-Claim Boundary, Field Mini Cases, Hand Teaching Note, Case Walkthrough, Course Role, Concept Connections, Belief Evidence, Domain Fit, Shape Follows, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Reader Answer Parts, Say It Back Check, Misread Repair Drill, Plain-Language Audit, Acceptance Sentence
- Topic: topics/partial-differential-equations.html
- Evidence packet: evidence-packets/partial-differential-equations.html
- Reader check: reader-checks/partial-differential-equations-check.html

### Operator Learning
- Common problem: one simulation answer is not enough when engineers need the whole map from inputs to solution fields
- Missing items: none
- Present required parts: First Principles, Big Picture Claim Chain, End-To-End Use Protocol, Before The Math Slow Walk, Teach From Zero, Application Claim Ladder, Plain Question To Answer Script, Know And Still Test, Failure Consequence, Slow Problem Shape Bridge, Plain Big Picture Essay, Slow Importance Essay, Long Everyday Importance Essay, From Scratch Story, No-Jargon Translation, Plain Retell Drill, Field Transfer Check, Wrong Path Repair, Course Bridge, Use Or Refuse Gate, Final Learner Proof, Next-Day Memory Check, Nearby Topic Comparison, Math Shape Rehearsal, Source-To-Claim Boundary, Field Mini Cases, Hand Teaching Note, Case Walkthrough, Course Role, Concept Connections, Belief Evidence, Domain Fit, Shape Follows, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Reader Answer Parts, Say It Back Check, Misread Repair Drill, Plain-Language Audit, Acceptance Sentence
- Topic: topics/operator-learning.html
- Evidence packet: evidence-packets/operator-learning.html
- Reader check: reader-checks/operator-learning-check.html

### Scientific Machine Learning
- Common problem: scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time
- Missing items: none
- Present required parts: First Principles, Big Picture Claim Chain, End-To-End Use Protocol, Before The Math Slow Walk, Teach From Zero, Application Claim Ladder, Plain Question To Answer Script, Know And Still Test, Failure Consequence, Slow Problem Shape Bridge, Plain Big Picture Essay, Slow Importance Essay, Long Everyday Importance Essay, From Scratch Story, No-Jargon Translation, Plain Retell Drill, Field Transfer Check, Wrong Path Repair, Course Bridge, Use Or Refuse Gate, Final Learner Proof, Next-Day Memory Check, Nearby Topic Comparison, Math Shape Rehearsal, Source-To-Claim Boundary, Field Mini Cases, Hand Teaching Note, Case Walkthrough, Course Role, Concept Connections, Belief Evidence, Domain Fit, Shape Follows, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Reader Answer Parts, Say It Back Check, Misread Repair Drill, Plain-Language Audit, Acceptance Sentence
- Topic: topics/scientific-machine-learning.html
- Evidence packet: evidence-packets/scientific-machine-learning.html
- Reader check: reader-checks/scientific-machine-learning-check.html

### Surrogate Modeling
- Common problem: a trusted simulator may be too slow to run for every design, control, or uncertainty question
- Missing items: none
- Present required parts: First Principles, Big Picture Claim Chain, End-To-End Use Protocol, Before The Math Slow Walk, Teach From Zero, Application Claim Ladder, Plain Question To Answer Script, Know And Still Test, Failure Consequence, Slow Problem Shape Bridge, Plain Big Picture Essay, Slow Importance Essay, Long Everyday Importance Essay, From Scratch Story, No-Jargon Translation, Plain Retell Drill, Field Transfer Check, Wrong Path Repair, Course Bridge, Use Or Refuse Gate, Final Learner Proof, Next-Day Memory Check, Nearby Topic Comparison, Math Shape Rehearsal, Source-To-Claim Boundary, Field Mini Cases, Hand Teaching Note, Case Walkthrough, Course Role, Concept Connections, Belief Evidence, Domain Fit, Shape Follows, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Reader Answer Parts, Say It Back Check, Misread Repair Drill, Plain-Language Audit, Acceptance Sentence
- Topic: topics/surrogate-modeling.html
- Evidence packet: evidence-packets/surrogate-modeling.html
- Reader check: reader-checks/surrogate-check.html

### Uncertainty And Generalization
- Common problem: a prediction is not enough unless the user knows when it should be believed
- Missing items: none
- Present required parts: First Principles, Big Picture Claim Chain, End-To-End Use Protocol, Before The Math Slow Walk, Teach From Zero, Application Claim Ladder, Plain Question To Answer Script, Know And Still Test, Failure Consequence, Slow Problem Shape Bridge, Plain Big Picture Essay, Slow Importance Essay, Long Everyday Importance Essay, From Scratch Story, No-Jargon Translation, Plain Retell Drill, Field Transfer Check, Wrong Path Repair, Course Bridge, Use Or Refuse Gate, Final Learner Proof, Next-Day Memory Check, Nearby Topic Comparison, Math Shape Rehearsal, Source-To-Claim Boundary, Field Mini Cases, Hand Teaching Note, Case Walkthrough, Course Role, Concept Connections, Belief Evidence, Domain Fit, Shape Follows, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Reader Answer Parts, Say It Back Check, Misread Repair Drill, Plain-Language Audit, Acceptance Sentence
- Topic: topics/uncertainty-and-generalization.html
- Evidence packet: evidence-packets/uncertainty-and-generalization.html
- Reader check: reader-checks/uncertainty-check.html

### Optimization For Learning
- Common problem: learning needs a way to decide which model settings are better or worse
- Missing items: none
- Present required parts: First Principles, Big Picture Claim Chain, End-To-End Use Protocol, Before The Math Slow Walk, Teach From Zero, Application Claim Ladder, Plain Question To Answer Script, Know And Still Test, Failure Consequence, Slow Problem Shape Bridge, Plain Big Picture Essay, Slow Importance Essay, Long Everyday Importance Essay, From Scratch Story, No-Jargon Translation, Plain Retell Drill, Field Transfer Check, Wrong Path Repair, Course Bridge, Use Or Refuse Gate, Final Learner Proof, Next-Day Memory Check, Nearby Topic Comparison, Math Shape Rehearsal, Source-To-Claim Boundary, Field Mini Cases, Hand Teaching Note, Case Walkthrough, Course Role, Concept Connections, Belief Evidence, Domain Fit, Shape Follows, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Reader Answer Parts, Say It Back Check, Misread Repair Drill, Plain-Language Audit, Acceptance Sentence
- Topic: topics/optimization-for-learning.html
- Evidence packet: evidence-packets/optimization-for-learning.html
- Reader check: reader-checks/optimization-for-learning-check.html

### Generative Modeling
- Common problem: some tasks need many possible examples, not one predicted answer
- Missing items: none
- Present required parts: First Principles, Big Picture Claim Chain, End-To-End Use Protocol, Before The Math Slow Walk, Teach From Zero, Application Claim Ladder, Plain Question To Answer Script, Know And Still Test, Failure Consequence, Slow Problem Shape Bridge, Plain Big Picture Essay, Slow Importance Essay, Long Everyday Importance Essay, From Scratch Story, No-Jargon Translation, Plain Retell Drill, Field Transfer Check, Wrong Path Repair, Course Bridge, Use Or Refuse Gate, Final Learner Proof, Next-Day Memory Check, Nearby Topic Comparison, Math Shape Rehearsal, Source-To-Claim Boundary, Field Mini Cases, Hand Teaching Note, Case Walkthrough, Course Role, Concept Connections, Belief Evidence, Domain Fit, Shape Follows, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Reader Answer Parts, Say It Back Check, Misread Repair Drill, Plain-Language Audit, Acceptance Sentence
- Topic: topics/generative-modeling.html
- Evidence packet: evidence-packets/generative-modeling.html
- Reader check: reader-checks/generative-modeling-check.html

### Graphs And Geometric Learning
- Common problem: many scientific objects are not simple rows of numbers; their connections matter
- Missing items: none
- Present required parts: First Principles, Big Picture Claim Chain, End-To-End Use Protocol, Before The Math Slow Walk, Teach From Zero, Application Claim Ladder, Plain Question To Answer Script, Know And Still Test, Failure Consequence, Slow Problem Shape Bridge, Plain Big Picture Essay, Slow Importance Essay, Long Everyday Importance Essay, From Scratch Story, No-Jargon Translation, Plain Retell Drill, Field Transfer Check, Wrong Path Repair, Course Bridge, Use Or Refuse Gate, Final Learner Proof, Next-Day Memory Check, Nearby Topic Comparison, Math Shape Rehearsal, Source-To-Claim Boundary, Field Mini Cases, Hand Teaching Note, Case Walkthrough, Course Role, Concept Connections, Belief Evidence, Domain Fit, Shape Follows, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Reader Answer Parts, Say It Back Check, Misread Repair Drill, Plain-Language Audit, Acceptance Sentence
- Topic: topics/graphs-and-geometric-learning.html
- Evidence packet: evidence-packets/graphs-and-geometric-learning.html
- Reader check: reader-checks/graphs-and-geometric-learning-check.html

### Neural Differential Equations
- Common problem: scientists may know that a system changes continuously but not know the exact rule for that change
- Missing items: none
- Present required parts: First Principles, Big Picture Claim Chain, End-To-End Use Protocol, Before The Math Slow Walk, Teach From Zero, Application Claim Ladder, Plain Question To Answer Script, Know And Still Test, Failure Consequence, Slow Problem Shape Bridge, Plain Big Picture Essay, Slow Importance Essay, Long Everyday Importance Essay, From Scratch Story, No-Jargon Translation, Plain Retell Drill, Field Transfer Check, Wrong Path Repair, Course Bridge, Use Or Refuse Gate, Final Learner Proof, Next-Day Memory Check, Nearby Topic Comparison, Math Shape Rehearsal, Source-To-Claim Boundary, Field Mini Cases, Hand Teaching Note, Case Walkthrough, Course Role, Concept Connections, Belief Evidence, Domain Fit, Shape Follows, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Reader Answer Parts, Say It Back Check, Misread Repair Drill, Plain-Language Audit, Acceptance Sentence
- Topic: topics/neural-differential-equations.html
- Evidence packet: evidence-packets/neural-differential-equations.html
- Reader check: reader-checks/neural-differential-equations-check.html

### Symbolic Regression And Model Discovery
- Common problem: a scientist may need a readable equation, not only a model that predicts well
- Missing items: none
- Present required parts: First Principles, Big Picture Claim Chain, End-To-End Use Protocol, Before The Math Slow Walk, Teach From Zero, Application Claim Ladder, Plain Question To Answer Script, Know And Still Test, Failure Consequence, Slow Problem Shape Bridge, Plain Big Picture Essay, Slow Importance Essay, Long Everyday Importance Essay, From Scratch Story, No-Jargon Translation, Plain Retell Drill, Field Transfer Check, Wrong Path Repair, Course Bridge, Use Or Refuse Gate, Final Learner Proof, Next-Day Memory Check, Nearby Topic Comparison, Math Shape Rehearsal, Source-To-Claim Boundary, Field Mini Cases, Hand Teaching Note, Case Walkthrough, Course Role, Concept Connections, Belief Evidence, Domain Fit, Shape Follows, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Reader Answer Parts, Say It Back Check, Misread Repair Drill, Plain-Language Audit, Acceptance Sentence
- Topic: topics/symbolic-regression.html
- Evidence packet: evidence-packets/symbolic-regression.html
- Reader check: reader-checks/symbolic-regression-check.html

### Foundation Models For PDEs
- Common problem: one trained model may be asked to handle many related equations, grids, parameters, or physical settings
- Missing items: none
- Present required parts: First Principles, Big Picture Claim Chain, End-To-End Use Protocol, Before The Math Slow Walk, Teach From Zero, Application Claim Ladder, Plain Question To Answer Script, Know And Still Test, Failure Consequence, Slow Problem Shape Bridge, Plain Big Picture Essay, Slow Importance Essay, Long Everyday Importance Essay, From Scratch Story, No-Jargon Translation, Plain Retell Drill, Field Transfer Check, Wrong Path Repair, Course Bridge, Use Or Refuse Gate, Final Learner Proof, Next-Day Memory Check, Nearby Topic Comparison, Math Shape Rehearsal, Source-To-Claim Boundary, Field Mini Cases, Hand Teaching Note, Case Walkthrough, Course Role, Concept Connections, Belief Evidence, Domain Fit, Shape Follows, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Reader Answer Parts, Say It Back Check, Misread Repair Drill, Plain-Language Audit, Acceptance Sentence
- Topic: topics/foundation-models-for-pdes.html
- Evidence packet: evidence-packets/foundation-models-for-pdes.html
- Reader check: reader-checks/foundation-pde-check.html

### Attention For Scientific Fields
- Common problem: a local patch of a field may depend on faraway information, but looking everywhere can be expensive
- Missing items: none
- Present required parts: First Principles, Big Picture Claim Chain, End-To-End Use Protocol, Before The Math Slow Walk, Teach From Zero, Application Claim Ladder, Plain Question To Answer Script, Know And Still Test, Failure Consequence, Slow Problem Shape Bridge, Plain Big Picture Essay, Slow Importance Essay, Long Everyday Importance Essay, From Scratch Story, No-Jargon Translation, Plain Retell Drill, Field Transfer Check, Wrong Path Repair, Course Bridge, Use Or Refuse Gate, Final Learner Proof, Next-Day Memory Check, Nearby Topic Comparison, Math Shape Rehearsal, Source-To-Claim Boundary, Field Mini Cases, Hand Teaching Note, Case Walkthrough, Course Role, Concept Connections, Belief Evidence, Domain Fit, Shape Follows, Formula Terms, Worked Example, Wrong-Use Example, Breaks Without Idea, Failure Boundary, Source Anchors, Reader Check, Reader Answer Parts, Say It Back Check, Misread Repair Drill, Plain-Language Audit, Acceptance Sentence
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
- Current evidence: Core topic pages and evidence packets include selected source anchors with claim, source page, reason, limit, concept-ranked transcript excerpts, and validation that rejects boilerplate lecture openings.
- Proof pages: topics/physics-informed-neural-networks.html, evidence-packets/foundation-models-for-pdes.html, evidence-packets/operator-learning.html, evidence-ledger.html
- Target pages: topics/physics-informed-neural-networks.html, topics/operator-learning.html, topics/uncertainty-and-generalization.html, topics/foundation-models-for-pdes.html, evidence-packets.html
- Work: Choose concept-specific transcript excerpts before generic course introductions.; Add a short source note beside each major claim: what the lecture supports, and what it does not settle.; Prefer concrete lecture moments over broad statements and reject boilerplate lecture openings.
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
- Current evidence: The diagrams index and core topic pages include six mathematical sketches with input, output, kept rule, and failure case, including symbolic regression and foundation PDE transfer.
- Proof pages: diagrams.html, topics/operator-learning.html, topics/symbolic-regression.html, topics/foundation-models-for-pdes.html
- Target pages: diagrams.html, topics/physics-informed-neural-networks.html, topics/operator-learning.html, topics/surrogate-modeling.html, topics/uncertainty-and-generalization.html, topics/symbolic-regression.html, topics/foundation-models-for-pdes.html
- Work: Add one sketch for measured points plus equation-check points.; Add one sketch for input field to output field.; Add one sketch for a fast surrogate inside repeated scientific choices.; Add one sketch for a shifted case where the model should admit doubt.; Add one sketch for measurements to a readable law.; Add one sketch for old PDE tasks to a new equation case.
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
- Evidence: topic pages embed Quality Gate Before Review tables and, with the concept ladder, glossary, derivations, quality rubric, and wording audit, require problem, domain, observed evidence, hidden quantity, formula shape, risky-word replacement tests, and failure test.

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
- Evidence: make check runs Python compile, build validation, and standalone generated-site validation; validator expects the manifest page count, wording audit page, and required sections.

### Create or verify the GitHub remote repository and push main.
- Status: locally verified
- Evidence: origin is configured at https://github.com/mehtama1234/physics-informed-machine-learning-concepts-research.git; main has been pushed and can be verified with git ls-remote --heads origin main.

### Run the generated-site checks in GitHub Actions for pushed commits.
- Status: locally verified
- Evidence: the check workflow runs make check on push and pull request; make ci-check verifies the current commit's workflow run through the GitHub Actions API.

