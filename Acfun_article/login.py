#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests


class Login:
    url = "https://id.app.acfun.cn/rest/web/login/signin"
    data = {
        "username": "13321270519",
        "password": "hxmh23wei"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/76.0.3809.100 Safari/537.36"}

    @staticmethod
    def login():
        login_session = requests.session()
        login_session.post(Login.url, data=Login.data, headers=Login.headers)
        return login_session
