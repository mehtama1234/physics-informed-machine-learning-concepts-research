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
    "learning-path.html",
    "glossary.html",
    "domains.html",
    "reader-checks.html",
    "decision-guide.html",
    "provenance.html",
    "coverage.html",
    "dependencies.html",
    "concept-ladder.html",
    "evidence-packets.html",
    "quality.html",
    "synthesis.html",
    "review-entrypoints.html",
    "review-search.html",
    "editorial-roadmap.html",
    "completion-audit.html",
    "meaty-goal.html",
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
)


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
        "site/handoff.html": ("Start Here", "Remote Verification Commands", "git push -u origin main", "Remaining Editorial Work"),
        "site/coverage.html": ("Coverage Matrix", "Reader Check"),
        "site/synthesis.html": ("Field Synthesis",),
        "site/quality.html": ("Editorial Quality Rubric",),
        "site/provenance.html": ("Provenance And Reproduction",),
        "site/decision-guide.html": ("Decision Guide",),
        "site/reader-checks.html": ("Reader Checks",),
        "site/review-entrypoints.html": ("Review Entrypoints", "End-To-End Test"),
        "site/review-search.html": ("Find Pages By Question", "Review Rule"),
        "site/editorial-roadmap.html": ("Editorial Roadmap", "Status:", "Current Evidence", "Acceptance Check", "locally completed", "Meaty End-To-End Goal"),
        "site/completion-audit.html": ("Completion Audit", "Requirement Evidence", "locally verified"),
        "site/meaty-goal.html": ("Meaty End-To-End Goal", "Done Means", "Every Core Page Must Contain", "Acceptance Sentence", "Not Done If"),
        "site/diagrams.html": ("Mathematical Sketches", "Kept Rule", "Failure Case"),
        "site/topics/operator-learning.html": ("Mathematical Sketch", "Field To Field", "Kept Rule"),
        "site/topics/surrogate-modeling.html": ("Mathematical Sketch", "Fast Stand-In", "Failure Case"),
        "site/comparisons/pinns-vs-neural-operators.html": ("How To Decide From First Principles", "Decision Checklist", "Concrete Choice Cases", "Wrong Choice Case", "Evidence That Exposes It"),
        "site/comparisons/solvers-vs-learned-surrogates.html": ("How To Decide From First Principles", "Decision Checklist", "Concrete Choice Cases", "Wrong Choice Case", "Evidence That Exposes It"),
        "site/learning-path/scientific-question-first.html": ("No-Jargon Explanation", "First-Principles Spine", "World:", "Reject it when:"),
        "site/learning-path/physics-as-check.html": ("No-Jargon Explanation", "First-Principles Spine", "Mathematical move:", "Reject it when:"),
        "site/dependencies.html": ("Concept Dependency Map", "Confusion It Prevents"),
        "site/concept-ladder.html": ("Concept Ladder", "Mathematical Move", "Failure Test"),
        "site/evidence-packets.html": ("Concept Evidence Packets",),
        "site/formula-guide.html": ("Plain Formula Guide", "Common Misread", "What To Check"),
        "site/misconceptions.html": ("Misconception Map", "Wrong Turn", "First-Principles Test"),
        "site/evidence-packets/physics-informed-neural-networks.html": ("Transcript Support", "What This Evidence Does Not Prove", "Review Links"),
        "site/evidence-packets/operator-learning.html": ("Transcript Support", "What This Evidence Does Not Prove", "Review Links"),
        "site/topics/physics-informed-neural-networks.html": ("First-Principles Essay", "What A Strong Explanation Must Say", "Selected Source Anchors", "Claim Anchored", "Limit:"),
        "site/evidence-packets/foundation-models-for-pdes.html": ("Selected Source Anchors", "Claim Anchored", "Limit:"),
        "site/derivations.html": ("Core Derivations",),
        "site/derivations/physics-informed-neural-networks.html": ("Hand Derivation", "Why It Enters", "Final Line"),
        "site/derivations/operator-learning.html": ("Hand Derivation", "Why It Enters", "Final Line"),
        "site/derivations/foundation-models-for-pdes.html": ("Hand Derivation", "Why It Enters", "Final Line"),
        "site/provenance/cross-channel-playbook.html": ("Cross-Channel Replication Playbook", "Process", "Checks"),
        "site/worked-examples/molecule-property-from-structure.html": ("First-Principles Story", "End-To-End Flow", "Claim Boundary"),
        "site/worked-examples/foundation-pde-model-on-new-equation.html": ("First-Principles Story", "End-To-End Flow", "Claim Boundary"),
        "site/domains/chemistry-and-biology.html": ("Walk The Domain From Scratch", "How The Methods Enter Without Jargon", "Concrete Scientific Job", "Observed Evidence", "Changed-Case Test"),
        "site/domains/materials-and-mechanics.html": ("Walk The Domain From Scratch", "How The Methods Enter Without Jargon", "Concrete Scientific Job", "Hidden Quantity", "Decision"),
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
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in pattern.finditer(text):
            line_no = text.count("\n", 0, match.start()) + 1
            errors.append(f"{path.relative_to(ROOT)}:{line_no}: restricted wording: {match.group(0)}")
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
    if len(manifest) != 178:
        errors.append(f"expected 178 pages, found {len(manifest)}")

    errors.extend(check_internal_links(manifest))
    errors.extend(check_required_sections())

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
