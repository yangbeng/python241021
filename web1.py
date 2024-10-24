# 웹크롤링에 관련된 선언
from bs4 import BeautifulSoup

page = open("Chap09_test.html", "rt", encoding="utf-8").read()

# html 파서 : 상수값 지정
soup = BeautifulSoup(page, "html.parser")

# 원하는 데이터 추출
# print(soup.prettify())

# <p> 태그 추출
# print(soup.find_all("p"))

# 첫번째 <p> 태그 추출
# print(soup.find("p"))

# 조건 검색: <P class="outer-text"> 추출
# print(soup.find_all("p", class_="outer-text"))

# attrs 속성 추출
# print(soup.find("p", attrs={"class": "outer-text"}))

# 태그 내부 문자열 출력
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)

# id로 검색
print(soup.find(id="first"))
