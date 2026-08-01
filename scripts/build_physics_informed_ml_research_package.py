#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import parse_qs, urlparse


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw-material"
ANALYSIS = ROOT / "analysis"
SITE = ROOT / "site"
EXPORTS = ROOT / "exports"


PLAYLISTS = [
    {
        "slug": "eth-aise-2025",
        "title": "ETH Zurich AI in the Sciences and Engineering 2025",
        "url": "https://www.youtube.com/playlist?list=PLJkYEExhe7rYBo2KBwsirSF-B0R3Q0nt7",
    },
    {
        "slug": "eth-aise-2024",
        "title": "ETH Zurich AI in the Sciences and Engineering 2024",
        "url": "https://www.youtube.com/playlist?list=PLJkYEExhe7rYFkBIB2U5pf_RWzYnFLj7r",
    },
]


CONCEPTS = [
    {
        "slug": "deep-learning",
        "name": "Deep Learning",
        "keywords": ["deep learning", "neural network", "neural networks", "backprop", "gradient descent"],
        "domain": "scientific prediction from large measured or simulated data sets",
        "problem": "scientists often have examples of behavior but no short rule that predicts the next case",
        "keeps": "many adjustable weights that turn inputs into predictions",
        "leaves_out": "a direct explanation of which physical reason caused each prediction",
        "why": "it can learn useful patterns when hand-written rules are incomplete, but the result still needs tests outside the examples used for fitting",
        "failure": "the model can fit familiar examples while failing on a new material, geometry, scale, or boundary condition",
    },
    {
        "slug": "physics-informed-neural-networks",
        "name": "Physics-Informed Neural Networks",
        "keywords": ["pinn", "pinns", "physics-informed", "physics informed", "residual", "collocation"],
        "domain": "differential equations in science and engineering",
        "problem": "measurements may be sparse, but the answer must still respect a known physical equation",
        "keeps": "a neural network prediction plus a penalty for violating the known equation",
        "leaves_out": "guaranteed accuracy when the equation, boundary data, or training points are poor",
        "why": "it lets known physics push the fit toward physically possible behavior instead of treating data points as the only evidence",
        "failure": "the equation penalty can look small while the solution is wrong in hard regions, sharp layers, or unseen boundary cases",
    },
    {
        "slug": "partial-differential-equations",
        "name": "Partial Differential Equations",
        "keywords": ["pde", "pdes", "differential equation", "partial differential", "boundary", "initial condition"],
        "domain": "fluids, heat, waves, mechanics, chemistry, climate, and other changing fields",
        "problem": "a quantity changes over space and time, so one number is not enough to describe the situation",
        "keeps": "a field, its rates of change, and the boundary or starting information needed to evolve it",
        "leaves_out": "unmodeled forces, unresolved scales, uncertain parameters, and numerical error",
        "why": "PDEs are the language many scientific models use before machine learning enters the story",
        "failure": "a learned shortcut can ignore boundary conditions or conservation behavior that the PDE was carrying",
    },
    {
        "slug": "operator-learning",
        "name": "Operator Learning",
        "keywords": ["operator learning", "deeponet", "fourier neural operator", "fno", "neural operator", "operator"],
        "domain": "fast prediction for families of scientific simulations",
        "problem": "one simulation answer is not enough when engineers need the whole map from inputs to solution fields",
        "keeps": "a learned map from a forcing, coefficient, shape, or starting field to a solution field",
        "leaves_out": "proof that the map works for resolutions, geometries, or physics outside the training family",
        "why": "it can replace many expensive solves with a fast approximation when the requested cases stay inside the tested family",
        "failure": "the learned map can give plausible-looking fields that violate the equation or fail on a shifted input family",
    },
    {
        "slug": "scientific-machine-learning",
        "name": "Scientific Machine Learning",
        "keywords": ["scientific machine learning", "sciML", "science", "engineering", "ai in the sciences"],
        "domain": "using data-driven models inside scientific workflows",
        "problem": "scientific work needs predictions that respect measurements, equations, uncertainty, and domain limits at the same time",
        "keeps": "data evidence, scientific structure, and validation against changed cases",
        "leaves_out": "the idea that a high score alone proves scientific understanding",
        "why": "it connects flexible prediction to the checks scientists already need: units, conservation, boundaries, uncertainty, and failure cases",
        "failure": "the method becomes a generic fitting tool if the physical quantity, scientific claim, and validation case are not named",
    },
    {
        "slug": "surrogate-modeling",
        "name": "Surrogate Modeling",
        "keywords": ["surrogate", "emulator", "reduced", "reduced order", "simulation", "solver"],
        "domain": "expensive simulation and design loops",
        "problem": "a trusted simulator may be too slow to run for every design, control, or uncertainty question",
        "keeps": "the input-output behavior needed for a specified family of queries",
        "leaves_out": "full simulation detail outside the tested query family",
        "why": "it makes repeated scientific decisions possible when full simulation cost would stop the workflow",
        "failure": "speed can hide missing physics when the surrogate is used beyond the regime where it was checked",
    },
    {
        "slug": "uncertainty-and-generalization",
        "name": "Uncertainty And Generalization",
        "keywords": ["uncertainty", "generalization", "error", "validation", "test", "out-of-distribution", "distribution"],
        "domain": "model use under new conditions",
        "problem": "a prediction is not enough unless the user knows when it should be believed",
        "keeps": "error checks, changed-case tests, and limits on where the model was trained",
        "leaves_out": "confidence in cases that were never tested",
        "why": "scientific models are used to make decisions, so the cost of being confidently wrong can be high",
        "failure": "training error can look good while the model fails under a new geometry, parameter range, sensor, or physical regime",
    },
    {
        "slug": "optimization-for-learning",
        "name": "Optimization For Learning",
        "keywords": ["optimization", "loss", "objective", "training", "gradient", "minimize"],
        "domain": "turning model fitting into a repeatable computation",
        "problem": "learning needs a way to decide which model settings are better or worse",
        "keeps": "a written score that compares model output against data, physics penalties, or design goals",
        "leaves_out": "everything the score forgot to penalize",
        "why": "the model only learns what the training score asks it to improve",
        "failure": "a model can optimize the written score while missing the scientific behavior the score failed to name",
    },
    {
        "slug": "generative-modeling",
        "name": "Generative Modeling",
        "keywords": ["generative", "diffusion", "score", "vae", "gan", "flow model"],
        "domain": "creating plausible scientific samples, fields, or candidate designs",
        "problem": "some tasks need many possible examples, not one predicted answer",
        "keeps": "a learned rule for sampling outputs that resemble the training family",
        "leaves_out": "a guarantee that each sample is physically valid or useful for a decision",
        "why": "it can explore candidate fields, shapes, or scenarios when direct enumeration is impossible",
        "failure": "generated samples can look realistic while breaking constraints, conservation, or rare-event behavior",
    },
    {
        "slug": "graphs-and-geometric-learning",
        "name": "Graphs And Geometric Learning",
        "keywords": ["graph", "gnn", "geometric", "mesh", "equivariant", "symmetry"],
        "domain": "systems made of interacting parts, meshes, molecules, or spatial relations",
        "problem": "many scientific objects are not simple rows of numbers; their connections matter",
        "keeps": "nodes, edges, spatial relations, and symmetry rules that should not change the answer",
        "leaves_out": "interactions or long-range effects not represented in the graph",
        "why": "it lets the model respect the structure of the object instead of flattening away important relations",
        "failure": "the graph can encode the wrong neighborhood, hide missing interactions, or fail when the mesh changes",
    },
    {
        "slug": "neural-differential-equations",
        "name": "Neural Differential Equations",
        "keywords": ["neural differential", "neural ode", "differential equation", "ode", "time integration"],
        "domain": "changing systems where time evolution is part of the model",
        "problem": "scientists may know that a system changes continuously but not know the exact rule for that change",
        "keeps": "a learned rate rule inside a time-stepping calculation",
        "leaves_out": "a guarantee that the learned rate respects hidden physics or long-time behavior",
        "why": "it lets learning focus on the missing change rule while the time update still carries the idea of continuous evolution",
        "failure": "small learned-rate errors can accumulate until long-time predictions drift away from the real system",
    },
    {
        "slug": "symbolic-regression",
        "name": "Symbolic Regression And Model Discovery",
        "keywords": ["symbolic regression", "model discovery", "equation discovery", "sparse", "formula"],
        "domain": "turning data into equations people can inspect",
        "problem": "a scientist may need a readable equation, not only a model that predicts well",
        "keeps": "candidate formulas that can be written, checked, and compared",
        "leaves_out": "terms that were not searched, variables that were not measured, and physics not excited by the data",
        "why": "a short equation can be tested, criticized, and reused more easily than a large fitted model",
        "failure": "a neat formula can fit the training data while using the wrong variables or failing on a changed experiment",
    },
    {
        "slug": "foundation-models-for-pdes",
        "name": "Foundation Models For PDEs",
        "keywords": ["foundation model", "foundation models", "poseidon", "large-scale", "scaling laws"],
        "domain": "broad families of PDE problems and scientific fields",
        "problem": "one trained model may be asked to handle many related equations, grids, parameters, or physical settings",
        "keeps": "shared structure across many scientific problem instances",
        "leaves_out": "certainty that shared training structure covers the new scientific case",
        "why": "a broad model could reduce repeated training cost if it keeps the physical features that matter across tasks",
        "failure": "the model can look broad while missing rare regimes, new boundary conditions, or quantities not represented in training",
    },
    {
        "slug": "attention-for-scientific-fields",
        "name": "Attention For Scientific Fields",
        "keywords": ["attention", "transformer", "transformers", "windowed attention"],
        "domain": "large scientific fields where distant parts may interact",
        "problem": "a local patch of a field may depend on faraway information, but looking everywhere can be expensive",
        "keeps": "selected interactions between parts of the input field",
        "leaves_out": "interactions the attention pattern never compares",
        "why": "it gives the model a way to move information across a field without treating every location as isolated",
        "failure": "windowing or scaling choices can miss long-range effects that matter for the scientific quantity being predicted",
    },
]


THEMES = [
    {
        "slug": "data-to-scientific-prediction",
        "name": "Data To Scientific Prediction",
        "problem": "The lectures repeatedly ask how examples become predictions that scientists can check.",
        "concepts": ["deep-learning", "scientific-machine-learning", "optimization-for-learning"],
    },
    {
        "slug": "physics-as-a-training-constraint",
        "name": "Physics As A Training Constraint",
        "problem": "The recurring pressure is that a learned model should not ignore equations, boundaries, or conservation behavior.",
        "concepts": ["physics-informed-neural-networks", "partial-differential-equations"],
    },
    {
        "slug": "fast-surrogates-for-expensive-solvers",
        "name": "Fast Surrogates For Expensive Solvers",
        "problem": "The practical need is to replace repeated expensive solves with checked approximations.",
        "concepts": ["operator-learning", "surrogate-modeling", "partial-differential-equations"],
    },
    {
        "slug": "trust-under-changed-conditions",
        "name": "Trust Under Changed Conditions",
        "problem": "The package must separate fitting familiar examples from earning belief on new scientific cases.",
        "concepts": ["uncertainty-and-generalization", "scientific-machine-learning", "generative-modeling"],
    },
    {
        "slug": "structure-in-scientific-objects",
        "name": "Structure In Scientific Objects",
        "problem": "Some scientific data carries geometry, connections, fields, or symmetries that a plain table would erase.",
        "concepts": ["graphs-and-geometric-learning", "operator-learning", "partial-differential-equations", "attention-for-scientific-fields"],
    },
    {
        "slug": "readable-laws-from-learned-models",
        "name": "Readable Laws From Learned Models",
        "problem": "The course also asks when learned behavior can be turned back into equations or mechanisms people can inspect.",
        "concepts": ["symbolic-regression", "neural-differential-equations", "optimization-for-learning"],
    },
    {
        "slug": "broad-models-for-many-scientific-tasks",
        "name": "Broad Models For Many Scientific Tasks",
        "problem": "The newest lectures ask whether one model can carry shared structure across many PDE or scientific tasks.",
        "concepts": ["foundation-models-for-pdes", "operator-learning", "uncertainty-and-generalization"],
    },
]


CONCEPT_DEPENDENCIES = [
    {
        "concept": "physics-informed-neural-networks",
        "depends_on": ["partial-differential-equations", "deep-learning", "optimization-for-learning"],
        "why": "A PINN combines a fitted neural network, a differential equation check, and a training score.",
        "confusion_prevented": "Without the dependencies, a reader may think a PINN is just a neural network with physics language attached.",
    },
    {
        "concept": "operator-learning",
        "depends_on": ["partial-differential-equations", "deep-learning", "surrogate-modeling"],
        "why": "Operator learning makes sense when the job is a fast map between full fields across many related solves.",
        "confusion_prevented": "Without fields and surrogates, a reader may mistake it for one more predictor on a table.",
    },
    {
        "concept": "surrogate-modeling",
        "depends_on": ["deep-learning", "uncertainty-and-generalization"],
        "why": "A surrogate is useful only when its repeated query family and tested use range are named.",
        "confusion_prevented": "Without uncertainty, speed can be mistaken for scientific trust.",
    },
    {
        "concept": "uncertainty-and-generalization",
        "depends_on": ["deep-learning", "scientific-machine-learning"],
        "why": "Uncertainty and generalization ask whether fitted behavior survives a changed scientific case.",
        "confusion_prevented": "Without the scientific job, uncertainty can look like a decorative confidence number.",
    },
    {
        "concept": "neural-differential-equations",
        "depends_on": ["partial-differential-equations", "deep-learning", "optimization-for-learning"],
        "why": "The learned part is a rate or missing change rule placed inside a time-evolution calculation.",
        "confusion_prevented": "Without differential equations, a reader may miss why small rate errors can accumulate over time.",
    },
    {
        "concept": "symbolic-regression",
        "depends_on": ["optimization-for-learning", "uncertainty-and-generalization"],
        "why": "Symbolic regression searches for a readable rule, then needs changed-case tests to reject neat but wrong formulas.",
        "confusion_prevented": "Without changed-case testing, a compact equation can be mistaken for truth.",
    },
    {
        "concept": "graphs-and-geometric-learning",
        "depends_on": ["deep-learning", "scientific-machine-learning"],
        "why": "Geometric learning keeps connections, shapes, and symmetries visible inside learned prediction.",
        "confusion_prevented": "Without the scientific object, graph structure can look like a modeling fashion rather than required information.",
    },
    {
        "concept": "attention-for-scientific-fields",
        "depends_on": ["operator-learning", "graphs-and-geometric-learning"],
        "why": "Attention is a way to move selected information across large fields or connected objects.",
        "confusion_prevented": "Without fields and connections, attention can be misread as proof that all important interactions were captured.",
    },
    {
        "concept": "generative-modeling",
        "depends_on": ["deep-learning", "uncertainty-and-generalization"],
        "why": "Generated scientific samples need checks for validity, rarity, and downstream use.",
        "confusion_prevented": "Without validation, plausible samples can be mistaken for physically useful samples.",
    },
    {
        "concept": "foundation-models-for-pdes",
        "depends_on": ["operator-learning", "partial-differential-equations", "uncertainty-and-generalization"],
        "why": "Broad PDE models depend on field-to-field maps, equation families, and tests on held-out task families.",
        "confusion_prevented": "Without these dependencies, scale can be mistaken for coverage of a new scientific case.",
    },
]


FAMILY_PAGES = [
    {
        "slug": "physics-constraints-family",
        "title": "Physics Constraints Family",
        "central_problem": "You have some observations, but the answer must also obey a rule scientists already trust.",
        "domain": "heat flow, fluids, waves, elasticity, reaction systems, and other systems described by differential equations",
        "concepts": ["partial-differential-equations", "physics-informed-neural-networks", "optimization-for-learning", "uncertainty-and-generalization"],
        "plain_route": [
            "Start with a quantity that changes across space or time.",
            "Write the rule that says how the quantity is allowed to change.",
            "Fit the unknown field to the measured values.",
            "Also check whether the fitted field breaks the rule between measured values.",
            "Test a changed boundary, changed source, or changed scale before trusting the result.",
        ],
        "what_the_math_buys": "The equation turns empty space between measurements into a checkable demand. The model cannot claim success only by touching the measured points.",
        "failure_boundary": "This family fails when the written equation is incomplete, the boundary information is wrong, or the training process avoids the hard regions where the rule matters most.",
    },
    {
        "slug": "neural-operators-family",
        "title": "Neural Operators Family",
        "central_problem": "One solved simulation is not enough; the scientific job needs the map from many inputs to many full fields.",
        "domain": "repeated PDE solves, design sweeps, weather-like fields, fluids, materials, and parameter studies",
        "concepts": ["operator-learning", "surrogate-modeling", "attention-for-scientific-fields", "foundation-models-for-pdes"],
        "plain_route": [
            "Start with many examples of input fields and output fields.",
            "Name the family: which equations, boundaries, geometries, grids, and parameter ranges are included.",
            "Learn the map from a new input field to a new output field.",
            "Use structure such as frequency, graph connections, or attention when the field needs it.",
            "Reject broad claims unless the model survives new cases from the intended family.",
        ],
        "what_the_math_buys": "The object being learned is a map between functions. That matters because a field is not a single row of numbers; it is a whole spatial object.",
        "failure_boundary": "This family fails when the new query is outside the learned family, when resolution changes reveal hidden errors, or when the output looks smooth but breaks the physical claim.",
    },
    {
        "slug": "model-discovery-family",
        "title": "Model Discovery Family",
        "central_problem": "Prediction alone is not enough when the scientist needs a readable law or missing change rule.",
        "domain": "mechanism discovery, dynamics, lab measurements, simplified physical laws, and interpretable scientific modeling",
        "concepts": ["symbolic-regression", "neural-differential-equations", "scientific-machine-learning", "optimization-for-learning"],
        "plain_route": [
            "Start with measurements of a system changing.",
            "Decide which quantities could explain that change.",
            "Search for a short rule or learn the missing rate rule.",
            "Check whether the rule predicts a changed experiment.",
            "Keep the rule only if it is both useful and honest about what was not measured.",
        ],
        "what_the_math_buys": "A compact equation is easier to inspect, criticize, and reuse than a large fitted object. The math turns a fit into a candidate explanation.",
        "failure_boundary": "This family fails when the needed variable was not measured, the experiment did not excite the important behavior, or the search space cannot express the true rule.",
    },
    {
        "slug": "scientific-surrogates-family",
        "title": "Scientific Surrogates Family",
        "central_problem": "The trusted simulator is too slow for repeated decisions, but a fast answer is dangerous if nobody states where it is valid.",
        "domain": "engineering design, uncertainty sweeps, control loops, inverse problems, and expensive simulation workflows",
        "concepts": ["surrogate-modeling", "deep-learning", "operator-learning", "uncertainty-and-generalization"],
        "plain_route": [
            "Start with an expensive solver or experiment.",
            "Name the repeated questions people need to ask.",
            "Train a cheaper stand-in only for those questions.",
            "Compare against the trusted source near the edge of intended use.",
            "Report the use range with the answer, not after the answer.",
        ],
        "what_the_math_buys": "The approximation becomes useful only after the input family, output quantity, error measure, and rejected cases are named.",
        "failure_boundary": "This family fails when speed hides missing physics, when users ask new questions the surrogate was not trained for, or when uncertainty is treated as decoration.",
    },
]


COMPARISON_PAGES = [
    {
        "slug": "pinns-vs-neural-operators",
        "title": "PINNs vs Neural Operators",
        "left": "Physics-informed neural networks",
        "right": "Neural operators",
        "shared_problem": "Both try to predict scientific fields without ignoring the physics that makes those fields meaningful.",
        "left_when": "Use this side when you have one problem instance, sparse data, and a known equation you want the fitted field to obey.",
        "right_when": "Use this side when you have many solved examples and need a fast map from new problem inputs to full solution fields.",
        "left_case": "A wall has a few temperature sensors and a trusted heat equation. Use a PINN to fit one temperature field while checking data, equation, and boundary errors.",
        "right_case": "A lab has thousands of solved heat-flow cases for many source fields. Use an operator model to learn the input-field to solution-field map.",
        "wrong_choice_case": "Using an operator model from one family on a boundary type it never saw, or using a PINN when the real need is thousands of fast repeated solves.",
        "evidence_that_exposes_it": "Hold out a changed boundary or input-field family and compare the full field and the scientific quantity, not only visual similarity.",
        "key_difference": "A PINN usually learns one field while being punished for breaking an equation. A neural operator learns the input-to-solution map for a named family of fields.",
        "wrong_turn": "Do not use either word as a badge of trust. Ask what changed case was tested.",
    },
    {
        "slug": "solvers-vs-learned-surrogates",
        "title": "Solvers vs Learned Surrogates",
        "left": "Trusted numerical solvers",
        "right": "Learned surrogates",
        "shared_problem": "Both produce answers for scientific or engineering questions.",
        "left_when": "Use this side when correctness, conservation, and known numerical behavior matter more than speed.",
        "right_when": "Use this side when many repeated queries make the full solver too costly and the query family is narrow enough to test.",
        "left_case": "A safety decision depends on a stress peak near a crack. Use the trusted solver because the local failure quantity matters more than speed.",
        "right_case": "A design team needs to screen thousands of similar wing shapes before choosing a few expensive solver runs. Use a surrogate inside that named shape family.",
        "wrong_choice_case": "Replacing the solver everywhere because the surrogate is fast, including edge cases where no solver comparison exists.",
        "evidence_that_exposes_it": "Compare against the solver near the design boundary and inspect the decision quantity, such as drag, lift, stress peak, or failure location.",
        "key_difference": "A solver follows the written equations step by step. A surrogate imitates the solver's input-output behavior inside a tested use range.",
        "wrong_turn": "A fast surrogate is not a replacement for the solver outside the cases where it was checked.",
    },
    {
        "slug": "symbolic-regression-vs-large-fitted-prediction",
        "title": "Symbolic Regression vs Large Fitted Prediction",
        "left": "Symbolic regression",
        "right": "Large fitted prediction",
        "shared_problem": "Both use data to make future or unseen cases easier to understand.",
        "left_when": "Use this side when the user needs a short equation that can be inspected and argued over.",
        "right_when": "Use this side when predictive accuracy on a complex pattern matters more than a compact human-readable rule.",
        "left_case": "A lab tracks a simple motion and wants a small equation that explains the rate of change. Use symbolic regression and test the law on a new experiment.",
        "right_case": "A molecular property depends on many structural details and the goal is accurate screening. Use a larger fitted predictor with clear use-range checks.",
        "wrong_choice_case": "Treating a neat formula as a law when an important variable was never measured, or demanding a tiny formula for a pattern that needs richer structure.",
        "evidence_that_exposes_it": "Run a changed experiment, add missing-variable checks, and compare error on cases that differ from the data that selected the formula.",
        "key_difference": "Symbolic regression searches for a small formula. Large fitted prediction can carry more detail but usually gives less direct explanation.",
        "wrong_turn": "A neat formula is not automatically true; it must survive changed data and missing-variable checks.",
    },
    {
        "slug": "data-only-vs-physics-informed-learning",
        "title": "Data-Only vs Physics-Informed Learning",
        "left": "Data-only learning",
        "right": "Physics-informed learning",
        "shared_problem": "Both try to turn examples into predictions.",
        "left_when": "Use this side when examples are abundant, the use range is narrow, and there is no trusted rule to add.",
        "right_when": "Use this side when a known equation, boundary condition, conservation law, unit, or symmetry should constrain the answer.",
        "left_case": "A measured property has many examples and no trusted equation for the target. Use data-only learning with a clear held-out test.",
        "right_case": "A temperature field has sparse measurements and a trusted heat equation. Add the physical rule so unsensed places are checked.",
        "wrong_choice_case": "Adding a physical rule that is incomplete or wrong for the experiment, or ignoring a trusted rule when data are sparse.",
        "evidence_that_exposes_it": "Compare changed cases where the rule matters: boundaries, conservation, units, symmetry, or regions between measurements.",
        "key_difference": "Data-only learning listens to examples. Physics-informed learning also listens to rules about what answers are allowed.",
        "wrong_turn": "Adding physics language does not help if the added rule is wrong, too weak, or never tested against the claim.",
    },
]


WORKED_EXAMPLES = [
    {
        "slug": "heat-equation-from-few-measurements",
        "title": "Heat Equation From Few Measurements",
        "domain": "heat moving through a rod, wall, chip, or material sample",
        "question": "What is the temperature everywhere if sensors only report a few places?",
        "observed": "sensor readings, starting temperature, boundary temperature, and the rule that heat flows from hot regions toward cold regions",
        "hidden": "temperature at every unsensed point and later time",
        "method_route": ["partial-differential-equations", "physics-informed-neural-networks", "scientific-machine-learning", "uncertainty-and-generalization"],
        "plain_steps": [
            "Draw the unknown temperature as a field, not as one number.",
            "Use the measured points as anchors.",
            "Use the heat rule as a check between anchors.",
            "Compare with held-out sensors or a trusted solve.",
        ],
        "why_it_teaches": "This is the cleanest entry point for PINNs because the physical rule is familiar: heat smooths out unless a source keeps adding energy.",
    },
    {
        "slug": "fast-fluid-field-surrogate",
        "title": "Fast Fluid Field Surrogate",
        "domain": "air or liquid flow around shapes",
        "question": "How can engineers test many shapes without running a full simulation every time?",
        "observed": "many prior simulations connecting shape, conditions, and resulting velocity or pressure fields",
        "hidden": "the flow field for a new shape or new condition",
        "method_route": ["surrogate-modeling", "operator-learning", "attention-for-scientific-fields"],
        "plain_steps": [
            "Name the range of shapes and flow conditions.",
            "Train a model on full fields from trusted simulations.",
            "Predict a new field quickly.",
            "Reject the shortcut if it misses boundary behavior, vortices, or pressure forces that matter.",
        ],
        "why_it_teaches": "It shows why speed is not the same as trust. The useful claim is a fast answer inside a tested design family.",
    },
    {
        "slug": "discovering-a-small-law-from-motion",
        "title": "Discovering A Small Law From Motion",
        "domain": "a measured system changing over time",
        "question": "Can data reveal a short rule for how the system moves?",
        "observed": "measurements of position, speed, concentration, or another changing quantity",
        "hidden": "the rate rule that causes the next moment",
        "method_route": ["symbolic-regression", "neural-differential-equations", "optimization-for-learning"],
        "plain_steps": [
            "Measure the variables that might matter.",
            "Estimate how they change from moment to moment.",
            "Search for a short rule or learn the missing rate.",
            "Test on a new experiment, not only the original trace.",
        ],
        "why_it_teaches": "It separates prediction from explanation. A readable rule becomes valuable only when it survives a changed experiment.",
    },
    {
        "slug": "molecule-property-from-structure",
        "title": "Molecule Property From Structure",
        "domain": "chemistry and biology, where atoms, bonds, shape, and measured activity all matter",
        "question": "Can a model predict a useful molecular property without flattening away the structure that causes it?",
        "observed": "molecular graphs, atom types, bond patterns, shape information, and measured properties from experiments or trusted calculations",
        "hidden": "which structural relations control the property for a new molecule",
        "method_route": ["graphs-and-geometric-learning", "generative-modeling", "deep-learning", "uncertainty-and-generalization"],
        "plain_steps": [
            "Represent the molecule as connected parts, not as an unordered list.",
            "Let information move along bonds and nearby spatial relations.",
            "Predict the target property for a new molecule.",
            "Reject the claim if a new scaffold, rare atom type, or changed assay breaks the prediction.",
        ],
        "why_it_teaches": "It shows why geometry and connections matter. The scientific object already has structure before the model sees it.",
    },
    {
        "slug": "material-stress-from-sparse-tests",
        "title": "Material Stress From Sparse Tests",
        "domain": "materials and mechanics, where stress and strain depend on shape, load, defects, and boundary conditions",
        "question": "How can a model estimate stress inside a material when only a few tests or simulations are available?",
        "observed": "sample geometry, load conditions, a few measured displacements or strains, and known mechanical balance laws",
        "hidden": "the internal stress field and the weak region where failure may begin",
        "method_route": ["partial-differential-equations", "physics-informed-neural-networks", "surrogate-modeling"],
        "plain_steps": [
            "Name the material quantity that matters for the decision.",
            "Use sparse measurements as anchors for the unknown field.",
            "Use mechanical balance as a check between measured places.",
            "Compare against held-out tests, changed loads, and trusted simulations near failure regions.",
        ],
        "why_it_teaches": "It connects physics constraints to a practical engineering risk: missing a local stress concentration can matter more than average error.",
    },
    {
        "slug": "mesh-field-on-irregular-geometry",
        "title": "Mesh Field On Irregular Geometry",
        "domain": "scientific fields on meshes, surfaces, networks, and irregular engineering shapes",
        "question": "How can a model predict a field when the points are connected in an uneven shape instead of a neat grid?",
        "observed": "mesh points, connections, boundary labels, local features, and solution fields from prior solves",
        "hidden": "how information should move across the irregular geometry for a new case",
        "method_route": ["graphs-and-geometric-learning", "operator-learning", "attention-for-scientific-fields"],
        "plain_steps": [
            "Keep the mesh connections visible.",
            "Pass information along nearby and important distant relations.",
            "Predict the field on the same kind of geometric object.",
            "Test changed meshes, boundaries, rotations, and refined regions before trusting the answer.",
        ],
        "why_it_teaches": "It shows why some scientific data cannot be treated like a flat table. The connections carry part of the physics.",
    },
    {
        "slug": "foundation-pde-model-on-new-equation",
        "title": "Foundation PDE Model On A New Equation",
        "domain": "many PDE tasks where one broad model is asked to help with a new scientific equation",
        "question": "When can a model trained on many PDE examples help with a new equation family?",
        "observed": "many prior equation tasks, grids, parameters, boundary types, and solution fields",
        "hidden": "which shared structure carries to the new equation and which parts do not",
        "method_route": ["foundation-models-for-pdes", "operator-learning", "uncertainty-and-generalization"],
        "plain_steps": [
            "List what the broad model has seen before.",
            "Name what is different about the new equation, boundary, scale, or field.",
            "Use the model only as a candidate shortcut for the new task.",
            "Compare against a trusted solve and look for the first changed condition where it fails.",
        ],
        "why_it_teaches": "It makes breadth concrete. A broad model is useful only when the new task shares the structure the model actually learned.",
    },
    {
        "slug": "climate-risk-under-shifted-conditions",
        "title": "Climate Risk Under Shifted Conditions",
        "domain": "climate, weather, and environmental fields where future conditions may differ from old data",
        "question": "How should a model report risk when the future case is not just another familiar example?",
        "observed": "historical fields, simulation ensembles, forcing conditions, regional measurements, and known physical constraints",
        "hidden": "how wrong the prediction may be under a changed climate, rare event, or new regional pattern",
        "method_route": ["uncertainty-and-generalization", "surrogate-modeling", "partial-differential-equations"],
        "plain_steps": [
            "Name the risk quantity before choosing a model.",
            "Separate familiar held-out cases from truly changed future conditions.",
            "Report prediction with the tested use range.",
            "Reject confident claims when rare events, regions, or forcing changes have not been checked.",
        ],
        "why_it_teaches": "It shows why uncertainty is not an add-on. The use range is part of the scientific answer.",
    },
]


TOPIC_DEEP_DIVES = {
    "physics-informed-neural-networks": {
        "one_sentence": "A PINN is a fitted field that must answer to both measured values and a known physical rule.",
        "use_when": "Use it when measurements are sparse, the equation is trusted, and the scientific job is one specific field or parameter case.",
        "do_not_use_when": "Do not treat it as magic for hard PDEs; if boundary data, scales, or sharp regions are poorly handled, the equation penalty can mislead.",
        "domain_story": "Imagine estimating temperature inside a wall from a few sensors. The sensor readings anchor the answer, while the heat equation checks the empty places between sensors.",
        "math_shape": [
            "Choose a neural network to represent the unknown field.",
            "Compare the field with measured data where measurements exist.",
            "Differentiate the field and check whether it breaks the equation.",
            "Also check boundary or starting values.",
            "Train by reducing all of those errors together.",
        ],
        "plain_formula": "total error = data error + equation error + boundary error",
        "important_because": "The equation gives the model a reason not to invent impossible behavior between data points.",
        "red_flags": [
            "The page reports only training error.",
            "The hard region has few check points.",
            "The equation is known to be incomplete for the experiment.",
            "No comparison is made against held-out measurements or a trusted solver.",
        ],
        "connects_to": ["partial-differential-equations", "optimization-for-learning", "uncertainty-and-generalization"],
    },
    "partial-differential-equations": {
        "one_sentence": "A PDE is a rule for how a whole field changes across space and time.",
        "use_when": "Use it when one value is not enough because neighbors, boundaries, and time all matter.",
        "do_not_use_when": "Do not reduce the problem to independent points if movement, flow, stress, diffusion, or waves connect those points.",
        "domain_story": "Weather, temperature, pressure, and fluid velocity are fields. A value at one location matters partly because of the values around it.",
        "math_shape": [
            "Name the field, such as temperature or velocity.",
            "Name the rates of change across space and time.",
            "Add sources, forces, material parameters, and boundaries.",
            "Use the rule to connect local change to nearby values.",
            "Check conservation, stability, and boundary behavior.",
        ],
        "plain_formula": "change over time = movement through space + sources + boundary effects",
        "important_because": "Most physics-informed machine learning borrows its scientific burden from PDEs.",
        "red_flags": [
            "The boundary condition is vague.",
            "The learned answer ignores conservation.",
            "The grid or resolution changes the conclusion.",
            "Small visual error hides a large error in the quantity people care about.",
        ],
        "connects_to": ["physics-informed-neural-networks", "operator-learning", "surrogate-modeling"],
    },
    "operator-learning": {
        "one_sentence": "Operator learning tries to learn the machine that turns one field into another field.",
        "use_when": "Use it when you have many solved examples and need fast answers for new inputs from the same named family.",
        "do_not_use_when": "Do not use it as proof of broad scientific skill unless the new equation, boundary, grid, and parameter range were tested.",
        "domain_story": "Instead of solving heat flow for one wall, learn the map from many wall materials and heat sources to their resulting temperature fields.",
        "math_shape": [
            "Collect many input fields and matching solution fields.",
            "Name the family those examples come from.",
            "Train a map from input function to output function.",
            "Use structure such as Fourier modes, graph connections, or attention when needed.",
            "Test on new fields that stress the intended use range.",
        ],
        "plain_formula": "input field -> learned field-to-field map -> output field",
        "important_because": "It targets repeated simulation work, where the valuable object is the whole input-output map.",
        "red_flags": [
            "The training family is not named.",
            "Only one resolution is tested.",
            "The output looks plausible but physical quantities are not checked.",
            "The model is used on a new boundary type without evidence.",
        ],
        "connects_to": ["surrogate-modeling", "attention-for-scientific-fields", "foundation-models-for-pdes"],
    },
    "surrogate-modeling": {
        "one_sentence": "A surrogate is a faster stand-in for a slower trusted process.",
        "use_when": "Use it when repeated simulation, design, or uncertainty questions would be too slow with the full solver.",
        "do_not_use_when": "Do not use it outside the query family where it has been compared against the trusted source.",
        "domain_story": "If every wing-shape test takes hours, a checked stand-in can screen many shapes before the expensive solver is used again.",
        "math_shape": [
            "Name the expensive source of truth.",
            "Name the inputs people will vary.",
            "Name the output quantity needed for decisions.",
            "Fit the cheap stand-in on trusted examples.",
            "Measure error near the edge of intended use.",
        ],
        "plain_formula": "new query -> fast stand-in -> approximate answer with a stated use range",
        "important_because": "Speed changes what questions scientists and engineers can afford to ask.",
        "red_flags": [
            "The surrogate is described without its use range.",
            "The edge cases are not tested.",
            "The output metric ignores the decision people actually make.",
            "The full solver is never used again for spot checks.",
        ],
        "connects_to": ["operator-learning", "deep-learning", "uncertainty-and-generalization"],
    },
    "uncertainty-and-generalization": {
        "one_sentence": "This topic asks when a prediction should be believed on a case the model did not learn from.",
        "use_when": "Use it whenever a model will guide a scientific or engineering decision under changed conditions.",
        "do_not_use_when": "Do not replace changed-case testing with a confident-looking number.",
        "domain_story": "A model trained on small clean lab samples may be asked about a large noisy field setup. The gap matters as much as the prediction.",
        "math_shape": [
            "Separate training cases from test cases.",
            "Name the changes that matter in the real domain.",
            "Measure error under those changes.",
            "Report the use range with the prediction.",
            "Look for the first condition where the model breaks.",
        ],
        "plain_formula": "prediction + tested use range + failure evidence",
        "important_because": "A scientific model is dangerous when it is most confident exactly where it has the least evidence.",
        "red_flags": [
            "Only familiar cases are reported.",
            "The test set differs from training only in name.",
            "Rare regimes are averaged away.",
            "No one states what condition would make the model unusable.",
        ],
        "connects_to": ["scientific-machine-learning", "surrogate-modeling", "foundation-models-for-pdes"],
    },
    "neural-differential-equations": {
        "one_sentence": "A neural differential equation learns the missing rule for how a system changes.",
        "use_when": "Use it when time evolution is central but the exact rate rule is partly unknown.",
        "do_not_use_when": "Do not trust long-time behavior just because short training windows fit well.",
        "domain_story": "If measurements show a chemical concentration changing but the reaction law is incomplete, the learned part can supply the missing rate.",
        "math_shape": [
            "Name the current state.",
            "Represent the unknown rate of change with a learned function.",
            "Use a time solver to move the state forward.",
            "Compare the predicted path with measurements.",
            "Run beyond the training window to test drift.",
        ],
        "plain_formula": "current state -> learned change rate -> next state",
        "important_because": "It keeps the idea of continuous motion while admitting that part of the motion rule is unknown.",
        "red_flags": [
            "The model is tested only over short times.",
            "Small rate errors accumulate unnoticed.",
            "Known conservation or stability behavior is not checked.",
            "The learned rate fits noise instead of mechanism.",
        ],
        "connects_to": ["symbolic-regression", "optimization-for-learning", "scientific-machine-learning"],
    },
    "symbolic-regression": {
        "one_sentence": "Symbolic regression searches for a short formula that explains measured behavior.",
        "use_when": "Use it when a readable equation is part of the scientific goal.",
        "do_not_use_when": "Do not believe a neat formula unless it survives missing-variable, noise, and changed-experiment checks.",
        "domain_story": "A lab may have measurements of motion and want a small law, not only a predictor that returns the next number.",
        "math_shape": [
            "Choose measured variables and candidate operations.",
            "Generate many possible formulas.",
            "Keep formulas that fit and stay small.",
            "Reject formulas that fail changed experiments.",
            "Inspect whether the remaining formula makes scientific sense.",
        ],
        "plain_formula": "candidate ingredients -> searched formulas -> tested small law",
        "important_because": "A compact equation can be criticized and reused in ways a large fitted object cannot.",
        "red_flags": [
            "Important variables were never measured.",
            "The formula is selected only on the original data.",
            "Noise creates a fake term.",
            "The search space could not express the real mechanism.",
        ],
        "connects_to": ["neural-differential-equations", "scientific-machine-learning", "optimization-for-learning"],
    },
    "foundation-models-for-pdes": {
        "one_sentence": "A PDE foundation model tries to reuse structure across many related field-prediction tasks.",
        "use_when": "Use it when many PDE tasks share enough structure that one broad model may reduce repeated training.",
        "do_not_use_when": "Do not confuse broad training with proof that a new scientific regime is covered.",
        "domain_story": "A model trained across many simulated fields may help on a new field task, but only if the new task shares the structure it learned.",
        "math_shape": [
            "Gather many field-prediction tasks.",
            "Train one model to keep shared structure across those tasks.",
            "Adapt or query it on a new task.",
            "Compare against trusted solves or measurements.",
            "Hold out whole task families, not just random examples.",
        ],
        "plain_formula": "many PDE tasks -> shared learned structure -> new task prediction",
        "important_because": "If it works, broad training could reduce repeated model-building for related scientific problems.",
        "red_flags": [
            "The held-out test is too similar to training.",
            "Rare regimes are missing.",
            "New boundaries or quantities are assumed rather than tested.",
            "Scale is treated as a substitute for scientific validation.",
        ],
        "connects_to": ["operator-learning", "uncertainty-and-generalization", "attention-for-scientific-fields"],
    },
}


HAND_DERIVATIONS = {
    "physics-informed-neural-networks": {
        "plain_start": "Start with an unknown field u. A few measurements tell us u at some points. The equation tells us what u should do between those points. The boundary tells us what must happen at the edge.",
        "line_steps": [
            {
                "term": "data error",
                "why_it_enters": "At measured points, the proposed field should match the observed values. This term keeps the answer tied to the sensors.",
                "check": "If this term is missing, the field may obey the equation while ignoring the actual measurements.",
            },
            {
                "term": "equation error",
                "why_it_enters": "Away from measured points, the proposed field can still be checked by putting it into the known equation and measuring leftover rule-breaking.",
                "check": "If this term is small only at easy points, the hard regions still need separate tests.",
            },
            {
                "term": "boundary error",
                "why_it_enters": "A field can satisfy the equation in the middle while using the wrong edge or starting values. This term pins down the problem being solved.",
                "check": "If boundaries are wrong, the solution can be a solution to a different physical problem.",
            },
        ],
        "final_line": "The loss is a written contract: match the measurements, obey the equation, and respect the edge information. The contract is only useful if each part matches the real scientific job.",
    },
    "operator-learning": {
        "plain_start": "Start with many solved cases. Each case has a whole input field and a whole output field. The unknown object is not one solution; it is the map that turns any allowed input field into its output field.",
        "line_steps": [
            {
                "term": "input field family",
                "why_it_enters": "The learner needs to know what kind of inputs it is allowed to receive: source terms, coefficients, shapes, boundaries, or starting fields.",
                "check": "If the input family is not named, no one knows where the learned map is allowed to be used.",
            },
            {
                "term": "field-to-field map",
                "why_it_enters": "The useful object is the rule from whole input field to whole output field, not a lookup table for one case.",
                "check": "If only one output is tested, the page has not shown that a map was learned.",
            },
            {
                "term": "new field test",
                "why_it_enters": "The map earns trust only when it works on new input fields from the named family.",
                "check": "If the new field changes resolution, boundary type, or geometry, that change must be named and tested.",
            },
        ],
        "final_line": "The derivation is a shift in the object being learned: from one answer to a reusable map between fields.",
    },
    "surrogate-modeling": {
        "plain_start": "Start with a trusted source that is too slow for repeated use. The scientist still needs many answers for design, search, or risk checks.",
        "line_steps": [
            {
                "term": "trusted source",
                "why_it_enters": "The stand-in needs something to imitate and something to be checked against.",
                "check": "If the trusted source is not named, the surrogate has no clear reference point.",
            },
            {
                "term": "cheap stand-in",
                "why_it_enters": "The learned model replaces repeated expensive calls inside a named use range.",
                "check": "If the use range is missing, speed can hide bad answers.",
            },
            {
                "term": "edge check",
                "why_it_enters": "Errors often matter most near the edge of the range where decisions are tempting and evidence is thin.",
                "check": "If only average error is reported, the decision quantity may still be wrong.",
            },
        ],
        "final_line": "A surrogate derivation is not just about fitting a curve; it is about earning a cheaper answer while keeping the trusted source in view.",
    },
    "uncertainty-and-generalization": {
        "plain_start": "Start with a model trained on old cases and a new case that may differ. The missing quantity is not only the prediction; it is how much trust the prediction deserves.",
        "line_steps": [
            {
                "term": "prediction",
                "why_it_enters": "The model gives an answer for the quantity the scientist asked for.",
                "check": "A prediction without a use range is incomplete.",
            },
            {
                "term": "tested use range",
                "why_it_enters": "The reader needs to know which cases actually support the answer.",
                "check": "If the test cases look like the training cases, changed-case trust is still unproved.",
            },
            {
                "term": "failure evidence",
                "why_it_enters": "Knowing where the model breaks is part of knowing where it can be used.",
                "check": "If no failure case is named, confidence is just a number without a boundary.",
            },
        ],
        "final_line": "The mathematical shape joins answer and boundary: report the prediction together with the evidence that says where belief should weaken.",
    },
    "symbolic-regression": {
        "plain_start": "Start with measured variables and a need for a readable law. The unknown object is the relation among the variables, not just the next predicted value.",
        "line_steps": [
            {
                "term": "candidate ingredients",
                "why_it_enters": "The search can only build formulas from measured variables and allowed operations.",
                "check": "If an important variable is missing, the best formula may still be false.",
            },
            {
                "term": "searched formulas",
                "why_it_enters": "Many possible short laws are tried because the correct relation is not known ahead of time.",
                "check": "If size is not controlled, the formula may only memorize noise.",
            },
            {
                "term": "changed experiment",
                "why_it_enters": "A readable formula becomes a scientific candidate only if it survives a new situation.",
                "check": "If it is tested only where it was found, it is not yet a law.",
            },
        ],
        "final_line": "The derivation is a search with a burden: the result must be short enough to inspect and strong enough to survive a new experiment.",
    },
    "foundation-models-for-pdes": {
        "plain_start": "Start with many PDE tasks. Each task teaches something about fields, equations, boundaries, or solution patterns. The new task is useful only if it shares structure the model actually learned.",
        "line_steps": [
            {
                "term": "many PDE tasks",
                "why_it_enters": "Broad training is the source of shared experience across equations or parameter ranges.",
                "check": "If the tasks are narrow, the model may only be broad in name.",
            },
            {
                "term": "shared learned structure",
                "why_it_enters": "The model must keep something reusable, such as field patterns, operator behavior, or equation-family regularities.",
                "check": "If the shared structure is not named, transfer to a new task is only a hope.",
            },
            {
                "term": "new task prediction",
                "why_it_enters": "The point is to use old task experience on a held-out scientific case.",
                "check": "If the held-out task is too similar to training, the broad claim is not tested.",
            },
        ],
        "final_line": "The derivation makes the transfer burden visible: old PDE tasks must carry something real into the new task, and the new task must be different enough to test that claim.",
    },
}


DIAGRAMS = [
    {
        "slug": "data-only-learning-flow",
        "title": "Data-Only Learning Flow",
        "topic_slugs": ["deep-learning", "scientific-machine-learning"],
        "purpose": "Show what a model sees when examples are the only source of correction.",
        "nodes": [
            "past examples",
            "adjustable model",
            "prediction",
            "compare with known answers",
            "test on a changed case",
        ],
        "watch_for": "If the changed case is too similar to the past examples, the test says little about scientific use.",
    },
    {
        "slug": "physics-informed-learning-flow",
        "title": "Physics-Informed Learning Flow",
        "topic_slugs": ["physics-informed-neural-networks"],
        "purpose": "Show how measured data and a known physical rule both push on the fitted field.",
        "nodes": [
            "sparse measurements",
            "known equation",
            "fitted field",
            "data check plus equation check",
            "held-out sensor or trusted solve",
        ],
        "watch_for": "The equation check must be hard enough to catch mistakes between measured points.",
    },
    {
        "slug": "pde-field-reasoning-flow",
        "title": "PDE Field Reasoning Flow",
        "topic_slugs": ["partial-differential-equations"],
        "purpose": "Show why fields need boundaries, neighbors, and time rather than isolated numbers.",
        "nodes": [
            "field value",
            "nearby values",
            "boundary or starting information",
            "local change rule",
            "future field",
        ],
        "watch_for": "A learned shortcut that ignores boundaries can look smooth while answering the wrong physical question.",
    },
    {
        "slug": "operator-learning-flow",
        "title": "Operator Learning Flow",
        "topic_slugs": ["operator-learning", "foundation-models-for-pdes", "attention-for-scientific-fields"],
        "purpose": "Show the difference between learning one answer and learning a map from input fields to output fields.",
        "nodes": [
            "many input fields",
            "many solved output fields",
            "learned field-to-field map",
            "new input field",
            "new output field",
        ],
        "watch_for": "The map is useful only for the named family of equations, grids, parameters, and boundaries.",
    },
    {
        "slug": "surrogate-validation-flow",
        "title": "Surrogate Validation Flow",
        "topic_slugs": ["surrogate-modeling", "uncertainty-and-generalization"],
        "purpose": "Show how a fast stand-in earns trust only by being checked against the slow source.",
        "nodes": [
            "expensive solver",
            "training cases",
            "fast stand-in",
            "edge-case comparison",
            "stated use range",
        ],
        "watch_for": "A speed claim is incomplete until the use range and failure case are stated.",
    },
    {
        "slug": "model-discovery-flow",
        "title": "Model Discovery Flow",
        "topic_slugs": ["symbolic-regression", "neural-differential-equations"],
        "purpose": "Show how measurements can lead to a candidate rule rather than only a prediction.",
        "nodes": [
            "measured motion",
            "candidate variables",
            "searched rule or learned rate",
            "readable law",
            "new experiment check",
        ],
        "watch_for": "A short law can be wrong if important variables were never measured.",
    },
]


CONCEPT_SKETCHES = [
    {
        "slug": "pinn-measurement-rule-sketch",
        "title": "PINNs: Points Plus Rule Checks",
        "topic_slugs": ["physics-informed-neural-networks"],
        "input": "few measured points, boundary values, and a known equation",
        "output": "a fitted field for the whole domain",
        "kept_rule": "the field should match data and leave little equation-breaking between data points",
        "failure_case": "the field matches sensors but breaks the equation, boundary, or held-out measurements",
        "caption": "Input: measured points and equation. Output: full field. Kept rule: data plus equation checks. Failure case: correct-looking fit that breaks physics in unmeasured regions.",
        "cells": [
            {"label": "measured points", "role": "input"},
            {"label": "equation-check points", "role": "rule"},
            {"label": "fitted field", "role": "output"},
            {"label": "held-out region", "role": "failure"},
        ],
    },
    {
        "slug": "operator-field-map-sketch",
        "title": "Operator Learning: Field To Field",
        "topic_slugs": ["operator-learning", "foundation-models-for-pdes"],
        "input": "a whole input field from a named family",
        "output": "the whole output field for that input",
        "kept_rule": "the learned object is a reusable map between fields, not one solved example",
        "failure_case": "a new input field changes the family, boundary, geometry, or resolution beyond the tested range",
        "caption": "Input: whole field. Output: whole field. Kept rule: reusable map between related cases. Failure case: new field outside the named family.",
        "cells": [
            {"label": "input field", "role": "input"},
            {"label": "learned map", "role": "rule"},
            {"label": "output field", "role": "output"},
            {"label": "new family", "role": "failure"},
        ],
    },
    {
        "slug": "surrogate-decision-sketch",
        "title": "Surrogate Modeling: Fast Stand-In With Boundaries",
        "topic_slugs": ["surrogate-modeling"],
        "input": "queries that would normally require a trusted slow source",
        "output": "fast approximate answers for repeated choices",
        "kept_rule": "the stand-in remains checked against the trusted source inside a named use range",
        "failure_case": "the stand-in is used near an edge case where the trusted source has not checked it",
        "caption": "Input: repeated query. Output: fast answer. Kept rule: checked against trusted source. Failure case: fast answer outside the tested use range.",
        "cells": [
            {"label": "repeated query", "role": "input"},
            {"label": "trusted source", "role": "rule"},
            {"label": "fast answer", "role": "output"},
            {"label": "edge case", "role": "failure"},
        ],
    },
    {
        "slug": "uncertainty-shift-sketch",
        "title": "Uncertainty: New Case Near The Edge",
        "topic_slugs": ["uncertainty-and-generalization", "foundation-models-for-pdes"],
        "input": "training cases and a new case that may be different",
        "output": "prediction with a tested use range",
        "kept_rule": "belief should weaken when the new case leaves the evidence range",
        "failure_case": "the model stays confident where training and validation no longer support confidence",
        "caption": "Input: old cases plus new case. Output: prediction with use range. Kept rule: doubt grows near the edge. Failure case: confident answer outside evidence.",
        "cells": [
            {"label": "old cases", "role": "input"},
            {"label": "use range", "role": "rule"},
            {"label": "prediction", "role": "output"},
            {"label": "shifted case", "role": "failure"},
        ],
    },
]


LEARNING_PATH = [
    {
        "slug": "scientific-question-first",
        "title": "Start With The Scientific Question",
        "question": "What is being predicted, explained, designed, or checked?",
        "why_first": "Physics-informed machine learning is not one trick. The method depends on the scientific job, the evidence in hand, and the changed case where a wrong answer would matter.",
        "plain_goal": "Name the quantity, the domain, the evidence, and the changed case before naming a method.",
        "first_principles_spine": [
            "World: a scientist needs an answer for a real quantity.",
            "Evidence: measurements, equations, simulations, or old cases give partial support.",
            "Missing piece: the quantity needed for the next case is not directly known.",
            "Mathematical move: choose the smallest learning route that carries the needed evidence.",
            "Reject it when: a changed case breaks the quantity the scientist actually needs.",
        ],
        "read": [
            {"label": "Scientific Machine Learning", "href": "topics/scientific-machine-learning.html"},
            {"label": "Data-Only Learning Flow", "href": "diagrams/data-only-learning-flow.html"},
            {"label": "Data-Only vs Physics-Informed Learning", "href": "comparisons/data-only-vs-physics-informed-learning.html"},
        ],
        "checkpoint": "You can say what answer the scientist wants and what would make that answer unusable.",
    },
    {
        "slug": "fields-and-equations",
        "title": "Understand Fields And Equations",
        "question": "Why is one number not enough?",
        "why_first": "Many scientific problems are fields: temperature, pressure, velocity, concentration, stress, or displacement across space and time.",
        "plain_goal": "See why boundaries, neighbors, rates of change, and starting values carry the scientific burden.",
        "first_principles_spine": [
            "World: the answer lives across space or time, not in one number.",
            "Evidence: some values, edges, starting values, and physical rules are known.",
            "Missing piece: the full field is unknown between measured or simulated cases.",
            "Mathematical move: describe how nearby values, rates, and boundaries restrict the answer.",
            "Reject it when: the field violates edges, neighbors, or measured behavior in a changed case.",
        ],
        "read": [
            {"label": "Partial Differential Equations", "href": "topics/partial-differential-equations.html"},
            {"label": "PDE Field Reasoning Flow", "href": "diagrams/pde-field-reasoning-flow.html"},
            {"label": "Heat Equation From Few Measurements", "href": "worked-examples/heat-equation-from-few-measurements.html"},
        ],
        "checkpoint": "You can explain why a field prediction must respect boundaries and nearby values.",
    },
    {
        "slug": "physics-as-check",
        "title": "Use Physics As A Check",
        "question": "How can a model be corrected where there are no measurements?",
        "why_first": "Sparse data leaves empty space. A known equation can check that empty space if the equation is trusted.",
        "plain_goal": "Understand PINNs as fitted fields that answer to both data and an equation.",
        "first_principles_spine": [
            "World: the true field should obey a known physical rule.",
            "Evidence: measured points, boundaries, starting values, and the equation are available.",
            "Missing piece: most field values are unmeasured.",
            "Mathematical move: score both data mismatch and equation mismatch.",
            "Reject it when: the fitted field matches points but breaks the equation, boundary, or changed test case.",
        ],
        "read": [
            {"label": "Physics-Informed Neural Networks", "href": "topics/physics-informed-neural-networks.html"},
            {"label": "Physics-Informed Learning Flow", "href": "diagrams/physics-informed-learning-flow.html"},
            {"label": "Physics Constraints Family", "href": "families/physics-constraints-family.html"},
        ],
        "checkpoint": "You can state the data error, equation error, boundary error, and the test case.",
    },
    {
        "slug": "maps-between-fields",
        "title": "Learn Maps Between Fields",
        "question": "What if the job is not one solution, but many related solutions?",
        "why_first": "Engineering and science often need repeated solves for many inputs, shapes, materials, or conditions.",
        "plain_goal": "Separate learning one answer from learning the map that turns an input field into an output field.",
        "first_principles_spine": [
            "World: many related scientific cases share an input-to-output relation.",
            "Evidence: solved examples show input fields paired with output fields.",
            "Missing piece: the full output field for a new input is unknown.",
            "Mathematical move: learn the map from whole input fields to whole output fields.",
            "Reject it when: a new input outside the learned family gives a bad field or a bad scientific quantity.",
        ],
        "read": [
            {"label": "Operator Learning", "href": "topics/operator-learning.html"},
            {"label": "Operator Learning Flow", "href": "diagrams/operator-learning-flow.html"},
            {"label": "PINNs vs Neural Operators", "href": "comparisons/pinns-vs-neural-operators.html"},
            {"label": "Neural Operators Family", "href": "families/neural-operators-family.html"},
        ],
        "checkpoint": "You can name the family of inputs and outputs where the learned map is allowed to be used.",
    },
    {
        "slug": "speed-with-boundaries",
        "title": "Use Speed Without Hiding Risk",
        "question": "When is a fast approximation useful?",
        "why_first": "A fast model is valuable only if the slow trusted source still defines where the fast answer is valid.",
        "plain_goal": "Treat surrogates as checked stand-ins with a stated use range.",
        "first_principles_spine": [
            "World: the scientist needs many answers faster than the trusted source can provide them.",
            "Evidence: trusted simulations or experiments define examples and limits.",
            "Missing piece: a cheap answer is needed for repeated choices.",
            "Mathematical move: train a stand-in and compare it against the trusted source inside a named range.",
            "Reject it when: speed hides error near the edge of the range or in the quantity used for the decision.",
        ],
        "read": [
            {"label": "Surrogate Modeling", "href": "topics/surrogate-modeling.html"},
            {"label": "Surrogate Validation Flow", "href": "diagrams/surrogate-validation-flow.html"},
            {"label": "Fast Fluid Field Surrogate", "href": "worked-examples/fast-fluid-field-surrogate.html"},
            {"label": "Solvers vs Learned Surrogates", "href": "comparisons/solvers-vs-learned-surrogates.html"},
        ],
        "checkpoint": "You can say what the surrogate replaces, what it does not replace, and where it was checked.",
    },
    {
        "slug": "trust-and-failure",
        "title": "Make Trust A Testable Claim",
        "question": "When should a prediction be believed?",
        "why_first": "Scientific mistakes often happen when a model is used outside the cases that taught it.",
        "plain_goal": "Attach every prediction to a use range, changed-case test, and failure boundary.",
        "first_principles_spine": [
            "World: the next scientific case may differ from the old cases.",
            "Evidence: training and validation cases show only part of the possible range.",
            "Missing piece: the model's reliability on the new case is unknown.",
            "Mathematical move: measure error, doubt, and changed-case behavior instead of reporting only a prediction.",
            "Reject it when: the model stays confident where the evidence no longer supports confidence.",
        ],
        "read": [
            {"label": "Uncertainty And Generalization", "href": "topics/uncertainty-and-generalization.html"},
            {"label": "Foundation Models For PDEs", "href": "topics/foundation-models-for-pdes.html"},
            {"label": "Neural Operators Family", "href": "families/neural-operators-family.html"},
            {"label": "Surrogate Validation Flow", "href": "diagrams/surrogate-validation-flow.html"},
        ],
        "checkpoint": "You can name the first changed condition that should make the model fail.",
    },
    {
        "slug": "readable-laws",
        "title": "Look For Readable Laws When Needed",
        "question": "When is prediction not enough?",
        "why_first": "Sometimes the scientific product is a rule people can inspect, criticize, and reuse.",
        "plain_goal": "Understand symbolic regression and neural differential equations as routes toward candidate mechanisms.",
        "first_principles_spine": [
            "World: the scientist wants a rule, not only an answer.",
            "Evidence: measured variables and changes over time suggest possible relations.",
            "Missing piece: the governing relation is unknown.",
            "Mathematical move: search for a small rule or learned rate that explains the observations.",
            "Reject it when: the rule fails a new experiment or depends on a missing variable.",
        ],
        "read": [
            {"label": "Symbolic Regression And Model Discovery", "href": "topics/symbolic-regression.html"},
            {"label": "Neural Differential Equations", "href": "topics/neural-differential-equations.html"},
            {"label": "Model Discovery Flow", "href": "diagrams/model-discovery-flow.html"},
            {"label": "Discovering A Small Law From Motion", "href": "worked-examples/discovering-a-small-law-from-motion.html"},
        ],
        "checkpoint": "You can explain why a short formula still needs a changed-experiment test.",
    },
]


GLOSSARY = [
    {
        "slug": "field",
        "term": "Field",
        "everyday": "a value spread across space or time, like temperature across a room",
        "problem": "one number cannot describe the whole situation",
        "why_it_matters": "many scientific predictions are about complete fields, not single answers",
        "watch_for": "a method that predicts isolated points may miss how neighboring points affect each other",
        "related": ["partial-differential-equations", "operator-learning"],
    },
    {
        "slug": "boundary-condition",
        "term": "Boundary Condition",
        "everyday": "what is known at the edge of the problem",
        "problem": "a field can have many possible answers unless the edges or starting situation are pinned down",
        "why_it_matters": "boundaries often decide the scientific answer as much as the equation does",
        "watch_for": "a model can look accurate inside the domain while quietly violating the edge information",
        "related": ["partial-differential-equations", "physics-informed-neural-networks"],
    },
    {
        "slug": "residual",
        "term": "Residual",
        "everyday": "the leftover rule-breaking after a proposed answer is checked",
        "problem": "a prediction may match measured points but still break the equation between them",
        "why_it_matters": "PINNs use this leftover error to push a fitted field toward physically allowed behavior",
        "watch_for": "a small reported residual does not prove the answer is correct in hard regions",
        "related": ["physics-informed-neural-networks", "optimization-for-learning"],
    },
    {
        "slug": "loss",
        "term": "Loss",
        "everyday": "the score the training process tries to lower",
        "problem": "a model needs a written way to decide which answer is better",
        "why_it_matters": "the model learns what the score asks for, not what the reader hoped it meant",
        "watch_for": "if the score forgets a scientific requirement, training can improve while the science gets worse",
        "related": ["optimization-for-learning", "physics-informed-neural-networks"],
    },
    {
        "slug": "operator",
        "term": "Operator",
        "everyday": "a machine that takes one whole function or field and returns another",
        "problem": "some tasks need the full input-to-output rule, not one solved example",
        "why_it_matters": "operator learning targets families of simulations where inputs and outputs are fields",
        "watch_for": "the learned machine only deserves trust inside the named family of cases",
        "related": ["operator-learning", "surrogate-modeling"],
    },
    {
        "slug": "surrogate",
        "term": "Surrogate",
        "everyday": "a faster stand-in for something slower",
        "problem": "trusted simulations or experiments may be too expensive to run repeatedly",
        "why_it_matters": "a checked stand-in can make design, search, and uncertainty studies possible",
        "watch_for": "speed is useful only where the stand-in has been compared against the trusted source",
        "related": ["surrogate-modeling", "uncertainty-and-generalization"],
    },
    {
        "slug": "generalization",
        "term": "Generalization",
        "everyday": "whether a model still works on a new case",
        "problem": "training examples do not cover every situation where the model may be used",
        "why_it_matters": "scientific use depends on changed cases, not only familiar examples",
        "watch_for": "a test that barely differs from training can create false confidence",
        "related": ["uncertainty-and-generalization", "foundation-models-for-pdes"],
    },
    {
        "slug": "uncertainty",
        "term": "Uncertainty",
        "everyday": "a warning about how much the answer may be wrong",
        "problem": "a single prediction hides how much evidence supports it",
        "why_it_matters": "scientific decisions need to know where belief should weaken",
        "watch_for": "uncertainty is weak if it is not tied to changed-case testing",
        "related": ["uncertainty-and-generalization", "surrogate-modeling"],
    },
    {
        "slug": "symbolic-regression",
        "term": "Symbolic Regression",
        "everyday": "searching for a short formula that fits measured behavior",
        "problem": "sometimes a scientist needs a readable rule, not only a prediction",
        "why_it_matters": "a compact formula can be inspected, criticized, and reused",
        "watch_for": "a neat formula can be wrong if key variables were missing from the search",
        "related": ["symbolic-regression", "neural-differential-equations"],
    },
    {
        "slug": "foundation-model",
        "term": "Foundation Model",
        "everyday": "one broad model trained across many related tasks",
        "problem": "training a new model for every scientific task can be expensive",
        "why_it_matters": "shared structure may reduce repeated training if the new task truly belongs to the learned family",
        "watch_for": "broad training is not proof that a new regime, boundary, or quantity is covered",
        "related": ["foundation-models-for-pdes", "operator-learning"],
    },
]


DOMAIN_GUIDES = [
    {
        "slug": "heat-and-diffusion",
        "title": "Heat And Diffusion",
        "real_quantity": "temperature, concentration, or another quantity spreading through space",
        "why_hard": "measurements may be sparse, but the unsensed region still matters",
        "common_question": "What is happening between sensors, later in time, or under a changed boundary?",
        "concepts": ["partial-differential-equations", "physics-informed-neural-networks", "uncertainty-and-generalization"],
        "domain_job": {
            "scientific_job": "Estimate the full temperature field inside a wall after a boundary temperature changes.",
            "observed_evidence": "a few sensor readings, starting temperature, boundary temperature, material constants, and the heat equation",
            "hidden_quantity": "the temperature at unsensed locations and later times",
            "decision": "decide whether the wall, chip, or sample will exceed a safe temperature",
            "changed_case_test": "move the heat source or change the boundary temperature and compare against held-out sensors or a trusted solve",
        },
        "methods": ["Use a PDE to name how spreading should behave.", "Use sparse measurements as anchors.", "Use held-out sensors or a trusted solve to check the claim."],
        "failure_test": "Change the boundary temperature, source strength, or sensor placement and see whether the prediction still follows the physical rule.",
        "example": "worked-examples/heat-equation-from-few-measurements.html",
    },
    {
        "slug": "fluids-and-flow",
        "title": "Fluids And Flow",
        "real_quantity": "velocity, pressure, vorticity, drag, lift, or other flow quantities",
        "why_hard": "small changes in shape, boundary, or regime can create large changes in the field",
        "common_question": "Can we predict flow fields or forces quickly enough for design while still catching important failures?",
        "concepts": ["operator-learning", "surrogate-modeling", "attention-for-scientific-fields", "uncertainty-and-generalization"],
        "domain_job": {
            "scientific_job": "Predict pressure and velocity around a new wing or channel shape before running the full solver.",
            "observed_evidence": "trusted simulations for earlier shapes, boundary conditions, inflow speed, and resulting velocity or pressure fields",
            "hidden_quantity": "the field and forces for a new shape near the edge of the design range",
            "decision": "screen designs and decide which cases deserve expensive solver runs",
            "changed_case_test": "hold out a new geometry or flow regime and check drag, lift, boundary behavior, and vortices",
        },
        "methods": ["Name the shape and flow family.", "Train on trusted simulated fields.", "Check forces, boundary behavior, and difficult regimes rather than only visual similarity."],
        "failure_test": "Hold out a new geometry or flow condition near the edge of the intended design range.",
        "example": "worked-examples/fast-fluid-field-surrogate.html",
    },
    {
        "slug": "materials-and-mechanics",
        "title": "Materials And Mechanics",
        "real_quantity": "stress, strain, displacement, failure location, or material response",
        "why_hard": "the same load can produce different behavior when geometry, defects, or material parameters change",
        "common_question": "Can a model predict how a material or structure responds under a new load or shape?",
        "concepts": ["partial-differential-equations", "surrogate-modeling", "graphs-and-geometric-learning", "uncertainty-and-generalization"],
        "domain_job": {
            "scientific_job": "Find the stress field and likely weak region in a part with a new load or defect pattern.",
            "observed_evidence": "geometry, mesh, loads, material parameters, sparse strain measurements, and trusted simulations",
            "hidden_quantity": "internal stress and the local region where failure may begin",
            "decision": "decide whether the part is safe enough or needs a changed design",
            "changed_case_test": "change the load path, defect, mesh, or boundary and check stress near failure regions",
        },
        "methods": ["Keep geometry and connections visible.", "Compare against trusted simulations or measurements.", "Name the load, material range, and failure quantity."],
        "failure_test": "Change the geometry, mesh, defect, or load path and check the physical quantity used for decisions.",
        "example": "worked-examples/material-stress-from-sparse-tests.html",
    },
    {
        "slug": "chemistry-and-biology",
        "title": "Chemistry And Biology",
        "real_quantity": "molecular property, reaction behavior, concentration, binding, or biological response",
        "why_hard": "the object may be a graph, a field, a time process, or a set of interacting parts",
        "common_question": "Can learned structure help predict scientific behavior while respecting the object being studied?",
        "concepts": ["graphs-and-geometric-learning", "generative-modeling", "symbolic-regression", "uncertainty-and-generalization"],
        "domain_job": {
            "scientific_job": "Predict a molecule property or biological activity for a new structure.",
            "observed_evidence": "atoms, bonds, shape, assay conditions, measured properties, and trusted calculations where available",
            "hidden_quantity": "which structural relations control the property or response in the new molecule",
            "decision": "choose which candidate molecules deserve synthesis, testing, or closer calculation",
            "changed_case_test": "test on a new scaffold, rare atom type, changed assay, or biological condition outside the familiar set",
        },
        "methods": ["Represent connections when interactions matter.", "Use generation only with scientific checks.", "Look for readable rules only when the measured variables support them."],
        "failure_test": "Test on a changed molecule, condition, experiment, or biological setting that was not close to training.",
        "example": "worked-examples/molecule-property-from-structure.html",
    },
    {
        "slug": "many-pde-tasks",
        "title": "Many PDE Tasks",
        "real_quantity": "solution fields across many equations, grids, parameters, or boundary settings",
        "why_hard": "a model may look broad while only covering the cases it saw often",
        "common_question": "Can one trained model reuse structure across many related scientific tasks?",
        "concepts": ["foundation-models-for-pdes", "operator-learning", "attention-for-scientific-fields", "uncertainty-and-generalization"],
        "domain_job": {
            "scientific_job": "Use a broad PDE model on a new equation case without pretending breadth is proof.",
            "observed_evidence": "many prior PDE tasks, fields, grids, parameters, boundary types, and trusted solution fields",
            "hidden_quantity": "which shared structure transfers to the new PDE case and which parts do not",
            "decision": "decide whether the broad model is a useful shortcut or whether a task-specific solve is still needed",
            "changed_case_test": "withhold a full equation family, boundary type, scale, or quantity and compare against trusted solves",
        },
        "methods": ["Train across many tasks.", "Hold out whole task families.", "Compare against trusted solves on changed equations, boundaries, and scales."],
        "failure_test": "Withhold a full equation family, boundary type, or scale and check whether the model still earns the claim.",
        "example": "worked-examples/foundation-pde-model-on-new-equation.html",
    },
]


READER_CHECKS = [
    {
        "slug": "pinns-check",
        "title": "PINNs Reader Check",
        "topic_slug": "physics-informed-neural-networks",
        "setup": "A wall has only a few temperature sensors, but the heat equation is trusted.",
        "questions": [
            "What is observed?",
            "What is hidden?",
            "Which physical rule checks the spaces between sensors?",
            "What error terms should the training score include?",
            "What changed case would make you doubt the claim?",
        ],
        "strong_answer": "Observed: sensor values, starting or boundary values, and the heat equation. Hidden: the full temperature field. The equation residual checks unsensed locations. The score needs data error, equation error, and boundary or starting error. A changed boundary, source, or held-out sensor should test the claim.",
        "weak_answer_warning": "A weak answer says only that the neural network fits data.",
        "related": ["topics/physics-informed-neural-networks.html", "worked-examples/heat-equation-from-few-measurements.html"],
    },
    {
        "slug": "operator-learning-check",
        "title": "Operator Learning Reader Check",
        "topic_slug": "operator-learning",
        "setup": "You have many solved PDE examples and want fast predictions for new input fields.",
        "questions": [
            "What is the input object?",
            "What is the output object?",
            "What family of cases must be named?",
            "How is this different from learning one solution?",
            "What test would expose overclaiming?",
        ],
        "strong_answer": "The input is a whole field or function, and the output is a whole solution field. The equation, boundary, grid, parameter, and geometry family must be named. The method learns a map between fields, not one field. A new boundary, resolution, parameter range, or equation family should test the claim.",
        "weak_answer_warning": "A weak answer says only that the model is fast.",
        "related": ["topics/operator-learning.html", "diagrams/operator-learning-flow.html"],
    },
    {
        "slug": "surrogate-check",
        "title": "Surrogate Reader Check",
        "topic_slug": "surrogate-modeling",
        "setup": "A trusted simulation is too slow for a design loop.",
        "questions": [
            "What trusted source does the surrogate replace?",
            "Which inputs will be varied?",
            "What output quantity matters for decisions?",
            "Where was the fast stand-in checked?",
            "When should the full solver be used again?",
        ],
        "strong_answer": "The surrogate replaces a named solver or experiment only inside a named query family. Inputs and outputs must match the decision. The stand-in should be checked near the edge of intended use, and the full solver should return when the query leaves that range or when errors affect the decision quantity.",
        "weak_answer_warning": "A weak answer treats speed as trust.",
        "related": ["topics/surrogate-modeling.html", "domains/fluids-and-flow.html"],
    },
    {
        "slug": "uncertainty-check",
        "title": "Uncertainty Reader Check",
        "topic_slug": "uncertainty-and-generalization",
        "setup": "A model works on familiar examples and is now proposed for a new scientific setting.",
        "questions": [
            "How is the new setting different from training?",
            "Which difference matters scientifically?",
            "What error should be measured?",
            "What use range can be stated?",
            "What first failure would stop use?",
        ],
        "strong_answer": "The answer names the actual shift, such as geometry, parameter range, sensor, scale, boundary, or regime. It measures the error that matters for the scientific decision, states the use range, and names a condition that would stop use.",
        "weak_answer_warning": "A weak answer reports one score without saying what changed.",
        "related": ["topics/uncertainty-and-generalization.html", "diagrams/surrogate-validation-flow.html"],
    },
    {
        "slug": "symbolic-regression-check",
        "title": "Symbolic Regression Reader Check",
        "topic_slug": "symbolic-regression",
        "setup": "Measurements suggest there may be a short law behind a changing system.",
        "questions": [
            "Which variables were measured?",
            "Which candidate ingredients were allowed?",
            "What does the selected formula claim?",
            "What missing variable could make the formula wrong?",
            "What changed experiment should test it?",
        ],
        "strong_answer": "The answer lists measured variables, allowed operations or ingredients, and the formula's claim about the system. It names at least one missing variable or untested regime and demands a changed experiment before calling the formula useful.",
        "weak_answer_warning": "A weak answer trusts a neat formula because it fits the original data.",
        "related": ["topics/symbolic-regression.html", "worked-examples/discovering-a-small-law-from-motion.html"],
    },
    {
        "slug": "foundation-pde-check",
        "title": "Foundation PDE Model Reader Check",
        "topic_slug": "foundation-models-for-pdes",
        "setup": "One broad model is trained across many PDE tasks.",
        "questions": [
            "What task families were included?",
            "What shared structure is the model expected to keep?",
            "What whole task family was held out?",
            "What trusted source checks the new task?",
            "What would show that scale did not create scientific coverage?",
        ],
        "strong_answer": "The answer names included and held-out task families, the shared structure being claimed, and a trusted solver or measurement for checking. It rejects broad claims when new equations, boundaries, scales, or rare regimes were not tested.",
        "weak_answer_warning": "A weak answer treats broad training size as proof of broad scientific trust.",
        "related": ["topics/foundation-models-for-pdes.html", "domains/many-pde-tasks.html"],
    },
]


DECISION_GUIDES = [
    {
        "slug": "sparse-data-known-equation",
        "title": "Sparse Data, Known Equation",
        "situation": "You have few measurements, but a trusted equation and boundary or starting information exist.",
        "best_start": "Physics-informed neural networks",
        "why": "The equation can check the fitted field where measurements are missing.",
        "use_if": ["the equation is trusted", "the scientific job is one specific field or case", "boundary or starting information can be stated"],
        "avoid_if": ["the equation is incomplete", "the hard regions are not checked", "the claim needs many different input fields"],
        "evidence_needed": "held-out measurements, boundary checks, equation residual checks, and comparison against a trusted solve when possible",
        "links": ["topics/physics-informed-neural-networks.html", "diagrams/physics-informed-learning-flow.html", "reader-checks/pinns-check.html"],
    },
    {
        "slug": "many-related-simulations",
        "title": "Many Related Simulations",
        "situation": "You have many solved examples and need fast answers for new inputs from the same family.",
        "best_start": "Operator learning",
        "why": "The useful object is the map from input fields to output fields, not one solved field.",
        "use_if": ["the input family can be named", "many trusted input-output field pairs exist", "new queries stay inside the tested family"],
        "avoid_if": ["only one problem instance exists", "the training family is vague", "new boundaries or grids are assumed rather than tested"],
        "evidence_needed": "held-out fields, changed resolution tests, boundary tests, and checks on the scientific output quantity",
        "links": ["topics/operator-learning.html", "diagrams/operator-learning-flow.html", "reader-checks/operator-learning-check.html"],
    },
    {
        "slug": "expensive-repeated-decisions",
        "title": "Expensive Repeated Decisions",
        "situation": "A trusted solver or experiment is too slow for design, search, control, or uncertainty sweeps.",
        "best_start": "Surrogate modeling",
        "why": "A fast stand-in can answer repeated questions if its use range is stated and checked.",
        "use_if": ["the slow trusted source is named", "the repeated query family is narrow enough to test", "the decision quantity is explicit"],
        "avoid_if": ["speed is the only evidence", "the query family keeps changing", "edge cases are not compared against the trusted source"],
        "evidence_needed": "full-solver comparisons near the edge of use, decision-metric error, and a stated use range",
        "links": ["topics/surrogate-modeling.html", "diagrams/surrogate-validation-flow.html", "reader-checks/surrogate-check.html"],
    },
    {
        "slug": "need-readable-law",
        "title": "Need A Readable Law",
        "situation": "Prediction is not enough; the output should be a formula or mechanism people can inspect.",
        "best_start": "Symbolic regression or neural differential equations",
        "why": "The scientific product is a candidate rule, not only a number returned by a fitted model.",
        "use_if": ["important variables are measured", "a changed experiment is available", "a compact rule would be useful for science"],
        "avoid_if": ["key variables are missing", "the formula is selected only on original data", "the system is too complex for the allowed ingredients"],
        "evidence_needed": "changed-experiment tests, missing-variable checks, noise checks, and scientific inspection of the selected rule",
        "links": ["topics/symbolic-regression.html", "topics/neural-differential-equations.html", "reader-checks/symbolic-regression-check.html"],
    },
    {
        "slug": "new-setting-risk",
        "title": "New Setting Risk",
        "situation": "A model trained in one setting is being used in another setting.",
        "best_start": "Uncertainty and generalization checks",
        "why": "The main question is whether the prediction should be believed under the change.",
        "use_if": ["the changed condition can be named", "the decision cost of being wrong matters", "held-out or shifted tests can be built"],
        "avoid_if": ["only familiar tests are available", "the error measure does not match the decision", "confidence is reported without a use range"],
        "evidence_needed": "changed-case tests, use-range statements, error on the decision quantity, and first-failure examples",
        "links": ["topics/uncertainty-and-generalization.html", "reader-checks/uncertainty-check.html", "domains/many-pde-tasks.html"],
    },
    {
        "slug": "broad-pde-coverage",
        "title": "Broad PDE Coverage",
        "situation": "One model is proposed for many equations, grids, parameters, or scientific tasks.",
        "best_start": "Foundation models for PDEs",
        "why": "The claim is about shared structure across tasks, so whole task families must be tested.",
        "use_if": ["many task families exist", "shared structure is plausible", "whole families can be held out"],
        "avoid_if": ["the new task is only assumed to be covered", "rare regimes are missing", "scale is treated as proof of scientific trust"],
        "evidence_needed": "held-out task-family tests, trusted-solver comparisons, boundary and scale tests, and failure reports",
        "links": ["topics/foundation-models-for-pdes.html", "reader-checks/foundation-pde-check.html", "domains/many-pde-tasks.html"],
    },
]


PROVENANCE_GUIDES = [
    {
        "slug": "source-playlists",
        "title": "Source Playlists",
        "purpose": "Name the exact course sources used by the package.",
        "steps": [
            "Start from the two ETH Zurich AI in the Sciences and Engineering playlist URLs.",
            "Store one flat playlist manifest for each year.",
            "Use the playlist manifests to define the 40-video source set.",
            "Keep each generated video page linked back to the original YouTube video.",
        ],
        "local_files": ["raw-material/playlists/eth-aise-2024.json", "raw-material/playlists/eth-aise-2025.json"],
        "checks": ["40 video records are present", "each record has a source URL", "each record has at least one concept"],
    },
    {
        "slug": "transcript-extraction",
        "title": "Transcript Extraction",
        "purpose": "Show how captions become local source material.",
        "steps": [
            "Use yt-dlp to download metadata, English captions, and automatic captions when provided.",
            "Store raw VTT caption files by playlist and video id.",
            "Clean VTT captions into plain text transcripts.",
            "Keep raw VTT and cleaned text so extraction can be inspected later.",
        ],
        "local_files": ["raw-material/transcripts/eth-aise-2024/raw-vtt/", "raw-material/transcripts/eth-aise-2024/clean/", "raw-material/transcripts/eth-aise-2025/raw-vtt/", "raw-material/transcripts/eth-aise-2025/clean/"],
        "checks": ["available transcript count equals 40", "clean transcript paths are recorded", "raw caption paths are recorded when present"],
    },
    {
        "slug": "analysis-build",
        "title": "Analysis Build",
        "purpose": "Show how source text becomes concepts, themes, evidence, and pages.",
        "steps": [
            "Load playlist records, metadata paths, captions, and cleaned transcript text.",
            "Match concept keywords against title and transcript text.",
            "Build concept, theme, evidence, domain, decision, glossary, and learning-path data.",
            "Write JSON analysis files before rendering the HTML site.",
        ],
        "local_files": ["analysis/summary.json", "analysis/concept_atlas.json", "analysis/evidence_ledger.json", "analysis/"],
        "checks": ["concept atlas has required fields", "evidence ledger names support type and limit", "summary counts match generated pages"],
    },
    {
        "slug": "site-generation",
        "title": "Site Generation",
        "purpose": "Show how the package turns analysis data into reviewable pages.",
        "steps": [
            "Render the home page, transcript index, topic pages, video pages, and all guide layers.",
            "Write a page manifest listing every generated HTML page.",
            "Serve the site locally from the site directory for review.",
            "Validate that required pages and links exist before committing.",
        ],
        "local_files": ["site/index.html", "site/page-manifest.json", "site/topics/", "site/videos/"],
        "checks": ["page manifest has the expected page count", "required guide pages exist", "local HTTP checks return OK"],
    },
    {
        "slug": "cli-reproduction",
        "title": "CLI Reproduction Checklist",
        "purpose": "Give another CLI enough detail to reproduce this package for another channel.",
        "steps": [
            "Create a repo named after the topic, not after a temporary extraction job.",
            "Save raw playlists, metadata, raw captions, and clean transcripts separately.",
            "Build concept pages from first principles: problem, domain, why it matters, kept information, left-out information, and failure boundary.",
            "Add family routes, comparisons, worked examples, diagrams, learning path, glossary, domains, reader checks, and decision guide.",
            "Run build validation and a wording scan before committing.",
            "Before remote handoff, run git status --short --branch and make check.",
            "Create or grant access to the GitHub repository configured as origin.",
            "Run git push -u origin main, then verify git ls-remote --heads origin main matches git rev-parse main.",
        ],
        "local_files": ["scripts/build_physics_informed_ml_research_package.py", "README.md", "Makefile"],
        "checks": ["repo has a clear topic name", "raw source material is preserved", "generated pages are validated", "commits are small enough to review", "remote main hash matches local main after push"],
    },
    {
        "slug": "cross-channel-playbook",
        "title": "Cross-Channel Replication Playbook",
        "purpose": "Give another CLI an end-to-end operating plan for building the same kind of package from a different channel or playlist family.",
        "steps": [
            "Start with named source URLs, playlist titles, intended topic name, and a short description of the audience.",
            "Download playlist manifests, metadata, raw captions, automatic captions, and cleaned transcript text before writing analysis.",
            "Create a first concept seed list from titles, repeated transcript phrases, paper names, equations, methods, and domain words.",
            "For each concept, write the common problem, domain, importance, kept information, ignored information, and failure boundary in plain language.",
            "Group concepts into families, comparisons, worked examples, diagrams, learning path, glossary, domain guides, checks, decisions, coverage, derivations, and review entrypoints.",
            "Separate transcript evidence from proof: cite where the channel discusses a concept, then state what the transcript does not prove.",
            "Run build validation, link validation, wording checks, HTTP smoke checks, and a final clean git status before asking for review.",
        ],
        "local_files": ["raw-material/playlists/", "raw-material/metadata/", "raw-material/transcripts/", "analysis/", "site/", "exports/research-package.md"],
        "checks": ["source URLs are named", "raw and clean transcripts are preserved", "concept pages explain problem/domain/importance/failure", "review entrypoints and coverage pages exist", "validation commands pass"],
    },
]


QUALITY_RUBRIC = [
    {
        "slug": "first-principles",
        "title": "First Principles",
        "standard": "The page starts from the real problem, observed evidence, hidden quantity, and scientific job before naming a method.",
        "strong_page": "A reader can say what exists in the world, what is measured, what is missing, and why the method is needed.",
        "weak_page": "The page starts by naming a method and assumes the reader already knows why it matters.",
        "check": "Look for sections that name the common problem, domain, observed quantity, hidden quantity, and changed-case test.",
    },
    {
        "slug": "plain-language",
        "title": "Plain Language",
        "standard": "The page translates technical terms into everyday meaning without hiding the mathematical idea.",
        "strong_page": "Terms such as field, residual, operator, loss, and generalization are tied to concrete jobs.",
        "weak_page": "The page uses method names, benchmark language, or vague praise instead of explaining the idea.",
        "check": "Look for glossary links, everyday anchors, concrete domain stories, and plain formulas.",
    },
    {
        "slug": "domain-grounding",
        "title": "Domain Grounding",
        "standard": "The page says where the concept matters in science or engineering and what quantity is being predicted or explained.",
        "strong_page": "The domain, real quantity, and domain-specific failure test are visible.",
        "weak_page": "The page describes a general model but never says what scientific object or quantity it serves.",
        "check": "Look for domain guide links, worked examples, and concrete anchor pages.",
    },
    {
        "slug": "failure-boundary",
        "title": "Failure Boundary",
        "standard": "The page states what the concept does not prove and what changed case could reject the claim.",
        "strong_page": "A reader sees the use range, red flags, and first failure test.",
        "weak_page": "The page says the method works without stating where it breaks.",
        "check": "Look for failure boundary, red flags, reader checks, and decision guide evidence requirements.",
    },
    {
        "slug": "evidence-discipline",
        "title": "Evidence Discipline",
        "standard": "The page separates transcript support from scientific proof.",
        "strong_page": "Transcript evidence is shown as support that a concept appears, while validation claims require explicit tests.",
        "weak_page": "The page treats a lecture mention as proof that a method works broadly.",
        "check": "Look for transcript evidence, support type, and explicit evidence limits.",
    },
    {
        "slug": "connected-map",
        "title": "Connected Map",
        "standard": "The page connects the concept to nearby concepts, families, diagrams, decisions, or checks.",
        "strong_page": "A reader can move from the concept to a route, comparison, diagram, or decision case.",
        "weak_page": "The page is isolated and does not show how the idea fits into the field.",
        "check": "Look for concept links, families, comparisons, visual maps, and coverage matrix entries.",
    },
]


SYNTHESIS_GUIDES = [
    {
        "slug": "central-problem",
        "title": "Central Problem",
        "claim": "Physics-informed machine learning asks how a learned answer can stay tied to the real scientific problem when measurements are sparse, equations are partial, simulations are costly, and future cases are different.",
        "explanation": "Start with the world, not the model. A scientist needs a quantity such as a temperature field, a force, a molecule property, or a failure risk. The available evidence is incomplete: some measurements, some equations, some solved cases, some trusted simulations. The mathematical job is to carry that evidence into a new case while leaving a clear test that can reject the answer.",
        "reader_takeaway": "A strong explanation names five things: the real quantity, the evidence, the missing quantity, the mathematical move, and the changed case that could reject the claim.",
        "links": ["learning-path.html", "decision-guide.html", "quality/first-principles.html"],
    },
    {
        "slug": "main-moves",
        "title": "Main Moves",
        "claim": "The main mathematical moves are different answers to different shortages: too few measurements, too many related solves, too much simulation cost, too much change between cases, or too little understanding of the rule.",
        "explanation": "PINNs add equation checks where measurements are missing. Operator learning learns a field-to-field map when many related solves are needed. Surrogates build a fast checked stand-in when the trusted source is too slow. Uncertainty asks when belief should weaken. Symbolic regression asks whether the data can support a readable rule.",
        "reader_takeaway": "Choose the move by naming the shortage first. If the shortage is unclear, the method choice is not yet justified.",
        "links": ["families.html", "comparisons.html", "diagrams.html"],
    },
    {
        "slug": "proof-burden",
        "title": "Proof Burden",
        "claim": "A method name never proves a scientific claim. The claim needs a test tied to the domain quantity the scientist will use.",
        "explanation": "A transcript mention shows that a topic appears in the course. A training score shows that a model matched a written score. Neither one alone proves that the model is safe for a new scientific use. The page has to state the domain, quantity, use range, evidence, and failure test.",
        "reader_takeaway": "Every strong page should say what the source supports, what remains unproved, and what changed case would expose a bad claim.",
        "links": ["evidence-ledger.html", "reader-checks.html", "quality/evidence-discipline.html"],
    },
    {
        "slug": "field-map",
        "title": "Field Map",
        "claim": "The field is best read as a map from scientific jobs to mathematical moves, not as a list of model names.",
        "explanation": "Sparse measurements point toward physics checks. Many solved fields point toward operator learning. Repeated costly decisions point toward surrogates. New settings point toward uncertainty. Need for a readable law points toward model discovery. Each route starts with a real quantity and ends with a failure test.",
        "reader_takeaway": "Start from the job, identify the shortage, then choose the concept family that carries the right evidence.",
        "links": ["decision-guide.html", "domains.html", "coverage.html"],
    },
]


REVIEW_HANDOFF = {
    "title": "Review Handoff",
    "purpose": "Give a reviewer the shortest reliable route through the package and the checks that prove the generated site is coherent.",
    "start_here": [
        {"label": "Field Synthesis", "href": "synthesis.html"},
        {"label": "Learning Path", "href": "learning-path.html"},
        {"label": "Coverage Matrix", "href": "coverage.html"},
        {"label": "Editorial Roadmap", "href": "editorial-roadmap.html"},
        {"label": "Decision Guide", "href": "decision-guide.html"},
        {"label": "Provenance", "href": "provenance.html"},
    ],
    "core_review_pages": [
        {"label": "PINNs", "href": "topics/physics-informed-neural-networks.html"},
        {"label": "Operator Learning", "href": "topics/operator-learning.html"},
        {"label": "Surrogate Modeling", "href": "topics/surrogate-modeling.html"},
        {"label": "Uncertainty And Generalization", "href": "topics/uncertainty-and-generalization.html"},
        {"label": "Symbolic Regression", "href": "topics/symbolic-regression.html"},
        {"label": "Foundation Models For PDEs", "href": "topics/foundation-models-for-pdes.html"},
    ],
    "validation_commands": [
        "python3 -m py_compile scripts/build_physics_informed_ml_research_package.py",
        "python3 scripts/build_physics_informed_ml_research_package.py --build --validate",
        "run the wording scan for restricted filler terms listed in the editorial quality rubric",
    ],
    "remaining_editorial_work": [
        "Remote repository is created and main is pushed.",
        "For any later commit, run git push and compare git ls-remote origin main with git rev-parse main.",
        "Keep this handoff updated whenever the latest local commit changes.",
        "Optional later editorial work: replace selected source anchors with manually verified short lecture quotes.",
    ],
    "remote_finish_commands": [
        "git status --short --branch",
        "git remote -v",
        "git rev-parse main",
        "git ls-remote --heads origin main",
        "git push -u origin main",
    ],
    "remote_status": "Configured origin is https://github.com/mehtama1234/physics-informed-machine-learning-concepts-research.git. The repository exists, main is pushed, and origin/main should match local main after each final push.",
}


EDITORIAL_ROADMAP = [
    {
        "priority": "P0",
        "slug": "pinning-the-core-argument",
        "title": "Pin Down The Core Argument",
        "goal": "Make the first review route say one thing clearly: physics-informed machine learning is about making learned answers answerable to data, physical rules, and changed scientific cases.",
        "why": "Without this, readers see a pile of methods. With it, every concept becomes a different answer to the same scientific pressure.",
        "target_pages": [
            {"label": "Field Synthesis", "href": "synthesis.html"},
            {"label": "Learning Path", "href": "learning-path.html"},
            {"label": "Review Handoff", "href": "handoff.html"},
            {"label": "Completion Audit", "href": "completion-audit.html"},
        ],
        "work": [
            "Rewrite the opening paragraphs so they start from the scientific problem before naming methods.",
            "Make every route explain what is observed, what is hidden, what rule is kept, and what changed case can reject the claim.",
            "Remove any sentence that sounds impressive but does not name evidence, domain, quantity, or failure test.",
        ],
        "acceptance_check": "A new reader can say the field's common problem in one sentence before opening any topic page.",
    },
    {
        "priority": "P0",
        "slug": "source-anchored-core-concepts",
        "title": "Add Source Anchors To Core Concepts",
        "goal": "Turn the main topic pages and evidence packets into source-backed teaching pages, not only generated summaries.",
        "why": "The package is transcript-backed only if the important claims point to lecture-specific support and state what that support does not prove.",
        "target_pages": [
            {"label": "PINNs Topic", "href": "topics/physics-informed-neural-networks.html"},
            {"label": "Operator Learning Topic", "href": "topics/operator-learning.html"},
            {"label": "Uncertainty Topic", "href": "topics/uncertainty-and-generalization.html"},
            {"label": "Foundation PDE Topic", "href": "topics/foundation-models-for-pdes.html"},
            {"label": "Evidence Packets", "href": "evidence-packets.html"},
        ],
        "work": [
            "Manually review the transcript excerpts for each core concept and choose the best source anchors.",
            "Add a short source note beside each major claim: what the lecture supports, and what it does not settle.",
            "Prefer concrete lecture moments over broad statements.",
        ],
        "acceptance_check": "Each core concept has at least two reviewed transcript anchors and one clear limit statement.",
    },
    {
        "priority": "P0",
        "slug": "hand-derivations",
        "title": "Deepen The Hand Derivations",
        "goal": "Make the math feel inevitable from the problem instead of appearing as a finished formula.",
        "why": "The reader should see why the terms show up: data error comes from measured points, physics error comes from the equation, uncertainty comes from possible wrong answers, and operators come from learning a map between fields.",
        "target_pages": [
            {"label": "Core Derivations", "href": "derivations.html"},
            {"label": "PINNs Derivation", "href": "derivations/physics-informed-neural-networks.html"},
            {"label": "Operator Learning Derivation", "href": "derivations/operator-learning.html"},
            {"label": "Foundation PDE Derivation", "href": "derivations/foundation-models-for-pdes.html"},
            {"label": "Plain Formula Guide", "href": "formula-guide.html"},
        ],
        "work": [
            "Add one handwritten derivation from observed evidence to loss shape for PINNs.",
            "Add one derivation showing why operator learning maps a whole input field to a whole output field.",
            "Add one derivation showing what must be shared before a PDE model can transfer to a new equation case.",
            "Keep each line in everyday language before adding symbols.",
        ],
        "acceptance_check": "A reader who skips the formula can still explain why each term exists and what would make it fail.",
    },
    {
        "priority": "P1",
        "slug": "figures-and-sketches",
        "title": "Add Figures And Mathematical Sketches",
        "goal": "Replace purely textual explanation where a picture would reveal the object being learned or checked.",
        "why": "Some ideas are spatial: a PDE field, a boundary, a residual point, an input field, an output field, or a shifted test case. A sketch can make the hidden quantity visible.",
        "target_pages": [
            {"label": "Diagrams", "href": "diagrams.html"},
            {"label": "PINNs Topic", "href": "topics/physics-informed-neural-networks.html"},
            {"label": "Operator Learning Topic", "href": "topics/operator-learning.html"},
            {"label": "Surrogate Modeling Topic", "href": "topics/surrogate-modeling.html"},
            {"label": "Uncertainty Topic", "href": "topics/uncertainty-and-generalization.html"},
        ],
        "work": [
            "Add one sketch for measured points plus equation-check points.",
            "Add one sketch for input field to output field.",
            "Add one sketch for a fast surrogate inside repeated scientific choices.",
            "Add one sketch for a shifted case where the model should admit doubt.",
        ],
        "acceptance_check": "Each sketch names input, output, kept rule, and failure case in the caption.",
    },
    {
        "priority": "P1",
        "slug": "domain-examples",
        "title": "Strengthen Domain Examples",
        "goal": "Make chemistry, materials, climate, fluids, and geometry pages show real scientific jobs rather than generic use cases.",
        "why": "The math matters because a scientist needs a quantity for a decision: a molecule property, stress field, flow force, climate risk, or field on an irregular shape.",
        "target_pages": [
            {"label": "Domain Guides", "href": "domains.html"},
            {"label": "Worked Examples", "href": "worked-examples.html"},
            {"label": "Molecule Example", "href": "worked-examples/molecule-property-from-structure.html"},
            {"label": "Material Example", "href": "worked-examples/material-stress-from-sparse-tests.html"},
            {"label": "Climate Example", "href": "worked-examples/climate-risk-under-shifted-conditions.html"},
        ],
        "work": [
            "Add one richer concrete example per domain.",
            "Name the observed evidence, hidden quantity, decision, and changed-case test.",
            "Tie each example back to one concept page, one derivation, and one evidence packet.",
        ],
        "acceptance_check": "Each domain page contains a concrete scientific job that cannot be mistaken for a generic prediction task.",
    },
    {
        "priority": "P1",
        "slug": "compare-nearby-methods",
        "title": "Sharpen Nearby Method Comparisons",
        "goal": "Make the comparison pages teach what changes when two methods sound similar.",
        "why": "Readers often confuse fitting data, obeying a rule, learning a solver shortcut, and building a cheap stand-in. The package should separate those by job and evidence.",
        "target_pages": [
            {"label": "Comparisons", "href": "comparisons.html"},
            {"label": "Decision Guide", "href": "decision-guide.html"},
            {"label": "Misconception Map", "href": "misconceptions.html"},
            {"label": "Concept Dependency Map", "href": "dependencies.html"},
        ],
        "work": [
            "For each comparison, add one situation where the left method is right and one where the right method is right.",
            "Add one wrong-choice example and the evidence that would expose it.",
            "Keep the language tied to the scientific job, not method labels.",
        ],
        "acceptance_check": "A reader can choose between two nearby methods by naming the job, evidence, and failure case.",
    },
    {
        "priority": "P2",
        "slug": "replication-and-remote-finish",
        "title": "Finish Replication And Remote State",
        "goal": "Make the package easy for another CLI to reproduce and push once the GitHub repository exists.",
        "why": "Local validation proves the package files. The final handoff also needs a verified remote so another person can clone and continue.",
        "target_pages": [
            {"label": "Cross-Channel Playbook", "href": "provenance/cross-channel-playbook.html"},
            {"label": "Provenance", "href": "provenance.html"},
            {"label": "Completion Audit", "href": "completion-audit.html"},
            {"label": "Handoff", "href": "handoff.html"},
        ],
        "work": [
            "Create or grant access to the GitHub repository named by origin.",
            "Push main and verify the branch exists remotely.",
            "Record the clone URL and latest commit in the handoff.",
        ],
        "acceptance_check": "git ls-remote origin main returns a commit hash that matches the local main branch.",
    },
]


ROADMAP_STATUS = {
    "pinning-the-core-argument": {
        "status": "locally completed",
        "evidence": "The home page, synthesis pages, and learning path now use the five-part route: real quantity, evidence, missing quantity, mathematical move, and changed-case test.",
        "proof_pages": ["index.html", "synthesis/central-problem.html", "learning-path/scientific-question-first.html"],
    },
    "source-anchored-core-concepts": {
        "status": "locally completed",
        "evidence": "Core topic pages and evidence packets include selected source anchors with claim, source page, reason, and limit.",
        "proof_pages": ["topics/physics-informed-neural-networks.html", "evidence-packets/foundation-models-for-pdes.html", "evidence-packets/operator-learning.html"],
    },
    "hand-derivations": {
        "status": "locally completed",
        "evidence": "Core derivation pages include Hand Derivation tables that explain each term, why it enters, and how to check it.",
        "proof_pages": ["derivations/physics-informed-neural-networks.html", "derivations/operator-learning.html", "derivations/foundation-models-for-pdes.html"],
    },
    "figures-and-sketches": {
        "status": "locally completed",
        "evidence": "The diagrams index and core topic pages include mathematical sketches with input, output, kept rule, and failure case.",
        "proof_pages": ["diagrams.html", "topics/operator-learning.html", "topics/surrogate-modeling.html"],
    },
    "domain-examples": {
        "status": "locally completed",
        "evidence": "Each domain guide includes a concrete scientific job with observed evidence, hidden quantity, decision, and changed-case test.",
        "proof_pages": ["domains/chemistry-and-biology.html", "domains/materials-and-mechanics.html", "domains/many-pde-tasks.html"],
    },
    "compare-nearby-methods": {
        "status": "locally completed",
        "evidence": "Each comparison page includes left-case, right-case, wrong-choice case, and evidence that exposes the wrong choice.",
        "proof_pages": ["comparisons/pinns-vs-neural-operators.html", "comparisons/solvers-vs-learned-surrogates.html"],
    },
    "replication-and-remote-finish": {
        "status": "locally completed",
        "evidence": "The GitHub repository exists, main is pushed, and git ls-remote origin main can be compared with git rev-parse main after each final push.",
        "proof_pages": ["completion-audit.html", "handoff.html", "provenance/cli-reproduction.html"],
    },
}


MEATY_END_TO_END_GOAL = {
    "title": "Meaty End-To-End Goal",
    "short_goal": "Turn the Physics-Informed Machine Learning site from a structured first-pass atlas into a teaching-grade research package that explains the paper family from first principles.",
    "target_reader": "A new reader who does not know the math, machine learning terms, benchmark language, causal language, optimization language, or systems language.",
    "done_means": [
        "The reader can start from a plain scientific problem before seeing a method name.",
        "The reader can name the real quantity being predicted, explained, controlled, designed, or discovered.",
        "The reader can name the available evidence: measurements, equations, simulations, boundary information, geometry, prior cases, or transcript support.",
        "The reader can name what is hidden, missing, or unknown.",
        "The reader can explain why the mathematical move follows from that missing piece.",
        "The reader can translate the formula shape into everyday language.",
        "The reader can say which domain the idea belongs to and why solving it matters there.",
        "The reader can say what the method keeps, what it ignores, and where it fails.",
        "The reader can name the changed case that would reject an overclaim.",
        "The reader can connect the concept to nearby concepts, examples, diagrams, and source anchors.",
    ],
    "core_pages": [
        {"label": "PINNs", "href": "topics/physics-informed-neural-networks.html"},
        {"label": "PDEs", "href": "topics/partial-differential-equations.html"},
        {"label": "Operator Learning", "href": "topics/operator-learning.html"},
        {"label": "Surrogate Modeling", "href": "topics/surrogate-modeling.html"},
        {"label": "Uncertainty And Generalization", "href": "topics/uncertainty-and-generalization.html"},
        {"label": "Symbolic Regression", "href": "topics/symbolic-regression.html"},
        {"label": "Neural Differential Equations", "href": "topics/neural-differential-equations.html"},
        {"label": "Foundation Models For PDEs", "href": "topics/foundation-models-for-pdes.html"},
        {"label": "Attention For Scientific Fields", "href": "topics/attention-for-scientific-fields.html"},
        {"label": "Graphs And Geometric Learning", "href": "topics/graphs-and-geometric-learning.html"},
        {"label": "Optimization For Learning", "href": "topics/optimization-for-learning.html"},
        {"label": "Generative Modeling", "href": "topics/generative-modeling.html"},
        {"label": "Scientific Machine Learning", "href": "topics/scientific-machine-learning.html"},
    ],
    "page_requirements": [
        "A concrete domain story that starts from a real scientific job.",
        "A first-principles derivation from observed evidence to hidden quantity to mathematical move.",
        "A plain formula explanation that says what every term carries.",
        "A worked example and a wrong-use example.",
        "A failure boundary and a changed-case rejection test.",
        "Transcript anchors that state what the source supports and what it does not prove.",
        "Links to nearby concepts, diagrams, derivations, examples, and reader checks.",
    ],
    "acceptance_sentence": "This concept exists because scientists need ___, but they only observe ___. The hidden thing is ___. The math does ___ because ___. It matters in ___ domain because ___. It fails when ___. I would test it by changing ___.",
    "not_done_if": [
        "The page starts with a method name but does not explain the world problem first.",
        "The page says a model learns patterns without naming the quantity, evidence, hidden part, and failure test.",
        "The page uses broad confidence words instead of a changed-case test.",
        "The page has transcript evidence but does not state what the evidence fails to prove.",
        "The page cannot be retold by a new reader in ordinary language.",
    ],
}


SOURCE_ANCHORS = {
    "physics-informed-neural-networks": [
        {
            "claim": "PINNs are introduced as learned fields checked against both measured data and physical equations.",
            "source": "ETH Zurich AISE 2025: Lecture 3 Physics-Informed Neural Networks Introduction",
            "href": "videos/eth-aise-2025-003-eth-zrich-aise-2025-lecture-3-physics-informed-neural-networks-introduction.html",
            "why_this_source": "This is the 2025 introductory PINNs lecture in the local transcript set.",
            "limit": "The source supports the course placement and core idea; it does not prove performance on every PDE or boundary setting.",
        },
        {
            "claim": "PINNs need theory and failure checks because satisfying a written training score is not the same as proving the field is right everywhere.",
            "source": "ETH Zurich AISE 2025: Lecture 4 PINNs Theoretical Insights",
            "href": "videos/eth-aise-2025-004-eth-zrich-aise-2025-lecture-4-pinns-theoretical-insights.html",
            "why_this_source": "This lecture is the 2025 theory follow-up for PINNs.",
            "limit": "The source anchors the need for theoretical care; the page still needs task-specific validation for any scientific claim.",
        },
    ],
    "operator-learning": [
        {
            "claim": "Operator learning is about learning maps from whole input fields or functions to whole output fields or functions.",
            "source": "ETH Zurich AISE 2025: Lecture 5 Operator Learning Introduction",
            "href": "videos/eth-aise-2025-005-eth-zrich-aise-2025-lecture-5-operator-learning-introduction.html",
            "why_this_source": "This is the 2025 introduction to the operator-learning block.",
            "limit": "The source supports the object being learned; it does not prove the learned map works outside the named input family.",
        },
        {
            "claim": "Fourier neural operators are one route for learning field-to-field maps in PDE settings.",
            "source": "ETH Zurich AISE 2025: Lecture 6 Operator Learning FNO",
            "href": "videos/eth-aise-2025-006-eth-zrich-aise-2025-lecture-6-operator-learning-fno.html",
            "why_this_source": "This lecture is the 2025 FNO treatment inside the operator-learning sequence.",
            "limit": "The source anchors the method family; reliability still depends on the training range, resolution, geometry, and target quantity.",
        },
    ],
    "surrogate-modeling": [
        {
            "claim": "Surrogates are useful when repeated scientific choices need answers faster than a trusted simulation or experiment can provide them.",
            "source": "ETH Zurich AISE 2024: Introduction to Hybrid Workflows Part 1",
            "href": "videos/eth-aise-2024-019-eth-zrich-aise-introduction-to-hybrid-workflows-part-1.html",
            "why_this_source": "This lecture starts the local hybrid-workflow block where learned components are placed next to trusted scientific tools.",
            "limit": "The source supports the need for faster learned components; it does not prove a surrogate is valid outside checked cases.",
        },
        {
            "claim": "A learned stand-in remains tied to the trusted source and must be checked where it will be used.",
            "source": "ETH Zurich AISE 2024: Introduction to Hybrid Workflows Part 2",
            "href": "videos/eth-aise-2024-020-eth-zrich-aise-introduction-to-hybrid-workflows-part-2.html",
            "why_this_source": "This lecture continues the hybrid-workflow treatment in the local transcript set.",
            "limit": "The source supports the review route; task-level error checks are still needed before using any stand-in for a decision.",
        },
    ],
    "uncertainty-and-generalization": [
        {
            "claim": "Trust depends on changed-case behavior, not only on matching familiar examples.",
            "source": "ETH Zurich AISE 2024: Windowed Attention and Scaling Laws",
            "href": "videos/eth-aise-2024-018-eth-zrich-aise-windowed-attention-and-scaling-laws.html",
            "why_this_source": "This source sits in the sequence where model behavior is discussed beyond a single training case.",
            "limit": "The source anchors the need to discuss scale and changed behavior; it does not certify uncertainty estimates for a specific domain.",
        },
        {
            "claim": "Foundation and operator-style PDE models need evaluation on held-out scientific cases before broad use.",
            "source": "ETH Zurich AISE 2025: Lecture 12 Foundation Models for PDEs Poseidon",
            "href": "videos/eth-aise-2025-012-eth-zrich-aise-2025-lecture-12-foundation-models-for-pdes-poseidon.html",
            "why_this_source": "This lecture anchors the broad PDE-model part of the 2025 playlist.",
            "limit": "The source supports the need for held-out case checks; it does not prove broad transfer for every equation family.",
        },
    ],
    "symbolic-regression": [
        {
            "claim": "Symbolic regression aims for a readable candidate law, not just a fitted prediction.",
            "source": "ETH Zurich AISE 2024: Symbolic Regression and Model Discovery",
            "href": "videos/eth-aise-2024-024-eth-zrich-aise-symbolic-regression-and-model-discovery.html",
            "why_this_source": "This is the local lecture dedicated to symbolic regression and model discovery.",
            "limit": "The source supports the concept and goal; a discovered law still needs a new-experiment test and measured variables that cover the real cause.",
        },
        {
            "claim": "Neural differential equations are a related route when the unknown object is the rate or rule of change.",
            "source": "ETH Zurich AISE 2024: Neural Differential Equations",
            "href": "videos/eth-aise-2024-021-eth-zrich-aise-neural-differential-equations.html",
            "why_this_source": "This lecture anchors the neighboring model-discovery route in the source set.",
            "limit": "The source supports the relation between learned dynamics and model discovery; it does not prove interpretability by itself.",
        },
    ],
    "foundation-models-for-pdes": [
        {
            "claim": "Foundation PDE models try to carry structure from many PDE tasks into a new PDE case.",
            "source": "ETH Zurich AISE 2025: Lecture 12 Foundation Models for PDEs Poseidon",
            "href": "videos/eth-aise-2025-012-eth-zrich-aise-2025-lecture-12-foundation-models-for-pdes-poseidon.html",
            "why_this_source": "This lecture is the 2025 source page for foundation models for PDEs.",
            "limit": "The source anchors the ambition and lecture treatment; the page must still state which new PDE case was held out and what failed.",
        },
        {
            "claim": "Broad PDE models build on operator-learning ideas because both care about maps between fields across many cases.",
            "source": "ETH Zurich AISE 2025: Lecture 5 Operator Learning Introduction",
            "href": "videos/eth-aise-2025-005-eth-zrich-aise-2025-lecture-5-operator-learning-introduction.html",
            "why_this_source": "This lecture anchors the operator-learning prerequisite for later broad PDE models.",
            "limit": "The source supports the dependency; it does not imply that a broad model works on every PDE family.",
        },
    ],
}


REVIEW_ENTRYPOINTS = [
    {
        "group": "Start The Review",
        "purpose": "Use these pages to see the whole argument before inspecting details.",
        "items": [
            {
                "label": "Review Handoff",
                "href": "handoff.html",
                "why": "Shows counts, validation commands, core pages, and remaining editorial work.",
                "question": "What exists now, and what still needs hand-written depth?",
            },
            {
                "label": "Find Pages By Question",
                "href": "review-search.html",
                "why": "Maps reviewer intents to the strongest pages for that job.",
                "question": "Which page should I open for the question I have right now?",
            },
            {
                "label": "Completion Audit",
                "href": "completion-audit.html",
                "why": "Maps the requested package requirements to local evidence and external status.",
                "question": "What is locally verified, and what is still outside the workspace?",
            },
            {
                "label": "Editorial Roadmap",
                "href": "editorial-roadmap.html",
                "why": "Turns the remaining hand-written depth work into prioritized tasks with acceptance checks.",
                "question": "What is the meaty next goal after the generated first pass?",
            },
            {
                "label": "Meaty Goal",
                "href": "meaty-goal.html",
                "why": "States the end-to-end done criteria for making the package teaching-grade rather than merely structured.",
                "question": "What must be true before these writeups should count as done?",
            },
            {
                "label": "Field Synthesis",
                "href": "synthesis.html",
                "why": "Turns the course family into one plain-language map of scientific jobs.",
                "question": "What problem holds the field together?",
            },
            {
                "label": "Learning Path",
                "href": "learning-path.html",
                "why": "Gives a reader who knows no jargon a route from data to scientific claims.",
                "question": "What should a new reader read first, second, and third?",
            },
            {
                "label": "Concept Ladder",
                "href": "concept-ladder.html",
                "why": "Lines up each concept by observed evidence, hidden quantity, mathematical move, and failure test.",
                "question": "Can each concept be explained without starting from the method name?",
            },
            {
                "label": "Dependency Map",
                "href": "dependencies.html",
                "why": "Shows what ideas to learn before each harder concept and what confusion that prevents.",
                "question": "Which missing prerequisite is making the concept feel vague?",
            },
            {
                "label": "Core Derivations",
                "href": "derivations.html",
                "why": "Slows the key mathematical ideas into plain step-by-step walkthroughs.",
                "question": "Can the reader see how the formula shape follows from the scientific problem?",
            },
            {
                "label": "Formula Guide",
                "href": "formula-guide.html",
                "why": "Translates plain formula shapes into parts, meaning, checks, and common misreads.",
                "question": "Can the reader understand what the formula carries without knowing notation first?",
            },
            {
                "label": "Misconception Map",
                "href": "misconceptions.html",
                "why": "Lists common wrong turns and the plain correction for each core concept.",
                "question": "Which vague or overconfident explanation should the reader avoid?",
            },
        ],
    },
    {
        "group": "Inspect Core Concepts",
        "purpose": "Use these pages to judge whether the main mathematical ideas are explained from first principles.",
        "items": [
            {
                "label": "PINNs",
                "href": "topics/physics-informed-neural-networks.html",
                "why": "Covers sparse measurements, known equations, equation error, and failure regions.",
                "question": "How can a learned curve be pushed to obey a known physical rule?",
            },
            {
                "label": "Operator Learning",
                "href": "topics/operator-learning.html",
                "why": "Covers learning maps from input fields to solution fields across a family of cases.",
                "question": "When is the object being learned a whole solver shortcut?",
            },
            {
                "label": "Surrogate Modeling",
                "href": "topics/surrogate-modeling.html",
                "why": "Covers cheap stand-ins for costly simulations and the limits of that trade.",
                "question": "When is speed useful, and where does it stop being trustworthy?",
            },
            {
                "label": "Uncertainty And Generalization",
                "href": "topics/uncertainty-and-generalization.html",
                "why": "Covers prediction limits, changed cases, and the difference between fit and trust.",
                "question": "How does the page say where the model may be wrong?",
            },
            {
                "label": "Symbolic Regression",
                "href": "topics/symbolic-regression.html",
                "why": "Covers searching for readable equations from observed variables and changed-case tests.",
                "question": "When is a short formula a scientific claim instead of a curve fit?",
            },
            {
                "label": "Foundation Models For PDEs",
                "href": "topics/foundation-models-for-pdes.html",
                "why": "Covers broad PDE training, shared structure, and held-out scientific tasks.",
                "question": "What must carry from old equation cases to a new one?",
            },
        ],
    },
    {
        "group": "Use The Package",
        "purpose": "Use these pages when choosing a method for a concrete scientific situation.",
        "items": [
            {
                "label": "Decision Guide",
                "href": "decision-guide.html",
                "why": "Starts from the scientific situation and names the evidence needed for a method choice.",
                "question": "Which method family fits the job in front of the reader?",
            },
            {
                "label": "Domain Guides",
                "href": "domains.html",
                "why": "Grounds the concepts in real domains such as fluids, climate, molecules, and materials.",
                "question": "What quantity does this domain actually need?",
            },
            {
                "label": "Worked Examples",
                "href": "worked-examples.html",
                "why": "Shows observed evidence, hidden quantity, method route, and failure test in concrete cases.",
                "question": "Can the reader follow one scientific job all the way through?",
            },
            {
                "label": "Comparisons",
                "href": "comparisons.html",
                "why": "Separates nearby methods by job, evidence, and failure case.",
                "question": "What changes when two methods sound similar?",
            },
        ],
    },
    {
        "group": "Check Coverage And Sources",
        "purpose": "Use these pages to audit completeness, source support, and wording quality.",
        "items": [
            {
                "label": "Coverage Matrix",
                "href": "coverage.html",
                "why": "Shows which concepts have evidence, deep dives, diagrams, checks, domains, and decisions.",
                "question": "Which important concepts still need more support?",
            },
            {
                "label": "Evidence Ledger",
                "href": "evidence-ledger.html",
                "why": "Links claims back to transcript or metadata evidence and states each limit.",
                "question": "What does the transcript support, and what does it not prove?",
            },
            {
                "label": "Evidence Packets",
                "href": "evidence-packets.html",
                "why": "Gathers transcript anchors, limits, and review links one concept at a time.",
                "question": "Can a reviewer audit one concept without hunting through the whole site?",
            },
            {
                "label": "Quality Rubric",
                "href": "quality.html",
                "why": "Defines the editorial standard for plain first-principles pages.",
                "question": "Does each page avoid empty language and explain the real problem?",
            },
            {
                "label": "Provenance",
                "href": "provenance.html",
                "why": "Documents source playlists, caption extraction, local files, and reproduction commands.",
                "question": "Could another CLI rebuild this package from the same sources?",
            },
            {
                "label": "Cross-Channel Playbook",
                "href": "provenance/cross-channel-playbook.html",
                "why": "Gives another CLI the ordered steps for creating the same kind of package from a different channel.",
                "question": "What exact source, concept, evidence, page, and validation steps should the next build follow?",
            },
        ],
    },
]


COMPLETION_REQUIREMENTS = [
    {
        "slug": "source-and-transcripts",
        "requirement": "Preserve transcript-backed source material for the two playlist family.",
        "local_evidence": "summary reports 2 playlists, 40 videos, and 40 available transcripts; provenance pages name playlists, caption extraction, and local files.",
        "status": "locally verified",
        "links": ["transcripts.html", "provenance/source-playlists.html", "provenance/transcript-extraction.html"],
    },
    {
        "slug": "plain-first-principles-concepts",
        "requirement": "Explain mathematical concepts from first principles without assuming prior jargon.",
        "local_evidence": "topic pages, concept ladder, glossary, derivations, and quality rubric require problem, domain, observed evidence, hidden quantity, formula shape, and failure test.",
        "status": "locally verified",
        "links": ["concept-atlas.html", "concept-ladder.html", "derivations.html", "quality.html"],
    },
    {
        "slug": "domains-and-examples",
        "requirement": "Connect concepts to real domains and concrete scientific jobs.",
        "local_evidence": "summary reports 5 domain guides and 8 worked examples; domain guides include concrete scientific job cards and worked examples include end-to-end flow traces.",
        "status": "locally verified",
        "links": ["domains.html", "worked-examples.html"],
    },
    {
        "slug": "evidence-discipline",
        "requirement": "Separate transcript support from proof and show limits of every claim.",
        "local_evidence": "evidence ledger and 14 concept evidence packets state transcript anchors, review links, and what evidence does not prove.",
        "status": "locally verified",
        "links": ["evidence-ledger.html", "evidence-packets.html", "coverage.html"],
    },
    {
        "slug": "review-and-replication",
        "requirement": "Give reviewers and another CLI an end-to-end route through the package.",
        "local_evidence": "review map, editorial roadmap, handoff, provenance, and cross-channel playbook name review route, extraction steps, build outputs, next tasks, and validation checks.",
        "status": "locally verified",
        "links": ["review-entrypoints.html", "editorial-roadmap.html", "handoff.html", "provenance/cross-channel-playbook.html"],
    },
    {
        "slug": "local-validation",
        "requirement": "Run local checks proving generated pages, links, counts, and wording gates are coherent.",
        "local_evidence": "make check runs Python compile, build validation, and standalone generated-site validation; validator expects the manifest page count and required sections.",
        "status": "locally verified",
        "links": ["provenance/site-generation.html", "provenance/analysis-build.html"],
    },
    {
        "slug": "remote-repository",
        "requirement": "Create or verify the GitHub remote repository and push main.",
        "local_evidence": "origin is configured at https://github.com/mehtama1234/physics-informed-machine-learning-concepts-research.git; main has been pushed and can be verified with git ls-remote --heads origin main.",
        "status": "locally verified",
        "links": ["handoff.html", "provenance/cli-reproduction.html"],
    },
]


REVIEW_SEARCH_INDEX = [
    {
        "intent": "I need the big picture first.",
        "look_for": "central problem, field map, learning order, and completion state",
        "pages": [
            {"label": "Completion Audit", "href": "completion-audit.html"},
            {"label": "Editorial Roadmap", "href": "editorial-roadmap.html"},
            {"label": "Field Synthesis", "href": "synthesis.html"},
            {"label": "Learning Path", "href": "learning-path.html"},
            {"label": "Review Handoff", "href": "handoff.html"},
        ],
    },
    {
        "intent": "I need to know the next serious goal.",
        "look_for": "priorities, hand-written depth tasks, target pages, and acceptance checks",
        "pages": [
            {"label": "Editorial Roadmap", "href": "editorial-roadmap.html"},
            {"label": "Review Entrypoints", "href": "review-entrypoints.html"},
            {"label": "Quality Rubric", "href": "quality.html"},
            {"label": "Core Derivations", "href": "derivations.html"},
        ],
    },
    {
        "intent": "I need to understand a concept from first principles.",
        "look_for": "problem, observed evidence, hidden quantity, formula shape, and failure test",
        "pages": [
            {"label": "Concept Ladder", "href": "concept-ladder.html"},
            {"label": "Dependency Map", "href": "dependencies.html"},
            {"label": "Formula Guide", "href": "formula-guide.html"},
            {"label": "Misconception Map", "href": "misconceptions.html"},
        ],
    },
    {
        "intent": "I need transcript support for a claim.",
        "look_for": "source video, transcript excerpt, support limit, and review links",
        "pages": [
            {"label": "Evidence Packets", "href": "evidence-packets.html"},
            {"label": "Evidence Ledger", "href": "evidence-ledger.html"},
            {"label": "Transcripts", "href": "transcripts.html"},
            {"label": "Coverage Matrix", "href": "coverage.html"},
        ],
    },
    {
        "intent": "I need to choose a method for a scientific job.",
        "look_for": "domain, quantity, method route, use range, and required evidence",
        "pages": [
            {"label": "Decision Guide", "href": "decision-guide.html"},
            {"label": "Domain Guides", "href": "domains.html"},
            {"label": "Worked Examples", "href": "worked-examples.html"},
            {"label": "Comparisons", "href": "comparisons.html"},
        ],
    },
    {
        "intent": "I need to audit quality.",
        "look_for": "plain language, failure boundary, evidence discipline, and connected map",
        "pages": [
            {"label": "Quality Rubric", "href": "quality.html"},
            {"label": "Reader Checks", "href": "reader-checks.html"},
            {"label": "Misconception Map", "href": "misconceptions.html"},
            {"label": "Completion Audit", "href": "completion-audit.html"},
        ],
    },
    {
        "intent": "I need another CLI to reproduce this for a different channel.",
        "look_for": "source capture, transcript extraction, analysis build, site generation, and review gates",
        "pages": [
            {"label": "Cross-Channel Playbook", "href": "provenance/cross-channel-playbook.html"},
            {"label": "CLI Reproduction Checklist", "href": "provenance/cli-reproduction.html"},
            {"label": "Transcript Extraction", "href": "provenance/transcript-extraction.html"},
            {"label": "Analysis Build", "href": "provenance/analysis-build.html"},
        ],
    },
]


@dataclass
class TranscriptRecord:
    video_id: str
    playlist_slug: str
    playlist_title: str
    index: int
    title: str
    url: str
    transcript_status: str
    clean_txt: str
    raw_vtt: str
    metadata_json: str
    word_count: int
    concepts: list[str]
    themes: list[str]
    evidence_excerpt: str


def slugify(value: str) -> str:
    value = re.sub(r"[^\w\s-]", "", value.lower(), flags=re.ASCII)
    value = re.sub(r"[-\s]+", "-", value).strip("-")
    return value or "item"


def playlist_id(url: str) -> str:
    return parse_qs(urlparse(url).query).get("list", [""])[0]


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, cwd=ROOT, check=True)


def clean_vtt_text(vtt_path: Path) -> str:
    lines: list[str] = []
    seen_recent: set[str] = set()
    for raw in vtt_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.strip()
        if not line or line == "WEBVTT" or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        if "-->" in line or re.match(r"^[0-9]+$", line):
            seen_recent.clear()
            continue
        line = re.sub(r"<[^>]+>", "", line)
        line = re.sub(r"\s+", " ", line).strip()
        if not line or line in seen_recent:
            continue
        seen_recent.add(line)
        lines.append(line)
    return "\n".join(lines).strip() + "\n"


def download_playlist(playlist: dict[str, str]) -> None:
    slug = playlist["slug"]
    raw_dir = RAW / "transcripts" / slug / "raw-vtt"
    clean_dir = RAW / "transcripts" / slug / "clean"
    meta_dir = RAW / "metadata" / slug
    playlist_dir = RAW / "playlists"
    for path in (raw_dir, clean_dir, meta_dir, playlist_dir):
        path.mkdir(parents=True, exist_ok=True)

    manifest_path = playlist_dir / f"{slug}.json"
    flat = subprocess.check_output(
        ["yt-dlp", "--flat-playlist", "--dump-single-json", playlist["url"]],
        cwd=ROOT,
        text=True,
    )
    manifest_path.write_text(flat, encoding="utf-8")

    run(
        [
            "yt-dlp",
            "--ignore-errors",
            "--skip-download",
            "--write-info-json",
            "--write-subs",
            "--write-auto-subs",
            "--sub-langs",
            "en,en-orig,en.*",
            "--sub-format",
            "vtt",
            "--download-archive",
            str(RAW / "transcripts" / slug / "download-archive.txt"),
            "-o",
            str(raw_dir / "%(playlist_index)03d-%(id)s-%(title).120B.%(ext)s"),
            playlist["url"],
        ]
    )

    for info in raw_dir.glob("*.info.json"):
        target = meta_dir / info.name
        if target.exists():
            target.unlink()
        info.replace(target)

    for vtt in sorted(raw_dir.glob("*.vtt")):
        clean_name = re.sub(r"\.(en|en-orig|en-[A-Za-z0-9_.-]+)\.vtt$", ".txt", vtt.name)
        (clean_dir / clean_name).write_text(clean_vtt_text(vtt), encoding="utf-8")


def load_manifest(playlist: dict[str, str]) -> dict[str, object]:
    path = RAW / "playlists" / f"{playlist['slug']}.json"
    if not path.exists():
        flat = subprocess.check_output(
            ["yt-dlp", "--flat-playlist", "--dump-single-json", playlist["url"]],
            cwd=ROOT,
            text=True,
        )
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(flat, encoding="utf-8")
    return json.loads(path.read_text(encoding="utf-8"))


def find_file_by_id(directory: Path, video_id: str, suffix: str) -> Path | None:
    matches = sorted(directory.glob(f"*-{video_id}-*{suffix}"))
    return matches[0] if matches else None


def concept_hits(text: str) -> list[str]:
    lowered = text.lower()
    hits = []
    for concept in CONCEPTS:
        if any(keyword.lower() in lowered for keyword in concept["keywords"]):
            hits.append(concept["slug"])
    if not hits:
        hits.append("scientific-machine-learning")
    return hits


def theme_hits(concepts: list[str]) -> list[str]:
    hits = []
    concept_set = set(concepts)
    for theme in THEMES:
        if concept_set.intersection(theme["concepts"]):
            hits.append(theme["slug"])
    return hits[:3] or ["data-to-scientific-prediction"]


def first_excerpt(text: str, terms: list[str], limit: int = 44) -> str:
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", text)
    if not words:
        return ""
    lowered_words = [word.lower() for word in words]
    term_words = [part for term in terms for part in term.lower().split()]
    start = 0
    for idx, word in enumerate(lowered_words):
        if word in term_words:
            start = max(0, idx - 8)
            break
    return " ".join(words[start : start + limit])


def load_records() -> list[TranscriptRecord]:
    records: list[TranscriptRecord] = []
    for playlist in PLAYLISTS:
        manifest = load_manifest(playlist)
        entries = manifest.get("entries") or []
        for fallback_index, entry in enumerate(entries, start=1):
            video_id = str(entry.get("id") or "")
            if not video_id:
                continue
            title = str(entry.get("title") or f"Video {fallback_index}")
            index = int(entry.get("playlist_index") or fallback_index)
            clean_path = find_file_by_id(RAW / "transcripts" / playlist["slug"] / "clean", video_id, ".txt")
            raw_path = find_file_by_id(RAW / "transcripts" / playlist["slug"] / "raw-vtt", video_id, ".vtt")
            meta_path = find_file_by_id(RAW / "metadata" / playlist["slug"], video_id, ".info.json")
            text = clean_path.read_text(encoding="utf-8", errors="ignore") if clean_path else ""
            concepts = concept_hits(f"{title}\n{text}")
            themes = theme_hits(concepts)
            concept_terms = []
            for slug in concepts:
                concept_terms.extend(next(item["keywords"] for item in CONCEPTS if item["slug"] == slug))
            records.append(
                TranscriptRecord(
                    video_id=video_id,
                    playlist_slug=playlist["slug"],
                    playlist_title=playlist["title"],
                    index=index,
                    title=title,
                    url=f"https://www.youtube.com/watch?v={video_id}&list={playlist_id(playlist['url'])}",
                    transcript_status="available" if clean_path and text.strip() else "missing",
                    clean_txt=str(clean_path.relative_to(ROOT)) if clean_path else "",
                    raw_vtt=str(raw_path.relative_to(ROOT)) if raw_path else "",
                    metadata_json=str(meta_path.relative_to(ROOT)) if meta_path else "",
                    word_count=len(re.findall(r"\w+", text)),
                    concepts=concepts,
                    themes=themes,
                    evidence_excerpt=first_excerpt(text, concept_terms),
                )
            )
    return sorted(records, key=lambda row: (row.playlist_slug, row.index, row.title))


def record_to_dict(record: TranscriptRecord) -> dict[str, object]:
    return {
        "video_id": record.video_id,
        "playlist_slug": record.playlist_slug,
        "playlist_title": record.playlist_title,
        "index": record.index,
        "title": record.title,
        "url": record.url,
        "transcript_status": record.transcript_status,
        "clean_txt": record.clean_txt,
        "raw_vtt": record.raw_vtt,
        "metadata_json": record.metadata_json,
        "word_count": record.word_count,
        "concepts": record.concepts,
        "themes": record.themes,
        "evidence_excerpt": record.evidence_excerpt,
    }


def build_analysis(records: list[TranscriptRecord]) -> dict[str, object]:
    ANALYSIS.mkdir(parents=True, exist_ok=True)
    EXPORTS.mkdir(parents=True, exist_ok=True)
    concept_counts: Counter[str] = Counter(slug for record in records for slug in record.concepts)
    concept_records: dict[str, list[TranscriptRecord]] = defaultdict(list)
    for record in records:
        for concept in record.concepts:
            concept_records[concept].append(record)

    concept_atlas = []
    for concept in CONCEPTS:
        supporting = concept_records.get(concept["slug"], [])
        if not supporting:
            continue
        concept_atlas.append(
            {
                **concept,
                "video_count": len(supporting),
                "evidence": [
                    {
                        "title": row.title,
                        "url": row.url,
                        "video_href": f"videos/{row.playlist_slug}-{row.index:03d}-{slugify(row.title)}.html",
                        "clean_txt": row.clean_txt,
                        "excerpt": row.evidence_excerpt,
                    }
                    for row in supporting[:6]
                ],
            }
        )

    theme_map = []
    for theme in THEMES:
        rows = [record for record in records if theme["slug"] in record.themes]
        theme_map.append(
            {
                **theme,
                "video_count": len(rows),
                "videos": [{"title": row.title, "url": row.url} for row in rows[:8]],
            }
        )

    evidence_ledger = []
    for record in records:
        for concept in record.concepts:
            evidence_ledger.append(
                {
                    "claim": f"{record.title} supports the concept {concept.replace('-', ' ')} inside this playlist family.",
                    "support_type": "direct transcript" if record.transcript_status == "available" else "metadata only",
                    "video": record.title,
                    "url": record.url,
                    "clean_txt": record.clean_txt,
                    "excerpt": record.evidence_excerpt,
                    "limit": "This evidence shows the lecture discusses the concept; it does not by itself prove the method is valid outside the examples in the course.",
                }
            )

    topic_treatments = []
    for concept in concept_atlas:
        topic_treatments.append(
            {
                "slug": concept["slug"],
                "title": concept["name"],
                "common_problem": concept["problem"],
                "domain": concept["domain"],
                "why_it_matters": concept["why"],
                "keeps": concept["keeps"],
                "leaves_out": concept["leaves_out"],
                "failure_boundary": concept["failure"],
                "everyday_anchor": everyday_anchor(str(concept["slug"])),
                "evidence": concept["evidence"],
            }
        )

    coverage_matrix = build_coverage_matrix(concept_atlas)
    dependency_map = build_dependency_map()
    concept_ladder = build_concept_ladder(topic_treatments)
    core_derivations = build_core_derivations(topic_treatments)
    concept_evidence_packets = build_concept_evidence_packets(topic_treatments)
    formula_guide = build_formula_guide(core_derivations)
    misconception_map = build_misconception_map(core_derivations)
    editorial_roadmap = []
    for item in EDITORIAL_ROADMAP:
        merged = dict(item)
        merged.update(ROADMAP_STATUS.get(str(item["slug"]), {}))
        editorial_roadmap.append(merged)

    data = {
        "summary": {
            "title": "Physics-Informed Machine Learning Concepts Research",
            "playlist_count": len(PLAYLISTS),
            "video_count": len(records),
            "available_transcripts": sum(1 for row in records if row.transcript_status == "available"),
            "missing_transcripts": sum(1 for row in records if row.transcript_status != "available"),
            "concept_count": len(concept_atlas),
            "theme_count": len(theme_map),
            "family_count": len(FAMILY_PAGES),
            "comparison_count": len(COMPARISON_PAGES),
            "worked_example_count": len(WORKED_EXAMPLES),
            "deep_dive_count": len(TOPIC_DEEP_DIVES),
            "core_derivation_count": len(core_derivations),
            "formula_guide_count": len(formula_guide),
            "misconception_count": len(misconception_map),
            "diagram_count": len(DIAGRAMS),
            "sketch_count": len(CONCEPT_SKETCHES),
            "learning_path_step_count": len(LEARNING_PATH),
            "glossary_term_count": len(GLOSSARY),
            "domain_guide_count": len(DOMAIN_GUIDES),
            "reader_check_count": len(READER_CHECKS),
            "decision_guide_count": len(DECISION_GUIDES),
            "provenance_guide_count": len(PROVENANCE_GUIDES),
            "coverage_row_count": len(coverage_matrix),
            "dependency_count": len(dependency_map),
            "concept_ladder_count": len(concept_ladder),
            "concept_evidence_packet_count": len(concept_evidence_packets),
            "quality_rubric_count": len(QUALITY_RUBRIC),
            "synthesis_guide_count": len(SYNTHESIS_GUIDES),
            "review_handoff_count": 1,
            "review_entrypoint_count": sum(len(group["items"]) for group in REVIEW_ENTRYPOINTS),
            "completion_requirement_count": len(COMPLETION_REQUIREMENTS),
            "review_search_intent_count": len(REVIEW_SEARCH_INDEX),
            "editorial_roadmap_count": len(editorial_roadmap),
            "editorial_roadmap_completed_count": sum(1 for item in editorial_roadmap if item.get("status") == "locally completed"),
            "source_anchor_count": sum(len(SOURCE_ANCHORS.get(str(row["slug"]), [])) or min(2, len(row.get("evidence") or [])) for row in concept_atlas),
            "meaty_goal_count": 1,
        },
        "transcript_index": [record_to_dict(record) for record in records],
        "concept_atlas": concept_atlas,
        "theme_map": theme_map,
        "evidence_ledger": evidence_ledger,
        "topic_treatments": topic_treatments,
        "family_pages": FAMILY_PAGES,
        "comparison_pages": COMPARISON_PAGES,
        "worked_examples": WORKED_EXAMPLES,
        "topic_deep_dives": TOPIC_DEEP_DIVES,
        "core_derivations": core_derivations,
        "formula_guide": formula_guide,
        "misconception_map": misconception_map,
        "diagrams": DIAGRAMS,
        "concept_sketches": CONCEPT_SKETCHES,
        "learning_path": LEARNING_PATH,
        "glossary": GLOSSARY,
        "domain_guides": DOMAIN_GUIDES,
        "reader_checks": READER_CHECKS,
        "decision_guides": DECISION_GUIDES,
        "provenance_guides": PROVENANCE_GUIDES,
        "coverage_matrix": coverage_matrix,
        "dependency_map": dependency_map,
        "concept_ladder": concept_ladder,
        "concept_evidence_packets": concept_evidence_packets,
        "meaty_goal": MEATY_END_TO_END_GOAL,
        "quality_rubric": QUALITY_RUBRIC,
        "synthesis_guides": SYNTHESIS_GUIDES,
        "review_handoff": REVIEW_HANDOFF,
        "review_entrypoints": REVIEW_ENTRYPOINTS,
        "completion_requirements": COMPLETION_REQUIREMENTS,
        "review_search_index": REVIEW_SEARCH_INDEX,
        "editorial_roadmap": editorial_roadmap,
        "source_anchors": SOURCE_ANCHORS,
    }
    for name, value in data.items():
        if name == "summary":
            continue
        (ANALYSIS / f"{name}.json").write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    (ANALYSIS / "summary.json").write_text(json.dumps(data["summary"], indent=2) + "\n", encoding="utf-8")
    write_markdown_export(data)
    return data


def everyday_anchor(slug: str) -> str:
    anchors = {
        "deep-learning": "A lab notebook may contain many examples of inputs and outcomes. Deep learning is the adjustable recipe that tries to match those examples, then must be checked on a new page of the notebook.",
        "physics-informed-neural-networks": "A student drawing a bridge cannot ignore gravity. A PINN is similar: the fitted curve is pushed to obey the equation, not only the measured dots.",
        "partial-differential-equations": "A weather map changes from place to place and hour to hour. A PDE is a way to say how nearby values push each other forward.",
        "operator-learning": "Instead of solving one puzzle, the learner tries to learn the machine that turns many puzzle inputs into many full answers.",
        "scientific-machine-learning": "A scientist does not just want a number; they want a number with a reason, a check, and a warning label for when it should fail.",
        "surrogate-modeling": "A wind-tunnel test is expensive. A surrogate is a cheaper stand-in that can be used only after showing which wind-tunnel questions it still answers.",
        "uncertainty-and-generalization": "A map is useful only if you know where it ends. Model uncertainty marks the edge of the map instead of pretending every road is known.",
        "optimization-for-learning": "Training is like grading many drafts with one rubric. The model improves the rubric score, so the rubric must match the scientific goal.",
        "generative-modeling": "A generator can make many candidate sketches. The scientific question is which sketches obey the rules, not only which ones look familiar.",
        "graphs-and-geometric-learning": "A molecule, mesh, or network is not just a list. The connections decide what can influence what.",
    }
    return anchors.get(slug, "Start with the observed object, name what must be predicted, then test the claim on a changed case.")


def source_anchor_cards(slug: str, evidence: list[dict[str, object]] | None = None, root_prefix: str = "") -> str:
    anchors = list(SOURCE_ANCHORS.get(slug, []))
    if not anchors and evidence:
        concept_name = next((str(item["name"]) for item in CONCEPTS if item["slug"] == slug), slug.replace("-", " ").title())
        for row in evidence[:2]:
            anchors.append(
                {
                    "claim": f"This lecture supports reviewing {concept_name} inside the local course family.",
                    "source": str(row.get("title") or "Source lecture"),
                    "href": str(row.get("video_href") or row.get("url") or ""),
                    "why_this_source": "This source is selected from the local transcript evidence for this concept.",
                    "limit": "The source shows where the concept appears in the course material; it does not prove the method works for every domain, data set, equation, or changed case.",
                }
            )
    if not anchors:
        return ""
    cards = []
    for item in anchors:
        href = str(item["href"])
        linked_href = href if href.startswith(("http://", "https://")) else f"{root_prefix}{href}"
        cards.append(
            f"""
<article class="card">
  <h3><a href="{html.escape(linked_href)}">{html.escape(str(item['source']))}</a></h3>
  <p><strong>Claim Anchored:</strong> {html.escape(str(item['claim']))}</p>
  <p><strong>Why this source:</strong> {html.escape(str(item['why_this_source']))}</p>
  <p><strong>Limit:</strong> {html.escape(str(item['limit']))}</p>
</article>
"""
        )
    return f"<h2>Selected Source Anchors</h2><p>These anchors identify the lecture pages that should be checked first when reviewing the core claim. They are source links with claim boundaries, not proof by themselves.</p><div class=\"grid\">{''.join(cards)}</div>"


def build_coverage_matrix(concept_atlas: list[dict[str, object]]) -> list[dict[str, object]]:
    rows = []
    for concept in concept_atlas:
        slug = str(concept["slug"])
        rows.append(
            {
                "slug": slug,
                "name": str(concept["name"]),
                "video_count": int(concept["video_count"]),
                "topic_page": True,
                "deep_dive": slug in TOPIC_DEEP_DIVES,
                "diagram": any(slug in diagram["topic_slugs"] for diagram in DIAGRAMS),
                "learning_path": any(any(str(item["href"]) == f"topics/{slug}.html" for item in step["read"]) for step in LEARNING_PATH),
                "glossary": any(slug in entry["related"] for entry in GLOSSARY),
                "domain": any(slug in guide["concepts"] for guide in DOMAIN_GUIDES),
                "reader_check": any(check["topic_slug"] == slug for check in READER_CHECKS),
                "decision_guide": any(f"topics/{slug}.html" in decision["links"] for decision in DECISION_GUIDES),
                "evidence_items": len(concept.get("evidence", [])),
            }
        )
    return rows


def build_dependency_map() -> list[dict[str, object]]:
    names = {str(item["slug"]): str(item["name"]) for item in CONCEPTS}
    rows = []
    for item in CONCEPT_DEPENDENCIES:
        concept = str(item["concept"])
        rows.append(
            {
                "concept": concept,
                "concept_name": names.get(concept, concept.replace("-", " ")),
                "concept_href": f"topics/{concept}.html",
                "depends_on": [
                    {
                        "slug": str(slug),
                        "name": names.get(str(slug), str(slug).replace("-", " ")),
                        "href": f"topics/{slug}.html",
                    }
                    for slug in item["depends_on"]
                ],
                "why": str(item["why"]),
                "confusion_prevented": str(item["confusion_prevented"]),
            }
        )
    return rows


def build_concept_ladder(topic_treatments: list[dict[str, object]]) -> list[dict[str, object]]:
    rows = []
    for topic in topic_treatments:
        derivation = topic_derivation(topic)
        evidence = topic.get("evidence") or []
        first_evidence = evidence[0] if isinstance(evidence, list) and evidence else {}
        rows.append(
            {
                "slug": str(topic["slug"]),
                "title": str(topic["title"]),
                "domain": str(topic["domain"]),
                "common_problem": str(topic["common_problem"]),
                "observed": str(derivation["observed"]),
                "hidden": str(derivation["hidden"]),
                "mathematical_move": str(derivation["move"]),
                "shape": str(derivation["form"]),
                "meaning": str(derivation["meaning"]),
                "failure_test": str(derivation["test"]),
                "topic_href": f"topics/{topic['slug']}.html",
                "evidence_title": str(first_evidence.get("title") or ""),
                "evidence_url": str(first_evidence.get("url") or ""),
            }
        )
    return rows


def build_core_derivations(topic_treatments: list[dict[str, object]]) -> list[dict[str, object]]:
    by_slug = {str(topic["slug"]): topic for topic in topic_treatments}
    rows = []
    for slug, deep in TOPIC_DEEP_DIVES.items():
        topic = by_slug.get(slug)
        if not topic:
            continue
        derivation = topic_derivation(topic)
        rows.append(
            {
                "slug": slug,
                "title": str(topic["title"]),
                "one_sentence": str(deep["one_sentence"]),
                "domain_story": str(deep["domain_story"]),
                "common_problem": str(topic["common_problem"]),
                "observed": str(derivation["observed"]),
                "hidden": str(derivation["hidden"]),
                "math_shape": list(deep["math_shape"]),
                "hand_derivation": HAND_DERIVATIONS.get(slug),
                "plain_formula": str(deep["plain_formula"]),
                "why_it_matters": str(deep["important_because"]),
                "failure_test": str(derivation["test"]),
                "red_flags": list(deep["red_flags"]),
                "connects_to": list(deep["connects_to"]),
                "topic_href": f"topics/{slug}.html",
                "derivation_href": f"derivations/{slug}.html",
            }
        )
    return rows


def build_concept_evidence_packets(topic_treatments: list[dict[str, object]]) -> list[dict[str, object]]:
    example_links: dict[str, list[dict[str, str]]] = defaultdict(list)
    for example in WORKED_EXAMPLES:
        for slug in example["method_route"]:
            example_links[str(slug)].append(
                {
                    "label": str(example["title"]),
                    "href": f"worked-examples/{example['slug']}.html",
                }
            )
    packets = []
    for topic in topic_treatments:
        slug = str(topic["slug"])
        evidence = list(topic.get("evidence") or [])
        links = [
            {"label": "Topic Page", "href": f"topics/{slug}.html"},
            {"label": "Concept Ladder", "href": "concept-ladder.html"},
            {"label": "Coverage Matrix", "href": "coverage.html"},
            {"label": "Evidence Ledger", "href": "evidence-ledger.html"},
        ]
        if slug in TOPIC_DEEP_DIVES:
            links.append({"label": "Derivation", "href": f"derivations/{slug}.html"})
        links.extend(example_links.get(slug, [])[:3])
        packets.append(
            {
                "slug": slug,
                "title": str(topic["title"]),
                "common_problem": str(topic["common_problem"]),
                "domain": str(topic["domain"]),
                "why_it_matters": str(topic["why_it_matters"]),
                "evidence_count": len(evidence),
                "evidence": evidence,
                "source_anchors": SOURCE_ANCHORS.get(slug, []),
                "limits": [
                    "Transcript evidence shows the concept appears in this course family.",
                    "It does not prove the method works for every equation, material, geometry, data size, or future case.",
                    "Trust requires a named scientific job, a changed-case test, and a failure boundary.",
                ],
                "review_links": links,
                "packet_href": f"evidence-packets/{slug}.html",
            }
        )
    return packets


def formula_parts(formula: str) -> list[str]:
    if "->" in formula:
        return [part.strip() for part in formula.split("->")]
    if "+" in formula and "=" in formula:
        left, right = formula.split("=", 1)
        return [left.strip(), *[part.strip() for part in right.split("+")]]
    if "+" in formula:
        return [part.strip() for part in formula.split("+")]
    if "=" in formula:
        return [part.strip() for part in formula.split("=")]
    return [formula.strip()]


def build_formula_guide(core_derivations: list[dict[str, object]]) -> list[dict[str, object]]:
    rows = []
    for derivation in core_derivations:
        formula = str(derivation["plain_formula"])
        rows.append(
            {
                "slug": str(derivation["slug"]),
                "title": str(derivation["title"]),
                "plain_formula": formula,
                "parts": formula_parts(formula),
                "everyday_reading": str(derivation["why_it_matters"]),
                "what_to_check": str(derivation["failure_test"]),
                "common_misread": "Do not read the formula as proof. Read it as a compact map of what information is being carried and what must be tested.",
                "derivation_href": str(derivation["derivation_href"]),
                "topic_href": str(derivation["topic_href"]),
            }
        )
    return rows


def build_misconception_map(core_derivations: list[dict[str, object]]) -> list[dict[str, object]]:
    check_by_slug = {str(check["topic_slug"]): check for check in READER_CHECKS}
    rows = []
    for derivation in core_derivations:
        slug = str(derivation["slug"])
        check = check_by_slug.get(slug, {})
        wrong_turns = list(derivation["red_flags"])
        weak_warning = str(check.get("weak_answer_warning") or "")
        if weak_warning:
            wrong_turns.insert(0, weak_warning)
        rows.append(
            {
                "slug": slug,
                "title": str(derivation["title"]),
                "wrong_turns": wrong_turns,
                "plain_correction": str(derivation["one_sentence"]),
                "first_principles_test": str(derivation["failure_test"]),
                "reader_check_href": f"reader-checks/{check['slug']}.html" if check else "",
                "derivation_href": str(derivation["derivation_href"]),
                "topic_href": str(derivation["topic_href"]),
            }
        )
    return rows


def write_style() -> None:
    assets = SITE / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    (assets / "style.css").write_text(
        """
:root {
  --bg: #f7f8fb;
  --text: #1b2430;
  --muted: #5e6b7a;
  --line: #d9e0ea;
  --card: #ffffff;
  --accent: #0f6b78;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.55;
}
.topbar {
  display: flex;
  gap: 18px;
  flex-wrap: wrap;
  align-items: center;
  padding: 14px 28px;
  border-bottom: 1px solid var(--line);
  background: #fff;
  position: sticky;
  top: 0;
}
.topbar a { color: var(--accent); text-decoration: none; font-weight: 700; }
main { max-width: 1180px; margin: 0 auto; padding: 34px 28px 72px; }
h1 { font-size: 2.35rem; line-height: 1.12; margin: 0 0 14px; }
h2 { margin-top: 34px; border-top: 1px solid var(--line); padding-top: 20px; }
h3 { margin-top: 0; }
p, li { max-width: 900px; }
.meta { color: var(--muted); font-size: .95rem; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; align-items: start; }
.route { display: grid; gap: 10px; max-width: 920px; }
.route-step {
  background: #fff;
  border: 1px solid var(--line);
  border-left: 5px solid var(--accent);
  border-radius: 8px;
  padding: 12px 14px;
}
.flow {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 10px;
  align-items: stretch;
  max-width: 1040px;
}
.flow-node {
  min-height: 92px;
  background: #fff;
  border: 1px solid var(--line);
  border-top: 5px solid #9b5b28;
  border-radius: 8px;
  padding: 12px;
  font-weight: 700;
}
.diagram-note {
  max-width: 1040px;
  background: #eef4f6;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 12px 14px;
}
.sketch {
  max-width: 1040px;
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 14px;
  margin: 14px 0;
}
.sketch-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(130px, 1fr));
  gap: 10px;
  align-items: stretch;
}
.sketch-cell {
  min-height: 100px;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 12px;
  display: grid;
  align-content: center;
  font-weight: 700;
  text-align: center;
}
.sketch-cell.input { background: #eef4f6; border-top: 5px solid #0f6b78; }
.sketch-cell.rule { background: #f4f0e8; border-top: 5px solid #9b5b28; }
.sketch-cell.output { background: #eef3ed; border-top: 5px solid #557a46; }
.sketch-cell.failure { background: #f6eded; border-top: 5px solid #a24a3c; }
.sketch-caption { max-width: 980px; color: var(--muted); margin-bottom: 0; }
.compare-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; }
.card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 16px;
}
.card a { color: var(--accent); text-decoration: none; }
table { width: 100%; border-collapse: collapse; background: #fff; }
th, td { border: 1px solid var(--line); padding: 10px; vertical-align: top; text-align: left; }
th { background: #eef4f6; }
code { background: #eef1f5; padding: 1px 4px; border-radius: 4px; }
@media (max-width: 760px) {
  main { padding: 24px 18px 56px; }
  h1 { font-size: 1.8rem; }
  .topbar { position: static; padding: 12px 18px; }
  .sketch-grid { grid-template-columns: 1fr; }
}
""".strip()
        + "\n",
        encoding="utf-8",
    )


def html_page(title: str, body: str, root_prefix: str = "") -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{root_prefix}assets/style.css">
</head>
<body>
<nav class="topbar">
  <a href="{root_prefix}index.html">Physics-Informed ML</a>
  <a href="{root_prefix}transcripts.html">Transcripts</a>
  <a href="{root_prefix}concept-atlas.html">Concept Atlas</a>
  <a href="{root_prefix}families.html">Families</a>
  <a href="{root_prefix}comparisons.html">Comparisons</a>
  <a href="{root_prefix}worked-examples.html">Examples</a>
  <a href="{root_prefix}diagrams.html">Diagrams</a>
  <a href="{root_prefix}derivations.html">Derivations</a>
  <a href="{root_prefix}formula-guide.html">Formulas</a>
  <a href="{root_prefix}misconceptions.html">Misreads</a>
  <a href="{root_prefix}learning-path.html">Path</a>
  <a href="{root_prefix}glossary.html">Glossary</a>
  <a href="{root_prefix}domains.html">Domains</a>
  <a href="{root_prefix}reader-checks.html">Checks</a>
  <a href="{root_prefix}decision-guide.html">Decide</a>
  <a href="{root_prefix}provenance.html">Provenance</a>
  <a href="{root_prefix}coverage.html">Coverage</a>
  <a href="{root_prefix}dependencies.html">Dependencies</a>
  <a href="{root_prefix}concept-ladder.html">Ladder</a>
  <a href="{root_prefix}evidence-packets.html">Packets</a>
  <a href="{root_prefix}quality.html">Quality</a>
  <a href="{root_prefix}synthesis.html">Synthesis</a>
  <a href="{root_prefix}review-entrypoints.html">Review Map</a>
  <a href="{root_prefix}review-search.html">Find</a>
  <a href="{root_prefix}editorial-roadmap.html">Roadmap</a>
  <a href="{root_prefix}completion-audit.html">Audit</a>
  <a href="{root_prefix}handoff.html">Handoff</a>
  <a href="{root_prefix}theme-map.html">Themes</a>
  <a href="{root_prefix}evidence-ledger.html">Evidence</a>
</nav>
<main>
{body}
</main>
</body>
</html>
"""


def card(title: str, text: str, href: str = "") -> str:
    heading = f'<h3><a href="{html.escape(href)}">{html.escape(title)}</a></h3>' if href else f"<h3>{html.escape(title)}</h3>"
    return f'<article class="card">{heading}<p>{html.escape(text)}</p></article>'


def concept_links(slugs: list[str], root_prefix: str = "") -> str:
    items = []
    concept_names = {str(item["slug"]): str(item["name"]) for item in CONCEPTS}
    for slug in slugs:
        name = concept_names.get(slug, slug.replace("-", " "))
        items.append(f'<li><a href="{root_prefix}topics/{html.escape(slug)}.html">{html.escape(name)}</a></li>')
    return "<ul>" + "".join(items) + "</ul>"


def topic_deep_dive_html(slug: str) -> str:
    deep = TOPIC_DEEP_DIVES.get(slug)
    if not deep:
        return ""
    math_steps = "".join(f"<div class=\"route-step\">{idx}. {html.escape(step)}</div>" for idx, step in enumerate(deep["math_shape"], start=1))
    red_flags = "".join(f"<li>{html.escape(item)}</li>" for item in deep["red_flags"])
    return f"""
<h2>Core Idea In One Sentence</h2>
<p>{html.escape(str(deep['one_sentence']))}</p>
<h2>Where This Is Useful</h2>
<p>{html.escape(str(deep['use_when']))}</p>
<h2>Where This Breaks</h2>
<p>{html.escape(str(deep['do_not_use_when']))}</p>
<h2>Concrete Domain Story</h2>
<p>{html.escape(str(deep['domain_story']))}</p>
<h2>Mathematical Shape Without Jargon</h2>
<div class="route">{math_steps}</div>
<p><strong>Plain formula:</strong> {html.escape(str(deep['plain_formula']))}</p>
<h2>Why This Matters</h2>
<p>{html.escape(str(deep['important_because']))}</p>
<h2>Red Flags</h2>
<ul>{red_flags}</ul>
<h2>Connects To</h2>
{concept_links(list(deep['connects_to']), root_prefix="../")}
"""


def diagram_flow_html(diagram: dict[str, object]) -> str:
    nodes = "".join(f"<div class=\"flow-node\">{idx}. {html.escape(str(node))}</div>" for idx, node in enumerate(diagram["nodes"], start=1))
    return f"""
<div class="flow">{nodes}</div>
<p class="diagram-note"><strong>Watch for:</strong> {html.escape(str(diagram['watch_for']))}</p>
"""


def sketch_html(sketch: dict[str, object]) -> str:
    cells = []
    for item in sketch["cells"]:
        role = str(item["role"])
        cells.append(
            f"""
<div class="sketch-cell {html.escape(role)}">
  <span>{html.escape(str(item['label']))}</span>
</div>
"""
        )
    return f"""
<article class="sketch">
  <h3>{html.escape(str(sketch['title']))}</h3>
  <div class="sketch-grid">{''.join(cells)}</div>
  <p><strong>Input:</strong> {html.escape(str(sketch['input']))}</p>
  <p><strong>Output:</strong> {html.escape(str(sketch['output']))}</p>
  <p><strong>Kept Rule:</strong> {html.escape(str(sketch['kept_rule']))}</p>
  <p><strong>Failure Case:</strong> {html.escape(str(sketch['failure_case']))}</p>
  <p class="sketch-caption">{html.escape(str(sketch['caption']))}</p>
</article>
"""


def topic_sketches_html(slug: str) -> str:
    sketches = [sketch for sketch in CONCEPT_SKETCHES if slug in sketch["topic_slugs"]]
    if not sketches:
        return ""
    return f"<h2>Mathematical Sketch</h2>{''.join(sketch_html(sketch) for sketch in sketches)}"


def topic_diagrams_html(slug: str) -> str:
    diagrams = [diagram for diagram in DIAGRAMS if slug in diagram["topic_slugs"]]
    if not diagrams:
        return ""
    cards = []
    for diagram in diagrams:
        cards.append(
            f"""
<article class="card">
  <h3><a href="../diagrams/{html.escape(str(diagram['slug']))}.html">{html.escape(str(diagram['title']))}</a></h3>
  <p>{html.escape(str(diagram['purpose']))}</p>
  {diagram_flow_html(diagram)}
</article>
"""
        )
    return f"<h2>Visual Map</h2>{''.join(cards)}"


def learning_step_card(step: dict[str, object], href_prefix: str = "") -> str:
    return f"""
<article class="card">
  <h3><a href="{href_prefix}learning-path/{html.escape(str(step['slug']))}.html">{html.escape(str(step['title']))}</a></h3>
  <p><strong>Question:</strong> {html.escape(str(step['question']))}</p>
  <p>{html.escape(str(step['plain_goal']))}</p>
</article>
"""


def reader_check_card(check: dict[str, object], href_prefix: str = "") -> str:
    return f"""
<article class="card">
  <h3><a href="{href_prefix}reader-checks/{html.escape(str(check['slug']))}.html">{html.escape(str(check['title']))}</a></h3>
  <p>{html.escape(str(check['setup']))}</p>
  <p><strong>Weak answer warning:</strong> {html.escape(str(check['weak_answer_warning']))}</p>
</article>
"""


def decision_card(decision: dict[str, object], href_prefix: str = "") -> str:
    return f"""
<article class="card">
  <h3><a href="{href_prefix}decision-guide/{html.escape(str(decision['slug']))}.html">{html.escape(str(decision['title']))}</a></h3>
  <p>{html.escape(str(decision['situation']))}</p>
  <p><strong>Start with:</strong> {html.escape(str(decision['best_start']))}</p>
</article>
"""


def provenance_card(guide: dict[str, object], href_prefix: str = "") -> str:
    return f"""
<article class="card">
  <h3><a href="{href_prefix}provenance/{html.escape(str(guide['slug']))}.html">{html.escape(str(guide['title']))}</a></h3>
  <p>{html.escape(str(guide['purpose']))}</p>
</article>
"""


def quality_card(item: dict[str, object], href_prefix: str = "") -> str:
    return f"""
<article class="card">
  <h3><a href="{href_prefix}quality/{html.escape(str(item['slug']))}.html">{html.escape(str(item['title']))}</a></h3>
  <p>{html.escape(str(item['standard']))}</p>
</article>
"""


def synthesis_card(item: dict[str, object], href_prefix: str = "") -> str:
    return f"""
<article class="card">
  <h3><a href="{href_prefix}synthesis/{html.escape(str(item['slug']))}.html">{html.escape(str(item['title']))}</a></h3>
  <p>{html.escape(str(item['claim']))}</p>
</article>
"""


def topic_reader_check_html(slug: str) -> str:
    checks = [check for check in READER_CHECKS if check["topic_slug"] == slug]
    if not checks:
        return ""
    return "<h2>Reader Check</h2>" + "".join(reader_check_card(check, href_prefix="../") for check in checks)


def topic_derivation_link_html(slug: str) -> str:
    if slug not in TOPIC_DEEP_DIVES:
        return ""
    return f"""
<h2>Full Derivation Walkthrough</h2>
<p><a href="../derivations/{html.escape(slug)}.html">Open the step-by-step derivation page</a>. It slows this concept down from observed evidence, to hidden quantity, to formula shape, to failure test.</p>
"""


def write_site(data: dict[str, object]) -> None:
    SITE.mkdir(parents=True, exist_ok=True)
    write_style()
    topic_dir = SITE / "topics"
    video_dir = SITE / "videos"
    family_dir = SITE / "families"
    comparison_dir = SITE / "comparisons"
    example_dir = SITE / "worked-examples"
    diagram_dir = SITE / "diagrams"
    derivation_dir = SITE / "derivations"
    learning_dir = SITE / "learning-path"
    glossary_dir = SITE / "glossary"
    domain_dir = SITE / "domains"
    check_dir = SITE / "reader-checks"
    decision_dir = SITE / "decision-guide"
    provenance_dir = SITE / "provenance"
    packet_dir = SITE / "evidence-packets"
    quality_dir = SITE / "quality"
    synthesis_dir = SITE / "synthesis"
    for generated_dir in (family_dir, comparison_dir, example_dir, diagram_dir, derivation_dir, learning_dir, glossary_dir, domain_dir, check_dir, decision_dir, provenance_dir, packet_dir, quality_dir, synthesis_dir):
        if generated_dir.exists():
            shutil.rmtree(generated_dir)
    topic_dir.mkdir(exist_ok=True)
    video_dir.mkdir(exist_ok=True)
    family_dir.mkdir(exist_ok=True)
    comparison_dir.mkdir(exist_ok=True)
    example_dir.mkdir(exist_ok=True)
    diagram_dir.mkdir(exist_ok=True)
    derivation_dir.mkdir(exist_ok=True)
    learning_dir.mkdir(exist_ok=True)
    glossary_dir.mkdir(exist_ok=True)
    domain_dir.mkdir(exist_ok=True)
    check_dir.mkdir(exist_ok=True)
    decision_dir.mkdir(exist_ok=True)
    provenance_dir.mkdir(exist_ok=True)
    packet_dir.mkdir(exist_ok=True)
    quality_dir.mkdir(exist_ok=True)
    synthesis_dir.mkdir(exist_ok=True)

    summary = data["summary"]
    concept_atlas = data["concept_atlas"]
    records = [TranscriptRecord(**row) for row in data["transcript_index"]]
    topics = data["topic_treatments"]
    themes = data["theme_map"]
    evidence = data["evidence_ledger"]
    family_pages = data["family_pages"]
    comparison_pages = data["comparison_pages"]
    worked_examples = data["worked_examples"]
    diagrams = data["diagrams"]
    concept_sketches = data["concept_sketches"]
    core_derivations = data["core_derivations"]
    formula_guide = data["formula_guide"]
    misconception_map = data["misconception_map"]
    learning_path = data["learning_path"]
    glossary = data["glossary"]
    domain_guides = data["domain_guides"]
    reader_checks = data["reader_checks"]
    decision_guides = data["decision_guides"]
    provenance_guides = data["provenance_guides"]
    coverage_matrix = data["coverage_matrix"]
    dependency_map = data["dependency_map"]
    concept_ladder = data["concept_ladder"]
    concept_evidence_packets = data["concept_evidence_packets"]
    quality_rubric = data["quality_rubric"]
    synthesis_guides = data["synthesis_guides"]
    review_handoff = data["review_handoff"]
    review_entrypoints = data["review_entrypoints"]
    completion_requirements = data["completion_requirements"]
    review_search_index = data["review_search_index"]
    editorial_roadmap = data["editorial_roadmap"]
    meaty_goal = data["meaty_goal"]

    index_body = f"""
<h1>Physics-Informed Machine Learning Concepts Research</h1>
<p>This package turns two ETH Zurich AI in the Sciences and Engineering playlists into a transcript-backed research map for physics-informed machine learning. It is built from first principles: what problem each idea solves, what scientific domain needs it, what information it keeps, what it leaves out, and how the claim can fail.</p>
<div class="grid">
{card("Videos", f"{summary['video_count']} source videos across two playlists, with {summary['available_transcripts']} available transcripts.", "transcripts.html")}
{card("Concepts", f"{summary['concept_count']} concepts extracted into plain-language topic treatments.", "concept-atlas.html")}
{card("Paper Families", f"{summary['family_count']} routes through related concept families.", "families.html")}
{card("Comparisons", f"{summary['comparison_count']} plain-language method comparisons.", "comparisons.html")}
{card("Worked Examples", f"{summary['worked_example_count']} concrete scientific examples.", "worked-examples.html")}
{card("Diagrams", f"{summary['diagram_count']} visual flows and {summary['sketch_count']} mathematical sketches for the main ideas.", "diagrams.html")}
{card("Derivations", f"{summary['core_derivation_count']} core walkthroughs from observed evidence to formula shape and failure test.", "derivations.html")}
{card("Formula Guide", f"{summary['formula_guide_count']} plain formula shapes translated into everyday meaning.", "formula-guide.html")}
{card("Misconceptions", f"{summary['misconception_count']} core wrong turns paired with plain corrections.", "misconceptions.html")}
{card("Learning Path", f"{summary['learning_path_step_count']} steps from first question to field-level understanding.", "learning-path.html")}
{card("Glossary", f"{summary['glossary_term_count']} field terms translated into everyday language.", "glossary.html")}
{card("Domains", f"{summary['domain_guide_count']} domain guides that ground concepts in real scientific work.", "domains.html")}
{card("Reader Checks", f"{summary['reader_check_count']} self-check prompts for core ideas.", "reader-checks.html")}
{card("Decision Guide", f"{summary['decision_guide_count']} method choices from concrete scientific situations.", "decision-guide.html")}
{card("Provenance", f"{summary['provenance_guide_count']} pages documenting source, extraction, build, and reproduction.", "provenance.html")}
{card("Coverage Matrix", f"{summary['coverage_row_count']} concepts checked across evidence and guide layers.", "coverage.html")}
{card("Dependencies", f"{summary['dependency_count']} concept dependencies showing what to learn before what.", "dependencies.html")}
{card("Concept Ladder", f"{summary['concept_ladder_count']} concepts laid out from observed evidence to failure test.", "concept-ladder.html")}
{card("Evidence Packets", f"{summary['concept_evidence_packet_count']} concept packets tying source support to review pages.", "evidence-packets.html")}
{card("Quality Rubric", f"{summary['quality_rubric_count']} editorial standards for first-principles pages.", "quality.html")}
{card("Synthesis", f"{summary['synthesis_guide_count']} pages tying the field into one argument.", "synthesis.html")}
{card("Meaty Goal", "End-to-end done criteria for turning the package into a teaching-grade first-principles research guide.", "meaty-goal.html")}
{card("Review Map", f"{summary['review_entrypoint_count']} entry points for end-to-end review, use, and source checks.", "review-entrypoints.html")}
{card("Find By Question", f"{summary['review_search_intent_count']} reviewer intents mapped to the right pages.", "review-search.html")}
{card("Editorial Roadmap", f"{summary['editorial_roadmap_completed_count']} of {summary['editorial_roadmap_count']} roadmap tasks are locally completed, including remote verification.", "editorial-roadmap.html")}
{card("Completion Audit", f"{summary['completion_requirement_count']} requirements checked against local evidence and external status.", "completion-audit.html")}
{card("Review Handoff", "Shortest route for reviewing the package and the remaining editorial work.", "handoff.html")}
{card("Themes", f"{summary['theme_count']} recurring research pressures across the course family.", "theme-map.html")}
{card("Evidence", "Each major claim links back to transcript or metadata evidence and states its limit.", "evidence-ledger.html")}
</div>
<h2>Central Big Picture</h2>
<p>The course family asks how machine learning can help science without throwing away the checks that make science usable. The recurring problem is not simply prediction. The real problem is carrying incomplete evidence into a new case while making clear what would reject the answer.</p>
<h2>Core Route Through The Material</h2>
<ol>
  <li>Name the real quantity: field, force, property, risk, or rule.</li>
  <li>Name the evidence: measurements, equations, solved cases, simulations, geometry, or prior cases.</li>
  <li>Name the missing quantity: the value, field, map, law, or trust estimate needed for the next case.</li>
  <li>Choose the mathematical move that carries the evidence without hiding its limits.</li>
  <li>Judge the result by the changed case that could reject the scientific claim.</li>
</ol>
"""
    (SITE / "index.html").write_text(html_page("Physics-Informed Machine Learning Concepts Research", index_body), encoding="utf-8")

    transcript_cards = []
    for record in records:
        href = f"videos/{record.playlist_slug}-{record.index:03d}-{slugify(record.title)}.html"
        transcript_cards.append(
            card(
                f"{record.index:03d}. {record.title}",
                f"{record.playlist_title}. Transcript: {record.transcript_status}. Words: {record.word_count}. Concepts: {', '.join(record.concepts)}.",
                href,
            )
        )
        write_video_page(video_dir / Path(href).name, record)
    (SITE / "transcripts.html").write_text(
        html_page("Physics-Informed ML Transcripts", f"<h1>Transcript Index</h1><div class=\"grid\">{''.join(transcript_cards)}</div>"),
        encoding="utf-8",
    )

    concept_cards = []
    for concept in concept_atlas:
        href = f"topics/{concept['slug']}.html"
        concept_cards.append(card(str(concept["name"]), str(concept["problem"]), href))
    (SITE / "concept-atlas.html").write_text(
        html_page("Physics-Informed ML Concept Atlas", f"<h1>Mathematical Concept Atlas</h1><div class=\"grid\">{''.join(concept_cards)}</div>"),
        encoding="utf-8",
    )
    for topic in topics:
        write_topic_page(topic_dir / f"{topic['slug']}.html", topic)

    family_cards = []
    for family in family_pages:
        href = f"families/{family['slug']}.html"
        family_cards.append(card(str(family["title"]), str(family["central_problem"]), href))
        write_family_page(family_dir / f"{family['slug']}.html", family)
    (SITE / "families.html").write_text(
        html_page("Physics-Informed ML Paper Families", f"<h1>Paper Family Routes</h1><p>These pages group related concepts by the real scientific problem they try to solve. Read them as routes through the field, not as labels.</p><div class=\"grid\">{''.join(family_cards)}</div>"),
        encoding="utf-8",
    )

    comparison_cards = []
    for comparison in comparison_pages:
        href = f"comparisons/{comparison['slug']}.html"
        comparison_cards.append(card(str(comparison["title"]), str(comparison["shared_problem"]), href))
        write_comparison_page(comparison_dir / f"{comparison['slug']}.html", comparison)
    (SITE / "comparisons.html").write_text(
        html_page("Physics-Informed ML Comparisons", f"<h1>Comparison Pages</h1><p>These pages separate nearby ideas by the job they are built for, the evidence they need, and the failure case that matters.</p><div class=\"grid\">{''.join(comparison_cards)}</div>"),
        encoding="utf-8",
    )

    example_cards = []
    for example in worked_examples:
        href = f"worked-examples/{example['slug']}.html"
        example_cards.append(card(str(example["title"]), str(example["question"]), href))
        write_worked_example_page(example_dir / f"{example['slug']}.html", example)
    (SITE / "worked-examples.html").write_text(
        html_page("Physics-Informed ML Worked Examples", f"<h1>Worked Examples</h1><p>These pages anchor the math in concrete scientific jobs. Each example names the observed evidence, the hidden quantity, the method route, and the test that keeps the claim honest.</p><div class=\"grid\">{''.join(example_cards)}</div>"),
        encoding="utf-8",
    )

    diagram_cards = []
    for diagram in diagrams:
        href = f"diagrams/{diagram['slug']}.html"
        diagram_cards.append(card(str(diagram["title"]), str(diagram["purpose"]), href))
        write_diagram_page(diagram_dir / f"{diagram['slug']}.html", diagram)
    sketch_cards = "".join(sketch_html(sketch) for sketch in concept_sketches)
    (SITE / "diagrams.html").write_text(
        html_page("Physics-Informed ML Diagrams", f"<h1>Diagram Index</h1><p>These diagrams and sketches show the flow of evidence, rules, learned objects, and validation checks. They are deliberately simple so the core idea is visible before any notation appears.</p><div class=\"grid\">{''.join(diagram_cards)}</div><h2>Mathematical Sketches</h2>{sketch_cards}"),
        encoding="utf-8",
    )

    derivation_cards = []
    for derivation in core_derivations:
        derivation_cards.append(card(str(derivation["title"]), str(derivation["one_sentence"]), str(derivation["derivation_href"])))
        write_core_derivation_page(derivation_dir / f"{derivation['slug']}.html", derivation)
    (SITE / "derivations.html").write_text(
        html_page("Physics-Informed ML Core Derivations", f"<h1>Core Derivations</h1><p>These pages slow down the main mathematical ideas. Each one starts from what is observed, names what is hidden, builds the formula shape in plain steps, and ends with the test that can reject the claim.</p><div class=\"grid\">{''.join(derivation_cards)}</div>"),
        encoding="utf-8",
    )

    write_formula_guide_page(SITE / "formula-guide.html", list(formula_guide))
    write_misconception_map_page(SITE / "misconceptions.html", list(misconception_map))

    learning_cards = []
    for step in learning_path:
        learning_cards.append(learning_step_card(step))
        write_learning_step_page(learning_dir / f"{step['slug']}.html", step)
    (SITE / "learning-path.html").write_text(
        html_page("Physics-Informed ML Learning Path", f"<h1>Learning Path From First Principles</h1><p>This path is for a reader who does not want jargon first. It starts with the scientific question, then builds toward equations, physics checks, learned maps, speed, trust, and readable laws.</p><div class=\"grid\">{''.join(learning_cards)}</div>"),
        encoding="utf-8",
    )

    glossary_cards = []
    for entry in glossary:
        href = f"glossary/{entry['slug']}.html"
        glossary_cards.append(card(str(entry["term"]), str(entry["everyday"]), href))
        write_glossary_page(glossary_dir / f"{entry['slug']}.html", entry)
    (SITE / "glossary.html").write_text(
        html_page("Physics-Informed ML Glossary", f"<h1>Plain-Language Glossary</h1><p>These terms are translated by the job they do. Each page states the everyday meaning, the real problem, why the term matters, and what to watch for.</p><div class=\"grid\">{''.join(glossary_cards)}</div>"),
        encoding="utf-8",
    )

    domain_cards = []
    for guide in domain_guides:
        href = f"domains/{guide['slug']}.html"
        domain_cards.append(card(str(guide["title"]), str(guide["common_question"]), href))
        write_domain_page(domain_dir / f"{guide['slug']}.html", guide)
    (SITE / "domains.html").write_text(
        html_page("Physics-Informed ML Domain Guides", f"<h1>Domain Guides</h1><p>These pages ground the concepts in real scientific settings. Each guide names the quantity, what makes the domain hard, which concepts matter, and the failure test.</p><div class=\"grid\">{''.join(domain_cards)}</div>"),
        encoding="utf-8",
    )

    check_cards = []
    for check in reader_checks:
        check_cards.append(reader_check_card(check))
        write_reader_check_page(check_dir / f"{check['slug']}.html", check)
    (SITE / "reader-checks.html").write_text(
        html_page("Physics-Informed ML Reader Checks", f"<h1>Reader Checks</h1><p>These prompts test whether a reader can name the observed evidence, hidden quantity, method, failure case, and domain claim without hiding behind method names.</p><div class=\"grid\">{''.join(check_cards)}</div>"),
        encoding="utf-8",
    )

    decision_cards = []
    for decision in decision_guides:
        decision_cards.append(decision_card(decision))
        write_decision_page(decision_dir / f"{decision['slug']}.html", decision)
    (SITE / "decision-guide.html").write_text(
        html_page("Physics-Informed ML Decision Guide", f"<h1>Decision Guide</h1><p>Start from the scientific situation, not the method name. Each case names when a method fits, when to avoid it, and what evidence would make the choice defensible.</p><div class=\"grid\">{''.join(decision_cards)}</div>"),
        encoding="utf-8",
    )

    provenance_cards = []
    for guide in provenance_guides:
        provenance_cards.append(provenance_card(guide))
        write_provenance_page(provenance_dir / f"{guide['slug']}.html", guide)
    (SITE / "provenance.html").write_text(
        html_page("Physics-Informed ML Provenance", f"<h1>Provenance And Reproduction</h1><p>These pages show how source playlists, captions, cleaned transcripts, analysis data, and generated pages fit together. They also state what another CLI should reproduce for a similar channel.</p><div class=\"grid\">{''.join(provenance_cards)}</div>"),
        encoding="utf-8",
    )

    write_coverage_page(SITE / "coverage.html", list(coverage_matrix))
    write_dependency_map_page(SITE / "dependencies.html", list(dependency_map))
    write_concept_ladder_page(SITE / "concept-ladder.html", list(concept_ladder))
    packet_cards = []
    for packet in concept_evidence_packets:
        packet_cards.append(card(str(packet["title"]), str(packet["common_problem"]), str(packet["packet_href"])))
        write_concept_evidence_packet_page(packet_dir / f"{packet['slug']}.html", packet)
    (SITE / "evidence-packets.html").write_text(
        html_page("Physics-Informed ML Evidence Packets", f"<h1>Concept Evidence Packets</h1><p>Each packet gathers one concept's transcript support, source limits, and review links. Use these pages to check what the course evidence supports before making wider claims.</p><div class=\"grid\">{''.join(packet_cards)}</div>"),
        encoding="utf-8",
    )

    quality_cards = []
    for item in quality_rubric:
        quality_cards.append(quality_card(item))
        write_quality_page(quality_dir / f"{item['slug']}.html", item)
    (SITE / "quality.html").write_text(
        html_page("Physics-Informed ML Quality Rubric", f"<h1>Editorial Quality Rubric</h1><p>This rubric defines what a strong page must do: start from first principles, use plain language, name the domain, state failure boundaries, separate evidence from proof, and connect the concept to the rest of the field.</p><div class=\"grid\">{''.join(quality_cards)}</div>"),
        encoding="utf-8",
    )

    synthesis_cards = []
    for item in synthesis_guides:
        synthesis_cards.append(synthesis_card(item))
        write_synthesis_page(synthesis_dir / f"{item['slug']}.html", item)
    (SITE / "synthesis.html").write_text(
        html_page("Physics-Informed ML Synthesis", f"<h1>Field Synthesis</h1><p>This section ties the package into one argument: start from the scientific job, choose the mathematical move that carries the right evidence, and test the claim under a changed case.</p><div class=\"grid\">{''.join(synthesis_cards)}</div>"),
        encoding="utf-8",
    )

    write_handoff_page(SITE / "handoff.html", dict(review_handoff), summary)
    write_review_entrypoints_page(SITE / "review-entrypoints.html", list(review_entrypoints))
    write_review_search_page(SITE / "review-search.html", list(review_search_index))
    write_editorial_roadmap_page(SITE / "editorial-roadmap.html", list(editorial_roadmap))
    write_completion_audit_page(SITE / "completion-audit.html", list(completion_requirements), summary)
    write_meaty_goal_page(SITE / "meaty-goal.html", dict(meaty_goal))

    theme_cards = []
    for theme in themes:
        video_links = "".join(f"<li>{html.escape(row['title'])}</li>" for row in theme["videos"][:5])
        theme_cards.append(f"<article class=\"card\"><h3>{html.escape(theme['name'])}</h3><p>{html.escape(theme['problem'])}</p><ul>{video_links}</ul></article>")
    (SITE / "theme-map.html").write_text(
        html_page("Physics-Informed ML Theme Map", f"<h1>Theme Map</h1><div class=\"grid\">{''.join(theme_cards)}</div>"),
        encoding="utf-8",
    )

    evidence_rows = []
    for row in evidence:
        evidence_rows.append(
            f"<tr><td>{html.escape(row['claim'])}</td><td>{html.escape(row['support_type'])}</td><td><a href=\"{html.escape(row['url'])}\">{html.escape(row['video'])}</a></td><td>{html.escape(row['limit'])}</td></tr>"
        )
    (SITE / "evidence-ledger.html").write_text(
        html_page(
            "Physics-Informed ML Evidence Ledger",
            f"<h1>Evidence Ledger</h1><table><thead><tr><th>Claim</th><th>Support</th><th>Video</th><th>Limit</th></tr></thead><tbody>{''.join(evidence_rows)}</tbody></table>",
        ),
        encoding="utf-8",
    )

    manifest = sorted(str(path.relative_to(ROOT)) for path in SITE.rglob("*.html"))
    (SITE / "page-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def write_video_page(path: Path, record: TranscriptRecord) -> None:
    excerpt = record.evidence_excerpt or "No transcript excerpt was available; this page is based on metadata until captions can be added."
    body = f"""
<h1>{html.escape(record.title)}</h1>
<p class="meta">{html.escape(record.playlist_title)} · transcript {html.escape(record.transcript_status)} · {record.word_count} words</p>
<p><a href="{html.escape(record.url)}">Source video</a></p>
<h2>Core Problem</h2>
<p>This lecture belongs to a course family about using AI for scientific and engineering claims. The page should be read by asking what scientific quantity is being predicted, what evidence is available, and what changed case would show the model is not ready.</p>
<h2>Key Concepts</h2>
<ul>{''.join(f'<li>{html.escape(concept)}</li>' for concept in record.concepts)}</ul>
<h2>Transcript-Backed Note</h2>
<p>{html.escape(excerpt)}</p>
<h2>What This Does Not Prove</h2>
<p>A transcript mention shows the concept appears in the lecture. It does not prove the method works for every scientific system, every data size, or every future case.</p>
<h2>Local Files</h2>
<ul>
  <li>Clean transcript: {html.escape(record.clean_txt or 'missing')}</li>
  <li>Raw captions: {html.escape(record.raw_vtt or 'missing')}</li>
  <li>Metadata: {html.escape(record.metadata_json or 'missing')}</li>
</ul>
"""
    path.write_text(html_page(record.title, body, root_prefix="../"), encoding="utf-8")


def topic_derivation(topic: dict[str, object]) -> dict[str, object]:
    slug = str(topic["slug"])
    derivations = {
        "physics-informed-neural-networks": {
            "observed": "some measured values, boundary values, starting values, and a known differential equation",
            "hidden": "the full field value at every point in space and time",
            "move": "fit a neural network while also measuring how badly its output violates the known equation",
            "form": "prediction error + equation error + boundary error",
            "meaning": "the model is not allowed to match points while freely breaking the equation between those points",
            "test": "move the training points, inspect sharp regions, and compare against a numerical solve or held-out measurements",
        },
        "operator-learning": {
            "observed": "many example inputs and their full solution fields",
            "hidden": "the rule that maps a new input field to its new solution field",
            "move": "learn the map from problem input to solution, not only one solution at a time",
            "form": "input function -> learned map -> output function",
            "meaning": "the learned object is a shortcut for a family of solves, so the family must be named",
            "test": "change resolution, coefficients, boundary conditions, or forcing and check whether the predicted field still satisfies the scientific quantity being claimed",
        },
        "partial-differential-equations": {
            "observed": "a field such as temperature, pressure, concentration, velocity, or displacement",
            "hidden": "how every point in the field affects nearby points over time",
            "move": "write a local change rule that uses rates across space and time",
            "form": "future change = spatial change + sources + boundary information",
            "meaning": "the equation carries how a whole field changes, not just how one number changes",
            "test": "change the boundary, grid, source term, or physical scale and check conservation, stability, and measured error",
        },
        "deep-learning": {
            "observed": "many input-output examples from experiments, simulations, or measurements",
            "hidden": "the exact rule that connects the input to the output",
            "move": "adjust many weights until the model maps familiar inputs to the right outputs",
            "form": "input -> layered adjustable calculation -> prediction",
            "meaning": "the model earns attention only when prediction survives examples it did not train on",
            "test": "hold out a changed material, geometry, parameter range, or sensor condition",
        },
        "scientific-machine-learning": {
            "observed": "data, equations, units, simulation outputs, and domain limits",
            "hidden": "which parts of the scientific system are missing, noisy, or too costly to compute directly",
            "move": "combine learned prediction with scientific checks that name what the claim is allowed to mean",
            "form": "data fit + scientific structure + validation case",
            "meaning": "the model is judged by a scientific job, not by a score floating away from the job",
            "test": "state the scientific quantity first, then test it under a changed case that matters in that domain",
        },
        "surrogate-modeling": {
            "observed": "expensive solver inputs and outputs for a limited set of cases",
            "hidden": "the solver answer for every new query someone wants to ask",
            "move": "train a cheaper stand-in for the expensive input-output behavior",
            "form": "query -> fast stand-in -> approximate answer",
            "meaning": "speed is useful only inside the query family where the stand-in was checked",
            "test": "compare against the full solver on new cases near the edge of the intended use",
        },
        "uncertainty-and-generalization": {
            "observed": "training cases, validation cases, prediction errors, and known shifts between cases",
            "hidden": "how wrong the model may be on a case unlike the ones it learned from",
            "move": "separate fit on familiar examples from evidence on changed examples",
            "form": "prediction + error check + stated use range",
            "meaning": "a prediction without a use range is not yet a scientific claim",
            "test": "move one important condition outside the training range and measure the first failure",
        },
        "optimization-for-learning": {
            "observed": "a written score that says which model behavior is better or worse",
            "hidden": "whether that score matches the scientific behavior the user actually cares about",
            "move": "change model settings to lower the written score",
            "form": "choose settings that reduce data error, physics error, or design cost",
            "meaning": "the model learns the score, so the score must include the scientific burden",
            "test": "inspect what the score ignores, then check whether the ignored behavior fails after training",
        },
        "generative-modeling": {
            "observed": "examples of fields, molecules, flows, shapes, or other scientific objects",
            "hidden": "the spread of possible valid objects beyond the examples",
            "move": "learn how to sample new candidates that resemble the training family",
            "form": "random seed + learned sampler -> candidate scientific object",
            "meaning": "a generated object must still pass physics and usefulness checks",
            "test": "measure constraints, rare cases, conservation, and downstream task performance on generated samples",
        },
        "graphs-and-geometric-learning": {
            "observed": "objects with parts and connections, such as meshes, molecules, or interacting components",
            "hidden": "which neighboring and long-range interactions control the scientific quantity",
            "move": "let information move along the object connections instead of flattening the object into a plain row",
            "form": "nodes + edges + update rule -> predicted property or field",
            "meaning": "the model keeps the structure of the scientific object visible",
            "test": "change the mesh, rotate or move the object, or add missing interactions and inspect what breaks",
        },
        "neural-differential-equations": {
            "observed": "measurements of a system changing over time",
            "hidden": "the rate rule that moves the present value into the future",
            "move": "learn the missing rate rule and place it inside a time-evolution calculation",
            "form": "current state -> learned rate -> next state",
            "meaning": "learning supplies the unknown change rule while the time update carries the idea of continuous motion",
            "test": "run longer than the training window and check whether small rate errors accumulate into drift",
        },
        "symbolic-regression": {
            "observed": "measured variables and candidate mathematical ingredients",
            "hidden": "which short formula, if any, actually explains the measured change",
            "move": "search for a readable equation that fits the data and survives a changed case",
            "form": "candidate formulas -> selected formula -> held-out test",
            "meaning": "a compact equation is a claim about structure, not just a curve through points",
            "test": "remove a needed variable, add noise, or test a new experiment and see whether the formula still predicts",
        },
        "foundation-models-for-pdes": {
            "observed": "many PDE problem instances across equations, grids, parameters, or physical settings",
            "hidden": "which shared structure carries from one scientific task to another",
            "move": "train one broad model to reuse structure across many related field-prediction tasks",
            "form": "many PDE tasks -> shared learned representation -> new task prediction",
            "meaning": "breadth is useful only if the new task shares the structure the model actually learned",
            "test": "hold out a new equation family, boundary type, scale, or rare regime and compare against a trusted solver",
        },
        "attention-for-scientific-fields": {
            "observed": "large fields where one location may depend on other locations",
            "hidden": "which distant parts matter for the local prediction",
            "move": "let the model choose which parts of the field exchange information",
            "form": "field pieces -> selected information exchange -> updated field pieces",
            "meaning": "attention is a routing rule for information, not proof that the selected route is physically complete",
            "test": "change the window size, inspect long-range effects, and compare behavior near boundaries or sharp structures",
        },
    }
    return derivations.get(
        slug,
        {
            "observed": "the available scientific evidence",
            "hidden": "the part of the system the evidence does not directly reveal",
            "move": "keep the information needed for the named scientific job",
            "form": "observed evidence -> kept representation -> checked claim",
            "meaning": "the concept is useful only where the kept information supports the claim",
            "test": "change the case and inspect the first visible failure",
        },
    )


def topic_wrong_use(topic: dict[str, object]) -> dict[str, str]:
    slug = str(topic["slug"])
    wrong_uses = {
        "physics-informed-neural-networks": {
            "mistake": "Use a PINN because sensor data are sparse, even though the boundary values are uncertain and the equation is missing a heat source.",
            "why_tempting": "The equation penalty gives the page a scientific look, and the fit can still pass through the measured points.",
            "what_breaks": "The model may satisfy the wrong problem: a field with the wrong boundary or missing source can look smooth while answering a different physical question.",
            "catch_test": "Change the boundary, add held-out sensors near the source region, and compare against a trusted solve.",
        },
        "partial-differential-equations": {
            "mistake": "Treat a field problem as independent point predictions and ignore boundaries, neighbors, and conservation.",
            "why_tempting": "Point predictions are easier to fit and can look accurate on randomly held-out samples.",
            "what_breaks": "The result may violate the movement of heat, mass, force, or momentum that made the field a scientific object in the first place.",
            "catch_test": "Change the boundary or grid and check conservation, stability, and error in the decision quantity.",
        },
        "operator-learning": {
            "mistake": "Train on one family of solved fields and use the learned map on a new boundary, geometry, or equation family without testing that shift.",
            "why_tempting": "The output field can look plausible, and the method is fast enough to invite broad reuse.",
            "what_breaks": "The learned map may be a shortcut for the training family rather than a reusable scientific solver.",
            "catch_test": "Hold out whole boundary types, coefficient ranges, resolutions, or equation families and compare the full field plus the scientific quantity.",
        },
        "deep-learning": {
            "mistake": "Use a large predictor because it fits old examples, then trust it on a new material, sensor, or geometry.",
            "why_tempting": "Low training or familiar-test error can hide that the new case asks a different scientific question.",
            "what_breaks": "The model can carry accidental patterns from old data instead of the physical relation needed for the new case.",
            "catch_test": "Build a test set that changes the material, geometry, scale, or measurement process and inspect the first failure.",
        },
        "scientific-machine-learning": {
            "mistake": "Call a model scientific because it is used on scientific data, without naming the quantity, evidence, domain limit, or rejection test.",
            "why_tempting": "The setting sounds scientific even when the model is judged only by a generic score.",
            "what_breaks": "The claim floats away from the scientific job and cannot say what would make the answer unusable.",
            "catch_test": "Rewrite the claim as quantity, evidence, hidden part, mathematical move, and changed-case test; reject it if any part is missing.",
        },
        "surrogate-modeling": {
            "mistake": "Replace the trusted simulator everywhere because the surrogate is much faster.",
            "why_tempting": "Speed immediately expands design sweeps, searches, and uncertainty runs.",
            "what_breaks": "The shortcut can silently fail near edge cases, peaks, rare regimes, or decision boundaries where the full solver was most needed.",
            "catch_test": "Run the trusted source again near the edge of intended use and compare the decision quantity, not only average error.",
        },
        "uncertainty-and-generalization": {
            "mistake": "Report a confidence number without testing the changed condition the user actually cares about.",
            "why_tempting": "A number looks like caution and can make a prediction feel complete.",
            "what_breaks": "Confidence can remain high exactly where the model has the least evidence.",
            "catch_test": "Name the real shift, measure error under that shift, and state the first condition where the model should not be used.",
        },
        "optimization-for-learning": {
            "mistake": "Optimize the written loss and assume the scientific goal improved with it.",
            "why_tempting": "The loss gives a clean progress number during training.",
            "what_breaks": "The model improves what was scored while ignoring what the score forgot: boundaries, rare cases, units, conservation, or the decision quantity.",
            "catch_test": "List what the loss does not penalize, then test those ignored requirements after training.",
        },
        "generative-modeling": {
            "mistake": "Accept generated fields, molecules, or designs because they look like the training examples.",
            "why_tempting": "Plausible samples make exploration feel successful before any physical check is done.",
            "what_breaks": "A generated object can resemble the data while breaking conservation, constraints, rarity, or downstream usefulness.",
            "catch_test": "Check constraints, physical validity, rare-event behavior, and the downstream decision before keeping generated samples.",
        },
        "graphs-and-geometric-learning": {
            "mistake": "Use a graph model because the data have connections, without checking whether the chosen graph represents the interactions that matter.",
            "why_tempting": "Nodes and edges make the representation look faithful to the scientific object.",
            "what_breaks": "Wrong neighborhoods, missing long-range effects, or mesh changes can hide the physical relation the graph was meant to keep.",
            "catch_test": "Change mesh resolution, rotate or move the object, add missing interactions, and compare the scientific quantity.",
        },
        "neural-differential-equations": {
            "mistake": "Fit short observed trajectories and trust the learned rate for long-time prediction.",
            "why_tempting": "The short path can match measurements while hiding small rate errors.",
            "what_breaks": "Small errors in the learned change rule can accumulate until the system drifts into impossible behavior.",
            "catch_test": "Run past the training window and check conservation, stability, long-time drift, and changed initial conditions.",
        },
        "symbolic-regression": {
            "mistake": "Treat the shortest fitted formula as a discovered law.",
            "why_tempting": "A compact equation is easy to read and can feel more truthful than a large fitted model.",
            "what_breaks": "The formula may use the wrong variables, fit noise, or work only because the experiment never excited the missing cause.",
            "catch_test": "Run a changed experiment, test missing variables, add noise checks, and reject formulas that fail outside the discovery data.",
        },
        "foundation-models-for-pdes": {
            "mistake": "Assume a broad PDE model covers a new equation because it was trained on many tasks.",
            "why_tempting": "Scale and breadth can sound like coverage.",
            "what_breaks": "The model may not have learned the structure needed for a rare regime, boundary type, scale, or output quantity.",
            "catch_test": "Hold out whole task families, not just random examples, and compare against trusted solves on the new family.",
        },
        "attention-for-scientific-fields": {
            "mistake": "Assume attention found the physically important interactions because it connected distant field parts.",
            "why_tempting": "The information-routing picture is intuitive and visually persuasive.",
            "what_breaks": "The chosen attention pattern can miss long-range effects, boundary behavior, sharp structures, or conservation needs.",
            "catch_test": "Vary the window or routing pattern, stress long-range interactions, and inspect the physical quantity near hard regions.",
        },
    }
    return wrong_uses.get(
        slug,
        {
            "mistake": "Use the concept because the label sounds relevant, without naming the scientific quantity and evidence.",
            "why_tempting": "The method name can make the page feel complete before the problem is clear.",
            "what_breaks": "The explanation cannot say what was kept, what was ignored, or what changed case would reject it.",
            "catch_test": "Rewrite the claim as observed evidence, hidden quantity, mathematical move, domain reason, and changed-case test.",
        },
    )


def topic_wrong_use_html(topic: dict[str, object]) -> str:
    wrong = topic_wrong_use(topic)
    return f"""
<h2>Concrete Wrong-Use Example</h2>
<table>
  <tbody>
    <tr><th>Mistake</th><td>{html.escape(wrong['mistake'])}</td></tr>
    <tr><th>Why It Is Tempting</th><td>{html.escape(wrong['why_tempting'])}</td></tr>
    <tr><th>What Breaks</th><td>{html.escape(wrong['what_breaks'])}</td></tr>
    <tr><th>Test That Catches It</th><td>{html.escape(wrong['catch_test'])}</td></tr>
  </tbody>
</table>
"""


def topic_worked_examples_html(slug: str) -> str:
    matches = [example for example in WORKED_EXAMPLES if slug in example["method_route"]]
    if not matches:
        return ""
    cards = []
    for example in matches[:2]:
        cards.append(
            f"""
<article class="card">
  <h3><a href="../worked-examples/{html.escape(str(example['slug']))}.html">{html.escape(str(example['title']))}</a></h3>
  <p><strong>Domain:</strong> {html.escape(str(example['domain']))}</p>
  <p><strong>Question:</strong> {html.escape(str(example['question']))}</p>
  <p><strong>Observed:</strong> {html.escape(str(example['observed']))}</p>
  <p><strong>Hidden:</strong> {html.escape(str(example['hidden']))}</p>
  <p><strong>Why this example belongs here:</strong> {html.escape(str(example['why_it_teaches']))}</p>
</article>
"""
        )
    return f"""
<h2>Concrete Worked Example</h2>
<p>This concept becomes clearer when it is attached to a scientific job with observed evidence, a hidden quantity, and a testable claim.</p>
<div class="grid">{''.join(cards)}</div>
"""


def write_topic_page(path: Path, topic: dict[str, object]) -> None:
    evidence = topic.get("evidence", [])
    evidence_items = []
    if isinstance(evidence, list):
        for row in evidence:
            evidence_items.append(f"<li><a href=\"{html.escape(str(row['url']))}\">{html.escape(str(row['title']))}</a>: {html.escape(str(row.get('excerpt') or 'metadata evidence'))}</li>")
    derivation = topic_derivation(topic)
    deep_dive = topic_deep_dive_html(str(topic["slug"]))
    sketches = topic_sketches_html(str(topic["slug"]))
    diagrams = topic_diagrams_html(str(topic["slug"]))
    reader_check = topic_reader_check_html(str(topic["slug"]))
    derivation_link = topic_derivation_link_html(str(topic["slug"]))
    source_anchors = source_anchor_cards(str(topic["slug"]), list(evidence) if isinstance(evidence, list) else [], root_prefix="../")
    first_principles_essay = topic_first_principles_essay_html(topic, derivation)
    wrong_use = topic_wrong_use_html(topic)
    worked_examples = topic_worked_examples_html(str(topic["slug"]))
    body = f"""
<h1>{html.escape(str(topic['title']))}</h1>
<h2>Common Problem This Solves</h2>
<p>{html.escape(str(topic['common_problem']))}</p>
<h2>Big Picture Plain Summary</h2>
<p><strong>Domain:</strong> {html.escape(str(topic['domain']))}</p>
<p><strong>Why it matters:</strong> {html.escape(str(topic['why_it_matters']))}</p>
<p><strong>What it keeps:</strong> {html.escape(str(topic['keeps']))}</p>
<p><strong>What it leaves out:</strong> {html.escape(str(topic['leaves_out']))}</p>
<h2>Everyday Anchor</h2>
<p>{html.escape(str(topic['everyday_anchor']))}</p>
{first_principles_essay}
<h2>First-Principles Walkthrough</h2>
<ol>
  <li><strong>Start with what is observed:</strong> {html.escape(str(derivation['observed']))}.</li>
  <li><strong>Name what is hidden:</strong> {html.escape(str(derivation['hidden']))}.</li>
  <li><strong>Make the smallest mathematical move:</strong> {html.escape(str(derivation['move']))}.</li>
  <li><strong>Read the shape:</strong> {html.escape(str(derivation['form']))}.</li>
  <li><strong>Say what it means:</strong> {html.escape(str(derivation['meaning']))}.</li>
</ol>
{deep_dive}
{sketches}
{diagrams}
{derivation_link}
{worked_examples}
{wrong_use}
<h2>Deeper Mathematical Why</h2>
<p>The mathematical point is to decide what information is allowed to carry the scientific claim. If the carried information is too small, the model misses the behavior that matters. If it is too broad, the page may claim more than the evidence supports. The useful middle is a named object, a named scientific job, and a changed case that can reject the claim.</p>
{reader_check}
<h2>Reader Test</h2>
<p>A reader understands this concept only if they can say what is observed, what is hidden, what is kept, what is ignored, and why this changed-case test matters: {html.escape(str(derivation['test']))}.</p>
<h2>Failure Boundary</h2>
<p>{html.escape(str(topic['failure_boundary']))}</p>
<h2>What The Transcript Does Not Prove</h2>
<p>The transcript evidence shows where the course introduces or uses this concept. It does not prove the concept works for every equation, data set, solver, material, geometry, or scientific task. That wider claim needs explicit validation evidence.</p>
{source_anchors}
<h2>Transcript Evidence</h2>
<ul>{''.join(evidence_items)}</ul>
"""
    path.write_text(html_page(str(topic["title"]), body, root_prefix="../"), encoding="utf-8")


def topic_first_principles_essay_html(topic: dict[str, object], derivation: dict[str, object]) -> str:
    title = str(topic["title"])
    domain = str(topic["domain"])
    problem = str(topic["common_problem"])
    observed = str(derivation["observed"])
    hidden = str(derivation["hidden"])
    move = str(derivation["move"])
    form = str(derivation["form"])
    meaning = str(derivation["meaning"])
    test = str(derivation["test"])
    keeps = str(topic["keeps"])
    leaves_out = str(topic["leaves_out"])
    why = str(topic["why_it_matters"])
    failure = str(topic["failure_boundary"])
    anchor = str(topic["everyday_anchor"])
    return f"""
<h2>First-Principles Essay</h2>
<p>Start before the method name. In {html.escape(domain)}, the real difficulty is this: {html.escape(problem)}. The concept called {html.escape(title)} is useful only if it helps carry the right information from the evidence already available to the answer the scientist still needs. The name of the method is secondary. The first question is what the world is asking us to recover, predict, explain, or check.</p>
<p>The observed side is {html.escape(observed)}. That is the part the page is allowed to use as evidence. The hidden side is {html.escape(hidden)}. That is the part a reader should keep their eyes on, because the hidden part is where bad explanations often slip in. A weak writeup says the model learns a pattern. A stronger writeup says exactly which hidden quantity is being asked for and what would count as evidence that the answer is wrong.</p>
<p>The mathematical move follows from that shortage. Here the move is: {html.escape(move)}. The shape is: {html.escape(form)}. Read that shape as a promise about information. It says which facts are kept, which checks are made, and which parts of the real scientific situation are not being carried. In this case, the concept keeps {html.escape(keeps)}. It leaves out {html.escape(leaves_out)}. That missing part is not a footnote; it is the boundary of the claim.</p>
<p>The reason this matters is not the method name. It matters because {html.escape(why)}. If the method works, it gives a scientist a usable answer for a named situation. If it fails, it usually fails in a concrete way: {html.escape(failure)}. That is why the page must end with a changed-case test rather than a general statement of confidence.</p>
<h3>Tiny Concrete Version</h3>
<p>{html.escape(anchor)} Strip away the notation and the question becomes: what do we know, what do we not know, what rule or pattern is allowed to connect them, and what changed case would make us stop trusting the answer?</p>
<h3>What A Strong Explanation Must Say</h3>
<ol>
  <li>Name the real quantity, not only the method.</li>
  <li>Name the evidence: data, equation, simulation, boundary, geometry, or previous cases.</li>
  <li>Name the hidden quantity the method is trying to recover.</li>
  <li>Name the mathematical move in plain language: {html.escape(meaning)}.</li>
  <li>Name the rejection test: {html.escape(test)}.</li>
</ol>
"""


def write_diagram_page(path: Path, diagram: dict[str, object]) -> None:
    topic_list = concept_links(list(diagram["topic_slugs"]), root_prefix="../")
    body = f"""
<h1>{html.escape(str(diagram['title']))}</h1>
<h2>Purpose</h2>
<p>{html.escape(str(diagram['purpose']))}</p>
<h2>Flow</h2>
{diagram_flow_html(diagram)}
<h2>Related Concepts</h2>
{topic_list}
<h2>How To Read It</h2>
<p>Move left to right. Each box names the information being carried forward. The last box is not decoration; it is the check that decides whether the claim should be trusted.</p>
"""
    path.write_text(html_page(str(diagram["title"]), body, root_prefix="../"), encoding="utf-8")


def write_core_derivation_page(path: Path, derivation: dict[str, object]) -> None:
    steps = "".join(
        f"<div class=\"route-step\">{idx}. {html.escape(str(step))}</div>"
        for idx, step in enumerate(derivation["math_shape"], start=1)
    )
    hand_block = ""
    hand = derivation.get("hand_derivation")
    if isinstance(hand, dict):
        hand_rows = []
        for item in hand["line_steps"]:
            hand_rows.append(
                f"""
<tr>
  <td>{html.escape(str(item['term']))}</td>
  <td>{html.escape(str(item['why_it_enters']))}</td>
  <td>{html.escape(str(item['check']))}</td>
</tr>
"""
            )
        hand_block = f"""
<h2>Hand Derivation</h2>
<p>{html.escape(str(hand['plain_start']))}</p>
<table>
  <thead>
    <tr>
      <th>Term</th>
      <th>Why It Enters</th>
      <th>Check</th>
    </tr>
  </thead>
  <tbody>{''.join(hand_rows)}</tbody>
</table>
<p><strong>Final Line:</strong> {html.escape(str(hand['final_line']))}</p>
"""
    red_flags = "".join(f"<li>{html.escape(str(item))}</li>" for item in derivation["red_flags"])
    related = concept_links(list(derivation["connects_to"]), root_prefix="../")
    body = f"""
<h1>{html.escape(str(derivation['title']))}</h1>
<p>{html.escape(str(derivation['one_sentence']))}</p>
<h2>Domain Story</h2>
<p>{html.escape(str(derivation['domain_story']))}</p>
<h2>Problem</h2>
<p>{html.escape(str(derivation['common_problem']))}</p>
<h2>Start With What Is Observed</h2>
<p>{html.escape(str(derivation['observed']))}</p>
<h2>Name What Is Hidden</h2>
<p>{html.escape(str(derivation['hidden']))}</p>
<h2>Build The Mathematical Shape</h2>
<div class="route">{steps}</div>
{hand_block}
<h2>Plain Formula</h2>
<p>{html.escape(str(derivation['plain_formula']))}</p>
<h2>Why This Matters</h2>
<p>{html.escape(str(derivation['why_it_matters']))}</p>
<h2>Failure Test</h2>
<p>{html.escape(str(derivation['failure_test']))}</p>
<h2>Red Flags</h2>
<ul>{red_flags}</ul>
<h2>Connects To</h2>
{related}
<h2>Topic Page</h2>
<p><a href="../{html.escape(str(derivation['topic_href']))}">Return to the main topic page</a></p>
"""
    path.write_text(html_page(str(derivation["title"]), body, root_prefix="../"), encoding="utf-8")


def write_formula_guide_page(path: Path, rows: list[dict[str, object]]) -> None:
    table_rows = []
    for row in rows:
        parts = "".join(f"<li>{html.escape(str(part))}</li>" for part in row["parts"])
        table_rows.append(
            f"""
<tr>
  <td>{html.escape(str(row['title']))}<br><a href="{html.escape(str(row['topic_href']))}">topic</a> · <a href="{html.escape(str(row['derivation_href']))}">derivation</a></td>
  <td><code>{html.escape(str(row['plain_formula']))}</code></td>
  <td><ul>{parts}</ul></td>
  <td>{html.escape(str(row['everyday_reading']))}</td>
  <td>{html.escape(str(row['what_to_check']))}</td>
  <td>{html.escape(str(row['common_misread']))}</td>
</tr>
"""
        )
    body = f"""
<h1>Plain Formula Guide</h1>
<p>This page translates the recurring formula shapes into everyday meaning. The goal is not to teach notation first. The goal is to show what information each formula carries, what it asks the model to do, and what test keeps the claim honest.</p>
<table>
  <thead>
    <tr>
      <th>Concept</th>
      <th>Formula Shape</th>
      <th>Parts</th>
      <th>Everyday Reading</th>
      <th>What To Check</th>
      <th>Common Misread</th>
    </tr>
  </thead>
  <tbody>{''.join(table_rows)}</tbody>
</table>
"""
    path.write_text(html_page("Physics-Informed ML Plain Formula Guide", body), encoding="utf-8")


def write_misconception_map_page(path: Path, rows: list[dict[str, object]]) -> None:
    table_rows = []
    for row in rows:
        wrong_turns = "".join(f"<li>{html.escape(str(item))}</li>" for item in row["wrong_turns"])
        check_link = ""
        if row["reader_check_href"]:
            check_link = f' · <a href="{html.escape(str(row["reader_check_href"]))}">reader check</a>'
        table_rows.append(
            f"""
<tr>
  <td><a href="{html.escape(str(row['topic_href']))}">{html.escape(str(row['title']))}</a></td>
  <td><ul>{wrong_turns}</ul></td>
  <td>{html.escape(str(row['plain_correction']))}</td>
  <td>{html.escape(str(row['first_principles_test']))}</td>
  <td><a href="{html.escape(str(row['derivation_href']))}">derivation</a>{check_link}</td>
</tr>
"""
        )
    body = f"""
<h1>Misconception Map</h1>
<p>This page lists common wrong turns for the core concepts. Each row pairs the misread with a plain correction and the first-principles test that should replace vague confidence.</p>
<table>
  <thead>
    <tr>
      <th>Concept</th>
      <th>Wrong Turn</th>
      <th>Plain Correction</th>
      <th>First-Principles Test</th>
      <th>Review Links</th>
    </tr>
  </thead>
  <tbody>{''.join(table_rows)}</tbody>
</table>
"""
    path.write_text(html_page("Physics-Informed ML Misconception Map", body), encoding="utf-8")


def write_learning_step_page(path: Path, step: dict[str, object]) -> None:
    read_items = []
    for item in step["read"]:
        read_items.append(f"<li><a href=\"../{html.escape(str(item['href']))}\">{html.escape(str(item['label']))}</a></li>")
    spine_items = "".join(f"<li>{html.escape(str(item))}</li>" for item in step["first_principles_spine"])
    body = f"""
<h1>{html.escape(str(step['title']))}</h1>
<h2>Question</h2>
<p>{html.escape(str(step['question']))}</p>
<h2>Why This Comes Here</h2>
<p>{html.escape(str(step['why_first']))}</p>
<h2>Plain Goal</h2>
<p>{html.escape(str(step['plain_goal']))}</p>
<h2>No-Jargon Explanation</h2>
<p>{learning_step_plain_essay(step)}</p>
<h2>First-Principles Spine</h2>
<ul>{spine_items}</ul>
<h2>Read Next</h2>
<ul>{''.join(read_items)}</ul>
<h2>Checkpoint</h2>
<p>{html.escape(str(step['checkpoint']))}</p>
"""
    path.write_text(html_page(str(step["title"]), body, root_prefix="../"), encoding="utf-8")


def learning_step_plain_essay(step: dict[str, object]) -> str:
    spine = [str(item) for item in step["first_principles_spine"]]
    return html.escape(
        " ".join(
            [
                "This step asks the reader to slow down before reaching for a method name.",
                spine[0],
                spine[1],
                spine[2],
                "The point is to make the missing piece visible before choosing any model.",
                spine[3],
                "That move is only useful if it survives the stated rejection test.",
                spine[4],
                "If a reader cannot say this in ordinary language, they are not ready to trust the technical page that follows.",
            ]
        )
    )


def write_glossary_page(path: Path, entry: dict[str, object]) -> None:
    body = f"""
<h1>{html.escape(str(entry['term']))}</h1>
<h2>Everyday Meaning</h2>
<p>{html.escape(str(entry['everyday']))}</p>
<h2>Problem It Names</h2>
<p>{html.escape(str(entry['problem']))}</p>
<h2>Why It Matters</h2>
<p>{html.escape(str(entry['why_it_matters']))}</p>
<h2>What To Watch For</h2>
<p>{html.escape(str(entry['watch_for']))}</p>
<h2>Related Concepts</h2>
{concept_links(list(entry['related']), root_prefix="../")}
"""
    path.write_text(html_page(str(entry["term"]), body, root_prefix="../"), encoding="utf-8")


def write_domain_page(path: Path, guide: dict[str, object]) -> None:
    method_items = "".join(f"<li>{html.escape(str(item))}</li>" for item in guide["methods"])
    job = guide["domain_job"]
    domain_essay = domain_first_principles_essay_html(guide)
    body = f"""
<h1>{html.escape(str(guide['title']))}</h1>
<h2>Real Quantity</h2>
<p>{html.escape(str(guide['real_quantity']))}</p>
<h2>Why This Domain Is Hard</h2>
<p>{html.escape(str(guide['why_hard']))}</p>
<h2>Common Question</h2>
<p>{html.escape(str(guide['common_question']))}</p>
{domain_essay}
<h2>Concrete Scientific Job</h2>
<table>
  <tbody>
    <tr><th>Scientific Job</th><td>{html.escape(str(job['scientific_job']))}</td></tr>
    <tr><th>Observed Evidence</th><td>{html.escape(str(job['observed_evidence']))}</td></tr>
    <tr><th>Hidden Quantity</th><td>{html.escape(str(job['hidden_quantity']))}</td></tr>
    <tr><th>Decision</th><td>{html.escape(str(job['decision']))}</td></tr>
    <tr><th>Changed-Case Test</th><td>{html.escape(str(job['changed_case_test']))}</td></tr>
  </tbody>
</table>
<h2>Concepts That Matter</h2>
{concept_links(list(guide['concepts']), root_prefix="../")}
<h2>How The Methods Enter</h2>
<ul>{method_items}</ul>
<h2>Failure Test</h2>
<p>{html.escape(str(guide['failure_test']))}</p>
<h2>Concrete Anchor</h2>
<p><a href="../{html.escape(str(guide['example']))}">Related page</a></p>
"""
    path.write_text(html_page(str(guide["title"]), body, root_prefix="../"), encoding="utf-8")


def domain_first_principles_essay_html(guide: dict[str, object]) -> str:
    job = guide["domain_job"]
    methods = " ".join(str(item) for item in guide["methods"])
    return f"""
<h2>Walk The Domain From Scratch</h2>
<p>Begin with the quantity, not the algorithm. In this domain the quantity is {html.escape(str(guide['real_quantity']))}. A useful page has to say where that quantity lives, how it is observed, and why a wrong estimate would matter. The hard part is not that the domain has technical vocabulary. The hard part is that {html.escape(str(guide['why_hard']))}.</p>
<p>The concrete job is: {html.escape(str(job['scientific_job']))} The evidence available is {html.escape(str(job['observed_evidence']))}. The hidden quantity is {html.escape(str(job['hidden_quantity']))}. This is the first-principles chain: evidence is partial, the needed quantity is larger than the evidence, and the method is only a bridge between the two.</p>
<p>The bridge matters because someone will make a decision: {html.escape(str(job['decision']))}. That decision gives the math its burden. Average visual similarity is not enough if the decision depends on a boundary layer, a rare event, a peak stress, a force, a concentration, or another local quantity. The domain test must therefore be: {html.escape(str(job['changed_case_test']))}.</p>
<h3>How The Methods Enter Without Jargon</h3>
<p>{html.escape(methods)} Read these as jobs, not labels. One method names how the quantity is allowed to change. Another makes a fast stand-in. Another keeps geometry or field structure visible. Another asks where belief should weaken. The right method is the one that carries the missing information needed for the decision and exposes the first condition where it breaks.</p>
"""


def write_reader_check_page(path: Path, check: dict[str, object]) -> None:
    questions = "".join(f"<li>{html.escape(str(question))}</li>" for question in check["questions"])
    related = "".join(f"<li><a href=\"../{html.escape(str(href))}\">{html.escape(str(href))}</a></li>" for href in check["related"])
    body = f"""
<h1>{html.escape(str(check['title']))}</h1>
<h2>Setup</h2>
<p>{html.escape(str(check['setup']))}</p>
<h2>Questions</h2>
<ol>{questions}</ol>
<h2>Strong Answer Should Say</h2>
<p>{html.escape(str(check['strong_answer']))}</p>
<h2>Weak Answer Warning</h2>
<p>{html.escape(str(check['weak_answer_warning']))}</p>
<h2>Related Pages</h2>
<ul>{related}</ul>
"""
    path.write_text(html_page(str(check["title"]), body, root_prefix="../"), encoding="utf-8")


def write_decision_page(path: Path, decision: dict[str, object]) -> None:
    use_if = "".join(f"<li>{html.escape(str(item))}</li>" for item in decision["use_if"])
    avoid_if = "".join(f"<li>{html.escape(str(item))}</li>" for item in decision["avoid_if"])
    links = "".join(f"<li><a href=\"../{html.escape(str(href))}\">{html.escape(str(href))}</a></li>" for href in decision["links"])
    body = f"""
<h1>{html.escape(str(decision['title']))}</h1>
<h2>Situation</h2>
<p>{html.escape(str(decision['situation']))}</p>
<h2>Best Starting Point</h2>
<p>{html.escape(str(decision['best_start']))}</p>
<h2>Why This Fits</h2>
<p>{html.escape(str(decision['why']))}</p>
<h2>Use If</h2>
<ul>{use_if}</ul>
<h2>Avoid If</h2>
<ul>{avoid_if}</ul>
<h2>Evidence Needed</h2>
<p>{html.escape(str(decision['evidence_needed']))}</p>
<h2>Related Pages</h2>
<ul>{links}</ul>
"""
    path.write_text(html_page(str(decision["title"]), body, root_prefix="../"), encoding="utf-8")


def write_provenance_page(path: Path, guide: dict[str, object]) -> None:
    steps = "".join(f"<li>{html.escape(str(step))}</li>" for step in guide["steps"])
    files = "".join(f"<li><code>{html.escape(str(item))}</code></li>" for item in guide["local_files"])
    checks = "".join(f"<li>{html.escape(str(check))}</li>" for check in guide["checks"])
    body = f"""
<h1>{html.escape(str(guide['title']))}</h1>
<h2>Purpose</h2>
<p>{html.escape(str(guide['purpose']))}</p>
<h2>Process</h2>
<ol>{steps}</ol>
<h2>Local Files</h2>
<ul>{files}</ul>
<h2>Checks</h2>
<ul>{checks}</ul>
"""
    path.write_text(html_page(str(guide["title"]), body, root_prefix="../"), encoding="utf-8")


def mark(value: object) -> str:
    return "yes" if bool(value) else "no"


def write_coverage_page(path: Path, rows: list[dict[str, object]]) -> None:
    table_rows = []
    for row in rows:
        table_rows.append(
            f"""
<tr>
  <td><a href="topics/{html.escape(str(row['slug']))}.html">{html.escape(str(row['name']))}</a></td>
  <td>{html.escape(str(row['video_count']))}</td>
  <td>{mark(row['deep_dive'])}</td>
  <td>{mark(row['diagram'])}</td>
  <td>{mark(row['learning_path'])}</td>
  <td>{mark(row['glossary'])}</td>
  <td>{mark(row['domain'])}</td>
  <td>{mark(row['reader_check'])}</td>
  <td>{mark(row['decision_guide'])}</td>
  <td>{html.escape(str(row['evidence_items']))}</td>
</tr>
"""
        )
    body = f"""
<h1>Coverage Matrix</h1>
<p>This page is a review surface. It shows which concepts are supported by transcript evidence and which guide layers explain, test, or apply the concept.</p>
<table>
  <thead>
    <tr>
      <th>Concept</th>
      <th>Videos</th>
      <th>Deep Dive</th>
      <th>Diagram</th>
      <th>Path</th>
      <th>Glossary</th>
      <th>Domain</th>
      <th>Reader Check</th>
      <th>Decision</th>
      <th>Evidence Items</th>
    </tr>
  </thead>
  <tbody>{''.join(table_rows)}</tbody>
</table>
"""
    path.write_text(html_page("Physics-Informed ML Coverage Matrix", body), encoding="utf-8")


def write_dependency_map_page(path: Path, rows: list[dict[str, object]]) -> None:
    table_rows = []
    for row in rows:
        depends = "".join(
            f"<li><a href=\"{html.escape(str(item['href']))}\">{html.escape(str(item['name']))}</a></li>"
            for item in row["depends_on"]
        )
        table_rows.append(
            f"""
<tr>
  <td><a href="{html.escape(str(row['concept_href']))}">{html.escape(str(row['concept_name']))}</a></td>
  <td><ul>{depends}</ul></td>
  <td>{html.escape(str(row['why']))}</td>
  <td>{html.escape(str(row['confusion_prevented']))}</td>
</tr>
"""
        )
    body = f"""
<h1>Concept Dependency Map</h1>
<p>This page shows which ideas should come before other ideas. Read it as a route for understanding, not as a ranking of importance.</p>
<table>
  <thead>
    <tr>
      <th>Concept</th>
      <th>Learn First</th>
      <th>Why This Dependency Matters</th>
      <th>Confusion It Prevents</th>
    </tr>
  </thead>
  <tbody>{''.join(table_rows)}</tbody>
</table>
<h2>How To Use This</h2>
<p>If a concept feels vague, move to its Learn First column and read those pages before returning. Most confusion comes from skipping the object being predicted, the rule being checked, or the failure test.</p>
"""
    path.write_text(html_page("Physics-Informed ML Concept Dependency Map", body), encoding="utf-8")


def write_concept_ladder_page(path: Path, rows: list[dict[str, object]]) -> None:
    table_rows = []
    for row in rows:
        evidence = ""
        if row["evidence_title"] and row["evidence_url"]:
            evidence = f'<a href="{html.escape(str(row["evidence_url"]))}">{html.escape(str(row["evidence_title"]))}</a>'
        table_rows.append(
            f"""
<tr>
  <td><a href="{html.escape(str(row['topic_href']))}">{html.escape(str(row['title']))}</a><br><span class="meta">{html.escape(str(row['domain']))}</span></td>
  <td>{html.escape(str(row['common_problem']))}</td>
  <td>{html.escape(str(row['observed']))}</td>
  <td>{html.escape(str(row['hidden']))}</td>
  <td>{html.escape(str(row['mathematical_move']))}</td>
  <td>{html.escape(str(row['shape']))}</td>
  <td>{html.escape(str(row['failure_test']))}</td>
  <td>{evidence}</td>
</tr>
"""
        )
    body = f"""
<h1>Concept Ladder</h1>
<p>This page lines up the main concepts by the same first-principles questions. Read each row from left to right: the real problem, what is observed, what is hidden, what mathematical move is made, what shape that move has, and what test can reject the claim.</p>
<table>
  <thead>
    <tr>
      <th>Concept</th>
      <th>Problem</th>
      <th>Observed</th>
      <th>Hidden</th>
      <th>Mathematical Move</th>
      <th>Shape</th>
      <th>Failure Test</th>
      <th>Evidence Anchor</th>
    </tr>
  </thead>
  <tbody>{''.join(table_rows)}</tbody>
</table>
<h2>How To Use This</h2>
<p>Pick one row and try to say it aloud without the method name. If the row still makes sense, the concept has a real job. If it only sounds important after the method name is added back, the explanation needs more work.</p>
"""
    path.write_text(html_page("Physics-Informed ML Concept Ladder", body), encoding="utf-8")


def write_concept_evidence_packet_page(path: Path, packet: dict[str, object]) -> None:
    evidence_items = []
    for item in packet["evidence"]:
        evidence_items.append(
            f"""
<li>
  <a href="{html.escape(str(item['url']))}">{html.escape(str(item['title']))}</a><br>
  <span class="meta">{html.escape(str(item.get('clean_txt') or 'transcript path missing'))}</span><br>
  {html.escape(str(item.get('excerpt') or 'No excerpt available.'))}
</li>
"""
        )
    limit_items = "".join(f"<li>{html.escape(str(item))}</li>" for item in packet["limits"])
    review_links = "".join(
        f"<li><a href=\"../{html.escape(str(item['href']))}\">{html.escape(str(item['label']))}</a></li>"
        for item in packet["review_links"]
    )
    source_anchors = source_anchor_cards(str(packet["slug"]), list(packet["evidence"]), root_prefix="../")
    body = f"""
<h1>{html.escape(str(packet['title']))}</h1>
<h2>Concept Job</h2>
<p><strong>Problem:</strong> {html.escape(str(packet['common_problem']))}</p>
<p><strong>Domain:</strong> {html.escape(str(packet['domain']))}</p>
<p><strong>Why it matters:</strong> {html.escape(str(packet['why_it_matters']))}</p>
{source_anchors}
<h2>Transcript Support</h2>
<p>This packet has {html.escape(str(packet['evidence_count']))} selected transcript anchors for review.</p>
<ul>{''.join(evidence_items)}</ul>
<h2>What This Evidence Does Not Prove</h2>
<ul>{limit_items}</ul>
<h2>Review Links</h2>
<ul>{review_links}</ul>
"""
    path.write_text(html_page(str(packet["title"]), body, root_prefix="../"), encoding="utf-8")


def write_quality_page(path: Path, item: dict[str, object]) -> None:
    body = f"""
<h1>{html.escape(str(item['title']))}</h1>
<h2>Standard</h2>
<p>{html.escape(str(item['standard']))}</p>
<h2>Strong Page</h2>
<p>{html.escape(str(item['strong_page']))}</p>
<h2>Weak Page</h2>
<p>{html.escape(str(item['weak_page']))}</p>
<h2>Check</h2>
<p>{html.escape(str(item['check']))}</p>
"""
    path.write_text(html_page(str(item["title"]), body, root_prefix="../"), encoding="utf-8")


def write_synthesis_page(path: Path, item: dict[str, object]) -> None:
    links = "".join(f"<li><a href=\"../{html.escape(str(href))}\">{html.escape(str(href))}</a></li>" for href in item["links"])
    body = f"""
<h1>{html.escape(str(item['title']))}</h1>
<h2>Claim</h2>
<p>{html.escape(str(item['claim']))}</p>
<h2>Explanation</h2>
<p>{html.escape(str(item['explanation']))}</p>
<h2>Reader Takeaway</h2>
<p>{html.escape(str(item['reader_takeaway']))}</p>
<h2>Follow The Links</h2>
<ul>{links}</ul>
"""
    path.write_text(html_page(str(item["title"]), body, root_prefix="../"), encoding="utf-8")


def link_list(items: list[dict[str, str]], prefix: str = "") -> str:
    return "<ul>" + "".join(f"<li><a href=\"{prefix}{html.escape(item['href'])}\">{html.escape(item['label'])}</a></li>" for item in items) + "</ul>"


def write_meaty_goal_page(path: Path, goal: dict[str, object]) -> None:
    done_items = "".join(f"<li>{html.escape(str(item))}</li>" for item in goal["done_means"])
    requirements = "".join(f"<li>{html.escape(str(item))}</li>" for item in goal["page_requirements"])
    not_done = "".join(f"<li>{html.escape(str(item))}</li>" for item in goal["not_done_if"])
    core_pages = link_list(list(goal["core_pages"]))
    body = f"""
<h1>{html.escape(str(goal['title']))}</h1>
<h2>Goal</h2>
<p>{html.escape(str(goal['short_goal']))}</p>
<h2>Target Reader</h2>
<p>{html.escape(str(goal['target_reader']))}</p>
<h2>Done Means</h2>
<ol>{done_items}</ol>
<h2>Core Pages To Finish To This Standard</h2>
{core_pages}
<h2>Every Core Page Must Contain</h2>
<ul>{requirements}</ul>
<h2>Acceptance Sentence</h2>
<p>A reviewer should be able to fill this in from the page alone:</p>
<blockquote>{html.escape(str(goal['acceptance_sentence']))}</blockquote>
<h2>Not Done If</h2>
<ul>{not_done}</ul>
<h2>How To Use This Goal</h2>
<p>Review one concept at a time. If the page cannot satisfy the acceptance sentence without relying on outside knowledge, keep editing that page. Passing validation only proves the site is structurally coherent; this goal defines the editorial finish line.</p>
"""
    path.write_text(html_page(str(goal["title"]), body), encoding="utf-8")


def write_handoff_page(path: Path, handoff: dict[str, object], summary: dict[str, object]) -> None:
    commands = "".join(f"<li><code>{html.escape(str(command))}</code></li>" for command in handoff["validation_commands"])
    remote_commands = "".join(f"<li><code>{html.escape(str(command))}</code></li>" for command in handoff["remote_finish_commands"])
    remaining = "".join(f"<li>{html.escape(str(item))}</li>" for item in handoff["remaining_editorial_work"])
    body = f"""
<h1>{html.escape(str(handoff['title']))}</h1>
<h2>Purpose</h2>
<p>{html.escape(str(handoff['purpose']))}</p>
<h2>Current Package Counts</h2>
<ul>
  <li>Videos: {html.escape(str(summary['video_count']))}</li>
  <li>Concepts: {html.escape(str(summary['concept_count']))}</li>
  <li>Available transcripts: {html.escape(str(summary['available_transcripts']))}</li>
  <li>Generated guide layers: learning path, glossary, domains, checks, decisions, provenance, coverage, quality, synthesis.</li>
</ul>
<h2>Start Here</h2>
{link_list(list(handoff['start_here']))}
<h2>Core Review Pages</h2>
{link_list(list(handoff['core_review_pages']))}
<h2>Validation Commands</h2>
<ul>{commands}</ul>
<h2>Remote Verification Commands</h2>
<p>{html.escape(str(handoff['remote_status']))}</p>
<ul>{remote_commands}</ul>
<h2>Remaining Editorial Work</h2>
<ul>{remaining}</ul>
"""
    path.write_text(html_page(str(handoff["title"]), body), encoding="utf-8")


def write_review_entrypoints_page(path: Path, groups: list[dict[str, object]]) -> None:
    sections = []
    for group in groups:
        item_cards = []
        for item in group["items"]:
            item_cards.append(
                f"""
<article class="card">
  <h3><a href="{html.escape(str(item['href']))}">{html.escape(str(item['label']))}</a></h3>
  <p><strong>Why open it:</strong> {html.escape(str(item['why']))}</p>
  <p><strong>Question it should answer:</strong> {html.escape(str(item['question']))}</p>
</article>
"""
            )
        sections.append(
            f"""
<h2>{html.escape(str(group['group']))}</h2>
<p>{html.escape(str(group['purpose']))}</p>
<div class="grid">{''.join(item_cards)}</div>
"""
        )
    body = f"""
<h1>Review Entrypoints</h1>
<p>This page gives a reviewer a concrete route through the package. It separates four jobs: see the whole argument, inspect the core concepts, use the package for a scientific situation, and check whether source support is clear.</p>
{''.join(sections)}
<h2>End-To-End Test</h2>
<p>A strong review can follow one concept from transcript evidence, to topic page, to diagram, to decision guide, to a domain example, then back to the coverage matrix. If that route breaks, the missing link is the next editorial task.</p>
"""
    path.write_text(html_page("Physics-Informed ML Review Entrypoints", body), encoding="utf-8")


def write_review_search_page(path: Path, rows: list[dict[str, object]]) -> None:
    cards = []
    for row in rows:
        pages = "".join(
            f"<li><a href=\"{html.escape(str(item['href']))}\">{html.escape(str(item['label']))}</a></li>"
            for item in row["pages"]
        )
        cards.append(
            f"""
<article class="card">
  <h3>{html.escape(str(row['intent']))}</h3>
  <p><strong>Look for:</strong> {html.escape(str(row['look_for']))}</p>
  <ul>{pages}</ul>
</article>
"""
        )
    body = f"""
<h1>Find Pages By Question</h1>
<p>This page maps reviewer questions to the strongest pages. Use it when you know what you need to check but not which index contains it.</p>
<div class="grid">{''.join(cards)}</div>
<h2>Review Rule</h2>
<p>Start from the question, open the page group, then follow links until the claim has a source, a domain, a formula shape, and a failure test.</p>
"""
    path.write_text(html_page("Physics-Informed ML Review Search", body), encoding="utf-8")


def write_editorial_roadmap_page(path: Path, rows: list[dict[str, object]]) -> None:
    cards = []
    for row in rows:
        targets = "".join(
            f"<li><a href=\"{html.escape(str(item['href']))}\">{html.escape(str(item['label']))}</a></li>"
            for item in row["target_pages"]
        )
        work = "".join(f"<li>{html.escape(str(item))}</li>" for item in row["work"])
        proof_pages = "".join(f"<li><a href=\"{html.escape(str(href))}\">{html.escape(str(href))}</a></li>" for href in row.get("proof_pages", []))
        cards.append(
            f"""
<article class="card">
  <p class="meta">{html.escape(str(row['priority']))}</p>
  <h3>{html.escape(str(row['title']))}</h3>
  <p><strong>Status:</strong> {html.escape(str(row.get('status', 'not started')))}</p>
  <p><strong>Goal:</strong> {html.escape(str(row['goal']))}</p>
  <p><strong>Why it matters:</strong> {html.escape(str(row['why']))}</p>
  <p><strong>Current Evidence:</strong> {html.escape(str(row.get('evidence', 'No local evidence recorded yet.')))}</p>
  <h4>Proof Pages</h4>
  <ul>{proof_pages}</ul>
  <h4>Target Pages</h4>
  <ul>{targets}</ul>
  <h4>Work</h4>
  <ul>{work}</ul>
  <p><strong>Acceptance Check:</strong> {html.escape(str(row['acceptance_check']))}</p>
</article>
"""
        )
    body = f"""
<h1>Editorial Roadmap</h1>
<p>This page tracks the next serious goal after the generated first pass: turn the strongest pages into hand-written, source-anchored teaching pages. The work is ordered by priority, each task has an acceptance check, and each row states the current local status.</p>
<div class="grid">{''.join(cards)}</div>
<h2>Meaty End-To-End Goal</h2>
<p>The end state is a package where a reader can start with a plain scientific problem, follow the evidence to a concept, see why the formula has its shape, inspect a domain example, and know the failure test. A task is not done until the target pages prove that route.</p>
"""
    path.write_text(html_page("Physics-Informed ML Editorial Roadmap", body), encoding="utf-8")


def write_completion_audit_page(path: Path, requirements: list[dict[str, object]], summary: dict[str, object]) -> None:
    rows = []
    for item in requirements:
        links = "".join(f"<li><a href=\"{html.escape(str(link))}\">{html.escape(str(link))}</a></li>" for link in item["links"])
        rows.append(
            f"""
<tr>
  <td>{html.escape(str(item['requirement']))}</td>
  <td>{html.escape(str(item['status']))}</td>
  <td>{html.escape(str(item['local_evidence']))}<ul>{links}</ul></td>
</tr>
"""
        )
    body = f"""
<h1>Completion Audit</h1>
<p>This page maps the requested end-to-end package to concrete local evidence. It also separates the local build state from the external GitHub remote state.</p>
<h2>Current Local Counts</h2>
<ul>
  <li>Videos: {html.escape(str(summary['video_count']))}</li>
  <li>Available transcripts: {html.escape(str(summary['available_transcripts']))}</li>
  <li>Concepts: {html.escape(str(summary['concept_count']))}</li>
  <li>Generated concept evidence packets: {html.escape(str(summary['concept_evidence_packet_count']))}</li>
  <li>Worked examples: {html.escape(str(summary['worked_example_count']))}</li>
  <li>Total audit requirements: {html.escape(str(summary['completion_requirement_count']))}</li>
</ul>
<h2>Requirement Evidence</h2>
<table>
  <thead>
    <tr>
      <th>Requirement</th>
      <th>Status</th>
      <th>Evidence</th>
    </tr>
  </thead>
  <tbody>{''.join(rows)}</tbody>
</table>
<h2>How To Read This</h2>
<p>Locally verified means the generated files and validation commands prove the item inside this workspace. External blocker means the local files are ready, but a condition outside the workspace still has to change.</p>
"""
    path.write_text(html_page("Physics-Informed ML Completion Audit", body), encoding="utf-8")


def write_family_page(path: Path, family: dict[str, object]) -> None:
    steps = "".join(f"<div class=\"route-step\">{idx}. {html.escape(step)}</div>" for idx, step in enumerate(family["plain_route"], start=1))
    body = f"""
<h1>{html.escape(str(family['title']))}</h1>
<h2>Problem This Family Solves</h2>
<p>{html.escape(str(family['central_problem']))}</p>
<h2>Where It Shows Up</h2>
<p>{html.escape(str(family['domain']))}</p>
<h2>Route Through The Ideas</h2>
<div class="route">{steps}</div>
<h2>Concepts In This Family</h2>
{concept_links(list(family['concepts']), root_prefix="../")}
<h2>What The Math Buys</h2>
<p>{html.escape(str(family['what_the_math_buys']))}</p>
<h2>Failure Boundary</h2>
<p>{html.escape(str(family['failure_boundary']))}</p>
<h2>Reader Check</h2>
<p>You understand this family when you can say the scientific job, the input family, the output quantity, the rule or structure being kept, and the changed case that would make the claim fail.</p>
"""
    path.write_text(html_page(str(family["title"]), body, root_prefix="../"), encoding="utf-8")


def write_comparison_page(path: Path, comparison: dict[str, object]) -> None:
    decision_essay = comparison_decision_essay_html(comparison)
    body = f"""
<h1>{html.escape(str(comparison['title']))}</h1>
<h2>Shared Problem</h2>
<p>{html.escape(str(comparison['shared_problem']))}</p>
<div class="compare-grid">
  <article class="card">
    <h3>{html.escape(str(comparison['left']))}</h3>
    <p>{html.escape(str(comparison['left_when']))}</p>
  </article>
  <article class="card">
    <h3>{html.escape(str(comparison['right']))}</h3>
    <p>{html.escape(str(comparison['right_when']))}</p>
  </article>
</div>
<h2>Key Difference</h2>
<p>{html.escape(str(comparison['key_difference']))}</p>
{decision_essay}
<h2>Concrete Choice Cases</h2>
<table>
  <tbody>
    <tr><th>Use {html.escape(str(comparison['left']))}</th><td>{html.escape(str(comparison['left_case']))}</td></tr>
    <tr><th>Use {html.escape(str(comparison['right']))}</th><td>{html.escape(str(comparison['right_case']))}</td></tr>
    <tr><th>Wrong Choice Case</th><td>{html.escape(str(comparison['wrong_choice_case']))}</td></tr>
    <tr><th>Evidence That Exposes It</th><td>{html.escape(str(comparison['evidence_that_exposes_it']))}</td></tr>
  </tbody>
</table>
<h2>Common Wrong Turn</h2>
<p>{html.escape(str(comparison['wrong_turn']))}</p>
<h2>First-Principles Test</h2>
<p>Before choosing a side, name the scientific quantity, the available evidence, the use range, and the changed case that would expose a bad answer.</p>
"""
    path.write_text(html_page(str(comparison["title"]), body, root_prefix="../"), encoding="utf-8")


def comparison_decision_essay_html(comparison: dict[str, object]) -> str:
    return f"""
<h2>How To Decide From First Principles</h2>
<p>Do not start by asking which side sounds more advanced. Start by asking what shortage creates the problem. The shared problem is: {html.escape(str(comparison['shared_problem']))} The two sides are different because they carry different evidence and fail in different places.</p>
<p>Use {html.escape(str(comparison['left']))} when this is the situation: {html.escape(str(comparison['left_when']))} In plain terms, this side is chosen when its evidence matches the job and its failure boundary can be tested. The concrete version is: {html.escape(str(comparison['left_case']))}</p>
<p>Use {html.escape(str(comparison['right']))} when this is the situation: {html.escape(str(comparison['right_when']))} In plain terms, this side is chosen when the scientific task asks for the kind of shortcut, rule, or evidence this side actually provides. The concrete version is: {html.escape(str(comparison['right_case']))}</p>
<p>The dangerous middle is the wrong-choice case: {html.escape(str(comparison['wrong_choice_case']))} This is where a shallow writeup usually fails. It names a method but does not name the quantity, use range, or changed case. The evidence that exposes the mistake is: {html.escape(str(comparison['evidence_that_exposes_it']))}</p>
<h3>Decision Checklist</h3>
<ol>
  <li>Name the real quantity the scientist will use.</li>
  <li>Name the evidence each side is allowed to use.</li>
  <li>Name the repeated use case, single case, or changed case.</li>
  <li>Name the first failure that would make the choice wrong.</li>
  <li>Choose the side whose burden matches the job, not the side with the more impressive label.</li>
</ol>
"""


def write_worked_example_page(path: Path, example: dict[str, object]) -> None:
    steps = "".join(f"<div class=\"route-step\">{idx}. {html.escape(step)}</div>" for idx, step in enumerate(example["plain_steps"], start=1))
    flow_nodes = [
        f"Observed: {example['observed']}",
        f"Hidden: {example['hidden']}",
        f"Route: {' -> '.join(str(slug).replace('-', ' ') for slug in example['method_route'])}",
        "Claim: answer only for the named scientific job",
        "Reject: changed case breaks the needed quantity",
    ]
    flow = "".join(f"<div class=\"flow-node\">{idx}. {html.escape(str(node))}</div>" for idx, node in enumerate(flow_nodes, start=1))
    first_principles_story = worked_example_story_html(example)
    body = f"""
<h1>{html.escape(str(example['title']))}</h1>
<h2>Scientific Job</h2>
<p><strong>Domain:</strong> {html.escape(str(example['domain']))}</p>
<p><strong>Question:</strong> {html.escape(str(example['question']))}</p>
{first_principles_story}
<h2>End-To-End Flow</h2>
<div class="flow">{flow}</div>
<h2>Observed And Hidden</h2>
<p><strong>Observed:</strong> {html.escape(str(example['observed']))}</p>
<p><strong>Hidden:</strong> {html.escape(str(example['hidden']))}</p>
<h2>Method Route</h2>
{concept_links(list(example['method_route']), root_prefix="../")}
<h2>Plain Steps</h2>
<div class="route">{steps}</div>
<h2>Why This Example Teaches The Field</h2>
<p>{html.escape(str(example['why_it_teaches']))}</p>
<h2>Claim Boundary</h2>
<p>The example supports a method only inside the named scientific job. A wider claim needs a new test, not stronger wording.</p>
"""
    path.write_text(html_page(str(example["title"]), body, root_prefix="../"), encoding="utf-8")


def worked_example_story_html(example: dict[str, object]) -> str:
    return f"""
<h2>First-Principles Story</h2>
<p>Start with the decision a person is trying to make. The question is: {html.escape(str(example['question']))} The observed evidence is {html.escape(str(example['observed']))}. That evidence is useful, but it is not the whole answer. The hidden part is {html.escape(str(example['hidden']))}.</p>
<p>The method route is not a list of names. It is the ordered bridge from evidence to hidden quantity: {html.escape(' -> '.join(str(slug).replace('-', ' ') for slug in example['method_route']))}. Each step has to earn its place. If a step does not add a rule, a structure, a cheaper calculation, or a trust check that the job needs, it should not be in the route.</p>
<p>This example teaches the field for a concrete reason: {html.escape(str(example['why_it_teaches']))} A reader should be able to retell it as a plain chain: what is known, what is missing, what mathematical object carries the missing part, what decision uses the answer, and what changed case would reject the claim.</p>
"""


def write_markdown_export(data: dict[str, object]) -> None:
    lines = ["# Physics-Informed Machine Learning Concepts Research", ""]
    lines.append("## Summary")
    for key, value in data["summary"].items():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Concepts"])
    for concept in data["concept_atlas"]:
        lines.extend(
            [
                f"### {concept['name']}",
                f"- Problem: {concept['problem']}",
                f"- Domain: {concept['domain']}",
                f"- Why: {concept['why']}",
                f"- Failure: {concept['failure']}",
                "",
            ]
        )
    lines.extend(["", "## Paper Family Routes"])
    for family in data["family_pages"]:
        lines.extend(
            [
                f"### {family['title']}",
                f"- Problem: {family['central_problem']}",
                f"- Domain: {family['domain']}",
                f"- What the math buys: {family['what_the_math_buys']}",
                f"- Failure boundary: {family['failure_boundary']}",
                "",
            ]
        )
    lines.extend(["", "## Comparisons"])
    for comparison in data["comparison_pages"]:
        lines.extend(
            [
                f"### {comparison['title']}",
                f"- Shared problem: {comparison['shared_problem']}",
                f"- Key difference: {comparison['key_difference']}",
                f"- Left case: {comparison['left_case']}",
                f"- Right case: {comparison['right_case']}",
                f"- Wrong choice case: {comparison['wrong_choice_case']}",
                f"- Evidence that exposes it: {comparison['evidence_that_exposes_it']}",
                f"- Wrong turn: {comparison['wrong_turn']}",
                "",
            ]
        )
    lines.extend(["", "## Worked Examples"])
    for example in data["worked_examples"]:
        lines.extend(
            [
                f"### {example['title']}",
                f"- Domain: {example['domain']}",
                f"- Question: {example['question']}",
                f"- Observed: {example['observed']}",
                f"- Hidden: {example['hidden']}",
                "",
            ]
        )
    lines.extend(["", "## Core Topic Deep Dives"])
    for slug, deep in data["topic_deep_dives"].items():
        lines.extend(
            [
                f"### {slug.replace('-', ' ').title()}",
                f"- One sentence: {deep['one_sentence']}",
                f"- Use when: {deep['use_when']}",
                f"- Do not use when: {deep['do_not_use_when']}",
                f"- Plain formula: {deep['plain_formula']}",
                f"- Why it matters: {deep['important_because']}",
                "",
            ]
        )
    lines.extend(["", "## Core Derivations"])
    for item in data["core_derivations"]:
        lines.extend(
            [
                f"### {item['title']}",
                f"- Problem: {item['common_problem']}",
                f"- Observed: {item['observed']}",
                f"- Hidden: {item['hidden']}",
                f"- Plain formula: {item['plain_formula']}",
                f"- Failure test: {item['failure_test']}",
                f"- Page: {item['derivation_href']}",
                "",
            ]
        )
        hand = item.get("hand_derivation")
        if isinstance(hand, dict):
            lines.extend([f"#### Hand Derivation For {item['title']}", f"- Start: {hand['plain_start']}"])
            for step in hand["line_steps"]:
                lines.append(f"- {step['term']}: {step['why_it_enters']} Check: {step['check']}")
            lines.extend([f"- Final line: {hand['final_line']}", ""])
    lines.extend(["", "## Plain Formula Guide"])
    for row in data["formula_guide"]:
        lines.extend(
            [
                f"### {row['title']}",
                f"- Formula shape: {row['plain_formula']}",
                f"- Parts: {', '.join(row['parts'])}",
                f"- Everyday reading: {row['everyday_reading']}",
                f"- What to check: {row['what_to_check']}",
                "",
            ]
        )
    lines.extend(["", "## Misconception Map"])
    for row in data["misconception_map"]:
        lines.extend(
            [
                f"### {row['title']}",
                f"- Correction: {row['plain_correction']}",
                f"- First-principles test: {row['first_principles_test']}",
                f"- Wrong turns: {'; '.join(row['wrong_turns'])}",
                "",
            ]
        )
    lines.extend(["", "## Diagrams"])
    for diagram in data["diagrams"]:
        lines.extend(
            [
                f"### {diagram['title']}",
                f"- Purpose: {diagram['purpose']}",
                f"- Flow: {' -> '.join(diagram['nodes'])}",
                f"- Watch for: {diagram['watch_for']}",
                "",
            ]
        )
    lines.extend(["", "## Mathematical Sketches"])
    for sketch in data["concept_sketches"]:
        lines.extend(
            [
                f"### {sketch['title']}",
                f"- Input: {sketch['input']}",
                f"- Output: {sketch['output']}",
                f"- Kept rule: {sketch['kept_rule']}",
                f"- Failure case: {sketch['failure_case']}",
                f"- Caption: {sketch['caption']}",
                "",
            ]
        )
    lines.extend(["", "## Learning Path"])
    for idx, step in enumerate(data["learning_path"], start=1):
        lines.extend(
            [
                f"### {idx}. {step['title']}",
                f"- Question: {step['question']}",
                f"- Why here: {step['why_first']}",
                f"- Goal: {step['plain_goal']}",
                f"- First-principles spine: {'; '.join(step['first_principles_spine'])}",
                f"- Checkpoint: {step['checkpoint']}",
                "",
            ]
        )
    lines.extend(["", "## Plain-Language Glossary"])
    for entry in data["glossary"]:
        lines.extend(
            [
                f"### {entry['term']}",
                f"- Everyday meaning: {entry['everyday']}",
                f"- Problem it names: {entry['problem']}",
                f"- Why it matters: {entry['why_it_matters']}",
                f"- Watch for: {entry['watch_for']}",
                "",
            ]
        )
    lines.extend(["", "## Domain Guides"])
    for guide in data["domain_guides"]:
        job = guide["domain_job"]
        lines.extend(
            [
                f"### {guide['title']}",
                f"- Real quantity: {guide['real_quantity']}",
                f"- Why hard: {guide['why_hard']}",
                f"- Common question: {guide['common_question']}",
                f"- Scientific job: {job['scientific_job']}",
                f"- Observed evidence: {job['observed_evidence']}",
                f"- Hidden quantity: {job['hidden_quantity']}",
                f"- Decision: {job['decision']}",
                f"- Changed-case test: {job['changed_case_test']}",
                f"- Failure test: {guide['failure_test']}",
                "",
            ]
        )
    lines.extend(["", "## Reader Checks"])
    for check in data["reader_checks"]:
        lines.extend(
            [
                f"### {check['title']}",
                f"- Setup: {check['setup']}",
                f"- Strong answer: {check['strong_answer']}",
                f"- Weak answer warning: {check['weak_answer_warning']}",
                "",
            ]
        )
    lines.extend(["", "## Decision Guide"])
    for decision in data["decision_guides"]:
        lines.extend(
            [
                f"### {decision['title']}",
                f"- Situation: {decision['situation']}",
                f"- Start with: {decision['best_start']}",
                f"- Why: {decision['why']}",
                f"- Evidence needed: {decision['evidence_needed']}",
                "",
            ]
        )
    lines.extend(["", "## Provenance And Reproduction"])
    for guide in data["provenance_guides"]:
        lines.extend(
            [
                f"### {guide['title']}",
                f"- Purpose: {guide['purpose']}",
                f"- Local files: {', '.join(guide['local_files'])}",
                f"- Checks: {', '.join(guide['checks'])}",
                "",
            ]
        )
    lines.extend(["", "## Coverage Matrix"])
    for row in data["coverage_matrix"]:
        lines.extend(
            [
                f"### {row['name']}",
                f"- Videos: {row['video_count']}",
                f"- Deep dive: {mark(row['deep_dive'])}",
                f"- Diagram: {mark(row['diagram'])}",
                f"- Reader check: {mark(row['reader_check'])}",
                f"- Evidence items: {row['evidence_items']}",
                "",
            ]
        )
    lines.extend(["", "## Concept Dependency Map"])
    for row in data["dependency_map"]:
        lines.extend(
            [
                f"### {row['concept_name']}",
                f"- Learn first: {', '.join(item['name'] for item in row['depends_on'])}",
                f"- Why: {row['why']}",
                f"- Confusion prevented: {row['confusion_prevented']}",
                "",
            ]
        )
    lines.extend(["", "## Concept Ladder"])
    for row in data["concept_ladder"]:
        lines.extend(
            [
                f"### {row['title']}",
                f"- Problem: {row['common_problem']}",
                f"- Observed: {row['observed']}",
                f"- Hidden: {row['hidden']}",
                f"- Mathematical move: {row['mathematical_move']}",
                f"- Shape: {row['shape']}",
                f"- Failure test: {row['failure_test']}",
                "",
            ]
        )
    lines.extend(["", "## Concept Evidence Packets"])
    for packet in data["concept_evidence_packets"]:
        lines.extend(
            [
                f"### {packet['title']}",
                f"- Problem: {packet['common_problem']}",
                f"- Domain: {packet['domain']}",
                f"- Evidence anchors: {packet['evidence_count']}",
                f"- Packet: {packet['packet_href']}",
                "",
            ]
        )
    lines.extend(["", "## Selected Source Anchors"])
    for slug, anchors in data["source_anchors"].items():
        lines.extend(["", f"### {slug.replace('-', ' ').title()}"])
        for item in anchors:
            lines.extend(
                [
                    f"- Source: {item['source']}",
                    f"- Page: {item['href']}",
                    f"- Claim anchored: {item['claim']}",
                    f"- Why this source: {item['why_this_source']}",
                    f"- Limit: {item['limit']}",
                    "",
                ]
            )
    lines.extend(["", "## Editorial Quality Rubric"])
    for item in data["quality_rubric"]:
        lines.extend(
            [
                f"### {item['title']}",
                f"- Standard: {item['standard']}",
                f"- Strong page: {item['strong_page']}",
                f"- Weak page: {item['weak_page']}",
                f"- Check: {item['check']}",
                "",
            ]
        )
    lines.extend(["", "## Field Synthesis"])
    for item in data["synthesis_guides"]:
        lines.extend(
            [
                f"### {item['title']}",
                f"- Claim: {item['claim']}",
                f"- Explanation: {item['explanation']}",
                f"- Reader takeaway: {item['reader_takeaway']}",
                "",
            ]
        )
    handoff = data["review_handoff"]
    lines.extend(["", "## Review Handoff", f"- Purpose: {handoff['purpose']}", ""])
    lines.append("### Start Here")
    for item in handoff["start_here"]:
        lines.append(f"- {item['label']}: {item['href']}")
    lines.extend(["", "### Remaining Editorial Work"])
    for item in handoff["remaining_editorial_work"]:
        lines.append(f"- {item}")
    lines.extend(["", "### Remote Verification Commands", f"- Status: {handoff['remote_status']}"])
    for command in handoff["remote_finish_commands"]:
        lines.append(f"- `{command}`")
    lines.extend(["", "## Review Entrypoints"])
    for group in data["review_entrypoints"]:
        lines.extend(["", f"### {group['group']}", f"- Purpose: {group['purpose']}"])
        for item in group["items"]:
            lines.append(f"- {item['label']}: {item['href']} | {item['question']}")
    lines.extend(["", "## Find Pages By Question"])
    for row in data["review_search_index"]:
        lines.extend(["", f"### {row['intent']}", f"- Look for: {row['look_for']}"])
        for item in row["pages"]:
            lines.append(f"- {item['label']}: {item['href']}")
    goal = data["meaty_goal"]
    lines.extend(
        [
            "",
            "## Meaty End-To-End Goal",
            f"- Goal: {goal['short_goal']}",
            f"- Target reader: {goal['target_reader']}",
            f"- Acceptance sentence: {goal['acceptance_sentence']}",
            "",
            "### Done Means",
        ]
    )
    for item in goal["done_means"]:
        lines.append(f"- {item}")
    lines.extend(["", "### Every Core Page Must Contain"])
    for item in goal["page_requirements"]:
        lines.append(f"- {item}")
    lines.extend(["", "### Not Done If"])
    for item in goal["not_done_if"]:
        lines.append(f"- {item}")
    lines.extend(["", "## Editorial Roadmap"])
    for item in data["editorial_roadmap"]:
        lines.extend(
            [
                f"### {item['priority']} {item['title']}",
                f"- Status: {item.get('status', 'not started')}",
                f"- Goal: {item['goal']}",
                f"- Why it matters: {item['why']}",
                f"- Current evidence: {item.get('evidence', 'No local evidence recorded yet.')}",
                f"- Proof pages: {', '.join(item.get('proof_pages', []))}",
                f"- Target pages: {', '.join(row['href'] for row in item['target_pages'])}",
                f"- Work: {'; '.join(item['work'])}",
                f"- Acceptance check: {item['acceptance_check']}",
                "",
            ]
        )
    lines.extend(["", "## Completion Audit"])
    for item in data["completion_requirements"]:
        lines.extend(
            [
                f"### {item['requirement']}",
                f"- Status: {item['status']}",
                f"- Evidence: {item['local_evidence']}",
                "",
            ]
        )
    (EXPORTS / "research-package.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def validate(data: dict[str, object] | None = None) -> None:
    if data is None:
        records_path = ANALYSIS / "transcript_index.json"
        concepts_path = ANALYSIS / "concept_atlas.json"
        themes_path = ANALYSIS / "theme_map.json"
        evidence_path = ANALYSIS / "evidence_ledger.json"
        for path in (records_path, concepts_path, themes_path, evidence_path):
            if not path.exists():
                raise SystemExit(f"missing analysis file: {path}")
        data = {
            "transcript_index": json.loads(records_path.read_text(encoding="utf-8")),
            "concept_atlas": json.loads(concepts_path.read_text(encoding="utf-8")),
            "theme_map": json.loads(themes_path.read_text(encoding="utf-8")),
            "evidence_ledger": json.loads(evidence_path.read_text(encoding="utf-8")),
        }

    records = data["transcript_index"]
    if len(records) != 40:
        raise SystemExit(f"expected 40 playlist records, found {len(records)}")
    for record in records:
        if record.get("transcript_status") not in {"available", "missing"}:
            raise SystemExit(f"bad transcript status: {record.get('title')}")
        if record.get("transcript_status") == "available" and not record.get("clean_txt"):
            raise SystemExit(f"available transcript missing clean path: {record.get('title')}")
        if not record.get("concepts"):
            raise SystemExit(f"record missing concepts: {record.get('title')}")
    required_fields = ("problem", "domain", "why", "keeps", "leaves_out", "failure", "evidence")
    concept_slugs = set()
    for concept in data["concept_atlas"]:
        concept_slugs.add(str(concept.get("slug")))
        for field in required_fields:
            if not concept.get(field):
                raise SystemExit(f"concept missing {field}: {concept.get('name')}")
    for slug in TOPIC_DEEP_DIVES:
        if slug not in concept_slugs:
            raise SystemExit(f"deep dive references missing concept: {slug}")
        topic_path = SITE / "topics" / f"{slug}.html"
        if not topic_path.exists():
            raise SystemExit(f"deep dive missing topic page: {slug}")
        topic_text = topic_path.read_text(encoding="utf-8")
        if "First-Principles Essay" not in topic_text or "What A Strong Explanation Must Say" not in topic_text or "Concrete Worked Example" not in topic_text or "Concrete Wrong-Use Example" not in topic_text or "Test That Catches It" not in topic_text or "Core Idea In One Sentence" not in topic_text or "Mathematical Shape Without Jargon" not in topic_text:
            raise SystemExit(f"deep dive not rendered on topic page: {slug}")
    worked_example_slugs = {str(slug) for example in WORKED_EXAMPLES for slug in example["method_route"]}
    concepts_without_examples = sorted(concept_slugs - worked_example_slugs)
    if concepts_without_examples:
        raise SystemExit(f"concepts missing worked example route: {concepts_without_examples}")
    for path in (
        SITE / "index.html",
        SITE / "transcripts.html",
        SITE / "concept-atlas.html",
        SITE / "families.html",
        SITE / "comparisons.html",
        SITE / "worked-examples.html",
        SITE / "diagrams.html",
        SITE / "derivations.html",
        SITE / "formula-guide.html",
        SITE / "misconceptions.html",
        SITE / "learning-path.html",
        SITE / "glossary.html",
        SITE / "domains.html",
        SITE / "reader-checks.html",
        SITE / "decision-guide.html",
        SITE / "provenance.html",
        SITE / "coverage.html",
        SITE / "dependencies.html",
        SITE / "concept-ladder.html",
        SITE / "evidence-packets.html",
        SITE / "quality.html",
        SITE / "synthesis.html",
        SITE / "review-entrypoints.html",
        SITE / "review-search.html",
        SITE / "editorial-roadmap.html",
        SITE / "completion-audit.html",
        SITE / "meaty-goal.html",
        SITE / "handoff.html",
        SITE / "theme-map.html",
        SITE / "evidence-ledger.html",
    ):
        if not path.exists():
            raise SystemExit(f"missing site page: {path}")
    for family in FAMILY_PAGES:
        if not (SITE / "families" / f"{family['slug']}.html").exists():
            raise SystemExit(f"missing family page: {family['title']}")
    for comparison in COMPARISON_PAGES:
        comparison_path = SITE / "comparisons" / f"{comparison['slug']}.html"
        if not comparison_path.exists():
            raise SystemExit(f"missing comparison page: {comparison['title']}")
        comparison_text = comparison_path.read_text(encoding="utf-8")
        if "How To Decide From First Principles" not in comparison_text or "Decision Checklist" not in comparison_text or "Concrete Choice Cases" not in comparison_text or "Wrong Choice Case" not in comparison_text or "Evidence That Exposes It" not in comparison_text:
            raise SystemExit(f"comparison page missing concrete cases: {comparison['title']}")
        for field in ("left_case", "right_case", "wrong_choice_case", "evidence_that_exposes_it"):
            if not comparison.get(field):
                raise SystemExit(f"comparison missing {field}: {comparison['title']}")
    for example in WORKED_EXAMPLES:
        example_path = SITE / "worked-examples" / f"{example['slug']}.html"
        if not example_path.exists():
            raise SystemExit(f"missing worked example page: {example['title']}")
        example_text = example_path.read_text(encoding="utf-8")
        if "First-Principles Story" not in example_text or "End-To-End Flow" not in example_text or "flow-node" not in example_text or "Claim Boundary" not in example_text:
            raise SystemExit(f"worked example not rendered correctly: {example['title']}")
        for slug in example["method_route"]:
            if not (SITE / "topics" / f"{slug}.html").exists():
                raise SystemExit(f"worked example method route missing topic: {example['title']} -> {slug}")
    required_examples = {
        "heat-equation-from-few-measurements",
        "fast-fluid-field-surrogate",
        "discovering-a-small-law-from-motion",
        "molecule-property-from-structure",
        "material-stress-from-sparse-tests",
        "mesh-field-on-irregular-geometry",
        "foundation-pde-model-on-new-equation",
        "climate-risk-under-shifted-conditions",
    }
    example_slugs = {str(example["slug"]) for example in WORKED_EXAMPLES}
    missing_examples = sorted(required_examples - example_slugs)
    if missing_examples:
        raise SystemExit(f"missing required worked examples: {missing_examples}")
    for diagram in DIAGRAMS:
        diagram_path = SITE / "diagrams" / f"{diagram['slug']}.html"
        if not diagram_path.exists():
            raise SystemExit(f"missing diagram page: {diagram['title']}")
        diagram_text = diagram_path.read_text(encoding="utf-8")
        if "flow-node" not in diagram_text or "Watch for:" not in diagram_text:
            raise SystemExit(f"diagram not rendered correctly: {diagram['title']}")
    sketch_index_text = (SITE / "diagrams.html").read_text(encoding="utf-8")
    if "Mathematical Sketches" not in sketch_index_text or "Kept Rule" not in sketch_index_text or "Failure Case" not in sketch_index_text:
        raise SystemExit("mathematical sketches not rendered on diagram index")
    if len(data.get("concept_sketches") or []) != len(CONCEPT_SKETCHES):
        raise SystemExit("concept sketch count mismatch")
    sketch_required_slugs = {"physics-informed-neural-networks", "operator-learning", "surrogate-modeling", "uncertainty-and-generalization", "foundation-models-for-pdes"}
    sketched_slugs = {str(slug) for sketch in CONCEPT_SKETCHES for slug in sketch["topic_slugs"]}
    missing_sketches = sorted(sketch_required_slugs - sketched_slugs)
    if missing_sketches:
        raise SystemExit(f"core concepts missing sketches: {missing_sketches}")
    for sketch in CONCEPT_SKETCHES:
        for field in ("input", "output", "kept_rule", "failure_case", "caption"):
            if not sketch.get(field):
                raise SystemExit(f"concept sketch missing {field}: {sketch['title']}")
        for slug in sketch["topic_slugs"]:
            topic_path = SITE / "topics" / f"{slug}.html"
            if topic_path.exists():
                topic_text = topic_path.read_text(encoding="utf-8")
                if str(sketch["title"]) not in topic_text or "Kept Rule" not in topic_text:
                    raise SystemExit(f"concept sketch not rendered on topic: {slug} -> {sketch['title']}")
    derivation_index = SITE / "derivations.html"
    derivation_index_text = derivation_index.read_text(encoding="utf-8")
    if "Core Derivations" not in derivation_index_text:
        raise SystemExit("derivation index not rendered correctly")
    derivation_rows = data.get("core_derivations") or []
    if len(derivation_rows) != len(TOPIC_DEEP_DIVES):
        raise SystemExit("core derivation count does not match deep dives")
    hand_required_slugs = {"physics-informed-neural-networks", "operator-learning", "foundation-models-for-pdes"}
    for item in derivation_rows:
        derivation_path = SITE / str(item["derivation_href"])
        if not derivation_path.exists():
            raise SystemExit(f"missing derivation page: {item['title']}")
        derivation_text = derivation_path.read_text(encoding="utf-8")
        for required in ("Start With What Is Observed", "Build The Mathematical Shape", "Failure Test", "Red Flags"):
            if required not in derivation_text:
                raise SystemExit(f"derivation page missing {required}: {item['title']}")
        if item["slug"] in hand_required_slugs:
            hand = item.get("hand_derivation")
            if not isinstance(hand, dict) or len(hand.get("line_steps") or []) < 3:
                raise SystemExit(f"core derivation missing hand derivation: {item['title']}")
            for required in ("Hand Derivation", "Why It Enters", "Final Line"):
                if required not in derivation_text:
                    raise SystemExit(f"hand derivation page missing {required}: {item['title']}")
        topic_path = SITE / str(item["topic_href"])
        if not topic_path.exists():
            raise SystemExit(f"derivation topic link missing: {item['topic_href']}")
        if str(item["derivation_href"]) not in topic_path.read_text(encoding="utf-8"):
            raise SystemExit(f"topic missing derivation link: {item['topic_href']}")
    formula_path = SITE / "formula-guide.html"
    formula_text = formula_path.read_text(encoding="utf-8")
    if "Plain Formula Guide" not in formula_text or "Common Misread" not in formula_text:
        raise SystemExit("formula guide not rendered correctly")
    formula_rows = data.get("formula_guide") or []
    if len(formula_rows) != len(derivation_rows):
        raise SystemExit("formula guide count does not match derivations")
    for row in formula_rows:
        if not row.get("parts") or not row.get("plain_formula"):
            raise SystemExit(f"formula guide row incomplete: {row.get('title')}")
        for href_field in ("topic_href", "derivation_href"):
            if not (SITE / str(row[href_field])).exists():
                raise SystemExit(f"formula guide link missing: {row[href_field]}")
    misconception_path = SITE / "misconceptions.html"
    misconception_text = misconception_path.read_text(encoding="utf-8")
    if "Misconception Map" not in misconception_text or "First-Principles Test" not in misconception_text:
        raise SystemExit("misconception map not rendered correctly")
    misconception_rows = data.get("misconception_map") or []
    if len(misconception_rows) != len(derivation_rows):
        raise SystemExit("misconception map count does not match derivations")
    for row in misconception_rows:
        if not row.get("wrong_turns") or not row.get("plain_correction"):
            raise SystemExit(f"misconception row incomplete: {row.get('title')}")
        for href_field in ("topic_href", "derivation_href"):
            if not (SITE / str(row[href_field])).exists():
                raise SystemExit(f"misconception link missing: {row[href_field]}")
        if row.get("reader_check_href") and not (SITE / str(row["reader_check_href"])).exists():
            raise SystemExit(f"misconception reader check link missing: {row['reader_check_href']}")
    for step in LEARNING_PATH:
        step_path = SITE / "learning-path" / f"{step['slug']}.html"
        if not step_path.exists():
            raise SystemExit(f"missing learning path page: {step['title']}")
        step_text = step_path.read_text(encoding="utf-8")
        if "No-Jargon Explanation" not in step_text or "Checkpoint" not in step_text or "Read Next" not in step_text or "First-Principles Spine" not in step_text:
            raise SystemExit(f"learning path page not rendered correctly: {step['title']}")
        if len(step.get("first_principles_spine") or []) != 5:
            raise SystemExit(f"learning path spine should have five parts: {step['title']}")
        for item in step["read"]:
            target = SITE / str(item["href"])
            if not target.exists():
                raise SystemExit(f"learning path link missing: {step['title']} -> {item['href']}")
    for entry in GLOSSARY:
        entry_path = SITE / "glossary" / f"{entry['slug']}.html"
        if not entry_path.exists():
            raise SystemExit(f"missing glossary page: {entry['term']}")
        entry_text = entry_path.read_text(encoding="utf-8")
        if "Everyday Meaning" not in entry_text or "What To Watch For" not in entry_text:
            raise SystemExit(f"glossary page not rendered correctly: {entry['term']}")
        for slug in entry["related"]:
            target = SITE / "topics" / f"{slug}.html"
            if not target.exists():
                raise SystemExit(f"glossary related concept missing: {entry['term']} -> {slug}")
    for guide in DOMAIN_GUIDES:
        guide_path = SITE / "domains" / f"{guide['slug']}.html"
        if not guide_path.exists():
            raise SystemExit(f"missing domain guide page: {guide['title']}")
        guide_text = guide_path.read_text(encoding="utf-8")
        if "Walk The Domain From Scratch" not in guide_text or "How The Methods Enter Without Jargon" not in guide_text or "Real Quantity" not in guide_text or "Failure Test" not in guide_text or "Concrete Scientific Job" not in guide_text:
            raise SystemExit(f"domain guide not rendered correctly: {guide['title']}")
        job = guide.get("domain_job") or {}
        for field in ("scientific_job", "observed_evidence", "hidden_quantity", "decision", "changed_case_test"):
            if not job.get(field):
                raise SystemExit(f"domain guide missing job field {field}: {guide['title']}")
        for label in ("Observed Evidence", "Hidden Quantity", "Decision", "Changed-Case Test"):
            if label not in guide_text:
                raise SystemExit(f"domain guide missing job label {label}: {guide['title']}")
        for slug in guide["concepts"]:
            target = SITE / "topics" / f"{slug}.html"
            if not target.exists():
                raise SystemExit(f"domain concept missing: {guide['title']} -> {slug}")
        if not (SITE / str(guide["example"])).exists():
            raise SystemExit(f"domain anchor missing: {guide['title']} -> {guide['example']}")
    for check in READER_CHECKS:
        check_path = SITE / "reader-checks" / f"{check['slug']}.html"
        if not check_path.exists():
            raise SystemExit(f"missing reader check page: {check['title']}")
        check_text = check_path.read_text(encoding="utf-8")
        if "Strong Answer Should Say" not in check_text or "Weak Answer Warning" not in check_text:
            raise SystemExit(f"reader check not rendered correctly: {check['title']}")
        topic_path = SITE / "topics" / f"{check['topic_slug']}.html"
        if not topic_path.exists():
            raise SystemExit(f"reader check topic missing: {check['title']} -> {check['topic_slug']}")
        topic_text = topic_path.read_text(encoding="utf-8")
        if str(check["title"]) not in topic_text:
            raise SystemExit(f"reader check not embedded in topic: {check['title']}")
        for href in check["related"]:
            if not (SITE / str(href)).exists():
                raise SystemExit(f"reader check related page missing: {check['title']} -> {href}")
    for decision in DECISION_GUIDES:
        decision_path = SITE / "decision-guide" / f"{decision['slug']}.html"
        if not decision_path.exists():
            raise SystemExit(f"missing decision guide page: {decision['title']}")
        decision_text = decision_path.read_text(encoding="utf-8")
        if "Best Starting Point" not in decision_text or "Evidence Needed" not in decision_text:
            raise SystemExit(f"decision guide not rendered correctly: {decision['title']}")
        for href in decision["links"]:
            if not (SITE / str(href)).exists():
                raise SystemExit(f"decision guide link missing: {decision['title']} -> {href}")
    for guide in PROVENANCE_GUIDES:
        guide_path = SITE / "provenance" / f"{guide['slug']}.html"
        if not guide_path.exists():
            raise SystemExit(f"missing provenance page: {guide['title']}")
        guide_text = guide_path.read_text(encoding="utf-8")
        if "Local Files" not in guide_text or "Checks" not in guide_text:
            raise SystemExit(f"provenance page not rendered correctly: {guide['title']}")
    coverage_path = SITE / "coverage.html"
    coverage_text = coverage_path.read_text(encoding="utf-8")
    if "Coverage Matrix" not in coverage_text or "Reader Check" not in coverage_text:
        raise SystemExit("coverage matrix not rendered correctly")
    coverage_rows = data.get("coverage_matrix") or []
    if len(coverage_rows) != len(data["concept_atlas"]):
        raise SystemExit("coverage matrix row count does not match concept atlas")
    dependency_path = SITE / "dependencies.html"
    dependency_text = dependency_path.read_text(encoding="utf-8")
    if "Concept Dependency Map" not in dependency_text or "Confusion It Prevents" not in dependency_text:
        raise SystemExit("dependency map not rendered correctly")
    dependency_rows = data.get("dependency_map") or []
    if len(dependency_rows) != len(CONCEPT_DEPENDENCIES):
        raise SystemExit("dependency map row count mismatch")
    for row in dependency_rows:
        if not (SITE / str(row["concept_href"])).exists():
            raise SystemExit(f"dependency concept link missing: {row['concept_href']}")
        for item in row["depends_on"]:
            if not (SITE / str(item["href"])).exists():
                raise SystemExit(f"dependency link missing: {item['href']}")
    ladder_path = SITE / "concept-ladder.html"
    ladder_text = ladder_path.read_text(encoding="utf-8")
    if "Concept Ladder" not in ladder_text or "Mathematical Move" not in ladder_text:
        raise SystemExit("concept ladder not rendered correctly")
    ladder_rows = data.get("concept_ladder") or []
    if len(ladder_rows) != len(data["concept_atlas"]):
        raise SystemExit("concept ladder row count does not match concept atlas")
    for row in ladder_rows:
        for field in ("observed", "hidden", "mathematical_move", "shape", "failure_test"):
            if not row.get(field):
                raise SystemExit(f"concept ladder missing {field}: {row.get('title')}")
        if not (SITE / str(row["topic_href"])).exists():
            raise SystemExit(f"concept ladder topic link missing: {row['topic_href']}")
    packet_index_path = SITE / "evidence-packets.html"
    packet_index_text = packet_index_path.read_text(encoding="utf-8")
    if "Concept Evidence Packets" not in packet_index_text:
        raise SystemExit("concept evidence packet index not rendered correctly")
    packets = data.get("concept_evidence_packets") or []
    if len(packets) != len(data["concept_atlas"]):
        raise SystemExit("concept evidence packet count does not match concept atlas")
    core_slugs = {"physics-informed-neural-networks", "operator-learning", "surrogate-modeling", "uncertainty-and-generalization", "symbolic-regression", "foundation-models-for-pdes"}
    for packet in packets:
        packet_path = SITE / str(packet["packet_href"])
        if not packet_path.exists():
            raise SystemExit(f"missing concept evidence packet: {packet['title']}")
        packet_text = packet_path.read_text(encoding="utf-8")
        for required in ("Transcript Support", "What This Evidence Does Not Prove", "Review Links"):
            if required not in packet_text:
                raise SystemExit(f"concept evidence packet missing {required}: {packet['title']}")
        if int(packet.get("evidence_count") or 0) <= 0:
            raise SystemExit(f"concept evidence packet has no evidence: {packet['title']}")
        for item in packet["review_links"]:
            if not (SITE / str(item["href"])).exists():
                raise SystemExit(f"concept evidence packet review link missing: {packet['title']} -> {item['href']}")
    source_anchors = data.get("source_anchors") or {}
    for slug in concept_slugs:
        topic_path = SITE / "topics" / f"{slug}.html"
        packet_path = SITE / "evidence-packets" / f"{slug}.html"
        for page_path in (topic_path, packet_path):
            page_text = page_path.read_text(encoding="utf-8")
            if "Selected Source Anchors" not in page_text or page_text.count("Claim Anchored") < 2:
                raise SystemExit(f"source anchors not rendered on page: {page_path}")
    for slug, anchors in source_anchors.items():
        for item in anchors:
            target = SITE / str(item["href"])
            if not target.exists():
                raise SystemExit(f"source anchor link missing: {slug} -> {item['href']}")
            for field in ("claim", "source", "why_this_source", "limit"):
                if not item.get(field):
                    raise SystemExit(f"source anchor missing {field}: {slug}")
    by_slug = {row["slug"]: row for row in coverage_rows}
    for slug in core_slugs:
        row = by_slug.get(slug)
        if not row:
            raise SystemExit(f"core concept missing coverage row: {slug}")
        for field in ("deep_dive", "diagram", "reader_check", "decision_guide"):
            if not row.get(field):
                raise SystemExit(f"core concept missing {field}: {slug}")
    for item in QUALITY_RUBRIC:
        item_path = SITE / "quality" / f"{item['slug']}.html"
        if not item_path.exists():
            raise SystemExit(f"missing quality rubric page: {item['title']}")
        item_text = item_path.read_text(encoding="utf-8")
        if "Strong Page" not in item_text or "Weak Page" not in item_text:
            raise SystemExit(f"quality rubric page not rendered correctly: {item['title']}")
    for item in SYNTHESIS_GUIDES:
        item_path = SITE / "synthesis" / f"{item['slug']}.html"
        if not item_path.exists():
            raise SystemExit(f"missing synthesis page: {item['title']}")
        item_text = item_path.read_text(encoding="utf-8")
        if "Reader Takeaway" not in item_text or "Follow The Links" not in item_text:
            raise SystemExit(f"synthesis page not rendered correctly: {item['title']}")
        for href in item["links"]:
            if not (SITE / str(href)).exists():
                raise SystemExit(f"synthesis link missing: {item['title']} -> {href}")
    goal_path = SITE / "meaty-goal.html"
    goal_text = goal_path.read_text(encoding="utf-8")
    if "Meaty End-To-End Goal" not in goal_text or "Done Means" not in goal_text or "Acceptance Sentence" not in goal_text or "Not Done If" not in goal_text:
        raise SystemExit("meaty goal page not rendered correctly")
    goal = data.get("meaty_goal") or {}
    if len(goal.get("done_means") or []) < 10:
        raise SystemExit("meaty goal needs at least ten done criteria")
    for item in goal.get("core_pages") or []:
        if not (SITE / str(item["href"])).exists():
            raise SystemExit(f"meaty goal core page link missing: {item['href']}")
    handoff_path = SITE / "handoff.html"
    handoff_text = handoff_path.read_text(encoding="utf-8")
    if "Start Here" not in handoff_text or "Remaining Editorial Work" not in handoff_text or "Remote Verification Commands" not in handoff_text:
        raise SystemExit("handoff page not rendered correctly")
    for command in REVIEW_HANDOFF["remote_finish_commands"]:
        if command not in handoff_text:
            raise SystemExit(f"handoff remote command missing: {command}")
    for group in ("start_here", "core_review_pages"):
        for item in REVIEW_HANDOFF[group]:
            if not (SITE / item["href"]).exists():
                raise SystemExit(f"handoff link missing: {item['href']}")
    review_entrypoints_path = SITE / "review-entrypoints.html"
    review_entrypoints_text = review_entrypoints_path.read_text(encoding="utf-8")
    if "Review Entrypoints" not in review_entrypoints_text or "End-To-End Test" not in review_entrypoints_text:
        raise SystemExit("review entrypoints page not rendered correctly")
    for group in REVIEW_ENTRYPOINTS:
        for item in group["items"]:
            if not (SITE / item["href"]).exists():
                raise SystemExit(f"review entrypoint link missing: {item['href']}")
    review_search_path = SITE / "review-search.html"
    review_search_text = review_search_path.read_text(encoding="utf-8")
    if "Find Pages By Question" not in review_search_text or "Review Rule" not in review_search_text:
        raise SystemExit("review search page not rendered correctly")
    review_search_rows = data.get("review_search_index") or []
    if len(review_search_rows) != len(REVIEW_SEARCH_INDEX):
        raise SystemExit("review search row count mismatch")
    for row in review_search_rows:
        for item in row["pages"]:
            if not (SITE / item["href"]).exists():
                raise SystemExit(f"review search link missing: {item['href']}")
    roadmap_path = SITE / "editorial-roadmap.html"
    roadmap_text = roadmap_path.read_text(encoding="utf-8")
    if "Editorial Roadmap" not in roadmap_text or "Acceptance Check" not in roadmap_text or "Meaty End-To-End Goal" not in roadmap_text:
        raise SystemExit("editorial roadmap page not rendered correctly")
    roadmap_rows = data.get("editorial_roadmap") or []
    if len(roadmap_rows) != len(EDITORIAL_ROADMAP):
        raise SystemExit("editorial roadmap row count mismatch")
    completed_rows = [row for row in roadmap_rows if row.get("status") == "locally completed"]
    if len(completed_rows) != data["summary"].get("editorial_roadmap_completed_count"):
        raise SystemExit("editorial roadmap completed count mismatch")
    for row in roadmap_rows:
        if not row.get("work") or not row.get("acceptance_check") or not row.get("status") or not row.get("evidence"):
            raise SystemExit(f"editorial roadmap row incomplete: {row.get('title')}")
        for item in row["target_pages"]:
            if not (SITE / str(item["href"])).exists():
                raise SystemExit(f"editorial roadmap link missing: {row['title']} -> {item['href']}")
        for href in row.get("proof_pages", []):
            if not (SITE / str(href)).exists() and not (ROOT / str(href)).exists():
                raise SystemExit(f"editorial roadmap proof link missing: {row['title']} -> {href}")
    audit_path = SITE / "completion-audit.html"
    audit_text = audit_path.read_text(encoding="utf-8")
    if "Completion Audit" not in audit_text or "Requirement Evidence" not in audit_text or "locally verified" not in audit_text:
        raise SystemExit("completion audit page not rendered correctly")
    requirements = data.get("completion_requirements") or []
    if len(requirements) != len(COMPLETION_REQUIREMENTS):
        raise SystemExit("completion requirement count mismatch")
    for item in requirements:
        for link in item["links"]:
            if not (SITE / str(link)).exists():
                raise SystemExit(f"completion audit link missing: {link}")
    manifest_path = SITE / "page-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    missing = [item for item in manifest if not (ROOT / item).exists()]
    if missing:
        raise SystemExit(f"manifest points to missing pages: {missing[:3]}")
    print(f"physics-informed ml package validation ok: {len(records)} videos, {len(data['concept_atlas'])} concepts, {len(manifest)} pages")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--download", action="store_true", help="Download playlist manifests, captions, and metadata with yt-dlp.")
    parser.add_argument("--build", action="store_true", help="Build analysis files and site pages.")
    parser.add_argument("--validate", action="store_true", help="Validate generated analysis and site files.")
    args = parser.parse_args()

    if args.download:
        for playlist in PLAYLISTS:
            download_playlist(playlist)
    data = None
    if args.build:
        records = load_records()
        data = build_analysis(records)
        write_site(data)
    if args.validate:
        validate(data)
    if not (args.download or args.build or args.validate):
        parser.print_help()


if __name__ == "__main__":
    main()
