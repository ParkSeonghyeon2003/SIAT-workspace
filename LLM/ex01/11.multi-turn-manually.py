# 10. single-turn.py
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# 대화 내용을 기록할 리스트
history = []

while True:
    user_input = input("사용자: ")
    if user_input == "exit":
        break

    # 사용자 입력을 대화 내용에 추가
    history.append({"role": "user", "content": user_input})

    response = client.responses.create(
        model="gpt-4.1-nano",
        instructions="당신은 사용자를 도와주는 상담사입니다.",
        input=history,
        max_output_tokens=100,
    )

    # 모델 응답을 대화 내용에 추가
    history.append({"role": "assistant", "content": response.output_text})

    print("상담사:", response.output_text)
    print()

# 대화 종료 후 대화 내용을 출력
print("\n대화 내용\n" + "-" * 50)

# > : 오른쪽 정렬
# 9 : 9칸 확보
# role 문자열을 9칸 공간에 오른쪽 정렬해서 출력
for message in history:
    print(f"{message['role']:>9}: {message['content']}")

