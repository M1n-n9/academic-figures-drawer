# Research-figure visual contract

Use this contract when a paper or description has no usable style guide. It encodes the requested visual language: high information density with low reading burden.

## Composition

- Prefer a landscape canvas and a single dominant reading direction.
- Make the first screenful answer four questions in order: what enters, how it is transformed, where the new idea occurs, and what leaves.
- Use one overview row and at most one detail row. Keep stage counts small; merge routine operations into a named block.
- Reserve the strongest contrast, largest stroke, or accent tint for the proposed module. Existing modules should recede but remain legible.
- Use dashed group borders for semantic containers, not as decoration. A panel title is sufficient; avoid nested frames unless they show hierarchy.

## Shape and connector grammar

- Rounded rectangles represent modules; pale containers represent stages; small pills or cards represent tensor snapshots/annotations.
- Use a consistent 10–16 px corner radius, 1.5–2 px box/arrow stroke, and filled triangular arrowheads for the main data path.
- Use gray dashed arrows for skip/feedback/control relations. Use a short label on an edge only when the relation is not obvious.
- Keep edges outside boxes and labels. Route fan-in/fan-out with explicit ports or waypoints instead of stacked lines.
- Use ellipses/cylinders only when they denote a real input, memory, dataset, or output object.

## Color semantics

Use the palette table in `SKILL.md` consistently. Never assign a color per block. If a new category is scientifically necessary, add it to the legend and use a low-saturation tint. The contribution accent is a semantic category, not a heat-map or gradient.

## Typography and notation

- Use one font family and a two-level hierarchy: panel/stage heading, then module/body label.
- Keep labels short. Prefer `Temporal Mixer` over a paragraph; put an equation or shape annotation beside the relevant arrow.
- Use exact paper symbols and dimensions. A dimension label must answer a question (`(B,T,D)`), not fill space.
- At two-column scale, prioritize stage names, the contribution label, and the output. Secondary tensor notes may be smaller but must remain readable.

## Real images and icons

- Use a photo or generated illustration only for data source, sensor/device, anatomy, waveform, or deployment context.
- Put the image in a bounded input/context panel with a small caption. Do not place photos inside attention/MLP blocks.
- Prefer editable primitive icons or bundled SVGs for generic concepts. Record every non-trivial asset and license/provenance in `asset-ledger.md`.

## Semantic gate

For every element, complete the sentence “This represents ___.” If the blank is unclear, remove the element or replace it with a labeled semantic shape. A figure that is visually attractive but semantically ungrounded is not camera-ready.
