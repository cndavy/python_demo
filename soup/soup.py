# coding=utf-8
import re
import threading
import requests
import urllib
from bs4 import BeautifulSoup
import time


'''
values ={'wd':'网球'}
encoded_param = urllib.urlencode(values)

url="http://fund.ccb.com/Channel/3218673?text_page="
resp=requests.get(url)
soup = BeautifulSoup(resp.text, "lxml")
pattern=re.compile(r"data4_c1* header*")
def filterClass(css_class):

    match=pattern.match(css_class)
    if match:
        print match.string
    return  match
#soup.prettify()
fund = soup.find_all('td')
i=0
ths=soup.select('#allshow > form > table > thead > tr.even')
for th in ths:
    print th.get_text()
data={
            '选择':None,
            '基金简称':None,
            '基金':None,
            '代码':None,
            '基金管理人':None,
            '基金分类':None,
            '份额':None,
            '净值':None,
            '累计份额':None,
            '净值':None,
            '日增长率'	:None,
            '过去一月':None,
            '过去三月':None,
            '过去一年':None,
            '成立以来':None,
            '三年':None,
            '净值':None,
            '走势图':None,
            '操作':None
}
list=[]
for td in fund:
    for th in ths:
        #print i,td.get_text()
        value=td.get_text()
        key=th.get_text()
        if key<>""  :
          data.key=value

    list.append(data)

'''
#urls 包含所有需要扫描的URL
#lists包含每个线程扫描的结果的列表的列表
lists = []
threads = []
urls=["http://fund.ccb.com/Channel/3218673?text_page=1#falg_link",
      "http://fund.ccb.com/Channel/3218673?text_page=2#falg_link",
      "http://fund.ccb.com/Channel/3218673?text_page=3#falg_link",
      "http://fund.ccb.com/Channel/3218673?text_page=4#falg_link"

]
def check_page(urls,temp) :
    for url in urls:
        soup = BeautifulSoup(requests.get(url).text, "lxml")
        #fund = soup.find_all('td')
        fund =soup.find_all('td',class_=re.compile('data4_c1*'))
        for f in fund:
            temp.append(f.get_text())

for i in range(4):
    temp = []
    lists.append(temp)
    t = threading.Thread(target = check_page, args = ([_ for _ in urls if urls.index(_) % 1 == i], temp))
    time.sleep(2)
    t.start()
    threads.append(t)

for t in threads: t.join()
datas=[]
data={}
for l in lists:
      for  i in range(len(l)):
       # print   l[i].replace("\r\n",""),
        value=l[i].replace("\r\n","")
        key=i%15

        if key==1 : data['基金简称']=value
        if key==2 : data[  '基金代码' ]=value

        if key==3 : data[ '基金管理人'   ]=value
        if key==4 : data[ '基金分类'  ]=value
        if key==5 : data[ '份额净值'  ]=value

        if key==6 : data[ '累计份额净值'   ]=value
        if key==7 : data[ '日增长率'   ]=value

        if key==8 : data[    '过去一月']=value
        if key==9 : data[  '过去三月' ]=value
        if key==10: data[   '过去一年'  ]=value
        if key==11: data[  '成立以来'  ]=value
        if key==12: data[  '三年'  ]=value

        if i % 15==0 :
           # print '--------------------------\n'
            datas.append(data)
            data={}


for data in datas:
    for key   in  data:
          print key, data[key]




