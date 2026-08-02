#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urlparse


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
ANALYSIS = ROOT / "analysis"

REQUIRED_ROOT_PAGES = {
    "index.html",
    "transcripts.html",
    "concept-atlas.html",
    "families.html",
    "comparisons.html",
    "worked-examples.html",
    "diagrams.html",
    "derivations.html",
    "formula-guide.html",
    "misconceptions.html",
    "course-spine.html",
    "topology-shape-guide.html",
    "shape-transfer-practice.html",
    "question-to-topic-guide.html",
    "field-application-guide.html",
    "importance-matrix.html",
    "end-to-end-walkthrough.html",
    "plain-capstone.html",
    "example-route-guide.html",
    "no-jargon-concept-guide.html",
    "learning-path.html",
    "glossary.html",
    "domains.html",
    "reader-checks.html",
    "plain-explanation-practice.html",
    "decision-guide.html",
    "provenance.html",
    "coverage.html",
    "dependencies.html",
    "concept-ladder.html",
    "evidence-packets.html",
    "quality.html",
    "wording-audit.html",
    "plain-essay-review.html",
    "synthesis.html",
    "review-entrypoints.html",
    "review-search.html",
    "review-queue.html",
    "hand-polish.html",
    "editorial-roadmap.html",
    "completion-audit.html",
    "meaty-goal.html",
    "meaty-goal-coverage.html",
    "handoff.html",
    "theme-map.html",
    "evidence-ledger.html",
}

RESTRICTED_PATTERNS = (
    "framework",
    "leverage",
    "paradigm",
    "utilize",
    "robust",
    "seamless",
    "black box",
    "black-box",
    "state of the art",
    "cutting edge",
    "powerful",
    "advanced",
    "complex",
    "many different",
)

MEATY_GOAL_REQUIREMENT_COUNT = 65


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        for name, value in attrs:
            if name == "href" and value:
                self.hrefs.append(value)


def html_links(path: Path) -> list[str]:
    parser = LinkParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser.hrefs


def is_external(href: str) -> bool:
    parsed = urlparse(href)
    return bool(parsed.scheme or parsed.netloc)


def check_internal_links(manifest: list[str]) -> list[str]:
    errors: list[str] = []
    for item in manifest:
        page = ROOT / item
        for raw_href in html_links(page):
            href, _fragment = urldefrag(raw_href)
            if not href or is_external(href):
                continue
            target = (page.parent / href).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{item}: link escapes repo: {raw_href}")
                continue
            if not target.exists():
                errors.append(f"{item}: missing link target: {raw_href}")
    return errors


def check_required_sections() -> list[str]:
    required = {
        "site/handoff.html": ("Review Now", "http://127.0.0.1:8022/hand-polish.html", "make review", "make remote-check", "make ci-check", "python3 scripts/verify_remote_state.py", "python3 scripts/verify_ci_status.py", "Start Here", "Remote Verification Commands", "git push -u origin main", "Remaining Editorial Work"),
        "site/coverage.html": ("Coverage Matrix", "Reader Check"),
        "site/synthesis.html": ("Field Synthesis",),
        "site/quality.html": ("Editorial Quality Rubric",),
        "site/domains.html": ("Domain Guides", "Quantity", "Decision", "Hidden Part", "Changed-Case Test"),
        "site/provenance.html": ("Provenance And Reproduction",),
        "site/decision-guide.html": ("Decision Guide",),
        "site/decision-guide/many-examples-no-rule.html": ("Best Starting Point", "Evidence Needed", "Deep learning"),
        "site/decision-guide/field-rule-before-method.html": ("Best Starting Point", "Evidence Needed", "Partial differential equations"),
        "site/decision-guide/need-many-valid-possibilities.html": ("Best Starting Point", "Evidence Needed", "Generative modeling"),
        "site/reader-checks.html": ("Reader Checks",),
        "site/reader-checks/pinns-check.html": ("Strong Answer Should Say", "Weak Answer Warning", "Acceptance Sentence", "First-Principles Scoring Rubric", "Changed-case rejection", "Forbidden shortcut"),
        "site/review-entrypoints.html": ("Review Entrypoints", "End-To-End Test"),
        "site/review-search.html": ("Find Pages By Question", "Open First", "Prove Before Moving On", "Reject The Route If", "Review Rule"),
        "site/review-queue.html": ("Review Queue", "Reviewed Anchors", "Broad Mentions", "Missing Layers", "Next Action", "P1"),
        "site/hand-polish.html": ("Hand Polish Audit", "Acceptance Checks", "Overclaim To Avoid", "First Rejection Test"),
        "site/editorial-roadmap.html": ("Editorial Roadmap", "Status:", "Current Evidence", "Acceptance Check", "locally completed", "Meaty End-To-End Goal"),
        "site/completion-audit.html": ("Completion Audit", "Requirement Evidence", "GitHub Actions", "locally verified"),
        "site/meaty-goal.html": ("Meaty End-To-End Goal", "Done Means", "Every Core Page Must Contain", "Acceptance Sentence", "Not Done If"),
        "site/meaty-goal-coverage.html": ("Meaty Goal Coverage Audit", "First Principles", "Big Picture Claim Chain", "Explanation Order", "Why Care Before Terms", "Workday Decision Rehearsal", "Sounds-Right Filter", "Draw Before Math", "Start-Here Gate", "Skeptical Reader Proof", "Oral Explanation Script", "Before-After Decision", "Outside-Classroom Use", "Learner Notebook Note", "Tiny Invented Case", "End-To-End Use Protocol", "Before The Math Slow Walk", "Teach From Zero", "Application Claim Ladder", "Field Decision Story", "From Scratch Story", "No-Jargon Translation", "Everyday Vocabulary Bridge", "Plain Retell Drill", "Field Transfer Check", "New Case Transfer Rehearsal", "Wrong Path Repair", "Confusion To Clarity", "Course Bridge", "Use Or Refuse Gate", "Final Learner Proof", "Teach Someone Handoff", "Topology Shape Story", "One-Page Mental Model", "Next-Day Memory Check", "Nearby Topic Comparison", "Math Shape Rehearsal", "Source-To-Claim Boundary", "Field Mini Cases", "Plain Question To Answer Script", "Know And Still Test", "Failure Consequence", "Slow Problem Shape Bridge", "Plain Big Picture Essay", "Slow Importance Essay", "Long Everyday Importance Essay", "Hand Teaching Note", "Case Walkthrough", "Course Role", "Concept Connections", "Belief Evidence", "Domain Fit", "Shape Follows", "Formula Terms", "Breaks Without Idea", "Reader Answer Parts", "Say It Back Check", "Reader Mistake Audit", "Misread Repair Drill", "Plain-Language Audit", "Acceptance Sentence", "Missing Items"),
        "site/families.html": ("Paper Family Routes",),
        "site/families/physics-constraints-family.html": ("Family Story From First Principles", "Concrete Family Case", "Route Burden Table", "Question It Answers", "Mistake It Catches", "Why The Concepts Appear In This Order", "Evidence Chain To Track", "What Each Concept Does In The Family", "Evidence Needed Before Trusting The Family", "Too Weak"),
        "site/families/neural-operators-family.html": ("Family Story From First Principles", "Concrete Family Case", "Route Burden Table", "Question It Answers", "Mistake It Catches", "Why The Concepts Appear In This Order", "Evidence Chain To Track", "What Each Concept Does In The Family", "Evidence Needed Before Trusting The Family", "Too Weak"),
        "site/families/model-discovery-family.html": ("Family Story From First Principles", "Concrete Family Case", "Route Burden Table", "Question It Answers", "Mistake It Catches", "Why The Concepts Appear In This Order", "Evidence Chain To Track", "What Each Concept Does In The Family", "Evidence Needed Before Trusting The Family", "Too Weak"),
        "site/families/scientific-surrogates-family.html": ("Family Story From First Principles", "Concrete Family Case", "Route Burden Table", "Question It Answers", "Mistake It Catches", "Why The Concepts Appear In This Order", "Evidence Chain To Track", "What Each Concept Does In The Family", "Evidence Needed Before Trusting The Family", "Too Weak"),
        "site/worked-examples.html": ("Worked Examples",),
        "site/worked-examples/heat-equation-from-few-measurements.html": ("First-Principles Story", "Decision Quantity", "Why Each Step Follows", "Why It Follows From The Evidence", "First Failure Signal", "Example Stress Test", "Passes Only If"),
        "site/worked-examples/fast-fluid-field-surrogate.html": ("First-Principles Story", "Decision Quantity", "Why Each Step Follows", "Why It Follows From The Evidence", "First Failure Signal", "Example Stress Test", "Passes Only If"),
        "site/diagrams.html": ("Mathematical Sketches", "Kept Rule", "Failure Case"),
        "site/topics/operator-learning.html": ("Big Picture Claim Chain", "Before The Math Slow Walk", "Say It Without Jargon", "What We Have", "What We Need", "Why The Idea Enters", "What To Try First", "Stop Trusting It When", "Everyday Problem", "Decision Or Quantity At Stake", "Hidden Thing Needed", "First Thing That Can Break The Claim", "End-To-End Use Protocol", "State The Scientific Job", "Name The Decision Quantity", "Inventory The Evidence", "Choose The Mathematical Carrier", "Build The Smallest Working Case", "Run The Changed-Case Test", "Reject Or Narrow The Claim When", "Final Claim Allowed", "Teach It From Zero", "Start With A Person", "What They Can See", "What They Cannot See Yet", "The First-Principles Move", "Where Shape Or Topology Enters", "Where People Use It", "End With The Claim", "Application Claim Ladder", "Application Field", "Evidence To Start From", "Hidden Answer Needed", "Changed Case That Tests It", "Plain Question To Answer Script", "Real question", "Evidence sentence", "Missing-answer sentence", "Shape or topology sentence", "Allowed-answer sentence", "Stop sentence", "What I Know And What I Still Test", "What I Know", "Evidence I Can Point To", "Answer I Still Need", "Move That Tries To Get There", "Shape Or Topology I Must Not Lose", "Claim I Can Say Carefully", "Test Still Needed", "Stop Or Narrow When", "Why The Failure Matters", "Missing Piece", "What Can Go Wrong", "Engineering Consequence", "Materials Or Biology Consequence", "Climate Or Field Consequence", "Smallest Prevention", "Slow Bridge From Problem To Shape", "Everyday Shortage", "Answer Type Needed", "Evidence Carrier", "Why A Single Number Is Not Enough", "Smallest Honest Shape", "What Would Make The Shape Too Weak", "Plain Big Picture Essay", "Why This Matters Slowly", "Topology and shape matter here", "The reader should leave this section with one plain sentence", "Applications In Everyday Words", "Topology and shape", "Engineering design", "Materials, chemistry, and biology", "Climate, fluids, and fields", "One Concrete Case From Start To Finish", "Observed Evidence", "Rejection Test", "Course Role In Plain Words", "Why It Appears Here", "Read Before This", "What It Unlocks Later", "Confusion This Prevents", "Plain Course Sentence", "How This Connects To Nearby Ideas", "Learn Before This", "Confusion It Prevents", "Evidence Needed To Believe This", "Strong Evidence", "Too Weak", "Reject Or Recheck When", "Where This Fits By Domain", "When To Avoid This In A Domain", "Changed-Case Test", "Plain Formula Term By Term", "What It Carries", "Concrete Worked Example", "Concrete Wrong-Use Example", "Test That Catches It", "What Breaks Without This Idea", "Minimum Proof Needed", "Reader Must Be Able To Say", "Say It Back Check", "Real Problem", "Evidence I Have", "Answer I Need", "Shape Or Topology Issue", "Claim I Am Allowed To Make", "Misread Repair Drill", "Likely Misread", "Why That Sounds Tempting", "Plain Repair", "Evidence To Name Before Trusting It", "Changed Case That Repairs The Overclaim", "One Sentence To Keep", "Plain-Language Audit", "Do Not Say", "Say Instead", "Rewrite Test", "Acceptance Sentence Filled", "I would test it by changing", "Mathematical Sketch", "Field To Field", "Kept Rule"),
        "site/topics/surrogate-modeling.html": ("Big Picture Claim Chain", "Before The Math Slow Walk", "Say It Without Jargon", "What We Have", "What We Need", "Why The Idea Enters", "What To Try First", "Stop Trusting It When", "Everyday Problem", "Decision Or Quantity At Stake", "Hidden Thing Needed", "First Thing That Can Break The Claim", "End-To-End Use Protocol", "State The Scientific Job", "Name The Decision Quantity", "Inventory The Evidence", "Choose The Mathematical Carrier", "Build The Smallest Working Case", "Run The Changed-Case Test", "Reject Or Narrow The Claim When", "Final Claim Allowed", "Teach It From Zero", "Start With A Person", "What They Can See", "What They Cannot See Yet", "The First-Principles Move", "Where Shape Or Topology Enters", "Where People Use It", "End With The Claim", "Application Claim Ladder", "Application Field", "Evidence To Start From", "Hidden Answer Needed", "Changed Case That Tests It", "Plain Question To Answer Script", "Real question", "Evidence sentence", "Missing-answer sentence", "Shape or topology sentence", "Allowed-answer sentence", "Stop sentence", "What I Know And What I Still Test", "What I Know", "Evidence I Can Point To", "Answer I Still Need", "Move That Tries To Get There", "Shape Or Topology I Must Not Lose", "Claim I Can Say Carefully", "Test Still Needed", "Stop Or Narrow When", "Why The Failure Matters", "Missing Piece", "What Can Go Wrong", "Engineering Consequence", "Materials Or Biology Consequence", "Climate Or Field Consequence", "Smallest Prevention", "Slow Bridge From Problem To Shape", "Everyday Shortage", "Answer Type Needed", "Evidence Carrier", "Why A Single Number Is Not Enough", "Smallest Honest Shape", "What Would Make The Shape Too Weak", "Plain Big Picture Essay", "Why This Matters Slowly", "Topology and shape matter here", "The reader should leave this section with one plain sentence", "Applications In Everyday Words", "Topology and shape", "Engineering design", "Materials, chemistry, and biology", "Climate, fluids, and fields", "One Concrete Case From Start To Finish", "Observed Evidence", "Rejection Test", "Course Role In Plain Words", "Why It Appears Here", "Read Before This", "What It Unlocks Later", "Confusion This Prevents", "Plain Course Sentence", "How This Connects To Nearby Ideas", "Learn Before This", "Confusion It Prevents", "Evidence Needed To Believe This", "Strong Evidence", "Too Weak", "Reject Or Recheck When", "Where This Fits By Domain", "When To Avoid This In A Domain", "Changed-Case Test", "Plain Formula Term By Term", "What It Carries", "Concrete Worked Example", "Concrete Wrong-Use Example", "Test That Catches It", "What Breaks Without This Idea", "Minimum Proof Needed", "Reader Must Be Able To Say", "Say It Back Check", "Real Problem", "Evidence I Have", "Answer I Need", "Shape Or Topology Issue", "Claim I Am Allowed To Make", "Misread Repair Drill", "Likely Misread", "Why That Sounds Tempting", "Plain Repair", "Evidence To Name Before Trusting It", "Changed Case That Repairs The Overclaim", "One Sentence To Keep", "Plain-Language Audit", "Do Not Say", "Say Instead", "Rewrite Test", "Acceptance Sentence Filled", "I would test it by changing", "Mathematical Sketch", "Fast Stand-In", "Failure Case"),
        "site/comparisons/pinns-vs-neural-operators.html": ("How To Decide From First Principles", "Decision Chain From First Principles", "Shortage That Creates The Choice", "Evidence Carried By", "First Wrong Answer To Look For", "Decision Checklist", "Decision Burden Table", "Swap Test", "Evidence Needed To Choose", "Concrete Choice Cases", "Wrong Choice Case", "Evidence That Exposes It"),
        "site/comparisons/solvers-vs-learned-surrogates.html": ("How To Decide From First Principles", "Decision Chain From First Principles", "Shortage That Creates The Choice", "Evidence Carried By", "First Wrong Answer To Look For", "Decision Checklist", "Decision Burden Table", "Swap Test", "Evidence Needed To Choose", "Concrete Choice Cases", "Wrong Choice Case", "Evidence That Exposes It"),
        "site/learning-path/scientific-question-first.html": ("No-Jargon Explanation", "First-Principles Spine", "World:", "Reject it when:"),
        "site/learning-path/physics-as-check.html": ("No-Jargon Explanation", "First-Principles Spine", "Mathematical move:", "Reject it when:"),
        "site/dependencies.html": ("Concept Dependency Map", "Confusion It Prevents"),
        "site/concept-ladder.html": ("Concept Ladder", "Mathematical Move", "Failure Test"),
        "site/evidence-packets.html": ("Concept Evidence Packets",),
        "site/formula-guide.html": ("Plain Formula Guide", "Common Misread", "What To Check", "Do not read the loss as proof", "Do not read broad training as coverage"),
        "site/misconceptions.html": ("Misconception Map", "Wrong Turn", "Why It Is Tempting", "Repair Sentence", "First-Principles Test"),
        "site/course-spine.html": ("Course Spine In Plain Words", "The Whole Course In One Human Problem", "First-Principles Route Through The Field", "Why Topology And Shape Belong In The Big Picture", "How Every Topic Fits The Spine", "Reader Test For The Whole Course", "Deep Learning", "Physics-Informed Neural Networks", "Operator Learning", "Topology", "shape", "changed case"),
        "site/topology-shape-guide.html": ("Topology And Shape In Plain Words", "The Everyday Meaning", "Why It Matters From First Principles", "How This Theme Crosses The Course", "Plain Shape Use", "First Shape Check", "What To Say Before Trusting A Shape Claim", "Reader Test", "mesh", "molecule", "boundary", "hole", "Graphs And Geometric Learning"),
        "site/shape-transfer-practice.html": ("Shape Transfer Practice", "Why This Practice Exists", "Transfer Matrix", "Plain Shape Use", "Why Shape Matters", "Engineering Transfer", "Materials Or Biology Transfer", "Climate Or Field Transfer", "Shape Test", "Transfer Drills", "Name the shaped object", "Name the relation", "Plain transfer sentence", "Pass Standard", "Deep Learning", "Operator Learning", "Graphs And Geometric Learning"),
        "site/question-to-topic-guide.html": ("Question To Topic Guide", "Start With The Need", "Everyday Question", "Open This Topic", "Why This Is The First Stop", "What To Check Before Trusting It", "If Your Question Mentions Shape", "Reader Test", "I have many examples", "I have a few measurements and a known equation", "mesh", "molecule", "changed case"),
        "site/field-application-guide.html": ("Field Application Guide In Plain Words", "Why Fields Need Their Own Map", "Engineering design", "Materials, chemistry, and biology", "Climate, fluids, and fields", "Plain Use", "Why It Matters", "First Field Check", "How To Read An Application Claim", "Reader Test", "stress", "molecule", "climate", "fluids", "changed case"),
        "site/importance-matrix.html": ("Importance Matrix", "Why Each Topic Matters Across Fields", "Concept", "Everyday Problem", "Why It Matters", "Topology Or Shape Link", "Other Fields", "First Test", "How To Use This Matrix", "Plain End-To-End Stories", "Reader Test", "Deep Learning", "Operator Learning", "Graphs And Geometric Learning", "changed case"),
        "site/plain-capstone.html": ("Plain Capstone", "Final Proof Of Understanding", "Capstone Answer Template", "Capstone Proof Table", "Everyday Need", "Evidence", "Hidden Answer", "First-Principles Move", "Shape Check", "Rejection Test", "Topic Capstone Prompts", "Final Answer Prompt", "Pass Standard", "Deep Learning", "Operator Learning", "Graphs And Geometric Learning"),
        "site/plain-essay-review.html": ("Plain Essay Review", "Teacher Review Goal", "Review Matrix", "Everyday Need", "First-Principles Chain", "Shape Or Topology", "Other Field Uses", "First Changed Case", "Review Method", "Per-Topic Review Burden", "Everyday Opening To Find", "Weak Spot To Inspect First", "Reader Pass Test", "Deep Learning", "Operator Learning", "Graphs And Geometric Learning"),
        "site/plain-explanation-practice.html": ("Plain Explanation Practice", "Practice Goal", "Quick Checklist", "Everyday Need", "Missing Answer", "Shape Check", "Changed Case", "Explanation Drills", "Everyday opening", "Evidence sentence", "Missing-answer sentence", "Shape or topology sentence", "Field transfer sentence", "Rewrite Task", "Pass Standard", "Deep Learning", "Operator Learning", "Graphs And Geometric Learning"),
        "site/end-to-end-walkthrough.html": ("End-To-End Course Walkthrough", "One Scientific Job From Start To Finish", "The Plain Route", "First Topic To Open", "Everyday Need", "What It Adds", "Rejection Check", "Shape And Field Checks", "What The Final Claim Can Say", "Final Say-It-Back Test", "sparse measurements", "shaped domain", "changed case"),
        "site/example-route-guide.html": ("Example Route Guide", "Start With A Concrete Job", "Worked Example Routes", "Open This Example", "Scientific Job", "Observed Evidence", "Hidden Answer", "Topic Route", "First Failure Signal", "How To Use A Route", "Reader Test", "heat", "molecule", "climate"),
        "site/no-jargon-concept-guide.html": ("No-Jargon Concept Guide", "Translate The Label Into A Job", "Concepts Without Hiding Behind Names", "Concept Label", "Everyday Job", "Evidence In Hand", "Hidden Answer Needed", "Plain Move", "First Rejection Check", "How To Read A Method Name", "Reader Test", "Deep Learning", "Physics-Informed Neural Networks", "Operator Learning"),
        "site/evidence-packets/physics-informed-neural-networks.html": ("Source Strength Audit", "Reviewed Source Anchors", "Broad Transcript Mentions", "Minimum Review Action", "Stronger Proof Needed", "Transcript Evidence vs Scientific Proof", "Transcript Can Support", "Transcript Cannot Support", "Stronger Validation Needed", "First Overclaim To Reject", "Reviewer Action", "Transcript Support", "What This Evidence Does Not Prove", "Review Links"),
        "site/evidence-packets/operator-learning.html": ("Source Strength Audit", "Reviewed Source Anchors", "Broad Transcript Mentions", "Minimum Review Action", "Stronger Proof Needed", "Transcript Evidence vs Scientific Proof", "Transcript Can Support", "Transcript Cannot Support", "Stronger Validation Needed", "First Overclaim To Reject", "Reviewer Action", "Transcript Support", "What This Evidence Does Not Prove", "Review Links"),
        "site/topics/physics-informed-neural-networks.html": ("Big Picture Claim Chain", "Before The Math Slow Walk", "Say It Without Jargon", "What We Have", "What We Need", "Why The Idea Enters", "What To Try First", "Stop Trusting It When", "Everyday Problem", "Decision Or Quantity At Stake", "Hidden Thing Needed", "First Thing That Can Break The Claim", "End-To-End Use Protocol", "State The Scientific Job", "Name The Decision Quantity", "Inventory The Evidence", "Choose The Mathematical Carrier", "Build The Smallest Working Case", "Run The Changed-Case Test", "Reject Or Narrow The Claim When", "Final Claim Allowed", "Teach It From Zero", "Start With A Person", "What They Can See", "What They Cannot See Yet", "The First-Principles Move", "Where Shape Or Topology Enters", "Where People Use It", "End With The Claim", "Application Claim Ladder", "Application Field", "Evidence To Start From", "Hidden Answer Needed", "Changed Case That Tests It", "Plain Question To Answer Script", "Real question", "Evidence sentence", "Missing-answer sentence", "Shape or topology sentence", "Allowed-answer sentence", "Stop sentence", "What I Know And What I Still Test", "What I Know", "Evidence I Can Point To", "Answer I Still Need", "Move That Tries To Get There", "Shape Or Topology I Must Not Lose", "Claim I Can Say Carefully", "Test Still Needed", "Stop Or Narrow When", "Why The Failure Matters", "Missing Piece", "What Can Go Wrong", "Engineering Consequence", "Materials Or Biology Consequence", "Climate Or Field Consequence", "Smallest Prevention", "Slow Bridge From Problem To Shape", "Everyday Shortage", "Answer Type Needed", "Evidence Carrier", "Why A Single Number Is Not Enough", "Smallest Honest Shape", "What Would Make The Shape Too Weak", "Plain Big Picture Essay", "Why This Matters Slowly", "Topology and shape matter here", "The reader should leave this section with one plain sentence", "Applications In Everyday Words", "Topology and shape", "Engineering design", "Materials, chemistry, and biology", "Climate, fluids, and fields", "First-Principles Essay", "What A Strong Explanation Must Say", "One Concrete Case From Start To Finish", "Observed Evidence", "Rejection Test", "Course Role In Plain Words", "Why It Appears Here", "Read Before This", "What It Unlocks Later", "Confusion This Prevents", "Plain Course Sentence", "How This Connects To Nearby Ideas", "Learn Before This", "Confusion It Prevents", "Evidence Needed To Believe This", "Strong Evidence", "Too Weak", "Reject Or Recheck When", "Where This Fits By Domain", "When To Avoid This In A Domain", "Changed-Case Test", "Plain Formula Term By Term", "What It Carries", "Concrete Worked Example", "Concrete Wrong-Use Example", "Test That Catches It", "What Breaks Without This Idea", "Minimum Proof Needed", "Reader Must Be Able To Say", "Say It Back Check", "Real Problem", "Evidence I Have", "Answer I Need", "Shape Or Topology Issue", "Claim I Am Allowed To Make", "Misread Repair Drill", "Likely Misread", "Why That Sounds Tempting", "Plain Repair", "Evidence To Name Before Trusting It", "Changed Case That Repairs The Overclaim", "One Sentence To Keep", "Plain-Language Audit", "Do Not Say", "Say Instead", "Rewrite Test", "Acceptance Sentence Filled", "I would test it by changing", "Selected Source Anchors", "Claim Anchored", "Limit:"),
        "site/evidence-packets/foundation-models-for-pdes.html": ("Selected Source Anchors", "Claim Anchored", "Limit:"),
        "site/derivations.html": ("Core Derivations",),
        "site/derivations/physics-informed-neural-networks.html": ("Hand Derivation", "Why It Enters", "Final Line", "Why This Shape And Not Another", "Observed Burden", "Rejection Burden", "Smallest Useful Formula", "First Wrong Simplification"),
        "site/derivations/operator-learning.html": ("Hand Derivation", "Why It Enters", "Final Line", "Why This Shape And Not Another", "Observed Burden", "Rejection Burden", "Smallest Useful Formula", "First Wrong Simplification"),
        "site/derivations/foundation-models-for-pdes.html": ("Hand Derivation", "Why It Enters", "Final Line", "Why This Shape And Not Another", "Observed Burden", "Rejection Burden"),
        "site/wording-audit.html": ("Wording Audit", "Severity", "Replacement Test", "Current Pages"),
        "site/provenance/cross-channel-playbook.html": ("Cross-Channel Replication Playbook", "Process", "Checks"),
        "site/worked-examples/molecule-property-from-structure.html": ("First-Principles Story", "End-To-End Flow", "Claim Boundary", "Example Stress Test", "Method Route Under Test", "Passes Only If"),
        "site/worked-examples/foundation-pde-model-on-new-equation.html": ("First-Principles Story", "End-To-End Flow", "Claim Boundary", "Example Stress Test", "Method Route Under Test", "Passes Only If"),
        "site/worked-examples/fast-fluid-field-surrogate.html": ("First-Principles Story", "End-To-End Flow", "Claim Boundary", "Example Stress Test", "Changed Case To Try", "Passes Only If"),
        "site/domains/chemistry-and-biology.html": ("Walk The Domain From Scratch", "How The Methods Enter Without Jargon", "Concrete Scientific Job", "Observed Evidence", "Changed-Case Test", "Domain Stress Test", "Quantity At Risk", "Concepts Under Pressure"),
        "site/domains/materials-and-mechanics.html": ("Walk The Domain From Scratch", "How The Methods Enter Without Jargon", "Concrete Scientific Job", "Hidden Quantity", "Decision", "Domain Stress Test", "Quantity At Risk", "Concepts Under Pressure"),
        "site/domains/fluids-and-flow.html": ("Walk The Domain From Scratch", "How The Methods Enter Without Jargon", "Concrete Scientific Job", "Changed-Case Test", "Domain Stress Test", "What Must Still Hold", "Concepts Under Pressure"),
    }
    errors: list[str] = []
    for rel_path, terms in required.items():
        path = ROOT / rel_path
        if not path.exists():
            errors.append(f"missing required page: {rel_path}")
            continue
        text = path.read_text(encoding="utf-8")
        for term in terms:
            if term not in text:
                errors.append(f"{rel_path}: missing section text: {term}")
    return errors


def check_restricted_words(paths: list[Path]) -> list[str]:
    errors: list[str] = []
    pattern = re.compile("|".join(re.escape(item) for item in RESTRICTED_PATTERNS), re.IGNORECASE)
    for path in paths:
        if path.relative_to(ROOT).as_posix() == "site/wording-audit.html":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in pattern.finditer(text):
            line_no = text.count("\n", 0, match.start()) + 1
            errors.append(f"{path.relative_to(ROOT)}:{line_no}: restricted wording: {match.group(0)}")
    return errors


def check_source_anchor_coverage() -> list[str]:
    errors: list[str] = []
    concepts_path = ANALYSIS / "concept_atlas.json"
    concepts = json.loads(concepts_path.read_text(encoding="utf-8"))
    for concept in concepts:
        slug = str(concept["slug"])
        for rel_path in (f"site/topics/{slug}.html", f"site/evidence-packets/{slug}.html"):
            path = ROOT / rel_path
            if not path.exists():
                errors.append(f"missing source-anchor page: {rel_path}")
                continue
            text = path.read_text(encoding="utf-8")
            if "Selected Source Anchors" not in text or text.count("Claim Anchored") < 2:
                errors.append(f"{rel_path}: expected at least two selected source anchors")
    return errors


def check_evidence_packet_proof_boundaries() -> list[str]:
    errors: list[str] = []
    packets = json.loads((ANALYSIS / "concept_evidence_packets.json").read_text(encoding="utf-8"))
    required_fields = (
        "transcript_can_support",
        "transcript_cannot_support",
        "stronger_validation_needed",
        "first_overclaim_to_reject",
        "reviewer_action",
    )
    required_terms = (
        "Transcript Evidence vs Scientific Proof",
        "Transcript Can Support",
        "Transcript Cannot Support",
        "Stronger Validation Needed",
        "First Overclaim To Reject",
        "Reviewer Action",
    )
    for packet in packets:
        title = str(packet.get("title") or packet.get("slug") or "untitled packet")
        boundary = packet.get("proof_boundary") or {}
        for field in required_fields:
            if not boundary.get(field):
                errors.append(f"evidence packet missing proof_boundary.{field}: {title}")
        href = str(packet.get("packet_href") or "")
        if not href:
            errors.append(f"evidence packet missing packet_href: {title}")
            continue
        path = ROOT / "site" / href.removeprefix("site/")
        if not path.exists():
            errors.append(f"missing evidence packet page: {href}")
            continue
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                errors.append(f"{path.relative_to(ROOT)}: missing proof-boundary term: {term}")
    return errors


def check_reader_check_coverage() -> list[str]:
    errors: list[str] = []
    concepts = json.loads((ANALYSIS / "concept_atlas.json").read_text(encoding="utf-8"))
    checks = json.loads((ANALYSIS / "reader_checks.json").read_text(encoding="utf-8"))
    check_by_slug = {str(check["topic_slug"]): check for check in checks}
    if len(check_by_slug) != len(concepts):
        errors.append(f"expected reader checks for {len(concepts)} concepts, found {len(check_by_slug)}")
    for concept in concepts:
        slug = str(concept["slug"])
        check = check_by_slug.get(slug)
        if not check:
            errors.append(f"missing reader check for concept: {slug}")
            continue
        topic_path = ROOT / f"site/topics/{slug}.html"
        check_path = ROOT / f"site/reader-checks/{check['slug']}.html"
        if not topic_path.exists():
            errors.append(f"missing reader-check topic page: site/topics/{slug}.html")
        else:
            topic_text = topic_path.read_text(encoding="utf-8")
            if "Reader Check" not in topic_text or str(check["title"]) not in topic_text or "Weak answer warning" not in topic_text:
                errors.append(f"site/topics/{slug}.html: embedded reader check missing")
        if not check_path.exists():
            errors.append(f"missing reader-check page: site/reader-checks/{check['slug']}.html")
        else:
            check_text = check_path.read_text(encoding="utf-8")
            if "Strong Answer Should Say" not in check_text or "Strong Answer Broken Into Parts" not in check_text or "Reader Must Say" not in check_text or "Weak If" not in check_text or "Weak Answer Warning" not in check_text:
                errors.append(f"site/reader-checks/{check['slug']}.html: reader check content missing")
        if len(check.get("answer_parts") or []) < 5:
            errors.append(f"reader check missing answer parts: {check['slug']}")
    return errors


def check_meaty_goal_coverage() -> list[str]:
    errors: list[str] = []
    concepts = json.loads((ANALYSIS / "concept_atlas.json").read_text(encoding="utf-8"))
    rows = json.loads((ANALYSIS / "meaty_goal_coverage.json").read_text(encoding="utf-8"))
    if len(rows) != len(concepts):
        errors.append(f"expected meaty goal coverage for {len(concepts)} concepts, found {len(rows)}")
    for row in rows:
        title = str(row.get("title"))
        if row.get("missing"):
            errors.append(f"meaty goal coverage has missing items: {title} -> {row.get('missing')}")
        if len(row.get("requirements") or []) != MEATY_GOAL_REQUIREMENT_COUNT:
            errors.append(f"meaty goal coverage requirement count mismatch: {title}")
        for href_field in ("topic_href", "evidence_packet_href", "reader_check_href"):
            href = str(row.get(href_field) or "")
            if not href:
                errors.append(f"meaty goal coverage missing {href_field}: {title}")
                continue
            if not (SITE / href).exists():
                errors.append(f"meaty goal coverage link missing: {title} -> {href}")
    return errors


def check_topic_shape_depth() -> list[str]:
    errors: list[str] = []
    concepts = json.loads((ANALYSIS / "concept_atlas.json").read_text(encoding="utf-8"))
    required_terms = (
        "Big Picture Claim Chain",
        "Before The Math Slow Walk",
        "Say It Without Jargon",
        "What We Have",
        "What We Need",
        "Why The Idea Enters",
        "What To Try First",
        "Stop Trusting It When",
        "Everyday Problem",
        "Domain Where It Matters",
        "Decision Or Quantity At Stake",
        "Evidence In Hand",
        "Hidden Thing Needed",
        "Mathematical Move",
        "First Thing That Can Break The Claim",
        "Changed Case To Try First",
        "Explanation Order Matters",
        "Start With The Problem",
        "Why This Must Come First",
        "Then Name The Evidence",
        "Why Evidence Comes Before The Move",
        "Then Name The Missing Answer",
        "Why The Missing Answer Comes Before Math",
        "Then Make The Plain Move",
        "Why The Move Comes Before The Claim",
        "Then Check Shape And Field Use",
        "Why Shape Comes Before Trust",
        "End With The Test",
        "Why The Test Comes Last",
        "Order Pass Test",
        "Why Care Before Any Technical Term",
        "Real Work At Risk",
        "Answer The Person Still Needs",
        "Topology Or Shape Reason",
        "Engineering Reason",
        "Materials Biology Or Chemistry Reason",
        "Climate Fluid Or Field Reason",
        "Plain Importance Test",
        "Workday Decision Rehearsal",
        "Morning Job",
        "First Thing They Write Down",
        "Question They Cannot Answer Yet",
        "Decision Waiting On The Answer",
        "Shape They Must Not Flatten",
        "Plain Move They Try Before Lunch",
        "End Of Day Claim",
        "Next Morning Recheck",
        "Rehearsal Pass Test",
        "Sounds-Right Filter",
        "Sounds Right But Is Weak",
        "Why Someone Might Believe It",
        "Evidence It Must Name Instead",
        "Missing Answer It Must Name Instead",
        "Plain Move It Must Explain",
        "Shape It Must Protect",
        "Field Use It Must Ground",
        "First Test It Must Survive",
        "Filter Pass Test",
        "Draw Before Math",
        "Box One: Problem",
        "Box Two: Evidence",
        "Box Three: Missing Answer",
        "Arrow: Plain Move",
        "Shape Mark",
        "Engineering Mark",
        "Field Mark",
        "Break Mark",
        "Claim Under The Drawing",
        "Drawing Pass Test",
        "Start-Here Gate",
        "Open This Topic When",
        "Evidence Signal",
        "Missing-Answer Signal",
        "Shape Or Topology Signal",
        "Read This First If Needed",
        "Why This Page Is The Right Stop",
        "Next Page To Open After This",
        "Do Not Start Here When",
        "Start-Here Rejection Test",
        "Gate Pass Test",
        "Skeptical Reader Proof",
        "Question A Skeptic Asks",
        "Evidence A Skeptic Needs",
        "Missing Answer They Watch",
        "Move They Must See",
        "Shape Check They Need",
        "Engineering Check They Need",
        "Field Check They Need",
        "What The Page Can Support",
        "What The Page Cannot Support",
        "First Test Before Belief",
        "Belief Pass Test",
        "Oral Explanation Script",
        "Sentence One: Everyday Need",
        "Sentence Two: Evidence In Hand",
        "Sentence Three: Missing Answer",
        "Sentence Four: Plain Move",
        "Sentence Five: Shape Or Topology",
        "Sentence Six: Field Transfer",
        "Sentence Seven: Careful Claim",
        "Sentence Eight: Belief Test",
        "Spoken Pass Test",
        "Before-After Decision Check",
        "Before Learning This",
        "After Learning This",
        "Decision They Can Now Make",
        "Shape Decision That Changes",
        "Engineering Decision That Changes",
        "Lab Or Biology Decision That Changes",
        "Field Decision That Changes",
        "Claim They Can Now Say",
        "Decision They Must Still Refuse",
        "Changed Case That Decides",
        "Before-After Pass Test",
        "Outside-Classroom Use Map",
        "Real-World Shortage",
        "Evidence That Travels Outside Class",
        "Missing Answer Outside Class",
        "Engineering Use Outside Class",
        "Lab Materials Or Biology Use Outside Class",
        "Climate Fluid Or Field Use Outside Class",
        "Topology Shape Use Outside Class",
        "Claim Allowed Outside Class",
        "Use Must Stop Outside Class When",
        "First Outside-Classroom Test",
        "Outside-Classroom Pass Test",
        "Learner Notebook Note",
        "Notebook Line: Problem",
        "Notebook Line: Evidence",
        "Notebook Line: Missing Answer",
        "Notebook Line: Move",
        "Notebook Line: Shape",
        "Notebook Line: Field Use",
        "Notebook Line: Allowed Claim",
        "Notebook Line: Stop Test",
        "Notebook Pass Test",
        "Tiny Invented Case Recipe",
        "Invent A Small Setting",
        "Name One Thing Seen",
        "Name One Thing Missing",
        "Name The Small Move",
        "Add One Shape Detail",
        "Add One Engineering Detail",
        "Add One Field Detail",
        "Say The Small Claim",
        "Change One Thing To Test It",
        "Invented Case Pass Test",
        "End-To-End Use Protocol",
        "State The Scientific Job",
        "Name The Decision Quantity",
        "Inventory The Evidence",
        "Choose The Mathematical Carrier",
        "Build The Smallest Working Case",
        "Run The Changed-Case Test",
        "Reject Or Narrow The Claim When",
        "Final Claim Allowed",
        "Teach It From Zero",
        "Start With A Person",
        "What They Can See",
        "What They Cannot See Yet",
        "The First-Principles Move",
        "Where Shape Or Topology Enters",
        "Where People Use It",
        "End With The Claim",
        "Application Claim Ladder",
        "Application Field",
        "Evidence To Start From",
        "Hidden Answer Needed",
        "Changed Case That Tests It",
        "Everyday Field Decision Story",
        "Decision Being Made",
        "Evidence On The Table",
        "Missing Answer For The Decision",
        "Plain Move That Connects Them",
        "Shape Issue Inside The Decision",
        "Engineering Decision Use",
        "Materials Or Biology Decision Use",
        "Climate Or Field Decision Use",
        "Concrete Decision Picture",
        "Decision Claim Allowed",
        "Decision Must Stop When",
        "Decision Story Pass Test",
        "Field Mini Cases In Plain Words",
        "Topology And Shape Mini Case",
        "Engineering Mini Case",
        "Materials Or Biology Mini Case",
        "Climate Or Field Mini Case",
        "What They Can See",
        "What They Need",
        "How The Topic Helps",
        "What The Math Is Doing",
        "Why This Matters In The Field",
        "First Check",
        "From Scratch Story In Plain Words",
        "The evidence in hand is",
        "The hidden side is",
        "The first-principles move is this",
        "Shape and topology enter",
        "The same idea also has to make sense",
        "A concrete case makes the story honest",
        "The plain ending is this",
        "No-Jargon Translation For This Topic",
        "Course Phrase",
        "Page Wording",
        "Everyday Meaning",
        "Reader Question",
        "Topic Name",
        "Hidden Answer",
        "Math Move",
        "Trust Boundary",
        "Everyday Vocabulary Bridge",
        "Word Job",
        "Page Words",
        "Everyday Words",
        "Check Question",
        "Object Word",
        "Evidence Word",
        "Missing-Answer Word",
        "Action Word",
        "Shape Word",
        "Decision Word",
        "Trust Word",
        "Vocabulary Pass Test",
        "Plain Retell Drill",
        "Start With The Shortage",
        "Name The Evidence",
        "Name The Hidden Answer",
        "Say The First-Principles Move",
        "Bring In Shape Or Topology",
        "Ground It In One Case",
        "State The Useful Answer",
        "Name The Trust Boundary",
        "End With A Changed Case",
        "Filled Retell Answer",
        "Retell Pass Test",
        "Field Transfer Check In Plain Words",
        "Field Where It Moves",
        "What Changes In The World",
        "Evidence That Still Starts It",
        "Hidden Answer That Still Matters",
        "Changed Case That Travels",
        "Same Chain Across Fields",
        "Transfer Pass Test",
        "New Case Transfer Rehearsal",
        "Original Case",
        "Original Evidence",
        "Original Missing Answer",
        "New Case To Try",
        "Evidence That Must Still Be Named",
        "Missing Answer In The New Case",
        "Move That Should Stay The Same",
        "Shape Or Boundary That May Change",
        "Claim Allowed After Transfer",
        "First Transfer Rejection Signal",
        "Transfer Rehearsal Pass Test",
        "Wrong Path To Right Path Repair",
        "Tempting Wrong Path",
        "Why A Learner Might Say It",
        "Missing First-Principles Piece",
        "Repair Step One",
        "Repair Step Two",
        "Repair Step Three",
        "Repaired Plain Claim",
        "Check That Proves The Repair",
        "Repair Pass Test",
        "Confusion To Clarity Story",
        "Confusing First Thought",
        "Why It Feels Reasonable",
        "Missing Everyday Question",
        "Clear Starting Evidence",
        "Clear Missing Answer",
        "Clear First-Principles Move",
        "Shape Check That Keeps It Honest",
        "Clear Claim",
        "Clarity Breaks When",
        "Clarity Pass Test",
        "Use Or Refuse Gate In Plain Words",
        "Use It When",
        "Narrow It When",
        "Refuse It When",
        "Evidence Required Before Use",
        "Hidden Answer Required Before Use",
        "First Changed Case Required",
        "Plain Final Decision",
        "Refusal Pass Test",
        "Final Learner Proof In Plain Words",
        "Problem Proof",
        "Evidence Proof",
        "Hidden-Answer Proof",
        "Move Proof",
        "Shape Proof",
        "Case Proof",
        "Use Proof",
        "Refusal Proof",
        "Accepted Final Answer",
        "Final Proof Pass Test",
        "Teach Someone Else Handoff",
        "First Sentence",
        "What They Can Point To",
        "What They Still Need",
        "Plain Move To Say Out Loud",
        "Shape Or Topology Line",
        "One Field Use",
        "Careful Ending",
        "Stop Teaching It As True When",
        "Full Handoff In Plain Words",
        "Handoff Pass Test",
        "Topology And Shape Story In Plain Words",
        "Everyday Meaning Of Shape",
        "Why It Enters This Topic",
        "Relation To Preserve",
        "Field Where The Relation Matters",
        "Concrete Picture",
        "Changed Shape To Try",
        "Claim After The Shape Check",
        "Shape Story Pass Test",
        "One-Page Mental Model",
        "Need",
        "Evidence",
        "Missing Answer",
        "Plain Move",
        "Shape To Keep",
        "Field Reason",
        "Allowed Claim",
        "First Test",
        "Stop Point",
        "Mental Model Pass Test",
        "Next-Day Memory Check",
        "Remember The Need",
        "Remember The Evidence",
        "Remember The Missing Answer",
        "Remember The Move",
        "Remember The Shape Issue",
        "Remember One Case",
        "Remember The First Check",
        "Remember When To Stop",
        "One-Minute Memory Answer",
        "Memory Pass Test",
        "Nearby Topic Comparison In Plain Words",
        "Compare With Earlier Idea",
        "Earlier Idea Job",
        "This Topic Job",
        "Compare With Later Idea",
        "Later Idea Job",
        "Difference In One Sentence",
        "Comparison Failure Test",
        "Nearby Comparison Pass Test",
        "Plain Question To Answer Script",
        "Real question",
        "Evidence sentence",
        "Missing-answer sentence",
        "Shape or topology sentence",
        "Allowed-answer sentence",
        "Stop sentence",
        "What I Know And What I Still Test",
        "What I Know",
        "Evidence I Can Point To",
        "Answer I Still Need",
        "Move That Tries To Get There",
        "Shape Or Topology I Must Not Lose",
        "Claim I Can Say Carefully",
        "Test Still Needed",
        "Stop Or Narrow When",
        "Why The Failure Matters",
        "Missing Piece",
        "What Can Go Wrong",
        "Engineering Consequence",
        "Materials Or Biology Consequence",
        "Climate Or Field Consequence",
        "Smallest Prevention",
        "Slow Bridge From Problem To Shape",
        "Everyday Shortage",
        "Answer Type Needed",
        "Evidence Carrier",
        "Why A Single Number Is Not Enough",
        "Smallest Honest Shape",
        "What Would Make The Shape Too Weak",
        "Plain Big Picture Essay",
        "Why This Matters Slowly",
        "Topology and shape matter here",
        "The reader should leave this section with one plain sentence",
        "Applications In Everyday Words",
        "Topology and shape",
        "Engineering design",
        "Materials, chemistry, and biology",
        "Climate, fluids, and fields",
        "Long Everyday Importance Essay",
        "Why The Topic Has To Exist",
        "First-Principles Reason In Plain Words",
        "Topology And Shape In Real Work",
        "Applications Beyond The Course",
        "Why This Is Important",
        "First-Principles Walkthrough",
        "Course Role In Plain Words",
        "Why It Appears Here",
        "Read Before This",
        "What It Unlocks Later",
        "Confusion This Prevents",
        "Plain Course Sentence",
        "Course Bridge In Plain Words",
        "What The Reader Should Already Have",
        "What This Topic Adds To The Course",
        "What Later Pages Can Now Use",
        "Why This Link Matters",
        "Confusion This Bridge Prevents",
        "Whole Course Sentence",
        "Bridge Pass Test",
        "Why This Shape Follows",
        "Why It Has To Be There",
        "What Breaks Without It",
        "Plain final line",
        "Smallest useful formula",
        "First wrong simplification",
        "Everyday Math Shape Rehearsal",
        "Start Object",
        "Missing Object",
        "Carry Step",
        "Formula Path In Plain Words",
        "What The Shape Allows",
        "What The Shape Must Not Hide",
        "Check The Shape",
        "Shape Rehearsal Pass Test",
        "Source-To-Claim Boundary In Plain Words",
        "Course Evidence Can Support",
        "Course Evidence Cannot Prove",
        "Claim Allowed On This Page",
        "Stronger Field Evidence Needed",
        "First Overclaim To Reject",
        "Reviewer Action",
        "Boundary Pass Test",
        "Plain Formula Term By Term",
        "Say It Back Check",
        "Real Problem",
        "Evidence I Have",
        "Answer I Need",
        "Move I Am Making",
        "Shape Or Topology Issue",
        "Claim I Am Allowed To Make",
        "Reader Mistake Audit",
        "Mistake To Look For",
        "What The Mistake Sounds Like",
        "Plain Repair Required",
        "Name-First Mistake",
        "Evidence Gap",
        "Missing-Answer Gap",
        "Move Gap",
        "Shape Gap",
        "Overclaim Gap",
        "Test Gap",
        "Likely Wrong Shortcut",
        "Mistake Audit Pass Test",
        "Misread Repair Drill",
        "Likely Misread",
        "Why That Sounds Tempting",
        "Plain Repair",
        "Evidence To Name Before Trusting It",
        "Changed Case That Repairs The Overclaim",
        "One Sentence To Keep",
        "Plain-Language Audit",
        "Do Not Say",
        "Say Instead",
        "Evidence Words Required",
        "Rewrite Test",
    )
    for concept in concepts:
        slug = str(concept["slug"])
        path = ROOT / f"site/topics/{slug}.html"
        if not path.exists():
            errors.append(f"missing topic page for shape-depth check: site/topics/{slug}.html")
            continue
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                errors.append(f"site/topics/{slug}.html: missing shape-depth term: {term}")
        if "Ask what stays connected, what has a hole, what touches what, and what can bend without changing the real question." in text:
            errors.append(f"site/topics/{slug}.html: plain applications still use the old shared topology wording")
    return errors


def check_decision_guide_depth() -> list[str]:
    errors: list[str] = []
    decisions = json.loads((ANALYSIS / "decision_guides.json").read_text(encoding="utf-8"))
    required_terms = (
        "Best Starting Point",
        "Decision Burden From First Principles",
        "Observed Evidence",
        "Hidden Need",
        "Why This Starting Point Earns Its Place",
        "First Rejection Test",
        "Choice Must Fail If",
        "Evidence Needed",
    )
    for decision in decisions:
        slug = str(decision["slug"])
        burden = decision.get("decision_burden") or {}
        for field in ("shortage", "observed", "hidden", "move", "carries", "rejection"):
            if not burden.get(field):
                errors.append(f"decision guide missing decision_burden.{field}: {slug}")
        path = ROOT / f"site/decision-guide/{slug}.html"
        if not path.exists():
            errors.append(f"missing decision guide page: site/decision-guide/{slug}.html")
            continue
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                errors.append(f"site/decision-guide/{slug}.html: missing decision-depth term: {term}")
    return errors


def check_domain_guide_depth() -> list[str]:
    errors: list[str] = []
    guides = json.loads((ANALYSIS / "domain_guides.json").read_text(encoding="utf-8"))
    required_terms = (
        "Walk The Domain From Scratch",
        "Concrete Scientific Job",
        "What Each Concept Must Carry In This Domain",
        "Domain Job It Handles",
        "Evidence It Uses",
        "What It Carries",
        "Domain Failure",
        "Domain Stress Test",
    )
    for guide in guides:
        slug = str(guide["slug"])
        burdens = guide.get("concept_burdens") or []
        if len(burdens) != len(guide.get("concepts") or []):
            errors.append(f"domain guide concept burden count mismatch: {slug}")
        for item in burdens:
            for field in ("slug", "name", "domain_job", "evidence_it_uses", "what_it_carries", "domain_failure"):
                if not item.get(field):
                    errors.append(f"domain guide missing concept_burdens.{field}: {slug}")
        path = ROOT / f"site/domains/{slug}.html"
        if not path.exists():
            errors.append(f"missing domain guide page: site/domains/{slug}.html")
            continue
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                errors.append(f"site/domains/{slug}.html: missing domain-depth term: {term}")
    return errors


def validate() -> None:
    manifest_path = SITE / "page-manifest.json"
    if not manifest_path.exists():
        raise SystemExit("missing site/page-manifest.json")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(manifest, list):
        raise SystemExit("site/page-manifest.json is not a list")

    errors: list[str] = []
    manifest_set = set(manifest)
    for page in REQUIRED_ROOT_PAGES:
        if f"site/{page}" not in manifest_set:
            errors.append(f"required root page missing from manifest: {page}")
    for item in manifest:
        path = ROOT / item
        if not path.exists():
            errors.append(f"manifest points to missing file: {item}")
        elif path.suffix != ".html":
            errors.append(f"manifest item is not html: {item}")

    summary_path = ANALYSIS / "summary.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    if summary.get("video_count") != 40:
        errors.append(f"expected 40 videos, found {summary.get('video_count')}")
    if summary.get("concept_count") != 14:
        errors.append(f"expected 14 concepts, found {summary.get('concept_count')}")
    if len(manifest) != 232:
        errors.append(f"expected 232 pages, found {len(manifest)}")

    errors.extend(check_internal_links(manifest))
    errors.extend(check_required_sections())
    errors.extend(check_source_anchor_coverage())
    errors.extend(check_evidence_packet_proof_boundaries())
    errors.extend(check_reader_check_coverage())
    errors.extend(check_meaty_goal_coverage())
    errors.extend(check_topic_shape_depth())
    errors.extend(check_decision_guide_depth())
    errors.extend(check_domain_guide_depth())

    scan_paths = [ROOT / "README.md", ROOT / "exports/research-package.md"]
    scan_paths.extend((ROOT / item) for item in manifest)
    errors.extend(check_restricted_words(scan_paths))

    if errors:
        for error in errors:
            print(error)
        raise SystemExit(f"generated site validation failed: {len(errors)} issue(s)")

    print(f"generated site validation ok: {len(manifest)} pages, {summary['video_count']} videos, {summary['concept_count']} concepts")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.parse_args()
    validate()


if __name__ == "__main__":
    main()
