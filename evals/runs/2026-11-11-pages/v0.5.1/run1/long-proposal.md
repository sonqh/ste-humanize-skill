# Proposal: move build and test from Jenkins to GitHub Actions

I ask you to approve this move for all 41 repositories. I need your decision by 28 November.

- The work: 2 engineers for 6 weeks, by my estimate.
- The cost: about $500 more per month.
- The date: our Jenkins LTS line stops getting security fixes at the end of March. A decision by 28 November lets the work finish before then, with some room to spare.
- The scope: build and test only. Deployments stay on Jenkins for now. We look at them next quarter.

## Why we cannot stay as we are

- Security. The upgrade to the next LTS line breaks at least nine of our plugins. Two of them have open CVEs today.
- If we do nothing, we have two outcomes. We run an unpatched CI system that holds deployment credentials, or we spend an unknown amount of time on the upgrade anyway.
- Speed. The median build time on the main application is 38 minutes. A developer gets maybe four or five full runs a day.
- Reliability. About 12% of builds fail for reasons that have nothing to do with the code. Most of these are agents that run out of disk or lose their connection. People have learned to press retry.
- Upkeep. We set up Jenkins in 2019 for three repositories, and it has served us well. Today it builds 41 repositories with about 300 jobs.
- Whoever has time looks after the two controller machines. In practice that is me and one other engineer. We have collected 60-odd plugins, and some are no longer maintained.

## What the pilot showed

For five weeks, three repositories built on GitHub Actions in parallel with Jenkins: the web app, the billing service, and the docs site.

- The median build time went from 38 minutes to 14 minutes. Most of the gain came from better caching and parallel test shards.
- The rate of failures unrelated to code went from 12% to 3%.
- Developers on those teams told us they do not want to go back.

Three repositories is a small sample, and they are among our simpler ones.

## Cost

| Item | Per month |
|---|---|
| Hosted runner minutes for all 41 repositories, based on the pilot usage | roughly $1,200 |
| The two Jenkins machines today | about $700 |
| Difference | about $500 more |

The 6 weeks cover all build and test jobs. They do not count the GPU repositories if the runners slip.

## What I am less sure about

- GPU tests. Two repositories run GPU tests, and those cannot run on hosted runners. They need self-hosted runners, which we have not set up before. This part may not be ready in the same time frame as the rest, and it could need more work than we think.
- Secrets. We have about 40 secrets in Jenkins credentials, and we have not tested moving them. Some are shared between jobs in ways nobody fully remembers.

## If something goes badly

We keep Jenkins in read-only mode for 30 days after the last repository moves. Any repository can go back to its old job when we revert one pull request.

## Other options I looked at briefly

- GitLab CI. It would mean moving our code hosting too, which nobody wants.
- CircleCI. It was comparable in speed in a one-day test. It would be a second vendor to manage next to GitHub. The price was higher, at about $1,900 per month for the same usage.

I can walk you through any of this in person.

Cut candidates: the 2019 history of Jenkins, the count of 300 jobs and 60-odd plugins, the GitLab CI option.
