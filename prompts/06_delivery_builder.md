# Atlas and HTML delivery builder

Read `prompts/COMMON.md`, `specs/07_delivery.md` and `specs/09_contracts.md`. The host supplies the task and relevant current records; resolve missing context with the host.

Build both outputs from a frozen release manifest and accepted attempts. Do not substitute missing panels. Produce deterministic Atlas PNG pages plus PDF, and an easy-to-use offline HTML portal. Read the delivery specification for layout, pixel preservation, PDF embedding, accessibility, zoom, provenance and checks.
Use image/PDF libraries for precise assembly, not generative image tools. No source resizing, cropping, mirroring or reordering unless a declared layout operation authorises it. Keep high-resolution masters separate from optional labelled thumbnails. Ensure PDF generation does not silently recompress image masters into lossy JPEG.
Implement the portal with TypeScript when a build is useful, and package compiled browser assets. Keep dependencies small; no remote CDN requirement. For direct file opening, embed the data index or use local script data rather than assuming fetch of local JSON works. Use safe text insertion for prompts/metadata. The user must not need Node to view the release.
Verify actual PNG geometry, PDF page rendering, HTML search/filter/zoom/download and links. Distinguish passed, failed and untested checks. If building only a partial draft, visibly show missing slots and failures. Do not silently ship an apparently complete atlas.

Return the shared handoff format. Write only within assigned output paths; propose shared-state edits to the host.
