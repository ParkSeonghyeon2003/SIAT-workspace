# time 모듈 : 코드 실행 사이에 잠시 대기 시간을 주기 위해 사용
import time

# OpenAI API를 사용하기 위한 공식 Python SDK
from openai import OpenAI

# .env 파일에 저장된 환경 변수를 불러오기 위한 라이브러리
from dotenv import load_dotenv


# .env 파일을 읽어 Python 환경 변수(os.environ)에 등록
# 여기서 OPENAI_API_KEY 같은 값이 로드됩니다.
load_dotenv()


# OpenAI API와 통시하기 위한 클라이언트 객체 생성
client = OpenAI()


# 이전 응답의 ID를 저장할 변수
# 첫 번째 요청에서는 이전 대화가 없기 때문에 None으로 시작
previous_id = None


# 테스트할 대화 턴 수
# 50번 반복하여 멀티턴 대화를 테스트
# (원하면 200 정도까지 늘려서 실험할 수 있음)
turns = 10


# 1번 턴부터 turns까지 반복
for i in range(1, turns + 1):

    # 현재 턴 번호를 출력 (대화 진행 상황 확인용)
    print(f"\n=== TURN {i} ===")


    # OpenAI 모델에게 요청을 보내는 부분
    response = client.responses.create(

        # 사용할 AI 모델
        model="gpt-4.1-nano",

        # 모델에게 전달할 질문
        # 이전 대화를 기억하고 있다면 현재 턴 번호를 맞히도록 요청
        input="이전 대화를 기억하고 있다면, 지금은 몇 번째 턴인지 숫자로만 말해.",

        # 이전 응답의 ID를 전달하여 대화 맥락을 이어주는 핵심 파라미터
        # 이 값을 전달하면 AI가 이전 대화를 참고하여 답변함
        previous_response_id=previous_id
    )


    # 현재 응답의 ID를 저장
    # 다음 턴에서 previous_response_id로 사용하여 대화를 계속 이어감
    previous_id = response.id


    # 모델이 생성한 텍스트 출력
    # output_text는 편의 속성으로, 생성된 텍스트를 바로 가져올 수 있음
    print("AI:", response.output_text)


    # 서버 요청을 너무 빠르게 반복하지 않도록 1초 대기
    # API 호출 속도 제한(rate limit)을 완화하는 용도로 사용
    time.sleep(1)