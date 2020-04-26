import http.client
import datetime,time

import pyautogui
import json
import pyautogui as pag

'''
    打包为exe:
    pyinstaller -F "E:\workspace\own\ss-learn-python\ss-learn-python-script\\frame\mouse\MouseClick.py" -p "E:\workspace\own\ss-record\\venv\Lib\site-packages"
    注意（pyinstaller版本）:
        -p 指定的是该项目的python env，如果不指定的话，当执行EXE是有可能出现找不到模块的问题
        -i 可指定图标 icon
'''

def getMouthPoint():
    x,y = pag.position()
    pos="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
    print(pos)

def sortFunc(elem):
    return int(elem.get("index"))

def clickTarget(points:list,clickRestTime):
    points.sort(key=sortFunc)
    for point in points:
        x = point.get("x")
        y = point.get("y")
        pyautogui.click(int(x),int(y))
        print(x+"\t"+y)
        if clickRestTime!=''and clickRestTime!='0':
            time.sleep(float(clickRestTime))

def theServerTime():
    try:
        http_connection = http.client.HTTPConnection("www.tencent.com")
        http_connection.request("get", "/")
        response = http_connection.getresponse()
        date_ = response.headers['Date']
        timestamp = datetime.datetime.strptime(date_, '%a, %d %b %Y %H:%M:%S GMT').timestamp()
        return int(timestamp*1000)
    except BaseException:
        return theServerTime();

def domain(beginTime,endTime,points:list,clickRestTime):
    oneDay = 60*60*24*1000#一天的时间
    # serverTime = theServerTime()#服务器的日期
    # time5 = serverTime+5000
    # intervalInSec = 1000/interval
    # curTime=0

    #等待到执行时间
    # sysTime = datetime.datetime.now().timestamp()
    #加八小时是因为时区问题造成时间戳会少八小时
    sysTime = int(time.time()*1000)+int(oneDay/3)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    todayNowTime = int(sysTime%oneDay);
    # todayNowTime = 5%oneDay
    slp = 0
    if todayNowTime<(beginTime*1000):
        slp=(beginTime*1000)-todayNowTime
    elif todayNowTime>(beginTime*1000):
        slp=(beginTime*1000)+(oneDay/1000)-todayNowTime
    slp = slp/1000
    while slp>=1:
        if slp==1:
            curNowTime = datetime.datetime.now().timestamp()%(oneDay/1000)
            if curNowTime==beginTime:
                slp=0
        else:
            print("等待:"+str(slp)+"s")
            time.sleep(slp)
            slp=1

    serverTime=theServerTime()
    print("A \t"+str((serverTime%oneDay))+"\t"+str(beginTime*1000)+"\t"+str((serverTime%oneDay)>=(beginTime*1000)))
    print("B \t"+str((serverTime%oneDay))+"\t"+str(endTime*1000)+"\t"+str((serverTime%oneDay)<=(endTime*1000)))
    while (serverTime%oneDay)>=(beginTime*1000) and (serverTime%oneDay)<=(endTime*1000):
        # if curTime==serverTime:
        #     # if intervalInSec<(curLocalTime-lastLocalTime):
        #     # print("执行时间"+str(serverTime))
        #     clickTarget(points,clickRestTime)
        #     localtime = time.localtime(serverTime/1000)
        #     formatTime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
        #     print("执行时间"+formatTime)
        # else:
        #     curTime = serverTime
        clickTarget(points,clickRestTime)
        localtime = time.localtime(serverTime/1000)
        formatTime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
        print("执行时间"+formatTime)
        serverTime=theServerTime()
        print("============================================")

def loadParam(params):
    # params = '{"beginTime":"86399","endTime":"300","point":[{"index":1,"x":"110","y":"110"},{"index":2,"x":"130","y":"140"},{"index":3,"x":"170","y":"170"}]}'
    data = json.loads(params)
    return int(data.get("beginTime")),int(data.get("endTime")),data.get("point")

def portal():
    try:
        params = input("请输入：")
        if params== '0':
            getMouthPoint()
        else:
            clickRestTime = input("请输入每秒最大频次：")
            beginTime,endTime,point = loadParam(params)
            domain(beginTime,endTime,point,clickRestTime)

        print("本次执行结束")
        print()
    except BaseException as e:
        print('取值范围不正确，或者JSON格式错误。'+str(e))
        print('取值范围有：\r\n\t0 或 JSON字符串。')
        print('\t\t1:获取鼠标坐标。')
        print('\t\tJSON模板:{"beginTime":"86399","endTime":"300","point":[{"index":1,"x":"110","y":"110"},{"index":2,"x":"130","y":"140"},{"index":3,"x":"170","y":"170"}]}')
        portal()

if __name__ == '__main__':
    #domain(5)
    while True:
        portal()


