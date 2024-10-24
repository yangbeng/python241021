# 파일 쓰기
# 유니코드로 쓰기:
f = open('demo.txt', 'wt', encoding='utf-8')
f.write('Hello, World!\n')
f.write('첫번째\n두번째\n세번째\n')
f.close()

# 파일 읽기
f = open('demo.txt', 'rt', encoding='utf-8')
text = f.read()
print(text)
f.close()

# str 클래스 메서드 연습
#print(dir(str))
data = ' < <<spam and eggs or sausage and bacon>>>'
result = data.strip('<> ')
print(data)
print(result)

result2 = result.replace('spam', 'spam and eggs')
print(result2)

result3 = result2.split()
print(result3)

result4 = ':)'.join(result3)
print(result4)

print("MBC2580".isalnum())
print("2580".isdecimal())
print("MBC".isalpha())

print(len("문자열길이"))



