from datetime import datetime
import time
import re
from urllib import request

First = 1
begin_follower = 0
begin_timer = 0

while True:
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    url = 'https://api.bilibili.com/x/relation/stat?vmid=777536'
    req = request.Request(url)
    page = request.urlopen(req).read()
    page = page.decode('utf-8')
    string = page

    time.sleep(1)

    if First == 1:
        begin_follower = int(re.findall('"follower":([0-9]*)', string, flags=0)[0])
        begin_timer = datetime.now()
        First = 0
    else:
        now_timer = datetime.now()
        now_follower = int(re.findall('"follower":([0-9]*)', string, flags=0)[0])
        dis_follower = begin_follower - now_follower
        print(localtime  + "\tLexburner粉丝现在为:" + str(now_follower) + "（自计时起总取关数：" + str(dis_follower) + "）")
        print("\t\t\t" + "该时段取关速度：" + str(dis_follower/(now_timer - begin_timer).seconds) + "个/秒")
