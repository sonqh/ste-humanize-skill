# Proposal: move build and test from Jenkins to GitHub Actions

I ask for approval to move build and test for all 41 repositories from Jenkins to GitHub Actions. The cost is 2 engineers for 6 weeks and about $500 more per month. I need a decision by 28 November. Then the work finishes before the end of March, with some room to spare.

## Why now

- Our Jenkins LTS line gets no security fixes after the end of March.
- The upgrade to the next line breaks at least nine of our plugins. Two of those have open CVEs today.
- If we do nothing, we have two options. We run an unpatched CI system that holds deployment credentials, or we spend an unknown amount of time on the upgrade anyway.
- The median build time on the main application is 38 minutes. A developer gets maybe four or five full runs a day.
- About 12% of builds fail for reasons that have nothing to do with the code. Mostly an agent runs out of disk or loses its connection. People have learned to press retry.
- Jenkins has grown since we set it up in 2019 for three repositories. It has served us well. Today it builds 41 repositories with about 300 jobs and 60-odd plugins, and some of those plugins are no longer maintained.
- Whoever has time looks after the two controller machines. In practice that is me and one other engineer.

## What the pilot showed

For five weeks, three repositories built on GitHub Actions in parallel with Jenkins: the web app, the billing service, and the docs site.

| Measure | Jenkins | GitHub Actions |
|---|---|---|
| Median build time | 38 minutes | 14 minutes |
| Failures unrelated to code | 12% | 3% |

Better caching and parallel test shards gave most of the gain in build time. Developers on those teams told us they do not want to go back. Three repositories is a small sample, and they are among our simpler ones.

## Cost

- Hosted runner minutes for all 41 repositories come to roughly $1,200 per month. This number comes from the pilot usage.
- The two Jenkins machines cost about $700 per month today. The difference is about $500 per month.
- I estimate 6 weeks for 2 engineers to move all build and test jobs. This estimate does not count the GPU repositories if the runners slip.

## What I am less sure about

- Two repositories run GPU tests, and those tests cannot run on hosted runners. They need self-hosted runners, which we have not set up before. This part may not be ready in the same time frame as the rest. It could need more work than we think.
- We have about 40 secrets in Jenkins credentials, and we have not tested how to move them. Jobs share some of them in ways nobody fully remembers.
- Deployment pipelines are not part of this proposal. Deployments stay on Jenkins for now, and we look at them next quarter.

## If something goes badly

We keep Jenkins in read-only mode for 30 days after the last repository moves. In that time, any repository can go back to its old job if we revert one pull request.

## Alternatives

I looked briefly at two other products.

- GitLab CI: we would have to move our code hosting too, and nobody wants that.
- CircleCI: its speed was comparable in a one-day test. It would be a second vendor to manage next to GitHub. The price was higher, at about $1,900 per month for the same usage.

I can go through any of this with you in person.

Cut candidates: the Jenkins history since 2019, the plugin count, who looks after the controller machines, the Alternatives section, the offer to meet.
