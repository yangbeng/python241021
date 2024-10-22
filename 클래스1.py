
# 1)클래스 정의
class persion:
    def __init__(self):
        # 초기화 작업
        self.name = "default"
    
    #메서드
    def print(self):
        print("My Name is {0}".format(self.name))

# 2) 인스턴스 생성
p1 = persion()
p2 = persion()
p1.name = "전우치"

p1.print()
p2.print()
    