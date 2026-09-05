# Behavioral evaluations

Install the exported plugin first. Run `python -B evals/run.py --output <new-external-directory>`
or select probes with repeated `--case <id>`. Each launches a fresh read-only Codex
invocation in an empty temporary directory, using the installed skill and normal
user model settings. It withholds expected criteria and saves final responses plus
actual tool events. No grading model or pass-by-keyword shortcut is included.

Review both response and events against every case's `must_demonstrate`. Check
actual skill/resource reads, not only self-reported resource names. Flag unnecessary
canon loading, false visual verification, ignored user constraints, invented writes
or redundant specialists. Negative engineering cases should not load Design Director.
These four probes cover only obvious activation, narrow scope, and missing-capability
behavior. They are not design-quality evidence or a runtime security boundary.

`benchmarks.json` defines the primary development evidence: six representative live
Figma design problems with explicit adequacy conditions, priority dimensions, and
reference roles. Run them only in a user-authorized test context. Judge the actual
editable artifacts and fresh matching renders using `docs/acceptance.md`; do not
turn these development fixtures into a mandatory user workflow.

The live gallery test is separate: start with an actual representative brief and
user-approved pool, inspect restrictions, retrieve gallery-provided images, record
visual analysis and candidate/working-set decisions as relevant signal diminishes.
Separate broad research, curated task references and the subset used per decision;
reject attractive mismatches and do not stop merely because a few images exist.
Reuse retained files and apply transferable principles in the test Figma draft. Preserve
references after the test. Do not replace this with mock network success.

## Evaluate the evaluator when a live benchmark is authorized

In an explicitly authorized new Figma test draft, create a small editable example
with seeded material defects and deliberate non-defects. Attach its actual render
to a fresh read-only Codex evaluation using `codex exec --image <image>`. Ask for a
concrete design review without revealing the defect list. Check that the review
finds actual defects, preserves intentional choices and distinguishes taste from
barriers. Keep the expected defect list outside the model's prompt.

Suggested seeds: low contrast essential text, clipped long title, missing error
recovery; controls all equally emphasized. Non-defects: human-approved violet gradient,
one typeface, purposeful density. After correction, inspect the same viewport/state
and ensure findings aren't repeated without evidence. No compulsory criticism quota.

Record every failure/correction and untested dimension in `docs/validation.md`.
For live Figma tests, use only the draft explicitly authorized by the user, never
existing drafts/projects. Retain the Figma artifact. Cleanup unit tests use synthetic
files under a test-owned temporary root and never real acquired references.
