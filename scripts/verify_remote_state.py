#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def main() -> int:
    branch = git("rev-parse", "--abbrev-ref", "HEAD")
    local = git("rev-parse", branch)
    remote_url = git("remote", "get-url", "origin")
    remote_line = git("ls-remote", "--heads", "origin", branch)
    remote = remote_line.split()[0] if remote_line else ""
    status = "match" if local == remote else "mismatch"

    print(f"branch: {branch}")
    print(f"origin: {remote_url}")
    print(f"local:  {local}")
    print(f"remote: {remote}")
    print(f"status: {status}")
    return 0 if status == "match" else 1


if __name__ == "__main__":
    sys.exit(main())
