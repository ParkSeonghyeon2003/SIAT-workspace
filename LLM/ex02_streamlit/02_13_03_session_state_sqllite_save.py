import streamlit as st
import sqlite3

def init_db():
    # DB 연결
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS counter (
        id INTEGER PRIMARY KEY,
        count INTEGER
    )
    """)
    # count 생성
    # OR IGNORE : id 1번 데이터가 없을 때에만 INSERT 수행
    cursor.execute("INSERT OR IGNORE INTO counter (id, count) VALUES (?, ?)", (1, 0))
    conn.commit()
    return conn, cursor

conn, cursor = init_db()

# 조회
cursor.execute("SELECT count FROM counter WHERE id = 1")
count = cursor.fetchone()[0]

# 증가
if st.button("증가"):
    count += 1
    cursor.execute("UPDATE counter SET count = ? WHERE id = 1", (count,))
    conn.commit()

# 초기화
if st.button("초기화"):
    count = 0
    cursor.execute("UPDATE counter SET count = ? WHERE id = 1", (count,))
    conn.commit()

# count 표시
st.write(count)

# 닫기
conn.close()