# Use Unleash for feature flags if its audit log meets SOC 2, otherwise LaunchDarkly

Status: Proposed, 2026-11-13. Thu decides by 2026-11-28.

## Context

The invoice export beta needs feature flags with percent rollouts. Today the platform team has only env var flags, which turn a feature on for everyone or for no one.

The team has 5 people. SOC 2 auditors asked who changed which flag and when, so an audit log is a hard requirement.

## Decision

We will use Unleash, self-hosted, if its audit log meets the SOC 2 list. If it does not, we will use LaunchDarkly. We will not build a flags table in our own Postgres.

Huy checks the Unleash audit log against the SOC 2 list. Thu decides by 2026-11-28. Until then this ADR stays Proposed.

## Criteria

1. Percent rollout.
2. An audit log that meets SOC 2.
3. Cost.
4. No new system in the on-call rota.

## Options

| Option | Percent rollout | Audit log for SOC 2 | Cost | New on-call system |
|---|---|---|---|---|
| LaunchDarkly | Yes | Yes | $1,000 a month (sales quote, email of 2026-11-10) | No |
| Unleash, self-hosted | Yes | Not known yet. Huy is checking. | Free to license | Yes. One more container and its own Postgres database. |
| Flags table in our Postgres | Only if we build it | No | About one week of work (Huy's estimate) | Not discussed |

- LaunchDarkly meets every criterion except cost. Huy gave the "Yes" entries in this table. Nobody has checked them against the SOC 2 list.
- Unleash costs nothing to license. Minh does not want another system in the on-call rota for a team of 5.
- The flags table is out. It has no percent rollout and no audit log unless we build both, and that is too much to build.

## Consequences

- If the Unleash audit log meets SOC 2, we pay no license fee. We run one more container and one more Postgres database, and the on-call rota carries both.
- If it does not, we pay $1,000 a month and add nothing to the on-call rota.
- We must decide again if the LaunchDarkly price or the seat count changes, or if the SOC 2 list changes.

## Open questions

- Does the Unleash audit log meet the SOC 2 list? Owner: Huy. Date: TBD (before 2026-11-28).
- Which option do we choose? Owner: Thu. Date: 2026-11-28.

Missing: the result of the Unleash audit log check, the cost of running Unleash (hosting and on-call time), the date by which Huy finishes the check, whether the flags table adds an on-call load, and a SOC 2 check of the LaunchDarkly audit log.
