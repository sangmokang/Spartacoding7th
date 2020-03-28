import requests # requests 라이브러리 설치 필요

# 특정 서버에 요청 할 때 코드상에서 Get, Post 방식으로 가져오는 것.

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()
print (rjson['RealtimeCityAir']['row'][0]['NO2'])
print(rjson)
rows = rjson['RealtimeCityAir']['row']

for row in rows:
    print(rjson['RealtimeCityAir']['row'][0]['NO2'])

