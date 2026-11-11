# Data contracts and handoffs

Schemas define portable record structure, not visual truth. Templates are created and maintained by agents. IDs are stable within the workshop; all file references in release packages are relative to the package root. Reject path traversal and absolute paths when implementing package readers/writers. Hash actual file bytes using SHA-256.

| Record | Minimum meaning |
|---|---|
| workshop | Scope, state, current versions, decisions and unanswered questions |
| source | Available or unavailable evidence, authority domains and annotations |
| panel | Intended documentation, dependencies, resolution and state |
| attempt | Exact request/prompt references, tool metadata, outputs and lineage |
| review | Exact attempt + baseline, required checks, evidence and outcome |
| task | Role, context, owned output paths, dependencies and handoff |

Nullable metadata must have an explanatory entry in `missing_metadata`; a null seed is not a recorded seed. Example tool names are never actual provider data. Tool metadata fields preserve exact reported names. If only a human-readable interface label is available, keep it as a label, not a verified backend model ID.

All worker tasks follow a host-created envelope: task ID and goal; role prompt path; workshop root; allowed source/record paths; output directory; baseline/layout versions; blockers; acceptance conditions; return format. No placeholders need filling by the user. Resolve dependencies before execution. If an input changes, the host reschedules the task with a new record.

Shared handoff has five sections: completed outputs; evidence and checks performed; unresolved questions/blockers; recommended next task; execution details and limitations. Return only observed success. Include filenames so another agent can verify and resume.

Schemas intentionally allow domain-specific extension fields under `extensions`; they do not fix any character features or source/panel counts. Draft records may be incomplete; production gates enforce completeness. Schema validation alone does not grant readiness or release acceptance.
