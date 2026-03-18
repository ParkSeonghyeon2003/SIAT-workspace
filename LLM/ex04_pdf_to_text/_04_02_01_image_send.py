from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(dotenv_path="C:/workspace/LLM/.env")

# OpenAI API 서버와 통신할 클라이언트 객체 생성합니다.
client = OpenAI()

# 로컬 이미지 파일을 OpenAI 서버에 업로드합니다.
# 파일 업로드가 완료되면 서버에서 고유한 file_id가 생성됩니다.
# 이 file_id를 이용하여 이후 API 요청에서 해당 파일을 사용할 수 있습니다.
file = client.files.create(
    file=open("output/page_high_res.png", "rb"),    # 업로드할 파일을 binary 모드("rb")로 열어서 전달합니다.
                                                    # binary 모드는 이미지나 PDF 같은 바이너리 파일을 읽을 때 사용합니다.
    purpose="vision"    # 파일의 사용 목적을 지정합니다.
                        # "vision" : 이미지 분석(vision) 작업에 사용할 파일이라는 의미입니다.
)

# 업로드된 이미지(file_id)를 AI 모델에게 전달하여 분석을 요청합니다.
response = client.responses.create(
    model="gpt-4.1-nano",
    input=[
        {
            "role": "user",
            "content": [        # content 안에는 여러 타입의 입력을 넣을 수 있습니다.
                {"type": "input_text", "text": "이 이미지 설명해줘"},   # 모델에게 요청할 질문입니다.
                {
                    "type": "input_image",  # 앞에서 업로드한 이미지 파일을 AI에게 전달합니다.
                    "file_id": file.id      # OpenAI 서버에 있는 file.id 이미지를 사용합니다.
                }
            ]
        } # type: ignore
    ],
    max_output_tokens=100
)


print(response.output_text)