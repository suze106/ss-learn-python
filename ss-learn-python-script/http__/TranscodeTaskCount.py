#/usr/bin/python3

import json;
import datetime;
import http.client;
from time import sleep;

def loopQuery():
    while True:
        querysdf();
        try:
            sleep(5);
        except KeyboardInterrupt as kbi:
            print("手动干预，强制退出");
            return;
            # print(kbi.__traceback__);

def querysdf():
     httpRq = http.client.HTTPConnection("hb.uts.le.com");
     httpRq.request("GET","/api/vod_resource.json");
     res = httpRq.getresponse();
     loadJson(res.read());
     httpRq.close();

'''
    获取当前时间（两种结果格式一样 eg.2018-08-14 17:32:01）：
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
        datetime.datetime.now().strftime('%F %T');
    格式化GMT：
        strptime = datetime.datetime.strptime(date_, '%a, %d %b %Y %H:%M:%S GMT')
    
    (import time)格式化GMT时间：
        eg.Fri, 24 Apr 2020 05:44:26 GMT
        time.mktime(time.strptime(date_,'%a, %d %b %Y %H:%M:%S GMT'))
    
'''
def loadJson(str):
     # print(str);
     #current time
     currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
     json_ = json.loads(str);
     count = Count();
     loadDict(json_,count);
     loadList(json_,count);
     print(count.get(),'-----------',currentTime);
     print();

def loadDict(dict_,count=None):
     if isinstance(dict_,dict):
          for k,v in dict_.items():

               if isinstance(v,list):
                    loadList(v,count);
               elif isinstance(v,dict):
                    loadDict(v,count)
               else:

                    if k=='in_use' and count is not None:
                         # print(count.get(),'\t',v)
                         count.incre(v);



def loadList(list_,count=None):
     if isinstance(list_,list):
          for item in list_:
               if isinstance(item,dict):
                    loadDict(item,count);
               elif isinstance(item,list):
                    loadList(item,count)
               else:
                    print(item);

'''
    用于统计当前正在执行的任务数据
'''
class Count:

    count = 0;

    def __init__(self,count=0):
        self.count = count;

    def incre(self,size):
        self.count+=size;

    def cutDown(self,size):
        self.count-=size;

    def get(self):
        return self.count;



if __name__ == '__main__':
    loopQuery();


