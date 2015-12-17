# encoding:utf-8
from __future__ import unicode_literals
import requests
from pyquery import PyQuery as pq
import re

pattern_isbn = re.compile(r"ajax_douban\.php\?isbn=(\d*)")


def get_tops():
    top = pq("http://210.35.251.243/opac/ajax_top_lend_shelf.php")
    lis = top('#search_container_center ul li')
    tops = []
    for li in lis:
        href = li.find('a').get('href')
        href = "http://210.35.251.243/opac/" + href
        text = li.text_content()
        print("Top: url=%s text=%s" % (href, text))
        tops.append(dict(url=href, text=text))
    return tops


def get_bookinfo(url):
    page = pq(url)
    info = []
    isbn = pattern_isbn.findall(page.html())[0]
    print("BookInfo: url=%s isbn=%s" % (url, isbn))
    info.append(('isbn', isbn))
    douban = get_douban(isbn)
    print("豆瓣简介".center(60, '-'))
    print(douban)
    info.append(("豆瓣简介", douban))
    items = page('#item_detail dl')
    for item in items:
        key = item.find('dt').text_content()
        value = item.find('dd').text_content()
        try:
            key.encode('gbk')
        except UnicodeEncodeError:
            key = ""
        print("Info: key=%s value=%s" % (key, value))
        info.append((key, value))
    return info


def get_douban(isbn):
    url = "http://210.35.251.243/opac/ajax_douban.php?isbn=%s" % isbn
    json = requests.get(url).json()
    return json['summary']


def main():
    tops = get_tops()
    results = [get_bookinfo(item['url']) for item in tops]
    return results


if __name__ == '__main__':
    results = main()
    print(results)
