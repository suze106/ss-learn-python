import http.client,urllib.parse

def get(url):
    http_connection = http.client.HTTPConnection(url)
    http_connection.request("get", "/")
    response = http_connection.getresponse()
    data = response.read()
    return data;

def post(url,params):
    http_connection = http.client.HTTPConnection(url)
    urllib.parse.urlencode()
    headers = {}
    http_connection.request("post","",params,headers)
    response = http_connection.getresponse()
    data = response.read()
    http_connection.close()
    return data;
