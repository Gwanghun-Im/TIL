import requests
from pprint import pprint
from bs4 import BeautifulSoup

weather_rule_dict = {
    'Snow':'눈',
    'Sleet': '진눈깨비',
    'Hail':'우박',
    'Thunderstom':'천둥번개',
    'Heavy Rain':'폭우',
    'Light Rain':'비',
    'Showers':'소나기',
    'Heavy Cloud':'구름많음',
    'Light Cloud':'구름',
    'Clear':'화창함'
}

# search location을 통해 부산의 woeid를 가져옴
location_search_url = "https://www.metaweather.com/api/location/search/?query=busan"
location_result = requests.get(location_search_url).json()
busan_id = location_result[0]["woeid"]

# location을 통해 부산의 날씨를 가져옴
weather_url = "https://www.metaweather.com/api/location/"+str(busan_id)
weather_result = requests.get(weather_url).json()
today_weather_dict = weather_result["consolidated_weather"][0]
# print(f'{weather_result["title"]}의 {today_weather_dict["applicable_date"]} 날씨는 {weather_rule_dict[today_weather_dict["weather_state_name"]]} 입니다.')

# 5일간의 날씨 print 자동화
for i in range(5):
    date = "day"+str(i)+"_weather_dict"
    locals()[date] = weather_result["consolidated_weather"][i]
    print(f'{weather_result["title"]}의 {locals()[date]["applicable_date"]} 날씨는 [{weather_rule_dict[locals()[date]["weather_state_name"]]}] 입니다.')
    print(f'\t 최대온도는 {round(locals()[date]["max_temp"],2)}, 최저온도는 {round(locals()[date]["min_temp"],2)}, 습도는 {locals()[date]["humidity"]} 입니다.\n')

