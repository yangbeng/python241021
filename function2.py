# Function2.py

# 약간 더 복잡한
# 합집합 함수
def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# 호출
print(union("ham", "Ham", "EGG"))
print(union("ham", "Ham", "EGG", "SPAM"))

# 람다 함수 정의
g = lambda x,y : x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))

print(globals())
print(dir())


