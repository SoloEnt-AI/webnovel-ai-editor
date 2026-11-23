#!/usr/bin/env python3
"""Install this skill only. Never access credentials or change MCP configuration."""

import argparse
import shutil
import sys
from pathlib import Path


SKILL_NAME = "webnovel-ai-editor"
FILES = ("SKILL.md", "README.md", "LICENSE")
DIRECTORIES = ("agents", "config", "references", "scripts")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--client", required=True, choices=("codex", "claude"))
    parser.add_argument("--scope", default="project", choices=("project", "user"))
    parser.add_argument("--project", type=Path, help="Existing project directory; required for project scope")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.scope == "project":
        if args.project is None:
            parser.error("--project is required for project scope")
        base = args.project.expanduser().resolve()
        if not base.is_dir():
            parser.error("--project must be an existing directory")
    else:
        if args.project is not None:
            parser.error("--project cannot be used with --scope user")
        base = Path.home()

    root = Path(__file__).resolve().parent.parent
    subdirectory = ".agents" if args.client == "codex" else ".claude"
    target = base / subdirectory / "skills" / SKILL_NAME

    # A collision, including a broken symlink, is never an implicit update request.
    if target.exists() or target.is_symlink():
        parser.error("skill destination already exists; inspect it before updating")
    for name in FILES + DIRECTORIES:
        if not (root / name).exists():
            parser.error("source skill package is incomplete")
    if root == target.resolve() or root in target.resolve().parents:
        parser.error("destination must not be inside the source skill")

    print(f"{'Would install' if args.dry_run else 'Installing'} {SKILL_NAME}: {target}")
    if args.dry_run:
        print("No files changed. MCP configuration and credentials are separate.")
        return 0

    # Reserve the destination exclusively, preventing a concurrent install overwrite.
    target.parent.mkdir(parents=True, exist_ok=True)
    target.mkdir()
    for name in FILES:
        shutil.copy2(root / name, target / name)
    for name in DIRECTORIES:
        shutil.copytree(
            root / name,
            target / name,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"),
        )
    print("Skill installed. MCP has not been configured or tested.")
    print(f"Read setup instructions: {target / 'references' / 'setup.md'}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except OSError:
        # Do not dump paths or config contents from unexpected filesystem errors.
        print("Installation failed; check permissions and any partially created destination.", file=sys.stderr)
        sys.exit(1)
