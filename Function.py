# Function.py

# call by reference??!!

# 1) 함수 정의
def times(a,b):
    return a*b

# 2) 함수를 호출
result  = times(3,4)
print(result)

x = 10

## local  지역 G 전역 
# 함수 정의
def  setValue(newvalue):
    x = newvalue
    print("함수 내부:", x)

# 호출
result = setValue(5)
print(result)
print(x)

# 전역변수와 지역변수
x = 5
def  func(a):
    return a+x

print(func(1))

def func2(a):
    x = 10
    return a+x
print(func2(1))

# 기본값 명시
def times(a=10, b=20):
    return a*b


# 호출
print(times())
print(times(5))
print(times(5,6))

# 키워드 인자방식(파라미터 변수명 기술)
def connectURI(server, port):
    strURL = "httl://" + server + ":" + port
    return strURL

print(connectURI("mulit.com", "80"))
print(connectURI(port="mulit.com", server="80"))

