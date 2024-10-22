# 전역 변수 초기화
strName = "Not Class Member"

class DemoString:
    def __init__(self):
        # 인스턴스 멤버 변수
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        # 약간의 버그 발생
        print(strName)
    def print(self, arg):
        # 약간의 버그 발생
        print(self.strName + "123")

d = DemoString()
d.set("First Message")
d.print()
d.print(123)
