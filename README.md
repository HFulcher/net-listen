# Network Connection Notifier
## Intro
Simple Python script that checks for a MAC address on the local network specified in a .env file. Little afternoon project to see if this could be used as a way to notify that someone has arrived at home. Inspiration is from [Kalle Hallden's automation video](https://github.com/KalleHallden/reddit_automations), he made a good starting place but think I've made it a bit cleaner.

The notification system uses [Klaxon](https://github.com/knowsuchagency/klaxon) to create MacOS notifications. Running this on non-Mac machines will cause issues. This will be fixed in future.

The .env file to specify MAC address and person name is handled using [Decouple](https://github.com/henriquebastos/python-decouple).


## Setup
* Install a virtual environment using requirements.txt
* Install arp-scan `brew install arp-scan`
* Create a `.env` file and specify `DEVICE=xx:xx:xx:xx:xx:xx`. Make sure characters are in lower case
* Specify `PERSON` as the name to include in notification


## Contribute
This is a very small project so I doubt any contributions will happen. But if you are interested take a look at the ideas below for inspiration or suggest your own. Fork, contribute and submit a PR!


## Ideas
* Be able to monitor multiple devices
* Have integration with home smart kits
* Make it Windows/Linux friendly