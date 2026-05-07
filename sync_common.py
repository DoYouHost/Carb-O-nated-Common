#!/usr/bin/env python3
"""
Sync shared .h files from DoYouHost.Carb-O-nated-Common into a project directory.

Usage:
    python3 sync_common.py                  # syncs to current working directory
    python3 sync_common.py <project_dir>    # syncs to specified directory
"""

import shutil
import sys
from pathlib import Path

SHARED_FILES = [
    "air_quality_levels.h",
    "translations.h",
    "display_helpers.h",
]

def main():
    common_dir = Path(__file__).parent.resolve()
    project_dir = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()

    if not project_dir.is_dir():
        print(f"Error: project directory not found: {project_dir}", file=sys.stderr)
        sys.exit(1)

    errors = []
    for filename in SHARED_FILES:
        src = common_dir / filename
        if not src.exists():
            errors.append(f"  missing in common: {filename}")
            continue
        dst = project_dir / filename
        shutil.copy2(src, dst)
        print(f"  synced  {filename}")

    if errors:
        print("\nErrors:", file=sys.stderr)
        for e in errors:
            print(e, file=sys.stderr)
        sys.exit(1)

    print(f"\nDone — synced {len(SHARED_FILES)} files to {project_dir}")

if __name__ == "__main__":
    main()
