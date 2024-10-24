import requests
from bs4 import BeautifulSoup
import openpyxl

# Naver 검색 URL
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# 헤더 설정 (브라우저를 모방)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}

# GET 요청으로 페이지 가져오기
response = requests.get(url, headers=headers)

# BeautifulSoup으로 페이지 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 기사 제목 추출
titles = []
for title in soup.find_all('a', class_='news_tit'):
    titles.append(title.get_text())

# 새로운 엑셀 파일 생성
workbook = openpyxl.Workbook()
sheet = workbook.active

# 첫 번째 행에 헤더 추가
sheet.append(["Index", "Article Title"])

# 크롤링한 결과를 엑셀 파일에 저장
for idx, title in enumerate(titles, 1):
    sheet.append([idx, title])

# 엑셀 파일 저장
workbook.save("results.xlsx")
