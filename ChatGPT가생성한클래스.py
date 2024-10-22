# Person 클래스 정의
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def printInfo(self):
        # f-string: 포멧 스트링(python 3.6)
        print(f"ID: {self.id}, Name: {self.name}")

# Manager 클래스 (Person을 상속)
class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title
    
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")

# Employee 클래스 (Person을 상속)
class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill
    
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

# 테스트 코드 작성
def run_tests():
    # Person 객체 생성 및 테스트
    person1 = Person(1, "Alice")
    person1.printInfo()  # ID: 1, Name: Alice

    person2 = Person(2, "Bob")
    person2.printInfo()  # ID: 2, Name: Bob

    # Manager 객체 생성 및 테스트
    manager1 = Manager(3, "Charlie", "Team Lead")
    manager1.printInfo()  # ID: 3, Name: Charlie, Title: Team Lead

    manager2 = Manager(4, "Dana", "Project Manager")
    manager2.printInfo()  # ID: 4, Name: Dana, Title: Project Manager

    # Employee 객체 생성 및 테스트
    employee1 = Employee(5, "Eve", "Python")
    employee1.printInfo()  # ID: 5, Name: Eve, Skill: Python

    employee2 = Employee(6, "Frank", "Java")
    employee2.printInfo()  # ID: 6, Name: Frank, Skill: Java

    # 추가 테스트
    person3 = Person(7, "Grace")
    person3.printInfo()  # ID: 7, Name: Grace

    manager3 = Manager(8, "Henry", "HR Manager")
    manager3.printInfo()  # ID: 8, Name: Henry, Title: HR Manager

    employee3 = Employee(9, "Ivy", "JavaScript")
    employee3.printInfo()  # ID: 9, Name: Ivy, Skill: JavaScript

    employee4 = Employee(10, "Jack", "C++")
    employee4.printInfo()  # ID: 10, Name: Jack, Skill: C++

# 테스트 실행
run_tests()
