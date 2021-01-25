# Mutable 데이터 복사

> 파이썬에서 대입문(=)은 객체를 복사하지 않고, 대상과 객체 사이에 바인딩을 만듭니다.
>
> Mutable 컬렉션 또는 Mutable 항목들을 포함한 컬렉션의 경우, **원본 컬렉션을 변경하지 않고 사본을 변경하기 위해 복사가 필요**합니다.
>
> 이 모듈은 일반적인 **얕은 복사**와 **깊은 복사** 연산을 제공합니다.

[Python Docs - Copy](https://docs.python.org/ko/3/library/copy.html)



## 1. 할당 (단순 복사)

> 메모리 상의 같은 주소를 바라보게 된다.

* 두 개의 변수 중 하나만 변경되어도, 나머지 하나도 함께 수정되는 현상이 발생한다.

    ```python
    list_a = [1, 2, 3]
    list_b = list_a

    print(list_a)  # [1, 2, 3]
    print(list_b)  # [1, 2, 3]

    list_b[0] = 5
    print(list_a)  # [5, 2, 3]
    print(list_b)  # [5, 2, 3]
    ```





## 2. 얕은 복사 (shallow copy)

>  새로운 리스트를 생성한다.

* **얕은 복사 세 가지 방법**
  
  1. 슬라이싱 : `list_b = list_a[:]`
  2. list() : `list_b = list(list_a)`
3. copy 모듈 : `list_b = copy.copy(list_a)`
  
    ```python
    list_a = [1, 2, 3]
  list_b = list_a[:]
  
    list_b[0] = 99
    print(list_b)  # [99, 2, 3]
    print(list_a)  # [1, 2, 3]
  ```
  
* 하지만 리스트 안의 리스트, **내부 리스트는 원본과 동일한 메모리 주소를 가리킨다**.

  ```python
  list_a = [1, 2, [3, 4]]
  list_b = list_a[:]
  
  list_b[2][0] = 99
  print(list_b)  # [1, 2, [99, 4]]
  print(list_a)  # [1, 2, [99, 4]]
  ```



## 3. 깊은 복사 (deep copy)

> 새로운 리스트를 생성하고, 그 안에 있는 리스트들도 새롭게 생성한다.

```python
import copy

list_a = [1, 2, [3, 4]]
list_b = copy.deepcopy(list_a)

list_b[2][0] = 99
print(list_b)  # [1, 2, [99, 4]]
print(list_a)  # [1, 2, [3, 4]]
```



