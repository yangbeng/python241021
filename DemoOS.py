import random

print(random.random())
print(random.randint(1, 10))
print(random.randrange(1, 10))
print(random.choice([1, 2, 3, 4, 5]))

# 로또 번호 생성
lotto = random.sample(range(1, 46), 5)
print(lotto)

from os.path import *

print(abspath('python.exe'))
print(basename('c:\\python310\\python.exe'))
print(getsize('c:\\python310\\python.exe'))

print(exists('c:\\python310\\python.exe'))

filename = 'c:\\python310\\python.exe'

if exists(filename):
    print("파일크기: ", getsize(filename))
else:
    print("파일이 없습니다.")

import os
print("운영체제이름: ", os.name) 
print("운영체제 환경변수: ", os.environ)

# 파일 목록 가져오기
import glob
lst = glob.glob('c:\\work\\*.py')
print(lst)

for item in lst:
    print(item)

