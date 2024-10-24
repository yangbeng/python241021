import sqlite3
import random

class 식료품데이터베이스:
    def __init__(self, db_이름="식료품.db"):
        self.conn = sqlite3.connect(db_이름)
        self.cursor = self.conn.cursor()
        self.테이블_생성()
    
    def 테이블_생성(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS 제품 (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                제품명 TEXT NOT NULL,
                                가격 REAL NOT NULL)''')
        self.conn.commit()

    def 제품_추가(self, 제품명, 가격):
        self.cursor.execute("INSERT INTO 제품 (제품명, 가격) VALUES (?, ?)", (제품명, 가격))
        self.conn.commit()

    def 제품_수정(self, 제품id, 제품명=None, 가격=None):
        if 제품명 and 가격:
            self.cursor.execute("UPDATE 제품 SET 제품명 = ?, 가격 = ? WHERE id = ?", (제품명, 가격, 제품id))
        elif 제품명:
            self.cursor.execute("UPDATE 제품 SET 제품명 = ? WHERE id = ?", (제품명, 제품id))
        elif 가격:
            self.cursor.execute("UPDATE 제품 SET 가격 = ? WHERE id = ?", (가격, 제품id))
        self.conn.commit()

    def 제품_삭제(self, 제품id):
        self.cursor.execute("DELETE FROM 제품 WHERE id = ?", (제품id,))
        self.conn.commit()

    def 모든_제품_조회(self):
        self.cursor.execute("SELECT * FROM 제품")
        return self.cursor.fetchall()

    def 연결_종료(self):
        self.conn.close()

def 샘플_데이터_생성(db, n=100):
    식료품_목록 = [
        "사과", "바나나", "오렌지", "우유", "빵", "치즈", "요구르트", "계란", "토마토", "감자",
        "양파", "당근", "오이", "상추", "시리얼", "쌀", "파스타", "소고기", "닭고기", "돼지고기",
        "생선", "새우", "참치캔", "콜라", "주스", "물", "커피", "차", "맥주", "와인"
    ]
    
    for _ in range(n):
        제품명 = random.choice(식료품_목록)
        가격 = round(random.uniform(1000, 50000), -2)  # 1000원에서 50000원 사이, 100원 단위로 반올림
        db.제품_추가(제품명, 가격)

# 사용 예시
if __name__ == "__main__":
    # 데이터베이스 및 클래스 초기화
    db = 식료품데이터베이스()

    # 샘플 데이터 100개 생성
    샘플_데이터_생성(db)

    # 모든 제품 조회 및 출력
    제품들 = db.모든_제품_조회()
    for 제품 in 제품들:
        print(제품)

    # 예시: 제품 수정
    db.제품_수정(1, 제품명="수정된 사과", 가격=2500)

    # 예시: 제품 삭제
    db.제품_삭제(2)

    # 수정 후 결과 확인
    수정된_제품들 = db.모든_제품_조회()
    print("\n수정 후 제품 목록:")
    for 제품 in 수정된_제품들:
        print(제품)

    # 데이터베이스 연결 종료
    db.연결_종료()