#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests, re, json, threading, time, os, random
from models import Sql
from login import Login

session = Login.login()
to_sql = Sql()


def acfun(url):
    conn_list = session.get(url, headers=Login.headers).text
    article_list = json.loads(conn_list)['data']['articleList']
    # article(article_list)
    t_list = []
    for data in article_list:
        conn_thread = threading.Thread(target=article, args=(data,))
        conn_thread.start()
        t_list.append(conn_thread)
    for j in t_list:
        j.join()


def article(data):
    id = data['id']
    comment_count = data["comment_count"]
    article_title = data['title']
    url = "http://www.acfun.cn/a/ac" + str(id)
    total_page = int(comment_count / 50) + 1

    for page in range(1, total_page + 1):
        print(page, end="--")
        req_url = f"https://www.acfun.cn/rest/pc-direct/comment/listByFloor?sourceId={id}&sourceType=3&page={page}&pivotCommentId=0&newPivotCommentId=0&_ts={int(100 * time.time())}"
        down(article_title, req_url, url, page)


def down(article_title, req_url, url, page):
    article_con = json.loads(session.get(req_url, headers=Login.headers).text)
    article_txt = article_con["commentsMap"]
    for data in article_txt:
        user_name = article_txt[data]["userName"]
        content = article_txt[data]["content"]
        postDate = article_txt[data]["postDate"]
        if user_name == "去无的止境":
            print("评论:", url)
            print("page:", page)
            print(content)

            to_sql.insert(article_title, page, content, url, postDate)

            # with open("%s.txt" % article_title, 'a+', encoding="utf-8") as article_write:
            #     article_write.write(article_title + '\n')
            #     article_write.write("page:" + str(page) + '\n')
            #     article_write.write(content + '\n')
            #     article_write.write(url + '\n')


def main(url, start, end):
    article_thread_list = []
    for page in range(start, end):
        print("\n第%s页" % page)
        url = re.sub("pageNo=\d+", f"pageNo={page}", url)
        # acfun(url)

        t = threading.Thread(target=acfun, args=(url,))
        t.start()
        article_thread_list.append(t)
        for t in article_thread_list:
            t.join()

    to_sql.close()