#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import telepot
from telepot.loop import MessageLoop

"""
After **inserting token** in the source code, run it:
```
```
[Here is a tutorial](http://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/)
teaching you how to setup a bot on Raspberry Pi. This simple bot does nothing
but accepts two commands:
- `/roll` - reply with a random integer between 1 and 6, like rolling a dice.
- `/time` - reply with the current time, like a clock.
"""

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print("Got command: " + str(command))

bot = telepot.Bot('525287946:AAF0eR_Gtu8f0TEM1SQZ2qyG4qixI8NqDhE')

MessageLoop(bot, handle).run_as_thread()
print ("I am listening ...")

while 1:
    time.sleep(10)