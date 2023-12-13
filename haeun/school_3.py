from flask import Flask, request, jsonify
import sys

app = Flask(__name__)

@app.route('/school_3', methods=['POST'])
def school_3():
    response = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "textCard": {
          "title": "🚌통학 셔틀 버스의 정보를 알려드립니다.🚌",
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
              "blockId": "65799fcbfd07443c623ecb4e",  
            }
          ]
        }
      }
    ]
  }
}

    return jsonify(response)

if __name__ == "__main__":

