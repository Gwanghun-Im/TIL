# 1. 필요한 라이브러리 import 하기
import requests
import pprint

# 2. API URL 및 KEY값 확인
key = 'WJYCcLe%2FuHsm6xfF7gP0ERa3cBbXlykQV3f8JN8gdkW6u7rvr4SN%2Fnu06ezOvjiLaMDRDTXftCEwkXCOl2dOzw%3D%3D'
sido ='광주'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType=json&numOfRows=100&pageNo=1&sidoName={sido}&ver=1.0'

# 3. 요청 및 응답값 확인
res = requests.get(url).json()
# pprint.pprint(res)

items = res['response']['body']['totalCount']
for i in range(items):
    dust = res['response']['body']['items'][i]['pm10Value']
    dong = res['response']['body']['items'][i]['stationName']
    print(f'{sido}의 미세먼지 농도는 {dust}입니다. (측정소:{dong})')


