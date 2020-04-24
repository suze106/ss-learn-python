import http.client;
import datetime;

def httpGetTimeFromServer(url):
    http_connection = http.client.HTTPConnection(url)
    http_connection.request("get", "/")
    response = http_connection.getresponse()
    date_ = response.headers['Date']
    # strftime = datetime.datetime.fromtimestamp(date_).strftime('%Y-%m-%d %H:%M:%S')
    info = response.info()
    print(info)
    print(len(info))
    print(response.headers['Date'])
    strptime = datetime.datetime.strptime(date_, '%a, %d %b %Y %H:%M:%S GMT')
    # print(time.mktime(time.strptime(date_,'%a, %d %b %Y %H:%M:%S GMT')))


if __name__ == '__main__':
    start = datetime.datetime.now().timestamp()
    httpGetTimeFromServer("www.baidu.com")
    end = datetime.datetime.now().timestamp()
    print("耗时:"+str(end-start))
