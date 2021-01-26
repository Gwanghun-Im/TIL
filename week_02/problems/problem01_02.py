import json


def average(scores):
    # 여기에 코드를 작성합니다.

    # 변수 설정
    total = 0 # 합
    n = len(scores) # scores의 개수

    # 리스트 요소 각각을 불러와 total에 더함
    for i in scores:
        total += i

    return total/n


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores_json = open('problem01_data.json')
    scores = json.load(scores_json)
    print(average(scores)) 
    # => 82.5