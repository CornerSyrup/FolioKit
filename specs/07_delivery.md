# Atlas, HTML and ZIP delivery specification

Both Atlas and HTML are standard deliverables. They read one versioned release manifest selecting exact accepted attempts; neither may quietly choose a different image. A partial workshop may provide visibly labelled draft outputs with placeholders and a missing-panel report, but these are not a complete release.

## Atlas

Output full-resolution stitched PNG pages and a corresponding PDF. Layout is programmatic and deterministic within the frozen layout version, including titles, labels, order, gutters and coordinates. Save masters without lossy recompression. PDF must embed images losslessly, preserve aspect ratio and declare physical page sizing; do not assume a library's default PDF exporter preserves PNG encoding quality. Inspect PDF image encodings and render pages to verify. Split oversized pages through declared pagination, not silent downsampling. Record font availability and assembly environment where they affect layout.

## HTML portal

Provide a compiled, self-contained offline portal in the ZIP, opened with `index.html`. It must support section navigation, thumbnail overview, panel search/filter, native-resolution zoom/pan, keyboard navigation, original PNG download, and access to prompt, tool metadata, lineage and review status. Show dimensions and source type (native, crop, AI reconstruction, interpolated derivative) without calling all of them native.

Use relative local asset paths, bundled CSS/JS/fonts and an embedded data index or local JS data. Do not rely on network services, build tools or fetching JSON over file:// at viewing time. Include semantic controls, focus visibility, labels, useful alternative text and responsive layouts. Insert untrusted prompts as text. Do not upload reference assets to a hosted site without authorisation. Optional derived thumbnails are PNG and clearly separate from masters.

Verification covers at least representative sections and each available status/filter, keyboard open/close, zoom/reset, panel downloads, metadata access, missing-file handling and no required network requests. Verify actual browser behaviour where available, otherwise record untested interaction checks; static link checks alone do not establish usability.

## ZIP structure

Required logical contents: README; character/baseline and source records; panel inventory; draft PNGs and selected crops used as inputs; production PNGs; prompts/requests/metadata/reviews and lineage; Atlas PNGs/PDF; offline HTML and assets; release/layout manifests; reproducible assembly instructions or scripts; progress/resume record; checksums and validation report.

Avoid duplicating large masters inside the portal; link to the same relative files. Failed attempt records are retained. Failed image inclusion is optional and explicitly listed. External references that cannot be redistributed are listed with availability constraints, not falsely counted as bundled. ZIP CRC checks are necessary but do not verify content fidelity. Check that no absolute paths, missing dependencies or secrets enter the archive.
