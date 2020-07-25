import requests

r = requests.post("http://www.baidu.com")
r.encoding = 'utf8'
print(r.text)