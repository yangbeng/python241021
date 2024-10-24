# demoform.py
# demoform.ui  파일을 읽어와서 화면 구성
# demoform.ui (화면단) demoform.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("demoform.ui")[0]

class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lbText.setText("첫번째 윈도우")

#진입점 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = DemoForm()
    myWindow.show()
    app.exec_()


