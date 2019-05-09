# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 19:25
# @Author  : Endless-cloud
# @Site    : 
# @File    : 项目2 爬取知乎 探索内容.py
# @Software: PyCharm
'''
 　　　　　　　 ┏┓　 ┏┓+ +
 　　　　　　　┏┛┻━━━┛┻┓ + +
 　　　　　　　┃　　　　　　┃ 　
 　　　　　　　┃　　　━　　 ┃ ++ + + +
 　　　　　　 ████━████  ┃+
 　　　　　　　┃　　　　　　　┃ +
 　　　　　　　┃　　　┻　　　┃
 　　　　　　　┃　　　　　　┃ + +
 　　　　　　　┗━┓　　　┏━┛
 　　　　　　　　 ┃　　　┃　　　　　　　　　　　
 　　　　　　　　 ┃　　　┃ + + + +
 　　　　　　　　 ┃　　　┃　　　　Code is far away from bug with the animal protecting　　　　　　　
 　　　　　　　　 ┃　　　┃ + 　　　　神兽保佑,代码无bug　　
 　　　　　　　　 ┃　　　┃
 　　　　　　　　 ┃　　　┃　　+　　　　　　　　　
 　　　　　　　　 ┃　 　 ┗━━━┓ + +
 　　　　　　　　 ┃ 　　　　   ┣┓
 　　　　　　　　 ┃ 　　　　　 ┏┛
 　　　　　　　　 ┗┓┓┏━┳┓┏┛ + + + +
 　　　　　　　　  ┃┫┫ ┃┫┫
 　　　　　　　　  ┗┻┛ ┗┻┛+ + + +
 '''
import requests
from pyquery import PyQuery as pq
import requests

'''asdasdasd'''
''' hahahahha'''
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

response = requests.get('https://www.zhihu.com/explore', headers=headers)
html =response.text
html=html
pp =response.encoding
print(pp)
print(html)
doc =pq(html)
items =doc('.explore-tab .feed-item').items()
for item in items:
    questions =item.find('h2').text()
    author =item.find('.author-link-line').text()
    answer =pq(item.find('.content').html()).text()
    with open('exit.txt','a',encoding='utf-8') as f:
        print(questions)
        print(answer)
        print(author)
        f.write('\n'.join([questions,author,answer]))
        f.write('\n'+"="*50+'\n')
print('程序完成')