# Choose a feature flag service for percent rollouts

Status: Proposed. The team has not decided. Thu decides by 2026-11-28.

Date: 2026-11-13

## Context

The invoice export beta needs feature flags with percent rollouts. Today we have only env var flags, which are all or nothing.

Four things decide the choice:

- Percent rollout.
- An audit log that meets SOC 2. SOC 2 auditors asked who changed which flag and when. This is a hard requirement.
- Cost.
- No new system in the on-call rota. The team has 5 people.

## Options

- LaunchDarkly. It meets all four needs except cost. Sales quoted $1,000 a month for our seat count (email of 2026-11-10).
- Self-hosted Unleash. It is free and has percent rollout. It adds one container and needs its own Postgres database, so it adds work to the on-call rota. Huy is not sure that its audit log meets SOC 2.
- A flags table in our own Postgres. It may take about a week to build. It has no percent rollout and no audit log unless we build them. Thu and Minh rule it out because it is too much to build.

## Decision

The team has not made the decision. The current lean is Unleash if its audit log is good enough for SOC 2, and LaunchDarkly if it is not.

Huy will check the Unleash audit log against the SOC 2 list. Thu decides by 2026-11-28, and this ADR then changes from Proposed to Accepted.

## Consequences

Not known until the decision. Two points are known now:

- LaunchDarkly costs $1,000 a month.
- Unleash adds one more service to the on-call rota of 5 people.
