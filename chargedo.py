from bs4 import BeautifulSoup as BS 
import requests
import sqlite3

import datetime

now = datetime.datetime.now()
url = "http://openapi.kepco.co.kr/service/EvInfoServiceV2/getEvSearchList" 
params = {} # dictionary 자료형
params['ServiceKey'] ="3BtB1QOAci15d9JFVNNAEeWHNTZ0Ztykdu7v53YXwDurXZL0zF4uaIwRU9gWQ5Q+aF9Hu5nj/i7Ik0Ywl5QXzQ=="
params['numOfRows'] = 10   # (optional) default 10
params['pageNo'] = 1   # (optional) default 1
# params['addr'] = "전라남도 나주시 빛가람동 120"

res = requests.get(url, params=params)
print(res.url) 
print(res.text)

'''
con = sqlite3.connect('chargedo.db', isolation_level=None)
cur = con.cursor()

cur.execute('INSERT INTO chargedo (resultCode, resultMsg, numOfRows, pageNo, totalCount, items, addr, chargeTp, cpId, cpNm, cpStat, cpTp, csId, csNm, lat, longi, statUpdateDatetime) VALUES (?, ?)',
            (1, 3.14))

'''