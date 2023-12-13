[[Ifrom flask import Flask, request, jsonify
import sys

app = Flask(__name__)

@app.route('/school', methods=['POST'])
def school():
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "어떤 학교 버스의 정보를 원하시나요?

(ex: 교내 or 교내 셔틀 입력)


- 교내 셔틀

- 평택 셔틀

- 통학 버스

- 캠간 셔틀"
                    }
                }
            ],
        }
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)

