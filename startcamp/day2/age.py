import requests

#API 요청 URL 확인 + 필요한 데이터 건네주기

name = 'gwanghun'
url = f'https://api.agify.io/?name={name}'

# URL로 요청 보내기
response = requests.get(url).json()
print(response)

name = response['name']
age = response['age']
print(f'{name}님의 예상 나이는 {age}입니다')

