# ADR: Use Unleash for feature flags, or LaunchDarkly if its audit log fails SOC 2

Status: Proposed. Date: 2026-11-13. Thu decides by 2026-11-28.

## Context

The invoice export beta needs percent rollouts. Today the platform has only env var flags, which turn a feature on for everyone or for no one.

SOC 2 auditors asked who changed which flag and when. Thu says an audit log is a hard requirement. The team has 5 people and does not want another system in the on-call rota.

## Decision

We will use self-hosted Unleash for feature flags, if its audit log meets the SOC 2 list. Huy will check the log against that list.

If the audit log does not meet the list, we will use LaunchDarkly. We will not build our own flags table in Postgres.

## Criteria

The thread named four criteria:

- Percent rollout.
- An audit log that meets SOC 2.
- Cost.
- No new system in the on-call rota.

## Options

| Option | Percent rollout | Audit log for SOC 2 | Cost | On-call load |
|---|---|---|---|---|
| LaunchDarkly | Yes | Yes | $1,000 a month (sales quote, email of 2026-11-10) | None named |
| Unleash, self-hosted | Yes | Not known. Huy has not checked it. | Free software. Hosting cost: TBD (owner unknown) | One more container and its own Postgres database |
| Flags table in our Postgres | Only if we build it | No | About one week of work (Huy's estimate, "maybe") | Not discussed |

Huy states that LaunchDarkly meets every criterion except cost. Minh does not want another container and database in the on-call rota, which is the main cost of Unleash.

We reject the flags table. It has no percent rollout and no audit log unless we build both, and the team judged that too much work. Thu and Minh agree.

## Consequences

- If the audit log of Unleash passes, we avoid the $1,000 monthly fee. The team takes on one more container and one more database to run and to put on call.
- If the audit log fails, we pay LaunchDarkly $1,000 a month and add nothing to the on-call rota.
- The team must decide again if the SOC 2 list changes, or if the LaunchDarkly price changes.

## Open questions

- Does the audit log of Unleash meet the SOC 2 list? Owner: Huy. Date: before 2026-11-28.
- What does it cost to host Unleash? TBD (owner unknown).

Missing: the result of the Unleash audit log check, the hosting cost of Unleash, the on-call load of the flags table, and the last names of the people.
