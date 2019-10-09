from bs4 import BeautifulSoup
import requests
import execjs
import json
username = input()
password = input()
session = requests.session()
url = r'https://sso.buaa.edu.cn/login'
Murl = requests.get(url).url
Lurl = session.get(Murl).content
soup = BeautifulSoup(Lurl,"lxml")
Bs = soup.find_all('input')
Value = []
for V in Bs[:]:
    datad = V.get('value')
    Value.append(datad)
print(list(Value))
execution = Value[4]
lt = Value[3]
data = {'username':username,'password':password,'code':'','submit':'登录','_eventId':'submit','lt':lt,'execution':execution}
f = session.post(url,data = data).url
f = f.encode('utf-8')
index = session.get(f).content.decode('utf-8')
headers={
"auth_token":"",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
'Referer':'http://bykc.buaa.edu.cn/login',
'Host':'bykc.buaa.edu.cn'
}
f2 = session.post(r'http://bykc.buaa.edu.cn/sscv/querySelectableCourse').url.encode('utf-8')
token = session.get('http://bykc.buaa.edu.cn/sscv/casLogin',headers = headers)
headers['auth_token'] = token.url.split('=')[1]
pc = json.loads(session.get(f2,headers = headers).content.decode('utf-8'))
len = len(pc['data'])
for i in range(len):
    print(str(pc['data'][i]['id'])+'--'+str(pc['data'][i]['courseName']))
