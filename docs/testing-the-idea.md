# Testing the Intention of Classroom Bot

When we recieved the Classroom Bot, we quickly realized that it was difficult to actually run the Classroom Bot and develop against it locally. Everything (including linting!) was done by creating ephemeral docker containers.

Our team decided that for this project to be viable, we needed to make it easier to for a developer to 
* run the code locally
* debug the code locally
* setup a reverse proxy to communicate with Slack
* minimize number of tools/languages required

## How?

We would like to evaluate if we have improved on these measurements from our efforts. How we would like to evaluate this is by performing a simple experiment to measure how quickly a developer can perform the following actions:

* download the repository
* run the entire solution on a developer's laptop
* login to the UI
* create a new Slack bot
* setup a reverse proxy
* have that slash command send data via a reverse-proxy to a running server on the developers laptop

Our goal is that a new developer should be able to do this in roughly 20 minutes. 

## What to Measure?

### Pre-Test
* has the developer ever used Slack bots before?
* has the developer ever used Django before?
* has the developer ever used reverse proxy before?

### Measurements
* how long it took to download the repo?
* how long it took to run the entire software solution?
* how long it took to login to the admin UI?
* how long it took to create a new Slack bot in a Slack workspace?
* how long it took to setup a reverse proxy?
* how long it took to setup and run a slashcommand in Slack

Additionally,
* how many mistakes were made?
* did the developer have to ask many questions?

### Suggested Analysis

* min, median, max of each time
* min, median, max of the total time
* min, median, max of mistakes made
* min, median, max of questions asked

Additionally,
* co-variance between
    * Django experience and total time
    * Slack experience and total time
    * Reverse proxy experience and total time
    

