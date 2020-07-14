#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests, re, json, threading, time, os, random
from models import Sql
from login import Login

session = Login.login()
to_sql = Sql()


def acfun(ac, url):
    req = session.get(url, headers=Login.headers).text
    try:
        title = re.findall(r"<title >(.*?) - AcFun", req)[0].strip()
        # print(title)
        page_url = f"https://www.acfun.cn/rest/pc-direct/comment/listByFloor?sourceId={ac}&sourceType=3&page=1&pivotCommentId=0&newPivotCommentId=0&_ts={int(100 * time.time())}"

        comment_req= json.loads(session.get(page_url, headers=Login.headers).text)
        total_page = comment_req["totalPage"]
        print(total_page)
        for page in range(1, total_page+1):
            print(page, end="-")
            comment_url = re.sub("page=1", f"page={page}", page_url)
            req = json.loads(session.get(comment_url, headers=Login.headers).text)
            commentsMap = req["commentsMap"]
            for data in commentsMap:
                user_name = commentsMap[data]["userName"]
                content = commentsMap[data]["content"]
                postDate = commentsMap[data]["postDate"]
                print(content)
                if user_name == "去无的止境":
                    print("评论:", url)
                    print("page:", page)
                    print(content)
                    to_sql.insert(title, page, content, url, postDate)

    except IndexError:
        pass


if __name__ == '__main__':
    article_thread_list = []
    # for ac in range(15996189, 2071656, -1):
    for ac in [16019480]:
        print(f"------------第ac{ac}------------")
        url = f"https://www.acfun.cn/a/ac{ac}"
        # acfun(ac, url)
        t = threading.Thread(target=acfun, args=(ac, url,))
        t.start()
        article_thread_list.append(t)
        for t in article_thread_list:
            t.join()

    to_sql.close()
