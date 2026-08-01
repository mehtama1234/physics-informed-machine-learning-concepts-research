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

## Commands

```bash
python3 scripts/build_physics_informed_ml_research_package.py --build --validate
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
- theme map
- evidence ledger
- per-topic and per-video pages

