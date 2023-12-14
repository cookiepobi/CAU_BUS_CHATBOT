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
                    "text": "교내 셔틀 / 평택 셔틀의 정류장 정보입니다."
            }
            },
            {
                "simpleImage": {
                    "imageUrl": "http://www.cau.ac.kr/attach/images/000143/campus_roadmap2_b_1.png",
                    "altText": "교내/평택 셔틀 정류장입니다."
                }
            }
        ]
    }
}

    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)



