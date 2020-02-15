#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import json
from pyecharts import Bar

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
res = requests.get('http://www.dzyong.top:3005/yiqing/province',headers = header)
res.encoding = 'utf-8'
res = json.loads(res.text)

provinceName = []
confirmedNum = []
curesNum = []
deathsNum = []

for e in res['data']:
    provinceName.append(e['provinceName'])
    confirmedNum.append(e['confirmedNum'])
    curesNum.append(e['curesNum'])
    deathsNum.append(e['deathsNum'])

bar = Bar('各省市疫情数据','中国加油！')
bar.add("确诊人数", provinceName, confirmedNum)
bar.add("治愈人数", provinceName, curesNum)
bar.add("死亡人数", provinceName, deathsNum)
#is_convert=True为xy轴交换
# bar.add("确诊人数", provinceName, confirmedNum,is_convert=True)
# bar.add("治愈人数", provinceName, curesNum,is_convert=True)
# bar.add("死亡人数", provinceName, deathsNum,is_convert=True)
bar.show_config()
bar.render("Provice_Data")