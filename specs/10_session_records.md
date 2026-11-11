# Session records and revision policy

The host creates a new `workshop/` directory, distinct from framework files. No user configuration step is required. Exact naming may vary if references remain consistent.

| Path | Content |
|---|---|
| `workshop/workshop.json` | Current status, decisions, questions and active versions |
| `workshop/sources/` | Source records; authorised source assets if distributable |
| `workshop/baselines/` | Immutable baseline versions and relevant reference panels |
| `workshop/panels/` | Inventory records and pose contracts |
| `workshop/layouts/` | Frozen layout versions, including variable-section pagination |
| `workshop/tasks/` | Host-created task contracts and worker handoffs |
| `workshop/attempts/` | Immutable generation attempts, original outputs and working PNGs |
| `workshop/reviews/` | Per-attempt and cross-panel review records |
| `workshop/releases/` | Release selection manifests and generated deliverables |
| `workshop/records/` | Resume notes, lessons, tool capability evidence and change history |

Baseline, layout and release templates are draft records. An empty draft is valid structure, but cannot pass a production gate. A release marked complete needs non-empty selected coverage, Atlas PNG page(s), PDF and HTML entry, all verified to exist. Any missing required panel or unresolved required check precludes complete status.

Baseline feature acceptance conditions must be actionable observations, not only adjectives. Record visual sources for qualities that prose alone cannot establish. A new baseline version retains the prior one and identifies downstream reviews needing renewal.

A layout revision records changed page geometry or ordering. Do not reflow fixed slots silently. Flexible content can increase page count under the declared pagination policy. Release manifests tie exact image and review IDs to one layout/baseline combination.

Schemas only validate record shape. Before executing any production task, the host also checks that IDs are assigned, placeholders are gone, references exist, dependencies are settled and the task's proposed output location is owned by its worker.
