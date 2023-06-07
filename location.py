from flask import Flask, render_template, jsonify
import json
import requests
import sqlite3
# import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/charge')
def charge():
    url = "https://api.odcloud.kr/api/EvInfoServiceV2/v1/getEvSearchList" 
    params = {} # dictionary 자료형
    params['serviceKey'] ="3RJiQ2qjq2JIZVrCFXK1dKOqOeQqjq21YEN/aO7D1o9wr4D/mcWuAPQQ57HV/VZMxZodnng1Su5jDJCcbVMtvg=="
    params['page'] = 1   # (optional) default 1
    params['perPage'] = 12   # (optional) default 10
    params['returnType'] = 'JSON' 
    # params['cond[addr::LIKE]'] = "전라남도 나주시 빛가람동 120" # default 전라남도 나주시 빛가람동 120
    params['cond[addr::LIKE]'] = "서울특별시 성북구 정릉동" 

    res = requests.get(url, params=params)
    # print(res.url) 
    # print(res.text)

    # jsonData = res.json()
    jsonObject = json.loads(res.text)
    # print(jsonData)
    
    if isinstance(jsonObject, dict):
        jsonData = jsonObject.get("data") # data라는 key의 value
        
        csId = []   # csId: 충전소 ID
        for td in jsonData:
            csId.append(td.get('csId')) 
        # print(csId)
        
        csNm = []   # csNm: 충전소 명칭
        for td in jsonData:
            csNm.append(td.get('csNm')) 
        # print(csNm)
        
        addr = []   # addr: 충전소 주소(샘플 : 전라남도 나주시 전력로 55)
        for td in jsonData:
            addr.append(td.get('addr')) 
        # print(addr)
        
        lat = []   # lat: 위도
        for td in jsonData:
            lat.append(td.get('lat')) 
        # print(lat)
        
        longi = []   # longi: 경도
        for td in jsonData:
            longi.append(td.get('longi')) 
        # print(longi)
        
        cpId = []   # cpId: 충전기 ID
        for td in jsonData:
            cpId.append(td.get('cpId')) 
        # print(cpId)
        
        cpNm = []   # cpNm: 충전기 명칭
        for td in jsonData:
            cpNm.append(td.get('cpNm')) 
        # print(cpNm)
        
        chargeTp = []   # chargeTp: 충전기타입(1:완속, 2: 급속)
        for td in jsonData:
            chargeTp.append(td.get('chargeTp')) 
        # print(chargeTp)
        
        cpTp = []   # cpTp: 충전방식(1:B타입(5핀), 2: C타입(5핀), 3:BC타입(5핀),4: BC타입(7핀),5: DC차 데모, 6:AC 3상, 7: DC콤보,8: DC차데모+DC콤보. 9:DC차데모+AC3상, 10: DC차데모+DC콤보, AC3상)
        for td in jsonData:
            cpTp.append(td.get('cpTp')) 
        # print(cpTp)
        
        statUpdatetime = []   # statUpdatetime
        for td in jsonData:
            statUpdatetime.append(td.get('statUpdatetime')) 
        # print(statUpdatetime)
        
        cpStat = []   # cpStat: 충전기 상태( 0: 상태확인불가, 1: 충전가능, 2: 충전중, 3:고장/점검, 4:통신장애, 5:통신미연결,9:충전예약)
        for td in jsonData:
            cpStat.append(td.get('cpStat')) 
        # print(cpStat)
    else:
        print('error!')

    # 2차원 리스트
    mylist = [csId, csNm, addr, lat, longi, cpId, cpNm, chargeTp, cpTp, statUpdatetime, cpStat]

    # 2차원 리스트 뒤집음
    final_list = list(map(list, zip(*mylist)))
    # print(final_list)

    con = sqlite3.connect('chargedo.db', isolation_level=None)
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS chargeDO(id INTEGER PRIMARY KEY, csId INTEGER, csNm TEXT, addr TEXT, lat REAL, longi REAL, cpId INTEGER, cpNm TEXT, chargeTp TEXT, cpTp TEXT, statUpdatetime TEXT, cpStat TEXT)")

    con.execute("DELETE FROM chargeDO")

    con.commit()

    cur.executemany('''INSERT INTO chargeDO(csId, csNm, addr, lat, longi, cpId, cpNm, chargeTp, cpTp, statUpdatetime, cpStat) VALUES (?,?,?,?,?,?,?,?,?,?,?)''', final_list)

    con.commit()
    
    cur.execute('SELECT * FROM chargeDO')
    
    rows = cur.fetchall()
    
    # for item in rows:
        # print(item)
    
    if rows:
        return jsonify({'csId': csId, 'csNm': csNm, 'addr': addr, 'lat': lat, 'longi': longi, 'cpId': cpId, 'chargeTp': chargeTp, 'cpTp': cpTp, 'statUpdatetime': statUpdatetime, 'cpStat': cpStat}) # 값 있으면 해당 값 전달
    else:
        return jsonify({'csId': 3069,'lat': 37.60992959003136, 'longi': 126.99738378955175}) # 값 없으면 (37.60992959003136, 126.99738378955175) 전달


if __name__ == '__main__':
    app.run(host='localhost', port=8001)
