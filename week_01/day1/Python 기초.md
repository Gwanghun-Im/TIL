# Python 기초

## 기초문법

### 주석

> `#`으로 표시
>
> `'''  '''`으로 여러 문장 가능

```python
# 한줄로 주석처리
"""
여러줄을
주석처리
"""
/* 
이건 안댐
*/
```

### 코드라인

> 여러줄 입력시 아래가 관례

```python
print('''Hello
World !''')
```

---

## 변수

### 변수

#### id

> `id()` 로 메모리 주소를 나타낸다.

```python
dust = 60
id(dust)
```

```bash
140705341640208
```



#### 식별자

> 식별자는 파이썬에서 식별할때 사용되는 이름
>
> `import keyword` 라이브러리 호출 후 `keyword.kwlist`로 확인가능

```python
import keyword
print(keyword.kwlist)
```

```bash
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```



## 데이터 타입

### 실수

#### 실수의 연산

> 실수의 경우 값을 처리할때 조심해야한다. 
>
> ```python
> 3.5 - 3.12 == 0.38
> ```
>
> *위의 결과값이 `False`라고 출력*
>
> `math`라이브러리의 `math.isclose(a, b)`로 확인가능

```python
a = 3.5 - 3.12
b = 0.38

import math
math.isclose(a, b)
```





# Data container

### 시퀀스에서 활용할 수 있는 연산자 함수

| operation    | 설명             |
| ------------ | ---------------- |
| x `in` s     | containment test |
| x `not in` s | containment test |
| s1 `+` s2    | concatenation    |
|s `*` n|n번만큼 반복하여 더하기|
|`s[i]`|indexing|
|`s[i:j]`|slicing|
|`s[i:j:k`]|k간격으로 slicing|
|len(s)|길이|
|min(s)|최솟값|
|max(s)|최댓값|
|s.count(x)|x의 개수|

 ## 비 시퀀스형 컨테이너

### `set`

> `{}` 로 표현가능 순서가 없다
>
> 중복된 값 불가능
>
> 차집합(`-`), 합집합(`|`), 교집합(`&`)

### 데이터 분류

> `mutable` vs. `immutable`
>
> 데이터는 크게 변경 가능한 것(`mutable`)들과 변경 불가능한 것(`immutable`)으로 나뉘며, python은 각각을 다르게 다룹니다

#### 변경 불가능한(`immutable`) 데이터

* 리터럴(literal)

    - 숫자(Number)
    - 글자(String)
    - 참/거짓(Bool)

* range()

* tuple()

* ~~frozenset()~~

### 변경 가능한(`mutable`) 데이터

- `list`
- `dict`
- `set`

```python
num1 = [1, 2, 3, 4]
num2 = num1
num2[0] = 100

print(num1)
print(num2)
```

```bash
[100, 2, 3, 4]
[100, 2, 3, 4]
```

```python
num1 = [1, 2, 3, 4]
num2 = list(num1)
num2[0] = 100

print(num1)
print(num2)
```

``` bash
[1, 2, 3, 4]
[100, 2, 3, 4]
```

