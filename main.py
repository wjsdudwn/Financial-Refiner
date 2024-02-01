from crawler import Crawler
import time
import telegram

prev = []  # list current news
cur = [] # list before 10sec news

while True:
    cur = Crawler().oil() # save current news
    
    if prev == cur: # if no change > continue
        time.sleep(10)
        continue
    
    prev = cur.copy() # else > update prev list

    # =========================== telegram code
    bot = telegram.Bot(token="6775298069:AAHjq49Sui3-mitDJ-siLIKmP6TD1gle1oo")
    bot.send_message(chat_id = "1002139751230", text="Hello world")


    print("Sent a message")
    # ===========================

    time.sleep(10)

bot = telegram.Bot(token="6775298069:AAHjq49Sui3-mitDJ-siLIKmP6TD1gle1oo")
bot.send_message(chat_id = 1002139751230, text="Hello world")
print("Sent a message")