# General Figure Quality Contract

This contract turns recurring figure-review feedback into reusable, project-independent rules. It applies to framework overviews, module-detail diagrams, and multi-panel ML/AI figures. The `.drawio` source remains authoritative; exported PDF, SVG, and PNG evidence determines whether the figure is ready.

## 1. Information hierarchy

- State one dominant story: input → transformation → contribution → output.
- Keep a framework overview to roughly 5–8 major stages. Move internal mechanics to a separate module panel when the overview becomes dense.
- Each panel must have one visually dominant title, one clear contribution area, and only the labels needed to decode the data flow.
- Replace prose paragraphs, repeated edge labels, and decorative micro-blocks with short noun phrases, compact formulas, or a single explanatory note.
- Every visible object must answer a reader question. Remove shapes, colors, symbols, and annotations that do not carry scientific meaning.

## 2. Paper-scale typography and density

- Judge readability at the intended manuscript width, not at editor zoom or a full-resolution canvas screenshot.
- Maintain a clear hierarchy: panel title > module title > key tensor/operation > annotation. Do not let helper labels compete with the innovation block.
- If text is too small, remove redundant content and enlarge the important block before shrinking fonts.
- Fit the canvas to the actual composition with a deliberate safety margin. Avoid large unused bands above, below, or between panels; use whitespace to separate concepts, not to fill an oversized page.
- Align panel edges, baselines, repeated cards, and output columns. Use a consistent grid and spacing rhythm, with intentional exceptions recorded in the review log.

## 3. Equations, symbols, and notation

- Store formulas in Draw.io MathJax/LaTeX form and verify that exports show rendered glyphs, not delimiter/source text.
- Use one notation consistently across the figure and paper. Check subscripts, superscripts, hats, operators, inequalities, Greek letters, and calligraphic symbols in PDF and PNG.
- Give a formula enough height and width for its rendered glyphs. Do not rely on the visual editor to hide overflow.
- Never use an unexplained symbol as a visual placeholder. Replace ambiguous dots, circled dots, or anonymous markers with a named operation, an explicit aggregation symbol, or a labeled node.

## 4. Real-object imagery and vector semantics

- Use transparent-background real-object cutouts only for an input, device, sensor, application, or other context where the physical object improves comprehension.
- Keep model computation, tensors, operators, and control logic as editable Draw.io vectors. Do not replace semantic modules with generated raster art.
- Record asset provenance and role in `asset-ledger.md`; inspect every image in the exported PDF/SVG/PNG for missing payloads, opaque backgrounds, halos, or accidental clipping.

## 5. Connector grammar

Before drawing an edge, record its source, target, direction, relation type, and forbidden crossing zones.

- Every arrow must have an unambiguous origin and destination. The number of arrows must match the scientific relation; do not imply three operations with two arrows or vice versa.
- Use arrowheads, line styles, and colors consistently for data flow, control, feedback, update, and annotation. Keep feedback/update paths visually distinct from the main path.
- Prefer short orthogonal routes. Add explicit waypoints and ports for fan-in/fan-out so edges do not cross boxes, formulas, labels, or unrelated panel boundaries.
- Route long feedback lines from a visible source card or budget/training split, not from an invisible anchor with no semantic label.
- Inspect arrowheads at paper scale; a connector that merely touches a border or disappears behind a node is not considered connected.

## 6. Export-driven review loop

For a user-critical or camera-ready figure, perform at least three screenshot → defect inventory → fix → re-export cycles:

1. Review the canvas-only export for hierarchy, missing elements, and gross whitespace.
2. Review the direct PDF/PNG/SVG for formula rendering, image payloads, alignment, arrow crossings, and clipping.
3. Compile the figure at manuscript width and review the smallest required text, symbols, and arrowheads.

At each cycle inspect nine zones (top-left, top, top-right, left, center, right, bottom-left, bottom, bottom-right), classify P0/P1/P2 defects, and fix all P0/P1 issues before proceeding. Static checker warnings must be reviewed individually: fix real collisions and overflow; document conservative false positives (for example, a MathJax-aware export that a plain-text heuristic cannot measure) in `defect-log.md`.

Required handoff checks:

- XML parses and has no duplicate IDs, off-page vertices, missing required cells, or unintended external images.
- PDF, SVG, and PNG exports exist and are visually consistent.
- The manuscript-width compilation succeeds and is inspected as an image.
- The editable `.drawio` source, latest preview, exports, validation reports, and defect log are delivered together.

## 7. Reference-image discipline

Reference images provide style and composition cues only. Extract their typography, palette, spacing, corner radius, stroke, arrow grammar, and density; derive scientific content from the paper or method source. Never copy unexplained symbols or invent modules merely because they appear in a reference.

