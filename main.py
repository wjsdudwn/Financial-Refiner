from crawler import Crawler
import time
import telegram

prev = []  # list current news
cur = [] # list before 10sec news
bot = telegram.Bot(token="6775298069:AAHjq49Sui3-mitDJ-siLIKmP6TD1gle1oo")

while True:
    try:
        cur = Crawler().oil() # save current news
        
        if prev == cur: # if no change > continue
            time.sleep(10)
            print("no change")
            bot.send_message(chat_id = "-1002139751230", text="dd")
            continue
        # if changed
        # =========================== telegram code
        for title in cur:
            if title not in prev:
                bot.send_message(chat_id = "-1002139751230", text="dd")
                print("sent a message")
        # ===========================
        prev = cur.copy()
        time.sleep(10)
    except Exception as e:
        time.sleep(3)
        continue
