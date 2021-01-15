import requests
import pprint

name = 'ruby'
url = f'https://api.nationalize.io/?name={name}'

# URL로 요청 보내기
response = requests.get(url).text
res = eval(response)
pprint.pprint(res)

# name = response['name']
# if len(response['country'])==0:
#     print(f'{name}님의 예상 국적은 없습니다.')
# else:
#     national = response['country'][0]['country_id']
#     probability = response['country'][0]['probability']
#     print(f'{name}님의 예상 국적은 {probability}확률로 {national}입니다')

# try :
#     national = response['country'][0]['country_id']
#     probability = round(response['country'][0]['probability']*100,2)
#     print(f'{name}님의 예상 국적은 {probability}% 확률로 {national}입니다')
# except:
#     print(f'{name}님의 예상 국적은 없습니다.')


