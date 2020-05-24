#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests, json, re
import time


def run(url):
    res = requests.get(url, headers=headers).text.split("(", 1)[1].rsplit(")", 1)[0]
    res = json.loads(res)["data"]["replies"]
    for i in res:
        content = i["content"]["message"]
        if "bgm" in content:
            print(content)
        elif "音乐" in content:
            print(content)


headers = {}

for page in range(0, 100):
    print(page)
    url = f"https://api.bilibili.com/x/v2/reply?callback=jQuery17208677126098755512_1571146595675&jsonp=jsonp&pn={page}&type=1&oid=71327501&sort=2&={100 * int(time.time())}"
    run(url)
