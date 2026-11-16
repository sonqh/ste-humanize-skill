# ADR: Use Unleash for feature flags, or LaunchDarkly if the Unleash audit log fails SOC 2

Status: Proposed. Thu decides by 2026-11-28.

Date: 2026-11-13

## Context

The invoice export beta needs feature flags with percent rollouts. Today we have only environment variable flags, which switch a feature on for everyone or for no one.

Four needs decide the choice:

- Percent rollout.
- An audit log that meets SOC 2. The SOC 2 auditors asked who changed which flag and when. This is a hard requirement.
- Low cost.
- No new system in the on-call rota. The team has 5 people.

## Decision

This decision is not made yet. The team leans this way:

- We will use Unleash, self-hosted, if its audit log meets the SOC 2 list.
- We will use LaunchDarkly if the Unleash audit log does not meet the list.

Huy checks the Unleash audit log against the SOC 2 list. Thu decides by 2026-11-28.

## Options

- LaunchDarkly. It has percent rollout and an audit log, and Huy believes it meets every need except cost. Sales quoted $1,000 a month for our seat count (email of 2026-11-10).
- Unleash, self-hosted. It is free and has percent rollout. Minh and Huy named two costs. It is one more container, and it needs its own Postgres database. Whether its audit log meets SOC 2 is not known yet.
- A flags table in our own Postgres. We rejected it. It may take a week to build, and it has no percent rollout or audit log unless we build them. Thu and Minh agree that this is too much to build.

## Consequences

- If we choose Unleash, we pay no license fee. We add a container and a Postgres database to run, and the on-call rota gains one system. Minh does not want that.
- If we choose LaunchDarkly, we pay $1,000 a month. We add no system to run.
- Either way, flags move from environment variables to a service, and the invoice export beta gets percent rollouts.
- We must decide again if the Unleash audit log fails the SOC 2 list. That result moves the choice to LaunchDarkly.
