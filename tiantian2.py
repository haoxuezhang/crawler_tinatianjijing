import signal
from pymongo import MongoClient
import pymongo
from lxml import etree
from selenium import webdriver
import time
import csv
import selenium
import re
import lxml


conn = pymongo.MongoClient()      # 连接MongDB数据库
post_info = conn.tiantian       # 指定数据库名称（yande_test），没有则创建


conn = MongoClient('localhost',27017)
db = conn.tiantian
# custom header
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           # 'Accept-Charset': 'utf-8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
           'Connection': 'keep-alive'
           }

# set custom headers
for key, value in headers.items():
    webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value
li = []
csv_reader = csv.reader(open('num.csv', encoding='utf-8'))
for row in csv_reader:
    li.append(row)
for rr in range(len(li)):
    try:
        main_url = 'http://fund.eastmoney.com/f10/jjjz_'  # 210009.html'
        print(li[rr][0] + li[rr][1])
        main_url += li[rr][0] + '.html'
        # f = open('num.csv', 'r')

        driver = webdriver.PhantomJS()  # or add to your PATH
        # driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--load-images=false'])  # or add to your PATH
        # driver = webdriver.Chrome()
        # set bigger windows height to dynamically load more data    //*[@id="pagebar"]/div[1]/label[7]

        driver.set_window_size(1280, 3200)  # optional
        driver.get(main_url)
        content1 = driver.page_source
        etr1 = etree.HTML(content1)
        num = etr1.xpath('//*[@id="pagebar"]/div[1]/label[last()-1]/text()')
        # with open(li[rr][0] + '+' + li[rr][1] + '.csv', 'w', newline='') as csvfile:
        for a in range(1, int(num[0]) + 1):
            try:
                dbname = post_info.li[rr][0]+"+"+li[rr][1]
            except:
                continue
            print(a)
            content = driver.page_source
            etr = etree.HTML(content)
            item = etr.xpath('//*[@id="jztable"]/table/tbody/tr')
            for info in item:
                data = []
                index = info.findall('td')
                time = index[0].text
                if time == None:
                    time = '0'
                unit = index[1].text
                if unit == None:
                    unit = '0'
                total = index[2].text
                if total == None:
                    total = '0'
                precent = index[3].text
                if precent == None:
                    precent = '0'
                buy = index[4].text
                if buy == None:
                    buy = '0'
                sel = index[5].text
                if sel == None:
                    sel = '0'
                f = time + ',' + unit + ',' + total + ',' + precent + ',' + buy + ',' + sel+'\n'
                # csvfile.write(f)
                try:
                    dbname.insert_one({'time': time, 'uniy': unit, 'precent': precent, 'buy': buy, 'sel': sel})
                    print('存入数据库成功')
                except:
                    continue
            import time

            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="pagebar"]/div[1]/label[last()]').click()
            time.sleep(1)
        driver.close()
    except:
        continue

# f = open('1.txt', 'w+')
# f.write(content)
# f.close()

# driver.close()
driver.quit()
# data.extend(time)
# data.extend(unit)
# data.extend(total)
# data.extend(precent)
# data.extend(buy)
# data.extend(sel)
