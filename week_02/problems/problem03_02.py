import json


def rotate(data):
    # 여기에 코드를 작성합니다.

    #변수 설정
    am_pm = {'am':[], 'pm':[]}

    # 변수에서 리스트 요소를 가져옴
    for i in data:
        # 0번째는 am에 추가
        am_pm['am'] += [i[0]]
        # 1번째는 pm에 추가
        am_pm['pm'] += [i[1]]

    # 반환
    return am_pm



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem03_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(rotate(temperature_list))
    # => {
    #     'am': [36.7, 36.9, 37.8, 36.7, 36.3, 36.5, 36.8], 
    #     'pm': [36.5, 37.5, 37.8, 36.5, 36.4, 36.5, 36.6]
    # }
