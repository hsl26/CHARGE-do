from bs4 import BeautifulSoup as BS 
import requests
import sqlite3

import datetime

now = datetime.datetime.now()
url = "https://api.odcloud.kr/api/EvInfoServiceV2/v1/getEvSearchList" 
params = {} # dictionary 자료형
params['serviceKey'] ="3RJiQ2qjq2JIZVrCFXK1dKOqOeQqjq21YEN/aO7D1o9wr4D/mcWuAPQQ57HV/VZMxZodnng1Su5jDJCcbVMtvg=="
params['page'] = 1   # (optional) default 1
params['perPage'] = 12   # (optional) default 10
params['returnType'] = 'XML' 
params['cond[addr::LIKE]'] = "전라남도 나주시 빛가람동 120"

res = requests.get(url, params=params)
print(res.url) 

# con = sqlite3.connect('chargedo.db', isolation_level=None)
# cur = con.cursor()

# cur.execute('INSERT INTO chargedo (resultCode, resultMsg, numOfRows, pageNo, totalCount, items, addr, chargeTp, cpId, cpNm, cpStat, cpTp, csId, csNm, lat, longi, statUpdateDatetime) VALUES (?, ?)',
#             (1, 3.14))

'''
url = "http://openapi.kepco.co.kr/service/EvInfoServiceV2/getEvSearchList" 
params = {} # dictionary 자료형
params['serviceKey'] ="3RJiQ2qjq2JIZVrCFXK1dKOqOeQqjq21YEN%2FaO7D1o9wr4D%2FmcWuAPQQ57HV%2FVZMxZodnng1Su5jDJCcbVMtvg%3D%3D"
params['pageNo'] = 1   # (optional) default 1
params['numOfRows'] = 10   # (optional) default 10
params['addr'] = '전라남도 나주시 빛가람동 120'

res = requests.get(url, params=params)
print(res.url) 
print(res.text)


con = sqlite3.connect('chargedo.db', isolation_level=None)
cur = con.cursor()

cur.execute('INSERT INTO chargedo (resultCode, resultMsg, numOfRows, pageNo, totalCount, items, addr, chargeTp, cpId, cpNm, cpStat, cpTp, csId, csNm, lat, longi, statUpdateDatetime) VALUES (?, ?)',
            (1, 3.14))

'''