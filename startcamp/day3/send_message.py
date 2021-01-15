# 가장 최근에 메시지를 보낸 사용자에게
# 메시지 보내기 



# 1. 요청에 필요한 라이브러리 import
import requests, pprint

# 2. API 요청 URL과 + Token 확인 
token = ''
api_url = f'https://api.telegram.org/bot{token}'

# 3. 메시지 보낸 사용자의 ID값 찾기
chat_id_url = f'{api_url}/getUpdates'
res = requests.get(chat_id_url).json()
chat_id = res['result'][0]['message']['chat']['id']

# 4. chat id 에게 메시지 보내기
text = input('메시지를 입력하세요 : ')
msg=f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(msg)


