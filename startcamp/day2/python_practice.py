# 1. 기초 자료형
# number=3 #숫자
# print(number)
# print(type(number))

string = '문자열'
# print(string)
# print(type(string))

boolean = True
# print(boolean)
# print(type(boolean))

string_number = '3'
# print(int(string_number) + 5)

# 2. f-string (string interpolation - 문자열 안에 변수 삽입)
name = '임광훈'
# print(f'제 이름은{name}입니다.')

# 3. list
my_list = ['python', 'html', 'markdown',]
# print(my_list[2]), print(my_list)
my_list[2] = 'java'
# print(my_list[2]), print(my_list)

# 4.dictionary
# 딕셔너리 선언
age_dict = {
    '박소현' : 25, 
    '김지용' : 83,
}

# 딕셔너리 요소 접근
# print(age_dict['김지용'])
# print(age_dict['박소현'])
# print(age_dict.get('김지용'))

#딕셔너리 요소 변경
age_dict['김지용'] = 103
# print(age_dict.get('김지용'))

# 기초 연산자
# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(100 / 5)
# print(100 // 5)
# print(100 % 5)
# print(3 ** 5)

# # 비교 연산자
# print(5 == 5)
# print(5 == '3')
# print(5 != 3)
# print(5 >= 3)
# print(5 < 3)

#조건문
n = 10
# 1. 주어진 양수 n이 홀수, 짝수인지 판단하여 출력하는코드를 작성해라
# if n%2 == 0 :
#     print('짝수')
# else :
#     print('홀수')

# 반복문
# numbers = [1,2,3] 
# for i in numbers:
#     print(i)

numbers = range(1,10)
for i in numbers:
    a = ['짝수','홀수']
    print(f'숫자 {i}는 {a[i%2]}입니다.')

