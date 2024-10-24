# demoform.py
# demoform2.ui  파일을 읽어와서 화면 구성
# demoform.ui (화면단) demoform2.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
# 크롤링 관련 선언
from bs4 import BeautifulSoup
#웹서버에 요청
import requests

form_class = uic.loadUiType("demoform2.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    # 슬롯 메서드 추가
    def firstClick(self):
        crawlingDaangn()
        self.label.setText("당근마켓 크롤링 완료")

    def secondClick(self):
        self.label.setText("두번째 버튼 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭")

#진입점 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = DemoForm()
    myWindow.show()
    app.exec_()

def crawlingDaangn():
    url = "https://www.daangn.com/fleamarket/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    f = open("daangn.txt", "a+", encoding="utf-8")
    posts = soup.find_all("div", attrs={"class": "card-desc"})
    for post in posts:
        titleElem = post.find("h2", attrs={"class": "card-title"})
        priceElem = post.find("div", attrs={"class": "card-price"})
        regionElem = post.find("div", attrs={"class": "card-region-name"})
        title = titleElem.text.replace("\n", "").strip()
        price = priceElem.text.replace("\n", "").strip()
        region = regionElem.text.replace("\n", "").strip()

        print(f"{title}, {price}, {region}")
        f.write(f"{title}, {price}, {region}\n")        
    f.close()        
