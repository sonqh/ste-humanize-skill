# Proposal: move build and test from Jenkins to GitHub Actions

Please approve the move of build and test for all repositories from Jenkins to GitHub Actions. The cost is 2 engineers for 6 weeks and about $500 more per month. I need a decision by 28 November. Then the work finishes before the end of March, when our Jenkins line stops getting security fixes, with some room to spare.

## What we get

A five-week pilot gave these results. Three repositories (the web app, the billing service, and the docs site) built on GitHub Actions in parallel with Jenkins.

| Measure | Jenkins | GitHub Actions |
|---|---|---|
| Median build time | 38 minutes | 14 minutes |
| Builds that fail for reasons unrelated to the code | 12% | 3% |

- The time came down mostly from better caching and parallel test shards.
- Developers on those teams told us they do not want to go back.
- Three repositories is a small sample, and they are among our simpler ones.

## What it costs

- People: 2 engineers for 6 weeks, by my estimate, to move all build and test jobs. This does not count the GPU repositories if their runners slip.
- Money: roughly $1,200 per month in hosted runner minutes for all 41 repositories, based on the pilot usage. The two Jenkins machines cost about $700 per month today. The difference is about $500 per month.

## What happens if we do nothing

The Jenkins LTS line we are on stops getting security fixes at the end of March. The upgrade to the next line breaks at least nine of our plugins. Two of those have open CVEs today. That leaves two outcomes:

- We run an unpatched CI system that holds deployment credentials.
- We spend an unknown amount of time on the upgrade anyway.

The daily problems also stay:

- The median build time on the main application is 38 minutes. A developer gets maybe four or five full runs a day.
- About 12% of builds fail for reasons that have nothing to do with the code. Mostly an agent runs out of disk or loses its connection. People have learned to press retry.

## Why GitHub Actions

I also looked briefly at GitLab CI and at CircleCI.

| Option | Speed | Cost per month | Problem |
|---|---|---|---|
| GitHub Actions | 14 minutes median in the pilot | Roughly $1,200 | See the risks below |
| CircleCI | Comparable in a one-day test | About $1,900 for the same usage | A second vendor to manage next to GitHub |
| GitLab CI | Not tested | Not estimated | We would have to move our code hosting too, which nobody wants |

## What can go wrong, and how we go back

We keep Jenkins in read-only mode for 30 days after the last repository moves. In that time, any repository can go back to its old job if we revert one pull request.

I am less sure about two parts:

- GPU tests. Two repositories run GPU tests, and those cannot run on hosted runners. They need self-hosted runners, which we have not set up before. This part may not be ready in the same time frame as the rest. It could need more work than we think.
- Secrets. We have about 40 secrets in Jenkins credentials. We have not tested how to move them. Some are shared between jobs in ways nobody fully remembers.

## What this proposal does not cover

This proposal is only about build and test. Deployments stay on Jenkins for now. We look at the deployment pipelines next quarter.

## Background

- We set up Jenkins in 2019, when the company had three repositories. It has served us well.
- Today 41 repositories build on it, with about 300 jobs.
- Whoever has time looks after the two controller machines. In practice that has been me and one other engineer.
- Over the years we have collected 60-odd plugins. Some are no longer maintained.
- We discussed this subject in the last few platform syncs, and I have looked at our CI for a while.

I can explain any part of this in person.

Cut candidates: the Background section (history, job and plugin counts, controller upkeep, platform syncs), the offer to explain in person.
