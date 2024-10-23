# 정규식 연습
import re

result = re.search('[0-9]*th', ' 35th')
print(result)
print(result.group())

# result2 = re.match('[0-9]*th', ' 35th')
# print(result2)
# print(result2.group())
result = re.search('apple', 'this is apple pie')
print(result.group())

result2 = re.search('\d{4}', '올해는 2024년입니다.')
print(result2.group())

result3 = re.search('\d{5}', '우리동네는 55123입니다. 55122입니다.')
print(result3.group())

# ... 기존 코드 ...

# 이메일 주소 체크
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'

def check_email(email):
    result = re.search(email_pattern, email)
    if result:
        print(f"유효한 이메일 주소입니다: {result.group()}")
    else:
        print("유효하지 않은 이메일 주소입니다.")

# 테스트
check_email("user@example.com")
check_email("invalid.email@com")
check_email("another.valid@email.co.kr")