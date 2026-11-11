# Generation and provenance contract

Each immutable attempt directory contains `prompt.txt`, `request.json`, `metadata.json`, `review.json` when reviewed, original tool output(s), and PNG working output(s). Unavailable raw responses are explicitly noted. For a multi-output request, record each output separately. Do not place secrets in recorded payloads; mark any redacted fields.

Store the exact final operator-submitted prompt and parameterised request, including supported reference ordering and negative prompts if actually used. Do not claim access to hidden service prompts or settings. Record provider, tool, exact reported model ID, reported version, quality mode, job ID, timestamps, seed, usage and cost only when exposed. Each unavailable field is null with a missing-metadata reason. Framework, schema, baseline, character, model and layout versions are separate concepts.

Track parents as explicit attempt/artifact IDs and hashed files. Each transformation records operation, inputs, outputs, crop rectangle in source pixels, resize/reconstruction parameters, tool identity and pixel dimensions. Preserve original outputs and every working-stage PNG. Non-PNG original output is retained alongside PNG conversion; disclose its encoding. Never call an enlarged crop native standalone generation. An invented tool label used in discussion is not metadata.

Tool capability evidence is workshop-local and dated: interface schema, actual tool response, or authoritative documentation. Do not bake maximum resolution or model availability into the generic framework. Missing controls stay unsupported/unknown; do not simulate seed control with prompt text.

Recommended prompt composition order: intended single-panel output; authoritative character baseline; required view and coverage; emotional/pose intent; physical support and anatomy; material and coverage details; lighting/background; panel-specific checks; explicit exclusions. Include only applicable features. Record exactly what was ultimately sent, including changes made after compilation.

PNG compression level changes file size without the repeated quantisation of lossy image formats. Still avoid unnecessary resizing, colour-space conversion, bit-depth reduction and AI re-encoding. Preserve colour profiles and transparency where relevant; record deliberate changes. PDF is a final container, not a working image stage.
