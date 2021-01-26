def swap(word):
    # 여기에 코드를 작성합니다.

    #변수 설정
    result = ''

    ''
    for i in word:
        # 요소를 10진수로 변환
        temp =ord(i)

        # 대문자와 소문자가 32차이가 남
        if temp >= 97:
            # 소문자인 경우 32를 뺀 값을 문자로 반환해서 result에 추가
            result += chr(temp - 32)
        else :
            # 대문자인 경우 32를 더한 값을 문자로 반환해서 result에 추가
            result += chr(temp + 32)
    #결과 반환
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(swap('aPpLe'))
    # => 'ApPlE'
    print(swap('SSAFY'))
    # => 'ssafy'
    print(swap('Python'))
    # => 'pYTHON'