# Panels, draft sub-atlases and deterministic layout

Panel counts and sections are discovered per workshop. No built-in eight-view turnaround, two-atlas limit or reference-count assumption. Useful optional sections include overview, viewpoints, pose concepts, portraits, body/structure angles and surface details.

Every panel needs a stable ID, purpose, fixed/flexible section, coverage, required features, pose contract, dependencies, baseline version and checks. Pose contract distinguishes exact reference geometry, conceptual emotional intent, camera/viewpoint and physical support. Do not force particular hands, props or expressions when only intent is specified. Exact-pose requirements need available evidence.

Draft sub-atlases group related compositions for exploration. They can have a different density and resolution from production pages. Preserve the complete draft PNG, selected crop coordinates and reviewer notes. A useful draft panel is not automatically accepted production material.

Production paths:
1. Fresh independent generation guided by authoritative references and draft composition.
2. Exact crop from draft, followed by AI reconstruction or upscaling guided by the same baseline.
Record the chosen route and lineage. Ordinary interpolation does not create missing texture. AI reconstruction may create detail, but its fidelity must be reviewed.

A resolution profile records supported native sizes, evidence for support, requested size, actual native output size and working size. Largest supported appropriate canvas means suitable aspect ratio and framing; do not treat a prompt's numeric request as proof of support. Freeze final slot dimensions after capability discovery. Any transformed derivative records method and actual dimensions separately.

Fixed sections have stable order, geometry and pagination within a layout version. Flexible sections can change count and crop, but assembly uses stable ordering (section order, declared rank, then panel ID). Extra panels create subsequent pages, not silently smaller panels. Each slot defines x/y/w/h in integer pixels, file selection, label area and fit policy. Default fit is exact 1:1; no implicit stretching, crop, mirror or resize. A deliberate contain/pad derivative preserves pixels; any resampling must be separately authorised and recorded.

Manifest validation checks unique IDs, no duplicate selections, file existence, bounds, overlap except explicitly permitted areas, dimensions and complete coverage. Same layout version + same pixel inputs + same assembly operations produce the same pixel arrangement; encoders may differ in byte output. Content generation itself is not deterministic.
