# -*- encoding=utf8 -*-
__author__ = "l6754"

from airtest.core.api import *

auto_setup(__file__)
# 贸易站
trade_group_1 =  [Template(r"a1德克萨斯.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"a1拉普兰德.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"a1能天使.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]

trade_group_2 = [Template(r"a3慕斯.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"a3雪雉.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"a3夜刀.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
trade_group_3 = [Template(r"a2古米.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"a2孑.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"a2银灰.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
trade_groups = [trade_group_1,trade_group_2,trade_group_3]
trade_group_working_1 = [Template(r"b1德克萨斯.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"b1拉普兰德.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"b1能天使.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
trade_group_working_2 = [Template(r"b3慕斯.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"b3雪雉.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"b3夜刀.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
trade_group_working_3 = [Template(r"b2古米.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"b2孑.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"b2银灰.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
trade_working_groups = [trade_group_working_1,trade_group_working_2,trade_group_working_3]
# 制造站
    # 狗粮，经验
experience_goup_1 = [Template(r"c断罪者.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"c食铁兽.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"c霜叶.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
experience_goup_2 = [Template(r"cCastle-3.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"c红豆.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"c白雪.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]


experience_goup_3 = [Template(r"c火神.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"c红云.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"c黑角.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
experience_goups = [experience_goup_1,experience_goup_2,experience_goup_3]
experience_working_goup_1 = [Template(r"d断罪者.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"d食铁兽.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"d霜叶.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
experience_working_goup_2 = [Template(r"dCastle-3.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"d红豆.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"d白雪.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
experience_working_goup_3 = [Template(r"d火神.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"d红云.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"d黑角.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]

experience_working_goups = [experience_working_goup_1,experience_working_goup_2,experience_working_goup_3]
    # gold，金属
gold_group_1 = [Template(r"e槐琥.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"e砾.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"e清流.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
gold_group_2 = [Template(r"e斑点.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"e梅尔.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"e迷迭香.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]



gold_group_3 = [Template(r"e史都华德.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"e白面鸮.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"e夜烟.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
gold_groups = [gold_group_1,gold_group_2,gold_group_3]
gold_working_group_1 = [Template(r"f槐琥.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"f砾.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"f清流.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
gold_working_group_2 = [Template(r"f斑点.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"f梅尔.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"f迷迭香.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]

gold_working_group_3 = [Template(r"f史都华德.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"f白面鸮.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"f夜烟.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
gold_working_groups = [gold_working_group_1,gold_working_group_2,gold_working_group_3]
# 电力
electric_group_1 = [Template(r"g阿消.png", threshold=0.9299999999999999, rgb=True, record_pos=(0, 0), resolution=(1280, 720)),Template(r"g雷蛇.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"g格雷伊.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]

electric_group_2 = [Template(r"gTHRM-EX.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"g伊芙利特.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"g阿消.png", threshold=0.9299999999999999, rgb=True, record_pos=(0, 0), resolution=(1280, 720))]

electric_group_3 = [Template(r"g雷蛇.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"g格雷伊.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"g伊芙利特.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
electric_groups = [electric_group_1,electric_group_2,electric_group_3]
electric_working_group_1 = [Template(r"h阿消.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"h雷蛇.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"h格雷伊.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
electric_working_group_2 = [Template(r"hTHRM-EX.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"h伊芙利特.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"h阿消.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720))]
electric_working_group_3 = [Template(r"h雷蛇.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"h格雷伊.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"h伊芙利特.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
electric_working_groups = [electric_working_group_1,electric_working_group_2,electric_working_group_3]
electric_station_group = [Template(r"w发电站01.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"w发电站02.png", threshold=0.9, rgb=True, record_pos=(0, 0), resolution=(1280, 720)),Template(r"w发电站03.png", threshold=0.9, rgb=True, record_pos=(0, 0), resolution=(1280, 720))]
# 办公室
workstation_group = [Template(r"i絮雨.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"i艾雅法拉.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720))]
workstation_working_group = [Template(r"j絮雨.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"j艾雅法拉.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720))]

# 控制中心
master_group_1 = [Template(r"阿米娅.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"红.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"陈.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"夕.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"清道夫.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
master_group_2 = [Template(r"阿米娅.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"红.png", threshold=0.85, record_pos=(0, 0), resolution=(1280, 720)),Template(r"临光.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"坚雷.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"清道夫.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]

master_group_3 = [Template(r"诗怀雅.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"临光.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"坚雷.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"夕.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"陈.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]

master_groups = [master_group_1,master_group_2,master_group_3]
# 会客室
parlor_group = [Template(r"l星极.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"l守林人.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"l断崖.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
parlor_working_group = [Template(r"m星极.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"m守林人.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"m断崖.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]

# 休息室
role_group_1 = [Template(r"n1闪灵.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"n1推进之王.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
role_group_2 = [Template(r"n2安比尔.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720)),Template(r"n3lancet-2.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
role_group_3 = [Template(r"n3杜林.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
# role_group_4 = [Template(r"n4夜莺.png",threshold=0.9,record_pos=(0,0),resolution=(1280,720))]
role_group_4 = []
roles_group = [role_group_1,role_group_2,role_group_3,role_group_4]
rest_position_1 = [[0.48,0.38],[0.58,0.69],[0.80,0.38]]
rest_position_2 = [[0.48,0.38],[0.58,0.38],[0.69,0.38]]
rest_position_3 = [[0.48,0.38],[0.48,0.69],[0.58,0.38],[0.58,0.69]]
# rest_position_4 = [[0.38,0.67],[0.48,0.38],[0.48,0.69],[0.58,0.38]]
rest_position_4 = [[0.38,0.38],[0.38,0.67],[0.48,0.38],[0.48,0.69],[0.58,0.38]]
rest_positions_group = [rest_position_1,rest_position_2,rest_position_3,rest_position_4]
rooms_group = [Template(r"w休息室01.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"w休息室02.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"w休息室03.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"w休息室04.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720))]




cart = [Template(r"v初级作战记录.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"v固源岩.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"v家具零件.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"v异铁.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"v技巧概要-卷1.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"v技巧概要-卷2.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"v招聘许可.png", threshold=0.98000000000000001, rgb=True, record_pos=(0, 0), resolution=(1280, 720)),Template(r"v源岩.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"v碳素.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"v聚酸酯.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"v装置.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"v赤金.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"v酮凝集.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"v龙门币.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"v破损装置.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"v糖.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720))]






recruit = [(1),(2),(12),(21),(14),(20),(25),(24),(23),(22),(15,19),(15),(21,19),(21),(18,19),(18),(14,13),(14,7),(27,7),(27,13),(14,15),(14,9),(17,9),(17,15),(27,9),(27,14),(18,12),(15,12),(15,21),(17,21),(17,12),(22,12),(22,25),(19,25),(19,12),(27,12),(27,23),(20,8),(20,15),(17,8),(17,16),(13,17),(13,15),(13,8),(17,15,8),(17,15,3),(20,16),(20,6),(18,6),(17,6),(11,22),(11,20),(11,15),(22,5),(22,26),(14,5),(14,26)]


recruit_pic_group = [Template(r"x0新手.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x1资深干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x2高级资深干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x3远程位.png", threshold=0.98, rgb=True, record_pos=(0.111, 0.019), resolution=(1280, 720)),Template(r"x4近战位.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x5先锋干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x6狙击干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x7医疗干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x8术师干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x9近卫干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x10重装干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x11辅助干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x12特种干员.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x13治疗.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x14支援.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x15输出.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x16群攻.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x17减速.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x18生存.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x19防护.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x20削弱.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x21位移.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x22控场.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x23爆发.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x24召唤.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x25快速复活.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x26费用回复.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720)),Template(r"x27支援机械.png", threshold=0.98, rgb=True, record_pos=(0,0), resolution=(1280, 720))]

recruit_position_group = [Template(r"w公开招募位1.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"w公开招募位2.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"w公开招募位3.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720)),Template(r"w公开招募位4.png", threshold=0.9, record_pos=(0,0), resolution=(1280, 720))]










