import json


def check(data):
    # 여기에 코드를 작성합니다.

    # 변수 설정
    cnt = 0

    #data 의 길이만큼 반복
    for i in range(len(data)):
        #오전 오후 2회 반복
        for j in range(2):
            # 37.5 이상이면 카운트를 1 증가
            if data[i][j] >= 37.5:
                cnt += 1

            # 37.5 미만이면 카운트 초기화
            else :
                cnt = 0

            # 카운트가 3 이상이면 True 반환
            if cnt >= 3:
                return True

    # 카운트가 3 미만이면 false 반환
    return False



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem03_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(check(temperature_list))
    # => True