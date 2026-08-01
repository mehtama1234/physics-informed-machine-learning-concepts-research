# Physics-Informed Machine Learning Concepts Research

Transcript-backed research package for the ETH Zurich AI in the Sciences and Engineering 2024 and 2025 playlists.

The purpose is not to summarize lectures. The purpose is to explain physics-informed machine learning from first principles: the problem each concept solves, the scientific domain it comes from, why the problem matters, what information the method keeps, what it leaves out, and how its claims can fail.

## Source Playlists

- ETH Zurich AI in the Sciences and Engineering 2025
- ETH Zurich AI in the Sciences and Engineering 2024

## Main Outputs

- `site/index.html`: package home page
- `site/transcripts.html`: 40-video transcript index
- `site/concept-atlas.html`: plain-language mathematical concept atlas
- `site/families.html`: paper-family routes through related concepts
- `site/comparisons.html`: plain-language comparisons between nearby methods
- `site/worked-examples.html`: 8 concrete scientific examples
- `site/diagrams.html`: visual flows for the main mathematical ideas
- `site/derivations.html`: core first-principles derivation walkthroughs
- `site/formula-guide.html`: plain-language guide to formula shapes
- `site/misconceptions.html`: core misconception map with plain corrections
- `site/learning-path.html`: step-by-step route through the field from first principles
- `site/glossary.html`: plain-language glossary for core terms
- `site/domains.html`: domain guides for real scientific settings
- `site/reader-checks.html`: self-check prompts for core ideas
- `site/decision-guide.html`: method choice guide from scientific situations
- `site/provenance.html`: source, extraction, build, and reproduction guide
- `site/provenance/cross-channel-playbook.html`: instructions for another CLI building a similar package
- `site/coverage.html`: concept coverage matrix across evidence and guide layers
- `site/dependencies.html`: concept dependency map for prerequisite ideas
- `site/concept-ladder.html`: first-principles concept ladder from evidence to failure test
- `site/evidence-packets.html`: per-concept source support and review links
- `site/quality.html`: editorial quality rubric for first-principles pages
- `site/synthesis.html`: field-level synthesis tying the concepts together
- `site/review-entrypoints.html`: end-to-end review route through the package
- `site/review-search.html`: reviewer-question index for finding the right page
- `site/editorial-roadmap.html`: prioritized roadmap for taking the first pass to hand-written depth
- `site/completion-audit.html`: requirement-by-requirement local completion evidence
- `site/handoff.html`: review route, validation commands, and remaining editorial work
- `site/theme-map.html`: recurring theme map
- `site/evidence-ledger.html`: transcript-backed evidence ledger
- `site/topics/`: first-principles concept pages
- `site/videos/`: per-video pages

## Data Layout

- `raw-material/playlists/`: playlist manifests
- `raw-material/metadata/`: per-video metadata from `yt-dlp`
- `raw-material/transcripts/`: raw VTT captions and clean transcript text
- `analysis/`: generated JSON research maps
- `exports/`: portable Markdown export
- `scripts/build_physics_informed_ml_research_package.py`: downloader, builder, and validator
- `scripts/validate_generated_site.py`: standalone generated-site link and content validator

## Commands

```bash
python3 scripts/build_physics_informed_ml_research_package.py --build --validate
python3 scripts/validate_generated_site.py
```

To refresh YouTube captions and metadata:

```bash
python3 scripts/build_physics_informed_ml_research_package.py --download --build --validate
```

To review locally:

```bash
python3 -m http.server 8022 --directory site
```

Then open:

```text
http://127.0.0.1:8022/index.html
```

## Current Coverage

- 2 playlists
- 40 videos
- 40 available transcripts
- concept atlas
- paper-family routes
- comparison pages
- 8 worked examples
- visual flow diagrams
- core derivation walkthroughs
- plain formula guide
- misconception map
- first-principles learning path
- plain-language glossary
- domain guides
- reader self-checks
- decision guide
- provenance and reproduction guide
- cross-channel replication playbook
- coverage matrix
- concept dependency map
- concept ladder
- concept evidence packets
- editorial quality rubric
- field synthesis
- review entrypoint map
- reviewer-question index
- editorial roadmap
- completion audit
- review handoff
- deep dives for core topics
- theme map
- evidence ledger
- per-topic and per-video pages
