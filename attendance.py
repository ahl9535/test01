import json
import os

# 데이터 파일 이름
DB_FILE = "attendance.json"

def load_data():
    """파일에서 출석 데이터를 불러옵니다."""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_data(data):
    """출석 데이터를 파일에 저장합니다."""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_attendance(data):
    """새로운 출석 기록을 추가합니다."""
    date = input("날짜를 입력하세요 (예: 2024-01-15): ").strip()
    name = input("이름을 입력하세요: ").strip()

    if not date or not name:
        print("날짜와 이름을 모두 입력해주세요.")
        return

    if date not in data:
        data[date] = []
    
    if name in data[date]:
        print(f"⚠️  이미 {name}님은 {date}에 출석 처리되었습니다.")
    else:
        data[date].append(name)
        save_data(data)
        print(f"✅ {date}자 {name}님 출석 완료!")

def show_attendance(data):
    """전체 출석 목록을 출력합니다."""
    if not data:
        print("\n📭 출석 기록이 없습니다.")
        return

    print("\n" + "="*40)
    print("📋 스터디 출석 명단")
    print("="*40)
    
    # 날짜순으로 정렬하여 출력
    for date in sorted(data.keys()):
        names = ", ".join(data[date])
        count = len(data[date])
        print(f"📅 {date} ({count}명): {names}")
    
    print("="*40)

def show_stats(data):
    """출석 통계를 보여줍니다."""
    if not data:
        print("\n📭 출석 기록이 없습니다.")
        return
    
    # 사람별 출석 횟수 계산
    person_count = {}
    total_sessions = len(data)
    
    for date, names in data.items():
        for name in names:
            person_count[name] = person_count.get(name, 0) + 1
    
    print("\n" + "="*40)
    print("📊 출석 통계")
    print("="*40)
    print(f"총 스터디 횟수: {total_sessions}회\n")
    print("개인별 출석 현황:")
    
    for name in sorted(person_count.keys()):
        count = person_count[name]
        percentage = (count / total_sessions) * 100
        print(f"  {name}: {count}회 ({percentage:.1f}%)")
    
    print("="*40)

def main():
    data = load_data()
    
    while True:
        print("\n" + "-"*40)
        print("🎓 스터디 출석부 프로그램")
        print("-"*40)
        print("1. 출석 체크")
        print("2. 출석 명단 보기")
        print("3. 출석 통계")
        print("4. 종료")
        print("-"*40)
        
        choice = input("메뉴 번호를 선택하세요 (1-4): ").strip()

        if choice == "1":
            add_attendance(data)
        elif choice == "2":
            show_attendance(data)
        elif choice == "3":
            show_stats(data)
        elif choice == "4":
            print("\n👋 프로그램을 종료합니다. 열공하세요!")
            break
        else:
            print("❌ 잘못된 입력입니다. 1-4 중에서 선택해주세요.")

if __name__ == "__main__":
    main()
