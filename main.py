from crawler import Crawler
import time
import telegram
import asyncio

prev = []  # list current news
cur = [] # list before 10sec news
bot = telegram.Bot(token="6775298069:AAHjq49Sui3-mitDJ-siLIKmP6TD1gle1oo")

while True:
    try:
        cur = Crawler().oil() # save current news
        
        if prev == cur: # if no change > continue
            print("no change")
            asyncio.run(bot.send_message(chat_id = "-1002139751230", text="No change for now"))
            time.sleep(30)
            continue
        # if changed
        # =========================== telegram code
        for title in cur:
            if title not in prev:
                asyncio.run(bot.send_message(chat_id = "-1002139751230", text="Changed!!"))
                print("sent a message")
        # ===========================
        prev = cur.copy()
        time.sleep(30)
    except Exception as e:
        time.sleep(30)
        continue
