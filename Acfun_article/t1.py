#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from at_spider import main
from threading import Thread

zonghe_url = "https://webapi.acfun.cn/query/article/list?pageNo=1&size=10&realmIds=5%2C22%2C3%2C4&originalOnly=false&orderType=2&periodType=-1&filterTitleImage=true"

qinggan_url = "https://webapi.acfun.cn/query/article/list?pageNo=1&size=10&realmIds=50%2C25%2C34%2C7%2C6%2C17%2C1%2C2%2C49&originalOnly=false&orderType=1&periodType=-1&filterTitleImage=true"

# Thread(target=main, args=(zonghe_url, 1, 500)).start()
# Thread(target=main, args=(zonghe_url, 500, 1000)).start()
Thread(target=main, args=(zonghe_url, 1000, 1500)).start()
# Thread(target=main, args=(zonghe_url, 1500, 2000)).start()
# Thread(target=main, args=(qinggan_url, 1, 500)).start()
# Thread(target=main, args=(qinggan_url, 500, 1000)).start()
Thread(target=main, args=(qinggan_url,1000, 1500)).start()
# Thread(target=main, args=(qinggan_url,1500, 2000)).start()

