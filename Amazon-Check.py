import sys
import re
import requests
import UserAgent
import time
import smtplib
import random
from lxml import html
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import telegram
####################### https://www.amazon.ae/dp/B08HHFL27C

def telegram_noti():
    botToken = "<INSERT BOT TOKEN HERE>"
    chatid = "<INSERT CHAT ID HERE>"
    bot = telegram.Bot(botToken)
    msg = "<INSERT BOT MSG HERE>"
    bot.send_message(chat_id=chatid, text=msg)
    print ("Message sent to Telegram")


def send_email():
    s = smtplib.SMTP("smtp.gmail.com:587")
    s.ehlo()
    s.starttls()
    s.login("<EMAIL TO SEND FROM>","<PASSWORD>")
    print ("Composing email...")

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "<EMAIL SUBJECT>"
    msg['From'] = "<EMAIL FROM>"
    msg['To'] = "<EMAIL TO>"

    text = "<EMAIL TEXT>"
    part = MIMEText(text, 'plain')
    msg.attach(part)
    s.sendmail("<EMAIL FROM>","<EMAIL TO>", msg.as_string())
    print ("Email sent")




def available(url, notification_choice):
    print ("Checking....")
    ua = UserAgent.UserAgent()

    r = requests.get(url,headers= {'User-Agent': ua.random()})
    print ("Status code: ", r.status_code)
    tree = html.fromstring(r.content)
    Amazon_Price = tree.xpath('//span[@id="priceblock_ourprice"]/text()')
    if not Amazon_Price:
        print ("Still not available")
    else:
        print ("found")
        if notification_choice == 1:
            telegram_noti()
            telegram_noti()
            telegram_noti()
            sys.exit(0)
        elif notification_choice == 2:
            send_email()
            sys.exit(0)
        elif notification_choice == 3:
            telegram_noti()
            telegram_noti()
            telegram_noti()
            send_email()
            sys.exit(0)
        else:
            send_email()
            sys.exit(0)

print ("Please enter the url")
amazon_url = input()
print ("Enter 1 for telegram, 2 for email, 3 for both - default option is email")
notification_choice = int(input())
attempt = int(1)
timez= int(150)

while True:
    available(amazon_url, notification_choice)
    interval_time = timez + random.randint(0,100)
    print ("sleeping for: ",interval_time," seconds....")
    time.sleep(interval_time)
    print (" ")
    attempt+=1
    print ('Attempt #',attempt)
