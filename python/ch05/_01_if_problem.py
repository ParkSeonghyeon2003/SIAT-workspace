user_id = "kim"
user_pw = "1234"

input_id = input("아이디 입력: ")
input_pw = input("비밀번호 입력: ")
""" 
if input_id == user_id:
    if input_pw == user_pw:
        print("로그인 성공!")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("존재하지 않는 아이디입니다.")
"""
if input_id != user_id:
    print("존재하지 않는 아이디입니다.")
elif input_pw != user_pw:
    print("비밀번호가 틀렸습니다.")
else:
    print("로그인 성공!")