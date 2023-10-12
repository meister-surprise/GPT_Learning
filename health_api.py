from flask import Flask

app = Flask(__name__)

@app.route('/gpt/health', methods=['GET'])
def healthcheck():
    return 'OK GPT Server'

if __name__ == '__main__':
    app.run()
