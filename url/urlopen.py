from http.client import HTTPMessage
import urllib
from urllib.request import urlopen, urlretrieve
from pip._vendor.requests import Response

__author__ = 'han'
from urllib import *

urltr=urlretrieve("http://www.sina.com")
u0=urltr[0]
def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print ("%.2f%%"% percent)

url = 'http://www.sina.com.cn'
local = 'd:\\sina.html'
urlretrieve(url, local, callbackfunc)

print(urltr[1])

for  i in urltr[1]._headers :
        print(i[0]+"-->"+i[1]);

exit (0)


