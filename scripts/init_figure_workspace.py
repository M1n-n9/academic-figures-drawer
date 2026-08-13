#!/usr/bin/env python3
"""Create the evidence workspace used by academic-figures-drawer.

The command is intentionally conservative: it creates missing files and never
overwrites an existing brief, style contract, asset ledger, or defect log.
"""

from __future__ import annotations

import argparse
from pathlib import Path


TEMPLATES = {
    "brief.md": """# Diagram brief\n\n## User goal\n- Audience: \n- Output: editable `.drawio` plus: \n- Must communicate: \n- Must not do: \n\n## Source inventory\n| Source | Role (content/structure/style/layout/asset) | Notes |\n|---|---|---|\n| | | |\n\n## Requirement traceability\n| Requirement | Diagram evidence (panel/cell/edge) | Status |\n|---|---|---|\n\n## Semantic model\n- Input: \n- Stages: \n- Proposed contribution: \n- Output: \n- Training-only path: \n\n## Open assumptions\n- \n""",
    "visual-spec.md": """# Visual specification\n\n## Global style\n- Canvas/aspect: landscape, 1600–2200 × 850–1200 px\n- Font: Arial/Helvetica (Noto Sans CJK for Chinese)\n- Grid/margins: 8 px grid; 16–28 px outer margin\n- Corner radius / stroke: 10–16 px / 1.5–2 px\n- Arrow grammar: solid filled arrowhead for data; gray dashed for skip/feedback\n\n## Semantic palette\n| Meaning | Fill | Stroke | Used in |\n|---|---|---|---|\n| Input/raw signal/context | #E8F2F5 | #58727D | |\n| Existing/standard | #EAF0F6 | #63758A | |\n| Feature/tensor transform | #EDE9F4 | #7B6A9A | |\n| Training/task/output head | #F4EEDC | #9A7B3F | |\n| Proposed contribution | #F1D7D4 | #B44948 | |\n| Output/decision | #E5F1E3 | #5A8A55 | |\n\n## Typography\n- Panel/stage heading: 16–24 px, semibold\n- Module/body: 10–14 px\n- Tensor/equation note: 9–12 px\n\n## Composition notes\n- Overview: \n- Detail: \n- Legend: \n""",
    "layout-grid.md": """# Layout grid\n\n- Canvas: \n- Coordinate origin: \n- Major panels and bounding boxes: \n- Baselines / columns: \n- Repeated block size: \n- Forbidden crossing zones: titles, labels, equations, dense icon rows\n- Drawing order: background → containers → shapes → edges → labels → legend\n""",
    "asset-ledger.md": """# Asset ledger\n\n| Asset | Role | Source/provenance | Editable? | Decision |\n|---|---|---|---|---|\n| | input/context | | | |\n\nGenerated concept images are references unless explicitly approved as input/context assets. Do not embed a screenshot of the entire algorithm as the final figure.\n""",
    "defect-log.md": """# Defect log\n\n## Pass 0 — Plan review\n- Status: \n- Open risks: \n\n## Screenshot review cycles\n\n### Cycle 1\n- Screenshot (canvas-only): \n- P0/P1 inventory: \n- Fixes and verification: \n\n### Cycle 2\n- Screenshot (canvas-only): \n- P0/P1 inventory: \n- Fixes and verification: \n\n### Cycle 3\n- Screenshot (canvas-only): \n- P0/P1 inventory: \n- Fixes and verification: \n\n## Red-team audit\n- Text: \n- Arrows: \n- Boxes/overlap: \n- Spacing/layout: \n- Color/typography: \n- Icons/assets: \n- Semantics/regressions: \n\n## Self-score\n| Dimension | Score /10 | Evidence |\n|---|---:|---|\n| Text readability | | |\n| Arrow accuracy | | |\n| Color coherence | | |\n| Layout consistency | | |\n| Style/spec match | | |\n| **Total /50** | | |\n\n## Remaining gaps\n- \n""",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("out", type=Path, help="figure work directory to create")
    parser.add_argument("--title", default="Untitled research figure")
    args = parser.parse_args()

    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    created = []
    for name, body in TEMPLATES.items():
        path = out / name
        if path.exists():
            continue
        path.write_text(body.replace("Untitled research figure", args.title), encoding="utf-8")
        created.append(name)

    print(f"Workspace: {out}")
    print("Created: " + (", ".join(created) if created else "nothing (all files already existed)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
