from crawler import Crawler
import time
import telegram
import asyncio

cur = []  # list current news
prev = [] # list before 30sec news


while True:
        
    cur = Crawler().oil() # save current news
    
    if prev == cur: # if no change > continue
        print("no change")
        # asyncio.run(bot.send_message(chat_id = "-1002139751230", text="No change for now"))
        time.sleep(30)
        continue
    # if changed
    # =========================== telegram code
    for title in cur:
        if title not in prev:
            bot = telegram.Bot(token="6775298069:AAHjq49Sui3-mitDJ-siLIKmP6TD1gle1oo")
            asyncio.run(bot.send_message(chat_id = "-1002139751230", text=title))
            print("sent a message")
    # ===========================
    prev = cur.copy()
    time.sleep(10)
