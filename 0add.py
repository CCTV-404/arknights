# -*- encoding=utf8 -*-
__author__ = "l6754"    
import sys
sys.path.append("D:\airtest_workplace\autoArknights.air")
from airtest.core.api import *
# from MyFangzhouZhushou import *
# from myvars import *
# from startLeidian import *

auto_setup(__file__)
# from apscheduler.schedulers.blocking import BlockingScheduler

# start_leidian()   
links = [

         "127.0.0.1:5037/emulator-5558", # 貌似我健忘
        "127.0.0.1:5037/emulator-5556",   # 天生
        ]

dev = connect_device("Android://127.0.0.1:5037/emulator-5558")
dev2 = connect_device( "Android://127.0.0.1:5037/emulator-5556")
print("*********************************")
print(G.DEVICE_LIST)
while True:
    set_current(0)
    if exists(Template(r"tpl1605375401635.png", threshold=0.8500000000000001, rgb=True, record_pos=(0.115, -0.198), resolution=(1280, 720))):
        touch(Template(r"tpl1605375420242.png", record_pos=(0.351, 0.17), resolution=(1280, 720)))
    set_current(1)
    if exists(Template(r"tpl1605375401635.png", threshold=0.8500000000000001, rgb=True, record_pos=(0.115, -0.198), resolution=(1280, 720))):
        touch(Template(r"tpl1605375420242.png", record_pos=(0.351, 0.17), resolution=(1280, 720)))
    sleep(3)

