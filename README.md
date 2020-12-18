# Amazon-Availability-Checker
> python script that checks for the availability of a specific product on amazon 

A simple python script that uses telegram bot library and smtp to notify users of when a specified product becomes available on amazon, best used for products that go in and out of stock quickly 

## Installation

OS X & Linux:

```sh
git clone https://github.com/ababhair/Amazon-Availability-Checker
```

## Usage example
```sh
python3 Amazon-Check.py
```

## Development setup

The following script requires these python3 libraries that can be installed using pip3
```sh
python-telegram-bot
lxml
```
Multiple variable should be edited within the script to succesfully send notifications to an email or a telegram bot, these variables include:

```sh
Telegram bot variables
botToken = "<INSERT BOT TOKEN HERE>"
chatid = "<INSERT CHAT ID HERE>"
msg = "<INSERT BOT MSG HERE>"
```
```sh
smpt variables
s.login("<EMAIL TO SEND FROM>","<PASSWORD>")
msg['Subject'] = "<EMAIL SUBJECT>"
msg['From'] = "<EMAIL FROM>"
msg['To'] = "<EMAIL TO>"
text = "<EMAIL TEXT>"
s.sendmail("<EMAIL FROM>","<EMAIL TO>", msg.as_string())
```
The interval by which the script checks for availability can be changed by changing the following variable (Note: To avoid being banned from amazon, it is recommended that the interval stays at 150 seconds)
```sh
timez= int(150)
```
To create a telegram bot, please refer to the telegram [Wiki][wiki]._
## Future work
* Create a json file to grab variables from rather than editing the script
* Add more notification options
* Add Price check feature

[wiki]: https://core.telegram.org/bots/api
