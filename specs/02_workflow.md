# Workflow and gates

| Stage | Responsible role | Output | Condition for dependent work |
|---|---|---|---|
| Discover | Host + curator | Sources, decisions, open questions | Inputs available for the intended task |
| Establish baseline | Baseline editor | Features, authority, variants, visual checks | Relevant identity-critical decisions resolved |
| Plan | Panel planner | Inventory, draft groups, layout proposal | Coverage and dependencies explicit |
| Draft | Generation operator + reviewer | PNG draft sub-atlases and findings | Useful compositions identified; errors recorded |
| Produce | Generation operator | Independent PNG candidates + attempt records | Actual tool support established; baseline fixed |
| Review | Fidelity reviewer | Per-panel and cross-panel reviews | No unresolved critical failures for selection |
| Assemble | Delivery builder | Atlas PNG/PDF + HTML | Accepted selections and layout version frozen |
| Archive | Archivist + host | ZIP, progress, checksums, resume state | Checks complete, or partial status conspicuous |

Drafting may loop. Fresh generation may bypass a draft when that is better supported by evidence. Crop reconstruction must retain the draft and must not inherit its errors as truth. A changed baseline invalidates affected downstream selections until reviewed against the new version.

Panel states: planned -> ready -> generated -> in_review -> accepted. Review may instead set rework_required or blocked; a new attempt returns to generated. Accepted candidates can be superseded or invalidated. Attempts themselves retain their outcome. “Generated” means a file exists, not that it is correct.

Independent source work and independent panel production may run concurrently after shared dependencies are fixed. Review and acceptance of a candidate depend on its actual output; assembly depends on accepted selection. The host alone edits shared selections and versions. Task records declare allowed reads, owned writes and blocked dependencies.

Quality failures do not expire. Retry policy should use reviewer evidence: targeted edits for isolated defects; fresh render for widespread identity or structural failure; alternate reference route for repeated composition failure. If stalled, give the user the evidence and a consequential choice, not a repetitive permission question. Respect generation limits and user budget without downgrading checks.
