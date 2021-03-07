# -*- encoding=utf8 -*-
__author__ = "l6754"

from airtest.core.api import *

auto_setup(__file__)
# 贸易站
trade_group_1 =  [Template(r"picture/a1德克萨斯.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/a1拉普兰德.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/a1能天使.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]

trade_group_2 = [Template(r"picture/a3慕斯.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/a3雪雉.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/a3夜刀.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
trade_group_3 = [Template(r"picture/a2古米.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/a2孑.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/a2银灰.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
trade_groups = [trade_group_1,trade_group_2,trade_group_3]
trade_group_working_1 = [Template(r"picture/b1德克萨斯.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/b1拉普兰德.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/b1能天使.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
trade_group_working_2 = [Template(r"picture/b3慕斯.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/b3雪雉.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/b3夜刀.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
trade_group_working_3 = [Template(r"picture/b2古米.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/b2孑.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/b2银灰.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
trade_working_groups = [trade_group_working_1,trade_group_working_2,trade_group_working_3]
# 制造站
    # 狗粮，经验
experience_goup_1 = [Template(r"picture/c断罪者.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/c食铁兽.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/c霜叶.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
experience_goup_2 = [Template(r"picture/cCastle-3.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/c红豆.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/c白雪.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]


experience_goup_3 = [Template(r"picture/c火神.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/c红云.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/c黑角.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
experience_goups = [experience_goup_1,experience_goup_2,experience_goup_3]
experience_working_goup_1 = [Template(r"picture/d断罪者.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/d食铁兽.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/d霜叶.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
experience_working_goup_2 = [Template(r"picture/dCastle-3.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/d红豆.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/d白雪.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
experience_working_goup_3 = [Template(r"picture/d火神.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/d红云.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/d黑角.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]

experience_working_goups = [experience_working_goup_1,experience_working_goup_2,experience_working_goup_3]
    # gold，金属
gold_group_1 = [Template(r"picture/e槐琥.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/e砾.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/e清流.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
gold_group_2 = [Template(r"picture/e斑点.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/e梅尔.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/e迷迭香.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]



gold_group_3 = [Template(r"picture/e史都华德.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/e白面鸮.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/e夜烟.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
gold_groups = [gold_group_1,gold_group_2,gold_group_3]
gold_working_group_1 = [Template(r"picture/f槐琥.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/f砾.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/f清流.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
gold_working_group_2 = [Template(r"picture/f斑点.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/f梅尔.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/f迷迭香.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]

gold_working_group_3 = [Template(r"picture/f史都华德.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/f白面鸮.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/f夜烟.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
gold_working_groups = [gold_working_group_1,gold_working_group_2,gold_working_group_3]
# 电力
electric_group_1 = [Template(r"picture/g阿消.png", threshold=0.9299999999999999, rgb=True, record_pos=(0, 0), resolution=(1280, 720)),Template(r"picture/g雷蛇.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/g格雷伊.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]

electric_group_2 = [Template(r"picture/gTHRM-EX.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/g伊芙利特.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/g阿消.png", threshold=0.9299999999999999, rgb=True, record_pos=(0, 0), resolution=(1280, 720))]

electric_group_3 = [Template(r"picture/g雷蛇.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/g格雷伊.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/g伊芙利特.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
electric_groups = [electric_group_1,electric_group_2,electric_group_3]
electric_working_group_1 = [Template(r"picture/h阿消.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/h雷蛇.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/h格雷伊.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
electric_working_group_2 = [Template(r"picture/hTHRM-EX.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/h伊芙利特.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/h阿消.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720))]
electric_working_group_3 = [Template(r"picture/h雷蛇.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/h格雷伊.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/h伊芙利特.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
electric_working_groups = [electric_working_group_1,electric_working_group_2,electric_working_group_3]
electric_station_group = [Template(r"picture/w发电站01.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/w发电站02.png", threshold=0.9, rgb=True, record_pos=(0, 0), resolution=(1280, 720)),Template(r"picture/w发电站03.png", threshold=0.9, rgb=True, record_pos=(0, 0), resolution=(1280, 720))]
# 办公室
workstation_group = [Template(r"picture/i絮雨.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/i艾雅法拉.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720))]
workstation_working_group = [Template(r"picture/j絮雨.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/j艾雅法拉.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720))]

# 控制中心
master_group_1 = [Template(r"picture/阿米娅.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/红.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/陈.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/夕.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/清道夫.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
master_group_2 = [Template(r"picture/阿米娅.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/红.png", threshold=0.85, record_pos=(0, 0), resolution=(1280, 720)),Template(r"picture/临光.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/坚雷.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/清道夫.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]

master_group_3 = [Template(r"picture/诗怀雅.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/临光.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/坚雷.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/夕.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/陈.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]

master_groups = [master_group_1,master_group_2,master_group_3]
# 会客室
parlor_group = [Template(r"picture/l星极.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/l守林人.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/l断崖.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
parlor_working_group = [Template(r"picture/m星极.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/m守林人.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/m断崖.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]

# 休息室
role_group_1 = [Template(r"picture/n1闪灵.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/n1推进之王.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
role_group_2 = [Template(r"picture/n2安比尔.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"picture/n3lancet-2.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
role_group_3 = [Template(r"picture/n3杜林.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
# role_group_4 = [Template(r"picture/n4夜莺.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
role_group_4 = []
roles_group = [role_group_1,role_group_2,role_group_3,role_group_4]
rest_position_1 = [[0.48,0.38],[0.58,0.69],[0.80,0.38]]
rest_position_2 = [[0.48,0.38],[0.58,0.38],[0.69,0.38]]
rest_position_3 = [[0.48,0.38],[0.48,0.69],[0.58,0.38],[0.58,0.69]]
# rest_position_4 = [[0.38,0.67],[0.48,0.38],[0.48,0.69],[0.58,0.38]]
rest_position_4 = [[0.38,0.38],[0.38,0.67],[0.48,0.38],[0.48,0.69],[0.58,0.38]]
rest_positions_group = [rest_position_1,rest_position_2,rest_position_3,rest_position_4]
rooms_group = [Template(r"picture/w休息室01.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/w休息室02.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/w休息室03.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/w休息室04.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720))]




cart = [Template(r"picture/v初级作战记录.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/v固源岩.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/v家具零件.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/v异铁.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/v技巧概要-卷1.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/v技巧概要-卷2.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/v招聘许可.png", threshold=0.98000000000000001, rgb=True, record_pos=(0, 0), resolution=(1280, 720)),Template(r"picture/v源岩.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/v碳素.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/v聚酸酯.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/v装置.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/v赤金.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/v酮凝集.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/v龙门币.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/v破损装置.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/v糖.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720))]






recruit = [(1),(2),(12),(21),(14),(20),(25),(24),(23),(22),(15,19),(15),(21,19),(21),(18,19),(18),(14,13),(14,7),(27,7),(27,13),(14,15),(14,9),(17,9),(17,15),(27,9),(27,14),(18,12),(15,12),(15,21),(17,21),(17,12),(22,12),(22,25),(19,25),(19,12),(27,12),(27,23),(20,8),(20,15),(17,8),(17,16),(13,17),(13,15),(13,8),(17,15,8),(17,15,3),(20,16),(20,6),(18,6),(17,6),(11,22),(11,20),(11,15),(22,5),(22,26),(14,5),(14,26)]


recruit_pic_group = [Template(r"picture/x0新手.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x1资深干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x2高级资深干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x3远程位.png", threshold=0.98, rgb=True, record_pos=(0.111, 0.019), resolution=(1280, 720)),Template(r"picture/x4近战位.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x5先锋干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x6狙击干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x7医疗干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x8术师干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x9近卫干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x10重装干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x11辅助干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x12特种干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x13治疗.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x14支援.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x15输出.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x16群攻.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x17减速.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x18生存.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x19防护.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x20削弱.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x21位移.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x22控场.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x23爆发.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x24召唤.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x25快速复活.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x26费用回复.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/x27支援机械.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720))]

recruit_position_group = [Template(r"picture/w公开招募位1.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/w公开招募位2.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/w公开招募位3.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"picture/w公开招募位4.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720))]










