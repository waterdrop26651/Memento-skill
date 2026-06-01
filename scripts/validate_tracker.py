#!/usr/bin/env python3
"""Validate an experiment tracker directory."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

REQUIRED_FILES = ("runs.csv", "contrasts.csv", "hypotheses.md")

RUN_REQUIRED_COLUMNS = {
    "run_id",
    "status",
    "date",
    "question_id",
    "hypothesis_id",
    "contrast_id",
    "role",
    "quality_flags",
    "notes",
}

CONTRAST_REQUIRED_COLUMNS = {
    "contrast_id",
    "question_id",
    "hypothesis_id",
    "status",
    "priority",
    "baseline_runs",
    "treatment_runs",
    "control_runs",
    "changed_axis",
    "controlled_axes",
    "prediction_direction",
    "predicted_min_delta",
    "predicted_reason",
    "actual_delta",
    "actual_result",
    "info_gain",
    "belief_update",
    "next_action",
    "risk",
    "decision",
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        return reader.fieldnames or [], rows


def split_ids(value: str) -> list[str]:
    if not value.strip():
        return []
    return [part.strip() for part in re.split(r"[,\|]", value) if part.strip()]


def error(message: str, errors: list[str]) -> None:
    errors.append(message)


def validate_runs(rows: list[dict[str, str]], errors: list[str]) -> set[str]:
    seen: set[str] = set()
    for index, row in enumerate(rows, start=2):
        run_id = row.get("run_id", "").strip()
        if not run_id:
            error(f"runs.csv:{index} missing run_id", errors)
            continue
        if run_id in seen:
            error(f"runs.csv:{index} duplicate run_id {run_id}", errors)
        seen.add(run_id)
        for key in ("question_id", "hypothesis_id", "contrast_id", "role", "status"):
            if not row.get(key, "").strip():
                error(f"runs.csv:{index} missing {key} for {run_id}", errors)
    return seen


def validate_contrasts(
    rows: list[dict[str, str]], run_ids: set[str], errors: list[str]
) -> set[str]:
    seen: set[str] = set()
    for index, row in enumerate(rows, start=2):
        contrast_id = row.get("contrast_id", "").strip()
        if not contrast_id:
            error(f"contrasts.csv:{index} missing contrast_id", errors)
            continue
        if contrast_id in seen:
            error(f"contrasts.csv:{index} duplicate contrast_id {contrast_id}", errors)
        seen.add(contrast_id)

        if not row.get("changed_axis", "").strip():
            error(f"contrasts.csv:{index} missing changed_axis for {contrast_id}", errors)

        status = row.get("status", "").strip()
        is_planned = status in {"planned", "queued", "running"}
        allows_future_runs = status in {"planned", "queued"}
        for key in ("prediction_direction", "predicted_min_delta", "predicted_reason"):
            if is_planned and not row.get(key, "").strip():
                error(f"contrasts.csv:{index} missing {key} for planned contrast {contrast_id}", errors)

        for field in ("baseline_runs", "treatment_runs", "control_runs"):
            for run_id in split_ids(row.get(field, "")):
                if allows_future_runs and field in {"treatment_runs", "control_runs"}:
                    continue
                if run_id in run_ids:
                    continue
                error(
                    f"contrasts.csv:{index} references unknown run_id {run_id} in {contrast_id}",
                    errors,
                )
    return seen


def validate_hypotheses(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for marker in ("Current belief:", "Evidence:", "Risk:", "Next most informative contrast:", "Update rule:"):
        if marker not in text:
            error(f"hypotheses.md missing marker: {marker}", errors)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_tracker.py <tracker_dir>", file=sys.stderr)
        return 2

    root = Path(sys.argv[1]).resolve()
    errors: list[str] = []

    for filename in REQUIRED_FILES:
        if not (root / filename).exists():
            error(f"missing required file: {filename}", errors)

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    run_fields, run_rows = read_csv(root / "runs.csv")
    contrast_fields, contrast_rows = read_csv(root / "contrasts.csv")

    for field in sorted(RUN_REQUIRED_COLUMNS - set(run_fields)):
        error(f"runs.csv missing required column: {field}", errors)
    for field in sorted(CONTRAST_REQUIRED_COLUMNS - set(contrast_fields)):
        error(f"contrasts.csv missing required column: {field}", errors)

    if not errors:
        run_ids = validate_runs(run_rows, errors)
        validate_contrasts(contrast_rows, run_ids, errors)
        validate_hypotheses(root / "hypotheses.md", errors)

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print("tracker validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
