# -*- encoding=utf8 -*-
__author__ = "l6754"

# from airtest.core.api import *
# from startLeidian import *
# from MyFangzhouZhushou import *
from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler
auto_setup(__file__)

def tick():
    start_leidian()   
    links = ["Android://127.0.0.1:5037/emulator-5556",   # 天生
         "Android://127.0.0.1:5037/emulator-5558" # 貌似我健忘
        ]
    account = MyFangzhouZhushou()
    for link in links:
        dev = connect_device(link)
        account.startZhuShou()
        account.startLoginFangZhou()
        account.recruition()
        account.friendstion()
        account.credit()
        account.factorying()
        account.tasktion()
        account.auto_fight()

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'cron', hour=5,minute=0)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass