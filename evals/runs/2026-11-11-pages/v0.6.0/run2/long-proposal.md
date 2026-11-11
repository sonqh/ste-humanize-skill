# Proposal: move build and test from Jenkins to GitHub Actions

Please approve the move of build and test for all 41 repositories from Jenkins to GitHub Actions. The cost is 2 engineers for 6 weeks and about $500 more per month. I need a decision by 28 November. Our Jenkins LTS line stops getting security fixes at the end of March. A decision by 28 November lets the work finish before that date with some room to spare.

## What we get

We ran a pilot for five weeks. Three repositories (the web app, the billing service, and the docs site) built on GitHub Actions in parallel with Jenkins. On those three:

- The median build time went from 38 minutes to 14 minutes. Most of the gain came from better caching and parallel test shards.
- The rate of failures unrelated to the code went from 12% of builds to 3%.
- The developers on those teams told us that they do not want to go back.

Three repositories is a small sample, and they are among our simpler ones.

For comparison, this is Jenkins today:

- The median build time on the main application is 38 minutes. A developer gets maybe four or five full runs a day.
- About 12% of builds fail for reasons unrelated to the code. Most of these are agents that have no disk space left or lose their connection. People have learned to press retry.

## What it costs

- I estimate 6 weeks for 2 engineers to move all build and test jobs. If the GPU runners slip, this estimate does not include the two GPU repositories.
- Hosted runner minutes for all 41 repositories come to roughly $1,200 per month, based on the pilot usage. The two Jenkins machines cost about $700 per month today. The difference is about $500 more per month.

## What happens if we do nothing

The next Jenkins LTS line breaks at least nine of our plugins. Two of those plugins have open CVEs today. That leaves two choices:

- We run a CI system that holds deployment credentials and gets no security fixes.
- We spend an unknown amount of time on the upgrade anyway.

## The other options

- GitLab CI would mean that we move our code hosting too. Nobody wants that.
- CircleCI was comparable in speed in a one-day test. It would be a second vendor to manage next to GitHub. The price was higher, about $1,900 per month for the same usage.

I looked at both only briefly.

## What can go wrong, and how we go back

I am less sure about two parts:

- Two repositories run GPU tests. These tests cannot run on hosted runners, so they need self-hosted runners. We have not set up self-hosted runners before. This part may not be ready in the same time frame as the rest, and it could need more work than we think.
- Jenkins credentials hold about 40 secrets. We have not tested the move of these secrets. Some are shared between jobs in ways that nobody fully remembers.

If something goes badly, there is a way back. We would keep Jenkins in read-only mode for 30 days after the last repository moves. In that time, any repository can go back to its old job when we revert one pull request.

## What this proposal does not cover

This proposal covers build and test only. Deployments would stay on Jenkins for now. We would look at the deployment pipelines next quarter.

## Background

- We set up Jenkins in 2019, when the company had three repositories. It has served us well.
- Today 41 repositories build on it, with about 300 jobs.
- Whoever has time looks after the two controller machines. In practice that has been me and one other engineer.
- Over the years we have collected 60-odd plugins. Some of them are no longer maintained.
- We discussed this topic in the last few platform syncs.

I can explain any part of this in person.

Cut candidates: the Background section (the history since 2019, the job count, the platform syncs), the offer to explain in person.
