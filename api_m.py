from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

api_key = "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"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["content"]
    
    messages = [{"role": "user", "content": user_message}]
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        api_key='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'
    )
    
    chat_response = completion.choices[0].message.content
    
    return jsonify({"response": chat_response})

if __name__ == "__main__":
    app.run(debug=True)
