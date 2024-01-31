from crawler import Crawler
import time

prev = []  # list current news
cur = [] # list before 10sec news
while True:
    cur = Crawler().oil() # save current news
    
    if prev == cur: # if no change > continue
        time.sleep(10)
        continue
    
    prev = cur.copy() # else > update prev list

    # =========================== telegram code



    # ===========================

    time.sleep(10)