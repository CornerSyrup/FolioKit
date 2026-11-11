# FolioKit

**FolioKit is a reusable, character-independent workshop for building faithful, well-documented character reference kits.** This repository contains the workshop instructions and supporting files. Each workshop starts fresh with the character and references supplied for that session.

## Start a workshop

1. Open [`prompts/00_host.md`](prompts/00_host.md) in this repository.
2. Copy its full contents and paste them into an AI service that can work with files and access the internet.
3. Send the prompt. The host will fetch the required FolioKit files from this repository's `dev` branch itself. You do not need to download or attach a FolioKit archive.
4. Describe the character-reference kit you want to make. Attach or provide any source material you already have. If you have not settled the design or gathered references yet, say so; the host will interview you and organise the decisions.
5. Answer follow-up questions, review draft work and flag details that need correction. The host maintains the workshop records; you do not need to fill in JSON, templates or a panel checklist.

The reusable prompts and documentation are written in English. **The host should speak with you in the language you use** and keep explanations and workshop-facing materials accessible in that language.

### What the workshop needs from you

Start with your goal and any character information or reference material you have. Useful input can include images, sketches, written descriptions, existing character sheets, specific features to preserve, pose or viewpoint preferences and intended use. There is no required number or type of references. You can provide material gradually. The host should ask only for information that matters to the next decision, and should keep unresolved facts distinct from established ones.

Use only sources available in the active workshop. The host must not assume it can see a file merely because it is named or described. If network access, source access or another needed capability is unavailable, it should explain the blocker and keep the work resumable.

### What you do during the workshop

The host interviews you, registers the actual sources, establishes a character baseline, plans a panel inventory, and may prepare draft sub-atlases to explore compositions. Production panels can be freshly generated or reconstructed from a draft crop. Each route and each image attempt must be recorded. You review progress and point out mismatches; the host arranges further generation and fidelity checks.

Identity, material, shape, coverage, asymmetry and other required details should be agreed before dependent panels are made. A subtle required-feature error is still a failed panel. PNG is used for image-stage working outputs to avoid adding lossy encoding at each step; PNG cannot restore detail already lost or changed during generation, resizing or reconstruction. The workshop favours character fidelity and consistency over speed.

### What you should receive

A completed workshop is intended to produce:

- Individual panel images in PNG, with prompts, available tool/model metadata, source lineage and review records.
- A deterministic, programmatically assembled **Atlas** in PNG and PDF.
- An easy-to-use **HTML portal** for browsing, searching, zooming and reviewing panel details.
- A **ZIP package** containing the README, host and specialist prompts, specifications, records, panel materials, manifests, assembly instructions or tools, and final outputs.

The actual available image sizes, model details and generation controls depend on the AI service. The host must record what the tool reports, leave unavailable metadata unknown, and never claim that a crop or enlarged image is a native standalone render. If any required panels remain failed or blocked, outputs must be labelled partial and accompanied by an accurate progress record.

## Repository contents

- `prompts/` — host, shared instructions and specialist-agent prompts.
- `specs/` — workshop interview, source and baseline, panel, generation, review and delivery rules.
- `schemas/` and `templates/` — machine-readable record structures maintained by the host.
- `tools/` — framework structure validator and future assembly utilities.
- `records/` — transferable lessons, without character-specific defaults.

The prompts are written in English to make them reusable. The host adapts workshop conversation to the user's language. No character, source count, panel count or pose is preselected by the framework.

## Using a packaged copy

If a service cannot fetch GitHub files, GitHub can provide a source ZIP from the repository page (Code → Download ZIP). Attach that ZIP to the AI service and have the host read the same files from the extracted copy. This is an optional fallback; the standard workflow needs only the copied host prompt and the host's ability to fetch repository files.

## Status

FolioKit is an evolving workshop framework. A validated framework structure does not mean an image-generation workshop has been run or that production images, an Atlas or an HTML portal already exist. Improve the workflow from observed results and record the evidence behind each lesson.
