# database sqlite3

import sqlite3

# 메모리에 데이터베이스 생성
# conn = sqlite3.connect(':memory:')

# 파일에 데이터베이스 생성
conn = sqlite3.connect(r'c:\work\sample.db')
# 커서 생성
cursor = conn.cursor()

# 테이블 생성
cursor.execute("CREATE TABLE if not exists PhoneBook (name TEXT, PhoneNumber TEXT)")

# 데이터 삽입
cursor.execute("INSERT INTO PhoneBook (name, PhoneNumber) VALUES ('Alice', '123-4567')")

#  입력 파라미터 처리
name = '홍길동'
phone_number = '010-1234-5678'
cursor.execute("INSERT INTO PhoneBook (name, PhoneNumber) VALUES (?, ?)", (name, phone_number))

# 여러건 입력
datalist = (('이순신', '010-1234-5678'), ('강감찬', '010-1234-5678'))

cursor.executemany("INSERT INTO PhoneBook (name, PhoneNumber) VALUES (?, ?)", datalist)
# 데이터 조회
cursor.execute("SELECT * FROM PhoneBook")
# for row in cursor:
#     print(row[0], row[1])

# print(cursor.fetchall())

print(cursor.fetchmany(2))

# 정상적으로 종료
conn.commit()
conn.close()
