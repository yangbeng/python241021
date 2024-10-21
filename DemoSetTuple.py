# DemoSetTuple.py

# 세트 형식
a = {1,2,3,4}
b = {3,4,4,5}
print(a)
print(b)
print(type(a))
print(type(b))
print(a.intersection(b))
print(a.difference(b))
print(a.union(b))


# tuple
tp = (10,20,30)
print(tp)
print(len(tp))
print(type(tp))

# 함수 정의
def calc(a,b):
    return a*b, a+b

# 함수 호출
result = calc(3,4)
print(result)
print("id %s, name:%s" %(result[0], result[1]))

# 형식 변환
a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(b)
c = tuple(a)
print(c)

# Dictionary

colors = {"apple" : "red", "banana" : "yellow" }
print(colors)
# 입력
colors["Cherry"] = "red"
print(colors)

# 삭제
del colors["apple"]
print(colors)

for k,v in colors.items():
    print(k,v)


#  bool 형식
isRight = True
print(type(isRight))
print(1 < 2)
print(1 != 2)
print(1 == 2)
print(True and True and False)
print(True or True or False)
print(True and True or False)


# 연산자
print(5/2)
print(5//2)
print(5%2)
print(5**2)