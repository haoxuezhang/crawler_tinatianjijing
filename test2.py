import signal
from lxml import etree
from selenium import webdriver
import time
import csv
import selenium
import re
import lxml

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

main_url = 'http://fund.eastmoney.com/data/fundranking.html'

driver = webdriver.PhantomJS()  # or add to your PATH
# driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--load-images=false'])  # or add to your PATH
# driver = webdriver.Chrome()
# set bigger windows height to dynamically load more data    //*[@id="pagebar"]/div[1]/label[7]

driver.set_window_size(1280, 3200)  # optional
driver.get(main_url)
driver.find_element_by_xpath('/html/body/div[7]/div[4]/div[3]/label/span').click()
time.sleep(8)
content1 = driver.page_source
etr1 = etree.HTML(content1)
with open('num.csv', 'w', newline='') as csvfile:
    item = etr1.xpath('//*[@id="dbtable"]/tbody/tr')
    for info in item:
        index = info.findall('td')
        number = index[2].find('a').text
        name = index[3].find('a').text
        data = number+','+name+'\n'
        csvfile.write(data)
        # content = driver.page_source
        # etr = etree.HTML(content)
        # item = etr.xpath('//*[@id="jztable"]/table/tbody/tr')
        # for info in item:
        #     data = []
        #     index = info.findall('td')
        #     time = index[0].text
        #     unit = index[1].text
        #     total = index[2].text
        #     precent = index[3].text
        #     buy = index[4].text
        #     sel = index[5].text
        #     f = '\n' + time + ',' + unit + ',' + total + ',' + precent + ',' + buy + ',' + sel
        #     csvfile.write(f)
        # import time
        # time.sleep(1)
        # driver.find_element_by_xpath('//*[@id="pagebar"]/div[1]/label[8]').click()
        # time.sleep(5)

# f = open('1.txt', 'w+')
# f.write(content)
# f.close()

driver.close()
driver.quit()
# data.extend(time)
# data.extend(unit)
# data.extend(total)
# data.extend(precent)
# data.extend(buy)
# data.extend(sel)
