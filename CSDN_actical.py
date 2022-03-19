#!/usr/bin/env python
# coding:utf-8
"""
Name : CSDN_actical.py
Author  : SongJian
Contect : songjianhitsz@qq.com
Time    : 2022/3/19 11:56
Desc    : 针对特定的文章刷阅读量
"""
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


    def visitor(self):

        self.article_list.append('https://blog.csdn.net/weixin_41960890/article/details/123591436')
        self.article_list.append('https://blog.csdn.net/weixin_41960890/article/details/120547099')
        self.article_list.append('https://blog.csdn.net/weixin_41960890/article/details/120418801')

        for article_url in self.article_list:
            response = requests.get(url=article_url, headers=self.headers)

    def run(self):
        while True:
            print("\r已访问次数：%s" % self.visitor_count, end='')
            self.visitor()
            self.visitor_count += 1
            time.sleep(60)


def main():
    url = "https://blog.csdn.net/weixin_41960890"  # 用于保存你的博客主页地址（根据实际情况更改）
    page_num = 1  # 用于保存你的博客页数 （根据实际情况更改）
    visitor = CsdnVisitor(url, page_num)
    visitor.run()


if __name__ == '__main__':
    main()