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
        "textCard": {
          "title": "🚌캠간 셔틀 버스의 정보를 알려드립니다.🚌",
          "buttons": [
            {
              "action": "block",
              "label": "정류장 위치"
              "blockId": "6579abab6ca2a0102a0860ba",  //셔틀캠간 정류장 정보 블록 id
            },
            {
              "action": "block",
              "label": "시간표"
              "blockId": "65799fcbfd07443c623ecb4e", 
            },
            {
              "action": "block",
              "label": "금액"
              "blockId": "6579d7556286e53ab4497776",  
            }
          ]
        }
      }
    ]
  }
}

    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)


