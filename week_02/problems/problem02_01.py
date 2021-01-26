import json


def over(movie):
    # 여기에 코드를 작성합니다.
    
    #movie의 평점을 가져와서 8이상이면 True 반환
    if movie.get('user_rating') >= 8:
        return True
    
    # 8 미만이면 False 반환
    return False


# 아래의 코드는 수정하지 않습니`다.
if __name__ == '__main__':
    movie_json = open('problem02_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(over(movie)) 
    # => True