from airtest.core.api import *
from myvars import *
from time import sleep
# from jiaoben import next_turn_num,turn_num
# from config import *

def skippable_wait_touch(target_skipple_wait,timeout =  10):
    try :
        position = wait(target_skipple_wait,timeout = timeout)
        touch(position)
        return True
    except BaseException:
        return False
class MyFangzhouZhushou():
    file_name = "./truns.txt"
    def __init__(self):
        turn_file = open(self.file_name,'r+')
        line_1 = turn_file.readline()
        self.turn_num = int(line_1)
        line_2 = turn_file.readline()
        turn_file.close()
        self.next_turn_num = (self.turn_num+1) % 3
    def __del__(self):
#         class_name = self.__class__.__name__
#         turn_file = open(self.file_name,'w+')
#         turn_file.truncate(0)
#         turn_file.write(str(self.next_turn_num))
#         turn_file.close()  
        pass
    def end(self):
        turn_file = open(self.file_name,'w+')
        turn_file.truncate(0)
        turn_file.write(str(self.next_turn_num))
        turn_file.close()  
    def find_swip_recovery(self,find_role,timeout = 5):
        flag = False
        while not skippable_wait_touch(find_role,timeout):

            swipe(Template(r"z笑脸.png", record_pos=(-0.021, 0.183), resolution=(1280, 720)),vector=[-0.4, 0])
            flag = True
            sleep(2)
        if flag:
            flag = self.recovery()
            
    def startZhuShou(self):# 启动方舟助手
        start_app("com.fangzhouai")
        sleep(5)
        skippable_wait_touch(Template(r"z启动辅助.png", record_pos=(0.0, 0.835), resolution=(720, 1280)),timeout=15)
    def startGame(self):

        self.startZhuShou()
        self.startLoginFangZhou()

    def startLoginFangZhou(self):# 启动和登陆登陆
        start_app("com.hypergryph.arknights",activity=None)
        if exists(Template(r"z公开招募.png", record_pos=(0.291, 0.112), resolution=(1280, 720))):
            return
        skippable_wait_touch(Template(r"zSTART.png", record_pos=(-0.006, 0.245), resolution=(1280, 720)),timeout=100)
        skippable_wait_touch(Template(r"z开始唤醒.png", record_pos=(-0.001, 0.122), resolution=(1280, 720)),timeout=100)

        sleep(3)
        if exists(Template(r"z记忆模糊.png", record_pos=(0.004, 0.043), resolution=(1280, 720))):
            touch(Template(r"z黑色圆对号.png", record_pos=(0.003, 0.115), resolution=(1280, 720)))
            sleep(3)
            
        if skippable_wait_touch(Template(r"z账号登录.png", record_pos=(-0.177, 0.114), resolution=(1280, 720)),timeout=5):
            touch(Template(r"z密码.png", record_pos=(0.003, 0.094), resolution=(1280, 720)))
            text("123456789")
            touch(Template(r"z确定.png", record_pos=(0.434, 0.218), resolution=(1280, 720)))
            touch(Template(r"z登录.png", record_pos=(0.003, 0.167), resolution=(1280, 720)))
        sleep(20)
            
    def after_login(self):
        sleep(5)
        while exists(Template(r"z关闭.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720))):
            if exists(Template(r"z领取.png", threshold=0.6999999999999998, rgb=False, target_pos=5, record_pos=(0.372, -0.044), resolution=(1280, 720))):
                skippable_wait_touch(Template(r"z领取.png", threshold=0.6999999999999998, rgb=False, record_pos=(0.372, -0.044), resolution=(1280, 720)))
                skippable_wait_touch(Template(r"z悬浮圆对号.png", record_pos=(-0.001, 0.216), resolution=(1280, 720)))
            
            skippable_wait_touch(Template(r"z关闭.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)))
            sleep(5)
            touch((0.2,0.2))
            sleep(5)

        skippable_wait_touch(Template(r"z空白.png", record_pos=(0.004, -0.212), resolution=(1280, 720)),timeout=10)
        skippable_wait_touch(Template(r"z关闭.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),timeout=10)
        if skippable_wait_touch(Template(r"z邮件.png", threshold=0.95, rgb=True, record_pos=(-0.345, -0.256), resolution=(1280, 720)),timeout = 3):
            sleep(3)
            skippable_wait_touch(Template(r"z邮件收取所有邮件.png", record_pos=(0.388, 0.237), resolution=(1280, 720)),timeout=5)
            sleep(3)
            skippable_wait_touch(Template(r"z悬浮圆对号.png", record_pos=(0.001, 0.221), resolution=(1920, 1081)))
            sleep(3)

            skippable_wait_touch(Template(r"z白色返回.png", record_pos=(-0.431, -0.247), resolution=(1280, 720)),timeout = 3)
            sleep(3)
    def recovery(self):
        skippable_wait_touch(Template(r"z1选择清单.png", record_pos=(0.42, -0.25), resolution=(1280, 720)))

        sleep(1)
        skippable_wait_touch(Template(r"z1未进驻.png", record_pos=(-0.158, -0.001), resolution=(1280, 720)))
        skippable_wait_touch(Template(r"z蓝色对号.png", record_pos=(0.237, 0.148), resolution=(1280, 720)))

        sleep(1)
        skippable_wait_touch(Template(r"z1选择清单.png", record_pos=(0.42, -0.25), resolution=(1280, 720)))

        sleep(1)
        skippable_wait_touch(Template(r"z1未进驻-蓝色.png", record_pos=(-0.159, -0.001), resolution=(1280, 720)))
        sleep(1)
        skippable_wait_touch(Template(r"z蓝色对号.png", record_pos=(0.237, 0.148), resolution=(1280, 720)))
        sleep(1)
        return False
    def recruition(self):# 公开招募
        sleep(4)
        if skippable_wait_touch(Template(r"z公开招募.png", record_pos=(0.291, 0.112), resolution=(1280, 720))):

            while skippable_wait_touch(Template(r"z聘用候选人.png", record_pos=(0.236, 0.017), resolution=(1280, 720)),timeout=5):
                skippable_wait_touch(Template(r"z跳过.png", record_pos=(0.453, -0.248), resolution=(1280, 720)),timeout=8)
                sleep(5)
                touch((0.1,0.9))
                sleep(2)
#             for i in range(0,len(recruit_position_group)): # len(recruit_position_group)
#                 if skippable_wait_touch(recruit_position_group[i],timeout=3):
#                     collection = ()
#                     for index in range(len(recruit_pic_group)):
#                         if exists(recruit_pic_group[index]):
#                             collection += (index,)
#                             print(index)
#                             print("========================================================================")
#                             print(collection)   
#                     temp_file = open('./recruit_log.txt','a+')
#                     temp_file.write(" ".join(map(str,collection)) + "\r")
#                     print(recruit)
#                     for recruit_item in recruit:
#                         if recruit_item in collection:
#                             for temp_item in recruit_item:
#                                 skippable_wait_touch(temp_item)
#                             skippable_wait_touch(Template(r"z蓝色圆对号.png", record_pos=(0, 0), resolution=(1280, 720)))
#                             sleep(2)
#                             print("***************************************************************************************")
#                             print(recruit_item)
#                             temp_file.write(str(recruit_item) + " yes \r")
#                             break
#                     temp_file.close()
#                     skippable_wait_touch(Template(r"z返回.png", record_pos=(-0.463, -0.252), resolution=(1280, 720)))
        skippable_wait_touch(Template(r"z返回.png", record_pos=(-0.463, -0.252), resolution=(1280, 720)))

        sleep(5)
    def tasktion(self):# 任务
        sleep(5)
        if skippable_wait_touch(Template(r"z任务.png", record_pos=(0.119, 0.18), resolution=(1280, 720))):
            while skippable_wait_touch(Template(r"z点击领取.png", threshold=0.95, rgb=True, record_pos=(0, 0), resolution=(1280, 720)),timeout=8):
                while exists(Template(r"z空白.png", record_pos=(0.004, -0.212), resolution=(1280, 720))):
                    touch(Template(r"z空白-黑色.png", record_pos=(-0.003, -0.105), resolution=(1280, 720)))
                sleep(2)
            skippable_wait_touch(Template(r"z返回.png", record_pos=(-0.463, -0.252), resolution=(1280, 720)))
        sleep(5)
        
    def friendstion(self):# 信用，访问好友
        sleep(5)
        if skippable_wait_touch(Template(r"z好友.png", record_pos=(-0.224, 0.165), resolution=(1280, 720))):
            sleep(1)
            skippable_wait_touch(Template(r"z好友列表.png", record_pos=(-0.405, -0.108), resolution=(1280, 720)))
            sleep(3)
            skippable_wait_touch(Template(r"z好友访问基建.png", record_pos=(0.277, 0.077), resolution=(1280, 720)))
            sleep(3)
            for i in range(1,12):
                skippable_wait_touch(Template(r"z好友访问下位.png", threshold=0.9000000000000001, rgb=True, record_pos=(0.427, 0.206), resolution=(1280, 720)))
                sleep(1)

                if exists(Template(r"z好友不可以访问下一位.png", threshold=0.8, rgb=True, record_pos=(0.424, 0.21), resolution=(1920, 1081))):
                    break
                if exists(Template(r"z好友交流达到上限.png", record_pos=(0.399, -0.198), resolution=(1280, 720))):

                    break
            skippable_wait_touch(Template(r"z主页菜单.png", threshold=0.9, rgb=True, record_pos=(0, 0), resolution=(1280, 720)))
            skippable_wait_touch(Template(r"z主页首页.png", threshold=0.9, rgb=True, record_pos=(0, 0), resolution=(1280, 720)))
    def credit(self):
        if skippable_wait_touch(Template(r"z采购中心.png", threshold=0.7, rgb=False, record_pos=(0, 0), resolution=(1280, 720))):
            sleep(1)
            if skippable_wait_touch(Template(r"z信用交易所.png", threshold=0.9, rgb=True, record_pos=(0, 0), resolution=(1280, 720))):
                sleep(3)
                skippable_wait_touch((808,67))
                if skippable_wait_touch(Template(r"z收取信用.png", threshold=0.9, rgb=True, record_pos=(0, 0), resolution=(1280, 720)),timeout = 3):
                    
                    sleep(3)   
                    skippable_wait_touch(Template(r"z悬浮圆对号.png", record_pos=(-0.001, 0.216), resolution=(1280, 720)))
                    sleep(3)
                    skippable_wait_touch((808,67))
                    sleep(3)
                
                # 购买信用产品
                for good in cart:
                    while exists(good):
                        if skippable_wait_touch(good,timeout=3):
                            sleep(1)
#                             skippable_wait_touch(Template(r"z返回.png", record_pos=(-0.456, -0.255), resolution=(1280, 720)))
#                             break
                            if skippable_wait_touch(Template(r"z信用购买物品.png", threshold=0.9, rgb=True, record_pos=(0, 0), resolution=(1280, 720))):

                                sleep(2)
                                skippable_wait_touch(Template(r"z悬浮圆对号.png", record_pos=(0.001, 0.221), resolution=(1920, 1081)))
                        sleep(2)
                    sleep(1)
            
#             skippable_wait_touch(Template(r"tpl1603372345111.png", record_pos=(-0.292, -0.253), resolution=(1920, 1081)),timeout = 5)
#             sleep(2)
#             skippable_wait_touch(Template(r"tpl1603372370469.png", record_pos=(0.439, -0.076), resolution=(1920, 1081)))
#             sleep(1)
#             skippable_wait_touch(Template(r"tpl1603372398989.png", record_pos=(0.441, -0.199), resolution=(1920, 1081)))
#             sleep(1)
#             if skippable_wait_touch(Template(r"tpl1603372423435.png", rgb=True, record_pos=(0.301, -0.252), resolution=(1920, 1081))):
#                 sleep(2)
#                 skippable_wait_touch(Template(r"tpl1603372449369.png", record_pos=(0.001, 0.221), resolution=(1920, 1081)))
#             for goods in cart:# 购买信用产品
#                 while exists(goods):
#                     skippable_wait_touch(goods,timeout=3)
#                     skippable_wait_touch(Template(r"tpl1603375195563.png", record_pos=(0.215, 0.17), resolution=(1920, 1081)))

#                     sleep(2)
#                     skippable_wait_touch(Template(r"tpl1603372449369.png", record_pos=(0.001, 0.221), resolution=(1920, 1081)))
#                     sleep(2)
#                 sleep(1)
            skippable_wait_touch(Template(r"z主页菜单.png", record_pos=(-0.29, -0.251), resolution=(1280, 720)))
            sleep(1)
            skippable_wait_touch(Template(r"z主页首页.png", record_pos=(-0.428, -0.075), resolution=(1280, 720)))
            sleep(3)
    def factorying(self):
        if self.factorytion():
            sleep(8)
            self.harvestion()
            self.tradetion()
            self.experiencetion()
            self.electriction()
            self.coretion()
            self.parlortion()
            self.workingtion()
            self.roomtion()
            self.back_home()
    def factorytion(self):# 基建
        return skippable_wait_touch(Template(r"z基建.png", record_pos=(0.268, 0.197), resolution=(1280, 720)),15)
    def harvestion(self):# 收获
        if skippable_wait_touch(Template(r"z基建提醒.png", record_pos=(0.442, -0.171), resolution=(1280, 720)),timeout=15):

            skippable_wait_touch(Template(r"z基建可收获.png", record_pos=(-0.301, 0.264), resolution=(1280, 720)),timeout=3)
            sleep(1)
            skippable_wait_touch(Template(r"z基建订单交付.png", record_pos=(-0.177, 0.26), resolution=(1280, 720)),timeout=3)
            sleep(1)
            skippable_wait_touch(Template(r"z基建干员信赖.png", record_pos=(-0.031, 0.26), resolution=(1280, 720)),timeout=3)
            sleep(1)
            touch((456,186))
            sleep(2)
    def tradetion(self):# 贸易站
        if skippable_wait_touch(Template(r"z贸易站.png", threshold=0.5999999999999999, rgb=True, record_pos=(-0.22, -0.032), resolution=(1280, 720)),timeout=5):
            skippable_wait_touch(Template(r"z贸易站进入.png", record_pos=(-0.129, 0.205), resolution=(1280, 720)))

            skippable_wait_touch(Template(r"z贸易站01.png", record_pos=(-0.43, -0.117), resolution=(1280, 720)))
            if exists(trade_working_groups[self.next_turn_num][0]):
                pass
            else :
                skippable_wait_touch(Template(r"z贸易站02.png", record_pos=(-0.422, -0.05), resolution=(1280, 720)))
            sleep(1)
            if skippable_wait_touch(trade_working_groups[self.next_turn_num][0],timeout=5):
                sleep(1)
                skippable_wait_touch(Template(r"z清空选择.png", record_pos=(-0.098, 0.25), resolution=(1280, 720)))
                sleep(1)

                for i in trade_groups[self.turn_num]:
                    self.find_swip_recovery(i,timeout=3)
                    
                skippable_wait_touch(Template(r"z确认.png", record_pos=(0.427, 0.248), resolution=(1280, 720)))
                sleep(1)

            skippable_wait_touch(Template(r"z返回.png", record_pos=(-0.456, -0.255), resolution=(1280, 720)))
            sleep(3)
            skippable_wait_touch(Template(r"z返回.png", record_pos=(-0.456, -0.255), resolution=(1280, 720)))
    def experiencetion(self):# 制造站
        sleep(3)
        # 狗粮替班
        if skippable_wait_touch(Template(r"z制造站.png", rgb=True, record_pos=(-0.216, 0.094), resolution=(1280, 720))):
            skippable_wait_touch(Template(r"z制造站进入.png", record_pos=(-0.155, 0.198), resolution=(1280, 720)))
            skippable_wait_touch(Template(r"z制造站01.png", rgb=True, record_pos=(-0.448, -0.116), resolution=(1280, 720)))
            if exists(experience_working_goups[self.next_turn_num][1]):
                pass
            else :
                skippable_wait_touch(Template(r"z制造站02.png", record_pos=(-0.442, -0.055), resolution=(1280, 720)))
            sleep(2)
            if skippable_wait_touch(experience_working_goups[self.next_turn_num][1]):
                skippable_wait_touch(Template(r"z清空选择.png", record_pos=(-0.098, 0.25), resolution=(1280, 720)))
                sleep(2)
                for i in experience_goups[self.turn_num]:
                    sleep(1)
                    self.find_swip_recovery(i,timeout=3)
                    
            # 消费电力
                skippable_wait_touch(Template(r"z确认.png", record_pos=(0.427, 0.248), resolution=(1280, 720)))
            sleep(1)
            skippable_wait_touch(Template(r"z制造站消耗电力.png", record_pos=(0.455, 0.141), resolution=(1280, 720)))
            sleep(1)
            skippable_wait_touch(Template(r"z制造站消耗电力最多.png", record_pos=(0.252, -0.022), resolution=(1280, 720)))
            sleep(1)
            skippable_wait_touch(Template(r"z确定蓝色.png", record_pos=(0.244, 0.17), resolution=(1280, 720)))
            sleep(2)
            touch(Template(r"z制造站收获.png", record_pos=(0.383, 0.222), resolution=(1280, 720)))
            sleep(3)
            # 金属替班

            skippable_wait_touch(Template(r"z制造站03.png", record_pos=(-0.423, 0.013), resolution=(1280, 720)))

            if exists(gold_working_groups[self.next_turn_num][1]):
                pass
            else :
                skippable_wait_touch(Template(r"z制造站04.png", record_pos=(-0.442, 0.079), resolution=(1280, 720)))
            sleep(2)
            if skippable_wait_touch(gold_working_groups[self.next_turn_num][1],timeout=5):
                skippable_wait_touch(Template(r"z清空选择.png", record_pos=(-0.098, 0.25), resolution=(1280, 720)))
                sleep(2)
                for i in gold_groups[self.turn_num]:
                    self.find_swip_recovery(i,timeout=3)
                    
                skippable_wait_touch(Template(r"z确认.png", record_pos=(0.427, 0.248), resolution=(1280, 720)))
            sleep(3)
            
            skippable_wait_touch(Template(r"z返回.png", record_pos=(-0.452, -0.251), resolution=(1280, 720))) 
            sleep(3)
        skippable_wait_touch(Template(r"z返回.png", record_pos=(-0.452, -0.251), resolution=(1280, 720))) 
        sleep(3)
    def electriction(self):# 发电站
        for i in range(0,len(electric_station_group)):
            if skippable_wait_touch(electric_station_group[i]):
                while not exists(Template(r"z清空.png", record_pos=(0.433, -0.255), resolution=(1280, 720))):
                    skippable_wait_touch(Template(r"z进驻信息.png", record_pos=(-0.452, -0.055), resolution=(1280, 720)))
                if skippable_wait_touch(electric_working_groups[self.turn_num][i],timeout = 5):
                    sleep(1)
#                     skippable_wait_touch(electric_groups[self.turn_num][i])
#                     sleep(1)
#                     skippable_wait_touch(Template(r"z确认.png", record_pos=(0.418, 0.247), resolution=(1280, 720)))
#                     sleep(1)
#                 if skippable_wait_touch(Template(r"z进驻.png", record_pos=(0.32, -0.162), resolution=(1280, 720))):
                    sleep(1)
                    self.find_swip_recovery(electric_groups[self.next_turn_num][i],timeout=3)
                    skippable_wait_touch(Template(r"z确认.png", record_pos=(0.418, 0.247), resolution=(1280, 720)))
                    sleep(3)
                skippable_wait_touch(Template(r"z返回.png", record_pos=(-0.452, -0.251), resolution=(1280, 720)))
        
    def coretion(self):# 核心，指挥中心
        if skippable_wait_touch(Template(r"z控制中枢.png", record_pos=(0.168, -0.17), resolution=(1280, 720))):    # 核心
            sleep(1)
            if not exists(Template(r"z清空.png", record_pos=(0.436, -0.259), resolution=(1280, 720))):
                skippable_wait_touch(Template(r"z进驻信息.png", record_pos=(-0.45, -0.054), resolution=(1280, 720)))
            skippable_wait_touch(Template(r"z清空.png", record_pos=(0.436, -0.259), resolution=(1280, 720)))
            sleep(2)
            skippable_wait_touch(Template(r"z红色圆对号.png", rgb=True, record_pos=(0.16, 0.113), resolution=(1280, 720)))
            sleep(2)
            skippable_wait_touch(Template(r"z进驻.png", record_pos=(0.305, -0.163), resolution=(1280, 720)))
            for i in master_groups[self.next_turn_num]:
                self.find_swip_recovery(i,timeout=3)
                
            skippable_wait_touch(Template(r"z确认.png", record_pos=(0.427, 0.248), resolution=(1280, 720)))
            sleep(2)
            skippable_wait_touch(Template(r"z返回.png", record_pos=(-0.452, -0.251), resolution=(1280, 720))) 
    def parlortion(self):# 会客室
        if skippable_wait_touch(Template(r"z会客室.png", record_pos=(0.435, -0.12), resolution=(1280, 720))):#     会客室
            sleep(5)

            if skippable_wait_touch(Template(r"z会客室进入.png", record_pos=(-0.18, 0.152), resolution=(1280, 720))):
                sleep(2)
                if exists(Template(r"z会客室收获.png", rgb=True, record_pos=(-0.401, -0.198), resolution=(1280, 720))):
                    touch(Template(r"z返回.png", record_pos=(-0.447, -0.255), resolution=(1280, 720)))   
                if skippable_wait_touch(Template(r"z领取线索.png", rgb=False, record_pos=(-0.447, -0.255), resolution=(1280, 720))):
                    skippable_wait_touch(Template(r"z领取线索2.png", record_pos=(-0.447, -0.255), resolution=(1280, 720)))
                    sleep(2)
                    skippable_wait_touch(Template(r"z领取线索3.png", record_pos=(-0.447, -0.255), resolution=(1280, 720)))
                if skippable_wait_touch(parlor_working_group[self.next_turn_num]):
                    skippable_wait_touch(Template(r"z清空选择.png", record_pos=(-0.105, 0.246), resolution=(1280, 720)))
                    sleep(1)
                    skippable_wait_touch(Template(r"z确认.png", record_pos=(0.427, 0.248), resolution=(1280, 720)))
                    sleep(1)
                    skippable_wait_touch(Template(r"z会客室选择干员.png", record_pos=(-0.409, -0.113), resolution=(1920, 1081)))
                    for i in range(0,len(parlor_group)):
                        if i == self.next_turn_num:
                            continue
                        self.find_swip_recovery(parlor_group[i],timeout=3)

                    if skippable_wait_touch(Template(r"z确认.png", record_pos=(0.427, 0.248), resolution=(1280, 720))):
                        sleep(2)
                    else:
                        skippable_wait_touch(Template(r"z返回.png", record_pos=(-0.452, -0.251), resolution=(1280, 720))) 
                    sleep(2)
                sleep(5)
                skippable_wait_touch(Template(r"z返回.png", record_pos=(-0.452, -0.251), resolution=(1280, 720))) 
            sleep(5)
            skippable_wait_touch(Template(r"z返回.png", record_pos=(-0.452, -0.251), resolution=(1280, 720))) 
                
    def workingtion(self):# 办公室
        swipe(Template(r"z办公室0.png", record_pos=(0.47, 0.042), resolution=(1280, 720)), vector=[-0.0944, 0.0055])    # 招募管理
        if skippable_wait_touch(Template(r"z办公室.png", record_pos=(0.47, 0.042), resolution=(1280, 720))):
            sleep(1)
            if skippable_wait_touch(workstation_working_group[self.turn_num%2]):
                sleep(1)
                if skippable_wait_touch(workstation_group[self.turn_num%2]):
                    sleep(1)
                    skippable_wait_touch(Template(r"z确认.png", record_pos=(0.427, 0.248), resolution=(1280, 720)))
                    sleep(1)
                    skippable_wait_touch(Template(r"z办公室进入.png", record_pos=(0.427, 0.248), resolution=(1280, 720)))
                    sleep(1)
                    self.find_swip_recovery(workstation_group[self.next_turn_num%2],timeout=3)
                    
                    skippable_wait_touch(Template(r"z确认.png", record_pos=(0.427, 0.248), resolution=(1280, 720)))
                    sleep(1)
#             skippable_wait_touch(Template(r"z返回.png", record_pos=(-0.452, -0.251), resolution=(1280, 720))) 
            skippable_wait_touch(Template(r"z返回.png", record_pos=(-0.452, -0.251), resolution=(1280, 720))) 


    def roomtion(self):# 休息室，宿舍
        width = G.DEVICE.display_info['width']
        height = G.DEVICE.display_info['height']
        for room_index in range(0,len(rooms_group)):
            if skippable_wait_touch(rooms_group[room_index]):
                if not exists(Template(r"z清空.png", record_pos=(0.436, -0.259), resolution=(1280, 720))):
                    skippable_wait_touch(Template(r"z进驻信息.png", record_pos=(-0.451, -0.071), resolution=(1280, 720)))
                skippable_wait_touch(Template(r"z清空.png", record_pos=(0.436, -0.259), resolution=(1280, 720)))
                sleep(1)
                skippable_wait_touch(Template(r"z进驻.png", record_pos=(0.324, -0.157), resolution=(1280, 720)))
                skippable_wait_touch(Template(r"z1选择清单.png", record_pos=(0.42, -0.251), resolution=(1280, 720)))
                skippable_wait_touch(Template(r"z恢复类后勤.png", record_pos=(0.245, 0.052), resolution=(1280, 720)))
                skippable_wait_touch(Template(r"z蓝色对号.png", record_pos=(0.237, 0.145), resolution=(1280, 720)))
                for role_index in range(len(roles_group[room_index])):
                    self.find_swip_recovery(roles_group[room_index][role_index],timeout=3)

                skippable_wait_touch(Template(r"z1选择清单.png", record_pos=(0.42, -0.251), resolution=(1280, 720)))
                skippable_wait_touch(Template(r"z恢复类后勤-蓝色.png", record_pos=(0.248, 0.053), resolution=(1280, 720)))
                skippable_wait_touch(Template(r"z1未进驻.png", record_pos=(-0.132, -0.005), resolution=(1280, 720)))
                skippable_wait_touch(Template(r"z蓝色对号.png", record_pos=(0.237, 0.145), resolution=(1280, 720)))
                sleep(1)
                for  rest_position in rest_positions_group[room_index]:
                    sleep(2)
                    touch((rest_position[0]*width,rest_position[1]*height))
                sleep(2)
                skippable_wait_touch(Template(r"z1选择清单.png", record_pos=(0.42, -0.251), resolution=(1280, 720)))
                skippable_wait_touch(Template(r"z1未进驻-蓝色.png", record_pos=(-0.156, -0.002), resolution=(1280, 720)))
                sleep(1)

                skippable_wait_touch(Template(r"z蓝色对号.png", record_pos=(0.255, 0.157), resolution=(1280, 720)))
                skippable_wait_touch(Template(r"z确认.png", record_pos=(0.419, 0.248), resolution=(1280, 720)))
                sleep(2)
                skippable_wait_touch(Template(r"z返回.png", record_pos=(-0.452, -0.251), resolution=(1280, 720)))
            sleep(2)
    def back_home(self):
        skippable_wait_touch(Template(r"z主页菜单.png", record_pos=(-0.29, -0.251), resolution=(1280, 720)))
        skippable_wait_touch(Template(r"z主页首页.png", record_pos=(-0.428, -0.075), resolution=(1280, 720)))
    def dajia(self):   
        pass
    def auto_fight(self):
        if skippable_wait_touch(Template(r"z作战.png", record_pos=(0.258, -0.158), resolution=(1280, 720))):
            skippable_wait_touch(Template(r"z作战主线.png", record_pos=(-0.436, 0.234), resolution=(1280, 720)))
            sleep(1)
            while not skippable_wait_touch(Template(r"z作战第一章.png", threshold=0.95, rgb=True, record_pos=(0.151, -0.087), resolution=(1280, 720))):

                swipe(Template(r"tpl1604668633935.png", record_pos=(-0.25, -0.177), resolution=(1280, 720)), vector=[0.6422, 0],duration=0.05)
                sleep(1)
            
            if skippable_wait_touch(Template(r"z作战1-7.png", threshold=0.98, rgb=False, record_pos=(0, 0), resolution=(1280, 720))):
                    
                if exists(Template(r"z作战否代理.png", threshold=0.9500000000000002, rgb=True, record_pos=(-0.021, 0.183), resolution=(1280, 720))):
                    skippable_wait_touch(Template(r"z作战否代理.png", threshold=0.9500000000000002, rgb=True, record_pos=(-0.021, 0.183), resolution=(1280, 720)))
                sleep(2)
                if skippable_wait_touch(Template(r"z作战方舟助手.png", threshold=0.5999999999999999, record_pos=(-0.021, 0.183), resolution=(1280, 720))):
                    skippable_wait_touch(Template(r"z作战方舟助手启动.png", record_pos=(-0.021, 0.183), resolution=(1280, 720)))
                
    def exit_auto_fight(self):
        width = G.DEVICE.display_info['width']
        height = G.DEVICE.display_info['height']
        skippable_wait_touch(Template(r"z准备停止自动化.png", threshold=0.6999999999999998, record_pos=(0, 0), resolution=(1280, 720)),timeout=5)
        sleep(2)
        skippable_wait_touch(Template(r"z停止自动化.png", threshold=0.6999999999999998, record_pos=(0, 0), resolution=(1280, 720)),timeout=5)
        sleep(2)
        touch((0.1*width,0.1*height))
        sleep(2)
        skippable_wait_touch(Template(r"z主页菜单.png", record_pos=(-0.29, -0.251), resolution=(1280, 720)),timeout = 300)
        skippable_wait_touch(Template(r"z主页首页.png", record_pos=(-0.428, -0.075), resolution=(1280, 720)),timeout = 300)
















