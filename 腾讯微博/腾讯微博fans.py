#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import time,requests
import json,re
from bs4 import BeautifulSoup
from pymysql_func.models import *
from threading import Thread

headers = {****your*****}


def con(url,page,side):
    text = json.loads(requests.get(url, headers=headers).text)
    print(page)
    html = text["info"]
    soup = BeautifulSoup(html, 'html.parser')
    res = soup.find_all(class_='userPic')
    for li in res:
        res = li.find_all('a', href=True)[0]
        href = res.get("href").strip("/")
        title = res.get("title").split("(")[0]
        if side == "fans":
            tosql_fans(name,href,title,page)
        else:
            tosql_follow(name,href, title, page)


name = "微博账号"
html = requests.get(f"http://t.qq.com/{name}",headers=headers).text
soup = BeautifulSoup(html, 'html.parser')
Fans = soup.find_all(attrs={"boss": "btnApolloFollower"})[0].find('span',class_="text_count").text
Follow = soup.find_all(attrs={"boss": "btnApolloFollowing"})[0].find('span',class_="text_count").text
print("***********fans:",Fans,"***********Follow:",Follow)
fans_page = int(int(Fans)/15+2)
follow_page = int(int(Follow)/15+2)

fans_list = []
for page in range(1,fans_page):

    fans_url = f"http://api.t.qq.com/relations/follow_apollo.php?" \
          f"u={name}&t=2&st=1&p={page}&apiType=14&apiHost=" \
          f"http://api.t.qq.com&_r={100*int(time.time())}&g_tk=282436490"

    t = Thread(target=con,args=(fans_url,page,"fans"))
    t.start()


follow_list = []
for page in range(1,follow_page):

    follow_url = f"http://api.t.qq.com/relations/follow_apollo.php?" \
                 f"u={name}&t=1&st=1&p={page}&apiType=14&apiHost=" \
                 f"http://api.t.qq.com&_r={100*int(time.time())}&g_tk=353249867"
    t = Thread(target=con,args=(follow_url,page,"follow"))
    t.start()


