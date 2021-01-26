def dec_to_bin(n):
    # 여기에 코드를 작성합니다.

    #변수 설정

    #2보다 작으면 그대로 반환
    if n < 2:
        return f'{n}'
    
    #2 이상이면 몫을 재귀하고 나머지 반환
    return dec_to_bin(n//2) + f'{n%2}'

    #결과 반환 (문자열)
    



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # => '1010'
    print(dec_to_bin(5))
    # => '101'
    print(dec_to_bin(50))
    # => '110010'