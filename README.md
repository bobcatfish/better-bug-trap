# Building a better bug trap with GitHub Actions

[Manning Twitch stream Jan 12, 2022](https://www.twitch.tv/manningpublications/schedule?seriesID=01d815ee-ca4a-4dae-8685-58289a711578)

Learn how to automate one of the two pieces of Continuous Delivery: always keeping your codebase in a releasable state. We’ll use GitHub actions to explore the lifecycle of a change, discover all the places where bugs can squirm their way in, and learn the best times to run your pipelines for the most effective bug-catching!

Overall goal: Always be in a releasable state (one of the 2 pieces of CD)

Go from a repo with no automation to a repo with:
* PR based automation
* Post-merge PR based automation
* Periodic automation

Setup automation to:
* Run unit tests

Demonstrate why you need:
* PR based automation - show getting the repo into a broken state
* Post-merge based - show example of conflicting changes making main broken
* Periodic automation - can highlight conflicting changes and catch flakes

What's still missing? (could explore if time)
* Demonstrating flakes being caught
* Build image & run system test
* Release automation (e.g. tag based)
* Linting

## Outline

1. Repo with a service that gets rates, includes dockerfile
1. Show a PR that breaks the repo ([1_bad_pr](https://github.com/bobcatfish/better-bug-trap/tree/1_bad_pr))
1. Add github action to run tests ([2_add_pr_tests](https://github.com/bobcatfish/better-bug-trap/tree/2_add_pr_tests))
1. Show how this fixes the original PR problem
1. Show 2 conflicting PRs and how a bug isn’t caught ([3_bad_pr_1](https://github.com/bobcatfish/better-bug-trap/tree/3_bad_pr_1), [3_bad_pr_2](https://github.com/bobcatfish/better-bug-trap/tree/3_bad_pr_2))
1. Add periodic action to highlight issue ([4_periodic](https://github.com/bobcatfish/better-bug-trap/tree/4_periodic))
1. Undo conflicting PRs
1. Open PRs again
1. Show requiring branch to be up to date ([docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#require-status-checks-before-merging))
1. Explain downsides (many PRs = many updates)
1. Undo requiring branch to be up to date
1. Show post merge action ([5_post_merge](https://github.com/bobcatfish/better-bug-trap/tree/5_post_merge))
1. Describe merge queues / merge trains ([GitHub merge queue docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/using-a-merge-queue))

## Building and running the image

```bash
docker build --tag coin-rates .
docker run -p 80:5000 coin-rates
```

Accessing in browser:

* http://localhost/?coin_type=catcoin
* http://localhost/?coin_type=dogcoin
