#!/usr/bin/env python
# coding:utf-8
"""
Name : main.py
Author  : SongJian
Contect : songjianhitsz@qq.com
Time    : 2022/3/19 11:40
Desc    : 根据你的个人主页，将所有文章的url爬取下来，逐一访问。
"""
# -*- coding: utf-8 -*-
import time
from bs4 import BeautifulSoup
import requests


class CsdnVisitor(object):
    def __init__(self, home_url, page_num):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/73.0.3679.0 Safari/537.36'}
        self.url = home_url
        self.page_url = []
        self.page_num = page_num  # 用于记录博客最大页数
        self.article_list = []  # 用于保存所有的文章链接
        self.visitor_count = 1  # 记录已访问次数

    def get_article_url(self, url):
        """
        找到每一页的所有文章链接，结果保存在article_list中
        :return:
        """
        response = requests.get(url=url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'lxml')
        h4 = soup.find_all("blog-list-box")
        for h in h4:
            self.article_list.append(h.a["href"])

    def make_page_url(self):
        for page in range(1, self.page_num + 1):
            self.page_url.append("{0}/article/list/{1}".format(self.url, page))

    def visitor(self):
        for article_url in self.article_list:
            response = requests.get(url=article_url, headers=self.headers)

    def run(self):
        self.make_page_url()
        for page_list_url in self.page_url:
            self.get_article_url(page_list_url)
        while True:
            print("\r已访问次数：%s" % self.visitor_count, end='')
            self.visitor()
            self.visitor_count += 1
            time.sleep(60)


def main():
    url = "https://blog.csdn.net/*************"  # 用于保存你的博客主页地址（根据实际情况更改）
    page_num = 7  # 用于保存你的博客页数 （根据实际情况更改）
    visitor = CsdnVisitor(url, page_num)
    visitor.run()


if __name__ == '__main__':
    main()
