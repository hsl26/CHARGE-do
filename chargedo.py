from bs4 import BeautifulSoup as BS 
import requests
import datetime

now = datetime.datetime.now()
url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst" 
params = {} # dictionary 자료형
params['serviceKey'] ="<인증키>"
#params['numOfRows'] = 50
#params['pageNo'] = 1
#params['dataType'] = 'XML' params['base_date'] = now.strftime("%Y%m%d") #params['base_time'] = now.strftime("%H%M") params['base_time'] = '0500' # 05시 발표 params['nx'] = 60 # 정릉제3동 (격자 X) params['ny'] = 128 # 정릉제3동 (격자 Y)