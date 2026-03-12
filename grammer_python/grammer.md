### 텍스트와 숫자 혼합
텍스트와 숫자를 쉼표로 구분하여 하나의 출력에서 결합할 수 있습니다

print("I am", 35, "years old.")


### 캐스팅
변수의 데이터 타입을 지정하고 싶다면, 캐스팅으로 할 수 있습니다.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


### 타입 구하기
함수로 변수의 데이터 타입을 얻을 수 있습니다.

print(type(x))


### 변수 이름
파이썬 변수에 대한 규칙:

변수 이름은 반드시 문자 또는 밑줄로 시작해야 합니다
변수 이름은 숫자로 시작할 수 없습니다
변수 이름은 알파벳-숫자 문자와 밑줄(A-z, 0-9, _)만 포함할 수 있습니다

- Camel Case
첫 번째 단어를 제외한 모든 단어는 대문자로 시작합니다:
myVariableName = "John"

- Pascal Case
각 단어는 대문자로 시작합니다:
MyVariableName = "John"

- Snake Case
각 단어는 밑줄이 붙은 문자로 구분됩니다:
my_variable_name = "John"


### Unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits


### 출력 

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

여러 변수를 출력할 때, 쉼표로 구분하면 다양한 데이터타입 동시에 출력 가능 
x = 5
y = "John"
print(x, y)


### 전역 변수
보통 함수 내에서 변수를 만들 때, 그 변수는 지역 함수 안에서만 사용 가능
함수 내에서 전역 변수를 만들려면 global 키워드 사용 가능

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)


### 내장 데이터 타입
텍스트 유형 : str
숫자 유형 : int, float, complex
Sequence 유형 : list, tuple, range
Mapping 유형 : dict
Set 유형 : set, frozenset
Boolean 유형 : bool
Binary 유형 : byte
None 유형 : NoneType

- complex 
복소수는 허수부로 "j" 표시

x = 3+5j
y = 5j
z = -5j


### 랜덤 넘버 
import random
print(random.randrange(1, 10))


### 다중 라인 스트링
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""


### 문자열
- 체크 스트링 in
특정 구절이나 문자가 문자열에 존재하는지 확인하기 위해 다음을 사용할 수 있습니다 핵심 단어.in
txt = "The best things in life are free!"
print("free" in txt)

- 여백 제거 strip()
시작이나 끝에서 모든 여백을 제거합니다:strip()
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

- 스트링 교체 replace()
한 문자열을 다른 문자열로 대체합니다:replace()
a = "Hello, World!"
print(a.replace("H", "J"))


- 스플릿 스트링 split()
구분자의 인스턴스를 찾으면 문자열을 부분문자열로 나눕니다:split()
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

- f - string
age = 36
txt = f"My name is John, I am {age}"
print(txt)

- 소수점 숫자
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

- 이스케이프 문자 \
이스케이프 문자는 평소에는 허용되지 않는 이중 따옴표를 사용할 수 있게 해줍니다:
txt = "We are the so-called \"Vikings\" from the north."
예시 : \' \\ \n \r \t \b \f \ooo \xhh

- 문자열 메서드
https://www.w3schools.com/python/python_strings_methods.asp



### boolean 값
- 함수를 통해 객체가 특정 데이터 타입에 속하는지 판단할 수 있습니다:isinstance()
x = 200
print(isinstance(x, int))

### 바다코끼리 연산자자 :=
대입과 동시에 그 값을 식의 결과로 쓰는 연산 
print(x := 3)

### 항등성 연산자
객체들이 같은지 여부가 아니라, 실제로 동일한 객체이고 동일한 메모리 위치를 가진 객체인지 비교하는 데 사용됩니다:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) #True
print(x is y) #False
print(x == y) #True 

