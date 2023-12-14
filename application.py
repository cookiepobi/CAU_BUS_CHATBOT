from flask import Flask, request
import sys
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello, World!'

@application.route("/name", methods = ["POST"])
def name_function():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])
    
    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "안녕하세요. 테스트 코드입니다. 😊"
                    }
                    
                }
            ]
        }
	}
    return responseBody


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]), debug = True)
