
#HI为history image
import requests
from pyecharts import Line
import json

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
res = requests.get('http://www.dzyong.top:3005/yiqing/history',headers = header)
res = json.loads(res.text)

date = []
confirmedNum = []
suspectedNum = []
curesNum = []
deathsNum = []
suspectedIncr = []

for e in res['data']:
    print(e)
    date.append(e['date'])
    confirmedNum.append(e['confirmedNum'])
    suspectedNum.append(e['suspectedNum'])
    curesNum.append(e['curesNum'])
    deathsNum.append(e['deathsNum'])
    suspectedIncr.append(e['suspectedIncr'])

date.reverse()
confirmedNum.reverse()
suspectedNum.reverse()
curesNum.reverse()
deathsNum.reverse()

line = Line('疫情趋势')
line.add('确诊人数',date,confirmedNum,is_smooth=True)
line.add('疑似人数',date,suspectedNum,is_smooth=True)
line.add('治愈人数',date,curesNum,is_smooth=True)
line.add('死亡人数',date,deathsNum,is_smooth=True)
# line.add('')
line.show_config()
line.render("History_Area")