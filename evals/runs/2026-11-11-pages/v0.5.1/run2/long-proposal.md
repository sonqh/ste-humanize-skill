# Proposal: move build and test from Jenkins to GitHub Actions

I ask you to approve the move of build and test for all 41 repositories from Jenkins to GitHub Actions.

- The work needs 2 engineers for 6 weeks.
- The running cost increases by about $500 per month.
- I need your decision by 28 November. Then the work finishes before the end of March, with some room to spare.

This proposal covers build and test only. Deployments stay on Jenkins for now, and we look at them next quarter.

## Why now

The Jenkins LTS line that we use gets no security fixes after the end of March. An upgrade to the next line breaks at least nine of our plugins. Two of those nine have open CVEs today. If we do nothing, one of two things occurs:

- We run an unpatched CI system that holds deployment credentials.
- We spend an unknown amount of time on the upgrade anyway.

Jenkins also costs us time each day. We discussed these problems in the last few platform syncs.

- The median build time of the main application is 38 minutes. A developer gets maybe four or five full runs a day.
- About 12% of builds fail for reasons that have nothing to do with the code. Most of these failures are agents that have no disk space left or that lose their connection. People have learned to press retry.
- We set up Jenkins in 2019 for three repositories, and it has served us well. Today two controller machines build 41 repositories with about 300 jobs.
- Whoever has time looks after the two machines. In practice that is me and one other engineer.
- We have collected 60-odd plugins. Some of them are no longer maintained.

## What the pilot showed

For five weeks, three repositories have built on GitHub Actions in parallel with Jenkins: the web app, the billing service, and the docs site.

| On those three repositories | Jenkins | GitHub Actions |
|---|---|---|
| Median build time | 38 minutes | 14 minutes |
| Builds that fail for reasons unrelated to code | 12% | 3% |

Better caching and parallel test shards gave most of the time gain. Developers on those teams have told us that they do not want to go back. Three repositories is a small sample, and they are among our simpler ones.

## Cost

- Hosted runner minutes for all 41 repositories come to roughly $1,200 per month. I based this on the pilot usage.
- The two Jenkins machines cost about $700 per month today.
- The difference is about $500 per month more.
- I estimate 6 weeks for 2 engineers to move all build and test jobs. This estimate does not include the GPU repositories if their runners are late.

## What I am less sure about

- Two repositories run GPU tests, and those tests cannot run on hosted runners. They need self-hosted runners, which we have not set up before. This part may not be ready in the same time frame as the rest. It could need more work than we think.
- Jenkins credentials hold about 40 secrets, and we have not tested how to move them. Jobs share some of them in ways that nobody fully remembers.

## If something goes badly

We keep Jenkins in read-only mode for 30 days after the last repository moves. In that time, any repository can go back to its old job if we revert one pull request.

## Other options

I also looked briefly at two other products.

- GitLab CI would make us move our code hosting too, and nobody wants that.
- CircleCI had comparable speed in a one-day test. It would be a second vendor to manage next to GitHub. Its price was higher, at about $1,900 per month for the same usage.

I can go through any of this with you in person.

Cut candidates: the 2019 history, the platform syncs, the plugin count, the GitLab CI option, the offer to meet in person.
