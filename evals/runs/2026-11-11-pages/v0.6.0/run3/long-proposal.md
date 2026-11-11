# Proposal: move build and test from Jenkins to GitHub Actions

I ask you to approve the move of build and test for all 41 repositories from Jenkins to GitHub Actions. The work needs 2 engineers for 6 weeks and about $500 more per month. I need your decision by 28 November. Then the work finishes before the end of March, when our Jenkins version stops getting security fixes, with some room to spare.

## What we get

We ran a pilot for five weeks. Three repositories (the web app, the billing service, and the docs site) built on GitHub Actions in parallel with Jenkins.

| Measure | Jenkins | GitHub Actions, in the pilot |
|---|---|---|
| Median build time | 38 minutes | 14 minutes |
| Builds that fail for reasons unrelated to the code | About 12% | 3% |

- Most of the time gain comes from better caching and parallel test shards.
- At 38 minutes, a developer on the main application gets maybe four or five full runs a day.
- Most of the unrelated failures on Jenkins come from agents that have no disk space left or lose their connection. People have learned to press retry.
- Developers on the pilot teams told us they do not want to return to Jenkins.

Three repositories is a small sample, and they are among our simpler ones.

## What it costs

| Item | Cost |
|---|---|
| Hosted runner minutes for all 41 repositories | Roughly $1,200 per month, based on the pilot usage |
| The two Jenkins machines today | About $700 per month |
| Difference | About $500 more per month |
| The work | My estimate is 6 weeks for 2 engineers, for all build and test jobs |

The estimate of 6 weeks does not count the two GPU repositories if their runners are late.

## If we do nothing

The Jenkins LTS line we use stops getting security fixes at the end of March. The upgrade to the next line breaks at least nine of our plugins. Two of those plugins have open CVEs today. Then we have two choices:

- We run an unpatched CI system that holds deployment credentials.
- We spend an unknown amount of time on the upgrade.

## The other options

I looked briefly at GitLab CI and at CircleCI.

- GitLab CI: we would have to move our code hosting too, and nobody wants that.
- CircleCI: the speed was comparable in a one-day test. It would be a second vendor to manage next to GitHub. The price was higher, at about $1,900 per month for the same usage.

## What can go wrong, and how we go back

We would keep Jenkins in read-only mode for 30 days after the last repository moves. In that time, any repository can return to its old job if we revert one pull request.

There are things I am less sure about:

- Two repositories run GPU tests, and those tests cannot run on hosted runners. They need self-hosted runners, which we have not installed before. This part may not be ready in the same time frame as the rest. It could need more work than we think.
- We have about 40 secrets in Jenkins credentials, and we have not tested the move of these secrets. Jobs share some of them in ways that nobody fully remembers.

## What this proposal does not cover

This proposal is only about build and test. Deployments would stay on Jenkins for now. We would look at the deployment pipelines next quarter.

## Background

- We discussed the state of our CI in the last few platform syncs.
- We installed Jenkins in 2019, when the company had three repositories. It has served us well.
- Today 41 repositories build on it, with about 300 jobs.
- Whoever has time maintains the two controller machines. In practice, that has been me and one other engineer.
- Over the years we have collected 60-odd plugins. Some of them are no longer maintained.

I can explain any part of this in person.

Cut candidates: the Background section. The offer to explain in person.
