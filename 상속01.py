# 부모 클래스
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

# 자식 클래스 정의
class Student(Person):
    # 덮어쓰기 (재정의, Override)
    def __init__(self, name, phoneNumber, subject, studentID):
        # self.name = name
        # self.phoneNumber = phoneNumber
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    # 덮어쓰기
    def printInfo(self):
        super().printInfo()
        print("Info(subject:{0}, studentID: {1})".format(self.subject, self.studentID))

# 인스턴스
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "인공지능", "241122")
# print(p.__dict__)
# print(s.__dict__)

# 메서드 호출
p.printInfo()
s.printInfo()


