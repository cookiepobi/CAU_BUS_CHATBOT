from flask import Flask, request, jsonify
import sys

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "어떤 종류의 버스 정보가 궁금하신가요?"
                    }
                }
            ],
            "quickReplies": [
                {
                    "messageText": "학교 버스",
                    "action": "message",
                    "label": "학교 버스"
                },
                {
                    "messageText": "광역 버스",
                    "action": "message",
                    "label": "광역 버스"
                }
            ]
        }
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)

