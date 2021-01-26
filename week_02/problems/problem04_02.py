def caesar(word, n):
    # 여기에 코드를 작성합니다.

    #변수 설절
    result = ''

    for i in word:
        # word 각 요소를 숫자로 변환
        temp = ord(i)

        #대문자일 경우
        if temp >= 65 and temp <= 90:
            # n 만큼 민다
            temp += n
            # 민 숫자가 Z를 초과할 경우 나머지에 65를 더한다
            temp %= 91
            temp = temp if temp >= 65 else temp + 65

        #소문자일 경우
        elif temp >= 97 and temp <= 122:
            # n 만큼 민다
            temp += n
            # 민 숫자가 z를 초과할 경우 나머지에 65를 더한다
            temp %= 123
            temp = temp if temp >= 97 else temp + 97

        # result에 결과값을 더한다.
        result += chr(temp)

    #반환
    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # => 'fuuqj'
    print(caesar('ssafy', 1))
    # => 'ttbgz'
    print(caesar('Python', 10))
    # => 'Zidryx'