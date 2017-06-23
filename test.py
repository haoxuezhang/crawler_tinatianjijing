from lxml import etree
import re
import lxml
import urllib
import urllib.request
import requests
import csv

# url = 'http://www.luoo.net/music/901'
# response = urllib.request.urlopen(url)
# html = response.read().decode('utf-8')
# html = etree.HTML(html)
# item_url = html.xpath('//*[@id="luooPlayerPlaylist"]/ul/li')
# for i in item_url:
#     index = i.xpath('//div/a/@rel')
#     for a in index:
#         print(a)
# f = open('num.txt','r')
# hao = f.read()
li =[]
csv_reader = csv.reader(open('num.csv', encoding='utf-8'))
for row in csv_reader:
    li.append(row)
for r in li:
    print(r[0])

