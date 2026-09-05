# Interaction and motion craft

Use only when behavior, state change, navigation, direct manipulation, or motion is
part of the request or a concrete issue. A still image cannot establish unseen motion.

## Interaction

- Make targets, current state, selection scope, affordance, consequence, and feedback
  apparent in the relevant context.
- Preserve a stable mental model across overview/detail, open/closed, edit/view, and
  loading/success/error transitions. Progressive disclosure should reveal complexity
  without hiding essential state or action.
- Account for keyboard, touch, pointer, focus, disabled, permission, undo, and recovery
  only where the task requires them. Do not annotate a universe of hypothetical states.

## Motion

Use an actual permitted motion reference when choreography matters. Extract trigger,
spatial anchor, sequence and perceptual purpose; a screenshot or motion adjective
cannot supply those decisions. Keep different reference mechanisms distinct and
synthesize them into one coherent behavior rather than unrelated entrance effects.

- Give motion a job: explain spatial continuity, reveal causality, direct attention,
  confirm change, preserve context, or express identity without impairing the task.
- Choose duration, easing, distance, staging, and choreography as one relationship.
  Small direct responses usually differ from large navigational transitions; no
  universal duration makes motion good.
- Keep input responsive and interruption behavior credible. Avoid serial ornament
  that delays frequent work or makes content inaccessible until animation completes.
- Provide a reduced-motion strategy and non-motion cues for information or status.
  Static Figma frames and prototype links do not certify runtime performance,
  interruption, focus, or reduced-motion behavior.

Inspect or prototype the exact transition before evaluating it. Record the starting
and ending states, trigger, changed properties, timing, and intended perceptual result.
If the tools cannot expose the motion, mark it unverified rather than inferring it.

Guidance synthesized from current Fluent motion and WCAG 2.2 sources recorded in
`sources.json`; system timings are examples, not mandatory values.
