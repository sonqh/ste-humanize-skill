# ADR: Add feature flags with percent rollout, using Unleash or LaunchDarkly

Status: Proposed, 2026-11-13. Thu decides by 2026-11-28.

## Context

The invoice export beta needs feature flags with percent rollouts. Today the team has only environment variable flags, which switch a feature on for everyone or for no one.

The SOC 2 auditors asked who changed which flag and when. An audit log of flag changes is a hard requirement. The team has 5 people and does not want another system in the on-call rota.

## Decision

We will use Unleash, self-hosted, if its audit log meets the SOC 2 list. We will use LaunchDarkly if it does not. We will not build a flags table in our own Postgres.

Huy checks the Unleash audit log against the SOC 2 list. Thu decides after that check, by 2026-11-28.

## Criteria

The team chose four criteria in the thread:

- Percent rollout.
- An audit log that meets SOC 2.
- Cost.
- No new system in the on-call rota.

## Options

| Option | Percent rollout | Audit log | Cost | New on-call load |
|---|---|---|---|---|
| LaunchDarkly | Yes (Huy) | Yes (Huy) | $1,000 a month, quoted by sales for our seat count on 2026-11-10 | None named |
| Unleash, self-hosted | Yes (Huy) | Not known. Huy has not checked it against SOC 2. | Free to license | One more container and its own Postgres database (Minh) |
| Flags table in our Postgres | Only if we build it | None unless we build it | About one week of work, Huy's estimate | Not discussed |

Why not each option:

- Flags table: Thu and Minh agree it is too much to build. It has no percent rollout and no audit log until the team builds both.
- LaunchDarkly: it meets every criterion except cost. It stays as the fallback.
- Unleash: it adds a container and a database to the on-call rota. It wins only if its audit log is good enough.
- Do nothing: environment variable flags cannot do a percent rollout and keep no record of changes. The beta is blocked.

## Consequences

- If we choose Unleash, we save $1,000 a month. We take on one more container and one more Postgres database. Both go in the on-call rota of 5 people.
- If we choose LaunchDarkly, we pay $1,000 a month. We run no new system.
- The team must decide again if the Unleash audit log fails the SOC 2 list. LaunchDarkly then becomes the choice.

## Open questions

- Does the Unleash audit log meet the SOC 2 list? Owner: Huy. Date: TBD (owner unknown for the date, before 2026-11-28).
- Which SOC 2 items does the audit log need to show? The list is TBD (owner unknown).

Missing: the result of the Unleash audit log check, the SOC 2 list itself, the date by which Huy finishes the check, and any estimate of the on-call load of Unleash.
