# Choose a feature flag system for percent rollouts

Status: Proposed. Date: 2026-11-13. Thu decides by 2026-11-28.

## Context

The invoice export beta needs feature flags with percent rollouts. Today we have only environment variable flags, which are all or nothing.

Four things decide the choice:

- Percent rollout.
- An audit log. SOC 2 auditors asked who changed which flag and when, so this is a hard requirement.
- Cost.
- No new system in the on-call rota. The team has 5 people.

## Decision

We have not decided yet. The current lean is this:

- We will use Unleash, self-hosted, if its audit log meets the SOC 2 list.
- We will use LaunchDarkly if the Unleash audit log does not meet the list.

Huy checks the Unleash audit log against the SOC 2 list. Thu decides by 2026-11-28.

## Options

- LaunchDarkly. It has percent rollout and an audit log, and Huy says it meets all four needs except cost. Sales quoted $1,000 a month for our seat count (email of 2026-11-10).
- Unleash, self-hosted. It is free and has percent rollout. Huy is not sure that its audit log meets SOC 2. It adds one container and needs its own Postgres database, so it adds one more thing to the on-call rota.
- A flags table in our own Postgres. We rejected it. It may take about a week to build. It has no percent rollout unless we build it, and it has no audit log.

## Consequences

- If we choose Unleash, we pay no license fee. We run one more container and one more database, and the on-call rota covers them.
- If we choose LaunchDarkly, we pay $1,000 a month and add no system to the on-call rota.
- The audit log check decides between the two. Update this record when Huy reports and when Thu decides.
