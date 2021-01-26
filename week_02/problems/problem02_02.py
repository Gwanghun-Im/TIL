import json


def title_length(movie):
    # 여기에 코드를 작성합니다.

    # title을 가져옴
    title = movie.get('title')

    #title의 길이를 반환
    return len(title)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem02_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(title_length(movie)) 
    # => 4