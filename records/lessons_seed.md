# Portable lessons from framework design

These are user-reported observations and requirements, not independently verified tool experiments. No character identities or source images are included.

| ID | Observation / goal | Rule to try | Verification |
|---|---|---|---|
| L01 | Dense atlases can leave too few pixels per detail | Generate production panels independently; atlas is assembled later | Inspect actual native resolution and details |
| L02 | Some poses appeared in composite drafts when standalone attempts failed | Try draft sub-atlas followed by fresh panel or crop reconstruction | Compare actual attempts, pose and identity |
| L03 | Repeated lossy stages can degrade images | PNG working output at every image stage; preserve originals | Check actual file formats and transformation history |
| L04 | Unsettled foundation details can cause downstream drift | Establish relevant baseline before dependent panels | Check feature dependencies and baseline versions |
| L05 | Subtle covering/opacity errors can contaminate future reference use | Reject required-feature divergence and regenerate | Separate presence/location/extent/opacity checks |
| L06 | Image-only delivery loses generation context | Retain prompts, tool metadata, lineage and reviews | Trace a selected image back to exact inputs |
| L07 | Users should not need to remember configuration fields | Host interviews and creates records itself | Start a new workshop with plain-language input only |
| L08 | A reusable kit must not inherit a previous character | Fresh per-workshop source/identity records | Test with a different character and reference count |

L02 is a candidate strategy, not a claim that all tools or poses behave this way. L03 prevents further encoding loss; it does not reverse existing loss or prevent generative drift.
