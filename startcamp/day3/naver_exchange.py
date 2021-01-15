import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
# print(type(response))//

# str을 구조화하여 데이터를 추출하기 쉬운 형태로 만들기
soup = BeautifulSoup(response, 'html.parser')

#경로를 건네주고 원하는 정보 추출하기
exchange = soup.select_one('a.head.usd > div > span.value').text

print(f'현재 원/달러 환율은, {exchange}입니다')