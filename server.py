from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API 키 설정
api_key = "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"
openai.api_key = api_key

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('user_input')
    
    messages = []
    messages.append({"role": "user", "content": user_input})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    chat_response = completion.choices[0].message.content

    return jsonify({"response": chat_response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)