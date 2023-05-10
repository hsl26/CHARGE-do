from bs4 import BeautifulSoup as BS 
import requests
import datetime

now = datetime.datetime.now()
url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst" 
params = {} # dictionary 자료형
params['serviceKey'] ="<인증키>"
#params['numOfRows'] = 50   # (optional) default 10
#params['pageNo'] = 1   # (optional) default 1
#params['dataType'] = 'XML'     # (optional) (XML/JSON) default XML
params['base_date'] = now.strftime("%Y%m%d") 
# #params['base_time'] = now.strftime("%H%M") 
params['base_time'] = '0500' # 05시 발표 
params['nx'] = 60 # 정릉제3동 (격자 X) 
params['ny'] = 128 # 정릉제3동 (격자 Y)

res = requests.get(url, params=params)
#print(res.url) # 전체 url을 string으로 구성하여 전달하는 것도 가능하기는 함. 
#print(res.text)

soup = BS(res.text, 'xml') 
#print(soup)

names = []
for td in soup.select('category'):
    names.append(td.get_text(strip=True)) 
#print(names)

values = []
for td in soup.select('fcstValue'):
    values.append(td.get_text(strip=True)) 
#print(values)

idx = names.index('TMP') # 1시간 기온 (°C) 
print(values[idx])