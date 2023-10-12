import requests

# Flask 앱의 URL
url = 'https://port-0-gpt-learning-jvpb2alnmi0kxx.sel5.cloudtype.app/chat'

# POST 요청에 보낼 데이터
data = {'user_input': '사용자의 입력 메시지'}

# POST 요청 보내기
response = requests.post(url, json=data)

# 응답 확인
if response.status_code == 200:
    result = response.json()
    chat_response = result.get('response')
    print(f'서버 응답: {chat_response}')
else:
    print(f'요청 실패. 상태 코드: {response.status_code}')
