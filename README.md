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
* Build artifact (skipping pushing to avoid handling secrets in livestream)
* Run system tests using artifact

Demonstrate why you need:
* PR based automation - show getting the repo into a broken state
* Post-merge based - show example of conflicting changes making main broken
* Periodic automation - can highlight conflicting changes and catch flakes

What's still missing?
* Linting
* Actually pushing artifacts
* Release automation (e.g. tag based)
* Demonstrating flakes being caught
