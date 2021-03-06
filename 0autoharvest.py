# -*- encoding=utf8 -*-
__author__ = "l6754"    
import sys
sys.path.append("D:\airtest_workplace\autoArknights.air")
from airtest.core.api import *
from MyFangzhouZhushou import *
# from myvars import *
from startLeidian import *
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import datetime
import logging
auto_setup(__file__)
# from apscheduler.schedulers.blocking import BlockingScheduler

# start_leidian()   
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
     datefmt='%Y-%m-%d %H:%M:%S',
     filename='log1.txt',
     filemode='a')
def my_work(id = 'my_work'):
    links = [
        "Android://127.0.0.1:5037/emulator-5556",   # 天生
         "Android://127.0.0.1:5037/emulator-5558" # 貌似我健忘
        ]
    account = MyFangzhouZhushou()
    for link in links:
        dev = connect_device(link)
        if account.factorytion():
            sleep(8)
            account.harvestion()
#             self.tradetion()
#             self.experiencetion()
#             self.electriction()
#             self.coretion()
#             self.parlortion()
#             self.workingtion()
#             self.roomtion()
            account.back_home()
#         account.auto_fight()
    del account
def my_job(id='my_job'):
    print (id,'-->',datetime.datetime.now())
scheduler = BlockingScheduler()
# scheduler.add_job(func=work, args=('一次性任务,会出错',), next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=15), id='date_task')
# scheduler.add_job(my_work, args=['job_once_now',],id='job_once_now')
scheduler.add_job(my_work, 'interval', minutes=30, args=['result'])
# scheduler.add_job(my_work, 'cron', hour='2,3', minute='0', args=['result'])
# scheduler.add_job(func=func, args=('循环任务',), trigger='interval', hour=3, id='interval_task')
# scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
# scheduler._logger = logging
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown() 
