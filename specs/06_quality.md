# Fidelity review and release checks

Use pass/fail/unknown/not_applicable per check. Record evidence source, candidate region, observed result and repair direction. Mark severity critical/major/minor. Any failed required check prevents acceptance; critical checks can never be waived by an average score. A user-requested specification change creates a new baseline rather than relabelling a faulty output as correct.

| Check family | Inspection |
|---|---|
| Identity | Required face/structure/marks, silhouette and proportions |
| Surface | Palette, texture, finish and lighting-dependent appearance |
| Garment/covering | Presence, construction, layers, length, position and opacity |
| Asymmetry | Character-relative side and all required directional features |
| Pose | Exact geometry if locked; emotional intent if conceptual |
| Plausibility | Applicable anatomy, balance, contacts, support and occlusion |
| Framing | Single intended view, full required coverage, no accidental crop |
| Cross-panel | Same baseline and variant, coherent proportions/materials/scale |
| File integrity | Actual image format/dimensions, hashes, provenance completeness |

Example of a transferable failure: required covering becomes bare surface in some views, or transparency drifts between views. Check presence, location, extent and opacity separately. Do not infer material presence from colour resemblance. If a hidden feature is outside a panel's scope, mark not_applicable; require other panels to document it where necessary.

Review at useful scales: overall framing and detail crops at native pixels. Enlarged display is not evidence of recovered detail. If pixels are insufficient to establish a required property, request a dedicated panel or new attempt. Fresh and reconstructed images have the same acceptance threshold.

Review exact attempt IDs against exact baseline versions. Single-panel acceptance does not replace cross-panel review. Release validation also checks atlas geometry, PDF rendered pages and HTML interactions. Archive machine results and human/visual findings separately. Self-review limitations are disclosed.
