[[Ifrom flask import Flask, request, jsonify
import sys

app = Flask(__name__)

@app.route('/bus', methods=['POST'])
def bus():
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text":" 어떤 학교 버스의 정보를 원하시나요?
(ex: 8200 or 수원 입력)

- 8200 (수원)
- 8201 (성남)
- 8202 (동탄)
- 4401 (양재)"
                    }
                }
            ],
        }
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)


