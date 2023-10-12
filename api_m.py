from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

api_key = "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"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["content"]
    
    messages = [{"role": "user", "content":  '''
Type {StringAAA} as shown in the text below
Text("{StringAAA}", 20, label)
Text("{StringAAA}", 20, label)
Spacer()
buttons ({}, "Find out more", {color})
At this time, the color is randomly selected among red, orange, yellow, green, blue, indigo, purple
Only,
If I type in {StringAAA}
On the first line, text ("{StringAAA}", 20, label) outputs the value I entered in this
In the second line, text ("{StringAAA}", 20, label) outputs the chatgpt's answer to the value I entered
On the third line, you must print out a spacer()
In the fourth line, a sentence of "buttons" ({}, "Find out more", {color}) is output,
and in this case, one of red, orange, yellow, green, blue, indigo, and purple is randomly added to the {color} and output

For example, when I type, "What's an apple?" you're like
Text ("What's an apple?" 20, label)
Text ("It's a red fruit," 20, label)
Spacer()
buttons ({}, "Find out more", blue)
You have to answer like this
At this time, I put the text I entered in the first line and printed out the text ("What's the apple?", 20, label)
and put the answer to the input in the second line
I'll print out the spacer() as it is
In the sentences buttons ({}, "Find out more", blue)
{color} red, orange, yellow, green, blue, indiI randomly put in one of go and purple and printed it out

Also, you cannot give the same answer to the second linef
For example, if you print Text ("It's a red fruit," 20, label) once, you can't print Text ("It's a red fruit," 20, label) again

You must provide a variety of answers to the input and not repeat it

What is the correct answer if the user type ''' + f"\"{user_message}\"?"}]
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        api_key='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'
    )
    
    chat_response = completion.choices[0].message.content
    
    return jsonify({"response": chat_response})


@app.route("/gpt/health", methods=["GET"])
def gpt_health():
    return "OK GPT Server"


if __name__ == "__main__":
    app.run(debug=True)
