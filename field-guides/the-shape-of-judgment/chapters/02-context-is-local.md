# 2. Context Is Local, Not Universal

Context is not extra prose around a problem. It is the set of conditions under which a claim, preference, or action changes meaning.

A scheduling recommendation can depend on labor rules, caregiving patterns, religious observance, accessibility, time zones, and local infrastructure. Calling one answer “universally optimal” hides whose constraints were treated as defaults.

## Principle

Map context as claims that can be sourced, challenged, and owned. Do not reduce culture to a demographic label or a model-generated summary.

A useful context map separates:

| Dimension | Questions |
|-----------|-----------|
| Domain | What practice, institution, or decision class is this? |
| Stakeholders | Who decides, benefits, pays, is exposed, or can appeal? |
| Constraints | Which legal, technical, financial, physical, or temporal limits apply? |
| Norms | Which expectations or values matter, and who says so? |
| Resources | What time, money, access, language, data, or expertise is available? |
| Variance | Which conditions differ across locations, groups, or cases? |
| Ownership | Who may validate or override each contextual claim? |

## Failure Mode: Universal by Omission

A system becomes “universal” by omission when it tests one context, erases local differences from its representation, and treats the resulting uniformity as proof of generality.

The corrective question is not “Did the model mention culture?” It is “Which decision changed because an affected stakeholder supplied different context?” If nothing can change, cultural sensitivity is ornamental.

## Mechanism: Context Claims

Record context in the same evidence system as other claims:

```yaml
claim: Weekend contact is acceptable for this audience.
source: campaign policy approved by regional owner
scope: region_a / opted_in_contacts
valid_from: 2026-01-01
review_by: 2026-10-01
owner: regional_operations
confidence: approved_policy
```

This prevents generated cultural generalizations from acquiring the authority of policy.

## Tradeoff

Context mapping can become an endless attempt to enumerate human complexity. Bound it to the current decision and consequence. Ask which contextual differences could change eligibility, interpretation, burden, safety, or recourse.

## Field Test

Run the same proposed decision through two deliberately different context maps. If the output never changes, either the decision is genuinely invariant or the context fields are not connected to the mechanism.

## Falsifier

Retire a contextual category if affected reviewers consistently find it irrelevant or harmful. Add one when omitted conditions repeatedly explain failures.

## Authority Boundary

Models may propose contextual questions and summarize supplied evidence. They should not declare that a population holds a belief, accepts a burden, or consents to an action without representative evidence and accountable review.
