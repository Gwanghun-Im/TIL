import random
# 1~45 숫자 만들어서 저장하기
numbers = range(1,46)

lucky_numbers = random.sample(numbers, 6)
print(sorted(lucky_numbers))
