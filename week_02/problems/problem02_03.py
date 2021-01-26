import json


def history(movie):
    # 여기에 코드를 작성합니다.

    # 줄거리를 가져옴
    overview = movie.get('overview')

    # 줄거리에 '과거'가 존재하면 True 반환
    if '과거' in overview:
        return True

    # 존재하지 않으면 False가 반환
    return False


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem02_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(history(movie)) 
    # => False