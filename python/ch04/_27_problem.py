# 방문 기록 (중복 포함)
# visited_today = ["김철수", "이영희", "김철수", "박민수", "이영희"]

# visited_names = sorted(set(visited_today))

# print(f"오늘 방문한 고유 고객 수: {len(visited_names)}")
# print(f"고객 명단: {visited_names}\n")



# # 메뉴판 생성
# menu = dict(아메리카노=4100, 라떼=4600, 에이드=5000)
# print(menu) # {"아메리카노": 4100, "라떼": 4600, "에이드": 5000}

# menu["케이크"] = 6000
# print(f"아메리카노 가격: {menu.get("아메리카노")}")
# print(f"전체 메뉴: {menu}\n")



book_list = ["파이썬 입문", "자바 스크립트", "HTML/CSS", "파이썬 입문"]

# 키를 뽑아서 (count 수, 키) 쌍 튜플 원소들을 갖는 리스트를 생성
# 리스트를 count 수에 맞춰 정렬
keys = list(set(book_list))
new_lst = [
    (book_list.count(keys[0]), keys[0]),
    (book_list.count(keys[1]), keys[1]),
    (book_list.count(keys[2]), keys[2])
]
new_lst.sort()

# (키, count 수) 처럼 정상 순서로 재배열하고, 딕셔너리화
book_dict = dict((
    (new_lst[0][1], new_lst[0][0]),
    (new_lst[1][1], new_lst[1][0]),
    (new_lst[2][1], new_lst[2][0])
))
print(book_dict)