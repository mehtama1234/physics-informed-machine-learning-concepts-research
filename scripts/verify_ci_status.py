#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OWNER = "mehtama1234"
REPO = "physics-informed-machine-learning-concepts-research"
WORKFLOW = "check.yml"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def main() -> int:
    head = git("rev-parse", "HEAD")
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows/{WORKFLOW}/runs?per_page=20"
    with urllib.request.urlopen(url, timeout=20) as response:
        data = json.load(response)

    runs = data.get("workflow_runs") or []
    match = next((run for run in runs if run.get("head_sha") == head), None)
    if not match:
        print(f"head: {head}")
        print(f"workflow: {WORKFLOW}")
        print("status: missing")
        print("No workflow run was found for the current local HEAD.")
        return 1

    status = str(match.get("status") or "")
    conclusion = str(match.get("conclusion") or "")
    html_url = str(match.get("html_url") or "")
    print(f"head: {head}")
    print(f"workflow: {WORKFLOW}")
    print(f"run: {html_url}")
    print(f"status: {status}")
    print(f"conclusion: {conclusion}")
    return 0 if status == "completed" and conclusion == "success" else 1


if __name__ == "__main__":
    sys.exit(main())
