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
        "method_route": ["partial-differential-equations", "physics-informed-neural-networks", "uncertainty-and-generalization"],
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


LEARNING_PATH = [
    {
        "slug": "scientific-question-first",
        "title": "Start With The Scientific Question",
        "question": "What is being predicted, explained, designed, or checked?",
        "why_first": "Physics-informed machine learning is not one trick. The method depends on the scientific job.",
        "plain_goal": "Name the quantity, the domain, the evidence, and the changed case before naming a method.",
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
        "methods": ["Keep geometry and connections visible.", "Compare against trusted simulations or measurements.", "Name the load, material range, and failure quantity."],
        "failure_test": "Change the geometry, mesh, defect, or load path and check the physical quantity used for decisions.",
        "example": "families/scientific-surrogates-family.html",
    },
    {
        "slug": "chemistry-and-biology",
        "title": "Chemistry And Biology",
        "real_quantity": "molecular property, reaction behavior, concentration, binding, or biological response",
        "why_hard": "the object may be a graph, a field, a time process, or a set of interacting parts",
        "common_question": "Can learned structure help predict scientific behavior while respecting the object being studied?",
        "concepts": ["graphs-and-geometric-learning", "generative-modeling", "symbolic-regression", "uncertainty-and-generalization"],
        "methods": ["Represent connections when interactions matter.", "Use generation only with scientific checks.", "Look for readable rules only when the measured variables support them."],
        "failure_test": "Test on a changed molecule, condition, experiment, or biological setting that was not close to training.",
        "example": "topics/graphs-and-geometric-learning.html",
    },
    {
        "slug": "many-pde-tasks",
        "title": "Many PDE Tasks",
        "real_quantity": "solution fields across many equations, grids, parameters, or boundary settings",
        "why_hard": "a model may look broad while only covering the cases it saw often",
        "common_question": "Can one trained model reuse structure across many related scientific tasks?",
        "concepts": ["foundation-models-for-pdes", "operator-learning", "attention-for-scientific-fields", "uncertainty-and-generalization"],
        "methods": ["Train across many tasks.", "Hold out whole task families.", "Compare against trusted solves on changed equations, boundaries, and scales."],
        "failure_test": "Withhold a full equation family, boundary type, or scale and check whether the model still earns the claim.",
        "example": "topics/foundation-models-for-pdes.html",
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
        ],
        "local_files": ["scripts/build_physics_informed_ml_research_package.py", "README.md", "Makefile"],
        "checks": ["repo has a clear topic name", "raw source material is preserved", "generated pages are validated", "commits are small enough to review"],
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
        "claim": "Physics-informed machine learning asks how data, equations, simulations, and scientific checks can work together without pretending any one of them is enough.",
        "explanation": "Data gives examples. Equations give rules. Simulations give trusted cases. Validation gives the right to use a model under a named condition. The field exists because scientific prediction often needs all four.",
        "reader_takeaway": "Do not ask first which model is popular. Ask what scientific quantity is needed, what evidence exists, and what changed case would reject the answer.",
        "links": ["learning-path.html", "decision-guide.html", "quality/first-principles.html"],
    },
    {
        "slug": "main-moves",
        "title": "Main Moves",
        "claim": "The recurring moves are fitting from data, constraining with physics, learning maps between fields, replacing expensive solves, estimating trust, and searching for readable rules.",
        "explanation": "PINNs use equations as checks. Neural operators learn field-to-field maps. Surrogates trade full cost for checked speed. Uncertainty asks when belief should weaken. Symbolic regression asks whether data can support a small law.",
        "reader_takeaway": "Each method is a response to a different pressure. Confusing those pressures is how vague explanations start.",
        "links": ["families.html", "comparisons.html", "diagrams.html"],
    },
    {
        "slug": "proof-burden",
        "title": "Proof Burden",
        "claim": "A method name never proves a scientific claim; only a named test under a meaningful changed case can carry that burden.",
        "explanation": "A transcript mention shows that a topic appears in the course. A training score shows that a model matched a written score. A scientific claim needs more: a domain, quantity, use range, and failure test.",
        "reader_takeaway": "Every strong page should say what the transcript supports and what it does not prove.",
        "links": ["evidence-ledger.html", "reader-checks.html", "quality/evidence-discipline.html"],
    },
    {
        "slug": "field-map",
        "title": "Field Map",
        "claim": "The field is best read as a map of scientific jobs, not a list of model names.",
        "explanation": "Sparse measurements point toward physics checks. Many solved fields point toward operator learning. Repeated expensive decisions point toward surrogates. New settings point toward uncertainty. Need for a readable law points toward model discovery.",
        "reader_takeaway": "Start from the job, then choose the concept family that carries the right evidence.",
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
        "Hand-write richer derivations for the highest-value concepts after reviewing the generated structure.",
        "Add more worked examples for chemistry, materials, graphs, attention, and foundation PDE models.",
        "Add real figures or mathematical sketches where a static flow diagram is not enough.",
        "Review transcript excerpts for places where better quotes or lecture-specific anchors should be selected.",
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
    concept_ladder = build_concept_ladder(topic_treatments)

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
            "diagram_count": len(DIAGRAMS),
            "learning_path_step_count": len(LEARNING_PATH),
            "glossary_term_count": len(GLOSSARY),
            "domain_guide_count": len(DOMAIN_GUIDES),
            "reader_check_count": len(READER_CHECKS),
            "decision_guide_count": len(DECISION_GUIDES),
            "provenance_guide_count": len(PROVENANCE_GUIDES),
            "coverage_row_count": len(coverage_matrix),
            "concept_ladder_count": len(concept_ladder),
            "quality_rubric_count": len(QUALITY_RUBRIC),
            "synthesis_guide_count": len(SYNTHESIS_GUIDES),
            "review_handoff_count": 1,
            "review_entrypoint_count": sum(len(group["items"]) for group in REVIEW_ENTRYPOINTS),
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
        "diagrams": DIAGRAMS,
        "learning_path": LEARNING_PATH,
        "glossary": GLOSSARY,
        "domain_guides": DOMAIN_GUIDES,
        "reader_checks": READER_CHECKS,
        "decision_guides": DECISION_GUIDES,
        "provenance_guides": PROVENANCE_GUIDES,
        "coverage_matrix": coverage_matrix,
        "concept_ladder": concept_ladder,
        "quality_rubric": QUALITY_RUBRIC,
        "synthesis_guides": SYNTHESIS_GUIDES,
        "review_handoff": REVIEW_HANDOFF,
        "review_entrypoints": REVIEW_ENTRYPOINTS,
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
  <a href="{root_prefix}learning-path.html">Path</a>
  <a href="{root_prefix}glossary.html">Glossary</a>
  <a href="{root_prefix}domains.html">Domains</a>
  <a href="{root_prefix}reader-checks.html">Checks</a>
  <a href="{root_prefix}decision-guide.html">Decide</a>
  <a href="{root_prefix}provenance.html">Provenance</a>
  <a href="{root_prefix}coverage.html">Coverage</a>
  <a href="{root_prefix}concept-ladder.html">Ladder</a>
  <a href="{root_prefix}quality.html">Quality</a>
  <a href="{root_prefix}synthesis.html">Synthesis</a>
  <a href="{root_prefix}review-entrypoints.html">Review Map</a>
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


def write_site(data: dict[str, object]) -> None:
    SITE.mkdir(parents=True, exist_ok=True)
    write_style()
    topic_dir = SITE / "topics"
    video_dir = SITE / "videos"
    family_dir = SITE / "families"
    comparison_dir = SITE / "comparisons"
    example_dir = SITE / "worked-examples"
    diagram_dir = SITE / "diagrams"
    learning_dir = SITE / "learning-path"
    glossary_dir = SITE / "glossary"
    domain_dir = SITE / "domains"
    check_dir = SITE / "reader-checks"
    decision_dir = SITE / "decision-guide"
    provenance_dir = SITE / "provenance"
    quality_dir = SITE / "quality"
    synthesis_dir = SITE / "synthesis"
    for generated_dir in (family_dir, comparison_dir, example_dir, diagram_dir, learning_dir, glossary_dir, domain_dir, check_dir, decision_dir, provenance_dir, quality_dir, synthesis_dir):
        if generated_dir.exists():
            shutil.rmtree(generated_dir)
    topic_dir.mkdir(exist_ok=True)
    video_dir.mkdir(exist_ok=True)
    family_dir.mkdir(exist_ok=True)
    comparison_dir.mkdir(exist_ok=True)
    example_dir.mkdir(exist_ok=True)
    diagram_dir.mkdir(exist_ok=True)
    learning_dir.mkdir(exist_ok=True)
    glossary_dir.mkdir(exist_ok=True)
    domain_dir.mkdir(exist_ok=True)
    check_dir.mkdir(exist_ok=True)
    decision_dir.mkdir(exist_ok=True)
    provenance_dir.mkdir(exist_ok=True)
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
    learning_path = data["learning_path"]
    glossary = data["glossary"]
    domain_guides = data["domain_guides"]
    reader_checks = data["reader_checks"]
    decision_guides = data["decision_guides"]
    provenance_guides = data["provenance_guides"]
    coverage_matrix = data["coverage_matrix"]
    concept_ladder = data["concept_ladder"]
    quality_rubric = data["quality_rubric"]
    synthesis_guides = data["synthesis_guides"]
    review_handoff = data["review_handoff"]
    review_entrypoints = data["review_entrypoints"]

    index_body = f"""
<h1>Physics-Informed Machine Learning Concepts Research</h1>
<p>This package turns two ETH Zurich AI in the Sciences and Engineering playlists into a transcript-backed research map for physics-informed machine learning. It is built from first principles: what problem each idea solves, what scientific domain needs it, what information it keeps, what it leaves out, and how the claim can fail.</p>
<div class="grid">
{card("Videos", f"{summary['video_count']} source videos across two playlists, with {summary['available_transcripts']} available transcripts.", "transcripts.html")}
{card("Concepts", f"{summary['concept_count']} concepts extracted into plain-language topic treatments.", "concept-atlas.html")}
{card("Paper Families", f"{summary['family_count']} routes through related concept families.", "families.html")}
{card("Comparisons", f"{summary['comparison_count']} plain-language method comparisons.", "comparisons.html")}
{card("Worked Examples", f"{summary['worked_example_count']} concrete scientific examples.", "worked-examples.html")}
{card("Diagrams", f"{summary['diagram_count']} visual flows for the main mathematical ideas.", "diagrams.html")}
{card("Learning Path", f"{summary['learning_path_step_count']} steps from first question to field-level understanding.", "learning-path.html")}
{card("Glossary", f"{summary['glossary_term_count']} field terms translated into everyday language.", "glossary.html")}
{card("Domains", f"{summary['domain_guide_count']} domain guides that ground concepts in real scientific work.", "domains.html")}
{card("Reader Checks", f"{summary['reader_check_count']} self-check prompts for core ideas.", "reader-checks.html")}
{card("Decision Guide", f"{summary['decision_guide_count']} method choices from concrete scientific situations.", "decision-guide.html")}
{card("Provenance", f"{summary['provenance_guide_count']} pages documenting source, extraction, build, and reproduction.", "provenance.html")}
{card("Coverage Matrix", f"{summary['coverage_row_count']} concepts checked across evidence and guide layers.", "coverage.html")}
{card("Concept Ladder", f"{summary['concept_ladder_count']} concepts laid out from observed evidence to failure test.", "concept-ladder.html")}
{card("Quality Rubric", f"{summary['quality_rubric_count']} editorial standards for first-principles pages.", "quality.html")}
{card("Synthesis", f"{summary['synthesis_guide_count']} pages tying the field into one argument.", "synthesis.html")}
{card("Review Map", f"{summary['review_entrypoint_count']} entry points for end-to-end review, use, and source checks.", "review-entrypoints.html")}
{card("Review Handoff", "Shortest route for reviewing the package and the remaining editorial work.", "handoff.html")}
{card("Themes", f"{summary['theme_count']} recurring research pressures across the course family.", "theme-map.html")}
{card("Evidence", "Each major claim links back to transcript or metadata evidence and states its limit.", "evidence-ledger.html")}
</div>
<h2>Central Big Picture</h2>
<p>The course family asks how machine learning can help science without throwing away physics. The recurring problem is not simply prediction. The real problem is turning data, equations, simulations, geometry, and uncertainty into models that can be trusted for a named scientific job.</p>
<h2>Core Route Through The Material</h2>
<ol>
  <li>Start with scientific data and the need to predict or explain a changed case.</li>
  <li>Add neural networks as adjustable function builders, but keep their limits visible.</li>
  <li>Bring in PDEs, physics penalties, operators, geometry, and uncertainty as ways to stop the model from becoming an unchecked fit.</li>
  <li>Judge every method by the scientific claim it can support and the failure case it can expose.</li>
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
    (SITE / "diagrams.html").write_text(
        html_page("Physics-Informed ML Diagrams", f"<h1>Diagram Index</h1><p>These diagrams show the flow of evidence, rules, learned objects, and validation checks. They are deliberately simple so the core idea is visible before any notation appears.</p><div class=\"grid\">{''.join(diagram_cards)}</div>"),
        encoding="utf-8",
    )

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
    write_concept_ladder_page(SITE / "concept-ladder.html", list(concept_ladder))

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


def write_topic_page(path: Path, topic: dict[str, object]) -> None:
    evidence = topic.get("evidence", [])
    evidence_items = []
    if isinstance(evidence, list):
        for row in evidence:
            evidence_items.append(f"<li><a href=\"{html.escape(str(row['url']))}\">{html.escape(str(row['title']))}</a>: {html.escape(str(row.get('excerpt') or 'metadata evidence'))}</li>")
    derivation = topic_derivation(topic)
    deep_dive = topic_deep_dive_html(str(topic["slug"]))
    diagrams = topic_diagrams_html(str(topic["slug"]))
    reader_check = topic_reader_check_html(str(topic["slug"]))
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
<h2>First-Principles Walkthrough</h2>
<ol>
  <li><strong>Start with what is observed:</strong> {html.escape(str(derivation['observed']))}.</li>
  <li><strong>Name what is hidden:</strong> {html.escape(str(derivation['hidden']))}.</li>
  <li><strong>Make the smallest mathematical move:</strong> {html.escape(str(derivation['move']))}.</li>
  <li><strong>Read the shape:</strong> {html.escape(str(derivation['form']))}.</li>
  <li><strong>Say what it means:</strong> {html.escape(str(derivation['meaning']))}.</li>
</ol>
{deep_dive}
{diagrams}
<h2>Deeper Mathematical Why</h2>
<p>The mathematical point is to decide what information is allowed to carry the scientific claim. If the carried information is too small, the model misses the behavior that matters. If it is too broad, the page may claim more than the evidence supports. The useful middle is a named object, a named scientific job, and a changed case that can reject the claim.</p>
{reader_check}
<h2>Reader Test</h2>
<p>A reader understands this concept only if they can say what is observed, what is hidden, what is kept, what is ignored, and why this changed-case test matters: {html.escape(str(derivation['test']))}.</p>
<h2>Failure Boundary</h2>
<p>{html.escape(str(topic['failure_boundary']))}</p>
<h2>What The Transcript Does Not Prove</h2>
<p>The transcript evidence shows where the course introduces or uses this concept. It does not prove the concept works for every equation, data set, solver, material, geometry, or scientific task. That wider claim needs explicit validation evidence.</p>
<h2>Transcript Evidence</h2>
<ul>{''.join(evidence_items)}</ul>
"""
    path.write_text(html_page(str(topic["title"]), body, root_prefix="../"), encoding="utf-8")


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


def write_learning_step_page(path: Path, step: dict[str, object]) -> None:
    read_items = []
    for item in step["read"]:
        read_items.append(f"<li><a href=\"../{html.escape(str(item['href']))}\">{html.escape(str(item['label']))}</a></li>")
    body = f"""
<h1>{html.escape(str(step['title']))}</h1>
<h2>Question</h2>
<p>{html.escape(str(step['question']))}</p>
<h2>Why This Comes Here</h2>
<p>{html.escape(str(step['why_first']))}</p>
<h2>Plain Goal</h2>
<p>{html.escape(str(step['plain_goal']))}</p>
<h2>Read Next</h2>
<ul>{''.join(read_items)}</ul>
<h2>Checkpoint</h2>
<p>{html.escape(str(step['checkpoint']))}</p>
"""
    path.write_text(html_page(str(step["title"]), body, root_prefix="../"), encoding="utf-8")


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
    body = f"""
<h1>{html.escape(str(guide['title']))}</h1>
<h2>Real Quantity</h2>
<p>{html.escape(str(guide['real_quantity']))}</p>
<h2>Why This Domain Is Hard</h2>
<p>{html.escape(str(guide['why_hard']))}</p>
<h2>Common Question</h2>
<p>{html.escape(str(guide['common_question']))}</p>
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


def write_handoff_page(path: Path, handoff: dict[str, object], summary: dict[str, object]) -> None:
    commands = "".join(f"<li><code>{html.escape(str(command))}</code></li>" for command in handoff["validation_commands"])
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
<h2>Common Wrong Turn</h2>
<p>{html.escape(str(comparison['wrong_turn']))}</p>
<h2>First-Principles Test</h2>
<p>Before choosing a side, name the scientific quantity, the available evidence, the use range, and the changed case that would expose a bad answer.</p>
"""
    path.write_text(html_page(str(comparison["title"]), body, root_prefix="../"), encoding="utf-8")


def write_worked_example_page(path: Path, example: dict[str, object]) -> None:
    steps = "".join(f"<div class=\"route-step\">{idx}. {html.escape(step)}</div>" for idx, step in enumerate(example["plain_steps"], start=1))
    body = f"""
<h1>{html.escape(str(example['title']))}</h1>
<h2>Scientific Job</h2>
<p><strong>Domain:</strong> {html.escape(str(example['domain']))}</p>
<p><strong>Question:</strong> {html.escape(str(example['question']))}</p>
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
    lines.extend(["", "## Learning Path"])
    for idx, step in enumerate(data["learning_path"], start=1):
        lines.extend(
            [
                f"### {idx}. {step['title']}",
                f"- Question: {step['question']}",
                f"- Why here: {step['why_first']}",
                f"- Goal: {step['plain_goal']}",
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
        lines.extend(
            [
                f"### {guide['title']}",
                f"- Real quantity: {guide['real_quantity']}",
                f"- Why hard: {guide['why_hard']}",
                f"- Common question: {guide['common_question']}",
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
    lines.extend(["", "## Review Entrypoints"])
    for group in data["review_entrypoints"]:
        lines.extend(["", f"### {group['group']}", f"- Purpose: {group['purpose']}"])
        for item in group["items"]:
            lines.append(f"- {item['label']}: {item['href']} | {item['question']}")
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
        if "Core Idea In One Sentence" not in topic_text or "Mathematical Shape Without Jargon" not in topic_text:
            raise SystemExit(f"deep dive not rendered on topic page: {slug}")
    for path in (
        SITE / "index.html",
        SITE / "transcripts.html",
        SITE / "concept-atlas.html",
        SITE / "families.html",
        SITE / "comparisons.html",
        SITE / "worked-examples.html",
        SITE / "diagrams.html",
        SITE / "learning-path.html",
        SITE / "glossary.html",
        SITE / "domains.html",
        SITE / "reader-checks.html",
        SITE / "decision-guide.html",
        SITE / "provenance.html",
        SITE / "coverage.html",
        SITE / "concept-ladder.html",
        SITE / "quality.html",
        SITE / "synthesis.html",
        SITE / "review-entrypoints.html",
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
        if not (SITE / "comparisons" / f"{comparison['slug']}.html").exists():
            raise SystemExit(f"missing comparison page: {comparison['title']}")
    for example in WORKED_EXAMPLES:
        if not (SITE / "worked-examples" / f"{example['slug']}.html").exists():
            raise SystemExit(f"missing worked example page: {example['title']}")
    for diagram in DIAGRAMS:
        diagram_path = SITE / "diagrams" / f"{diagram['slug']}.html"
        if not diagram_path.exists():
            raise SystemExit(f"missing diagram page: {diagram['title']}")
        diagram_text = diagram_path.read_text(encoding="utf-8")
        if "flow-node" not in diagram_text or "Watch for:" not in diagram_text:
            raise SystemExit(f"diagram not rendered correctly: {diagram['title']}")
    for step in LEARNING_PATH:
        step_path = SITE / "learning-path" / f"{step['slug']}.html"
        if not step_path.exists():
            raise SystemExit(f"missing learning path page: {step['title']}")
        step_text = step_path.read_text(encoding="utf-8")
        if "Checkpoint" not in step_text or "Read Next" not in step_text:
            raise SystemExit(f"learning path page not rendered correctly: {step['title']}")
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
        if "Real Quantity" not in guide_text or "Failure Test" not in guide_text:
            raise SystemExit(f"domain guide not rendered correctly: {guide['title']}")
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
    core_slugs = {"physics-informed-neural-networks", "operator-learning", "surrogate-modeling", "uncertainty-and-generalization", "symbolic-regression", "foundation-models-for-pdes"}
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
    handoff_path = SITE / "handoff.html"
    handoff_text = handoff_path.read_text(encoding="utf-8")
    if "Start Here" not in handoff_text or "Remaining Editorial Work" not in handoff_text:
        raise SystemExit("handoff page not rendered correctly")
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
