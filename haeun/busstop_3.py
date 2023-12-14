from flask import Flask, request, jsonify
import sys

app = Flask(__name__)

@app.route('/school_4', methods=['POST'])
def school_4():
    response = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
            "simpleText": {
                    "text": "광역 버스의 정류장 정보입니다. \n 정류장은 정문에서 횡단보도를 건너면 위치해있으며, 정류장 이름은 '중앙대.롯데캐슬아파트(34151)입니다."
            }
            }
        ]
    }
}

    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)



