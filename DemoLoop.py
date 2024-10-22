lst = [100, 200, 300]
for item in lst:
    print(item)

# Range 함수
print("------------ 절취선 ----------")
print(list(range(10)))
print(list(range(2000,2025)))
print(list(range(1,32)))

print("------------ 리스트 내장 ----------")
lst = list(range(1,11))
print(lst)
print([1**2 for i in lst if i >5])

tp = ("apple", "orange", "kiwi")
print( [len(i) for i in tp])

d = {100:"apple", 200:"orange"}
print( [v.upper() for v in d.values()])

print("------------ 필터링 ----------")
lst = [10, 25, 30]
items = filter(None, lst)
for i  in items:
    print("item:{0}".format(i))

print("------------ 필터링 함수 정의 ----------")
def getBiggerFilter20(i):
    return i >20
lst = [10, 25, 30]
items = filter(getBiggerFilter20, lst)
for i  in items:
    print("item:{0}".format(i))


print("------------ 필터링 함수 정의 ----------")
lst = [10, 25, 30]
items = filter(lambda x:x>20, lst)
for i  in items:
    print("item:{0}".format(i))