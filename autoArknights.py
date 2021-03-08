# -*- encoding=utf8 -*-
__author__ = "l6754"

from airtest.core.api import *
from MyFangzhouZhushou import * 
from startLeidian import *
# from config import *
auto_setup(__file__)
# dev = connect_device("Android://127.0.0.1:5037/emulator-5558")
# begintion()
links = [
        "Android://127.0.0.1:5037/emulator-5558",   # 貌似
        "Android://127.0.0.1:5037/emulator-5556", # 天生
#         "Android://127.0.0.1:5037/emulator-5558"    # 貌似
        ]
account = MyFangzhouZhushou()
flag = False
# flag = True
if flag:
#     start_leidian()
    for link in links:
        dev = connect_device(link)
        account.startZhuShou()
        account.startLoginFangZhou()
        account.after_login()
sleeptime = 3600*3.5
# sleep(sleeptime)


for link in links:
    dev = connect_device(link)
    account.factorying()
    account.friendstion()
    account.credit()
    account.recruition()
    account.tasktion()
    sleep(3600*1.5)
account.end()
# sleep(3600*3)
# for link in links:
#     dev = connect_device(link)
#     account.factorying()
#     account.friendstion()
#     account.credit()
#     account.recruition()
#     account.tasktion()
# account.end()
