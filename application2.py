from flask import Flask, request, jsonify
import sys
app = Flask(__name__)


@app.route('/text',methods=['POST'])
def text():
    response = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": "무료입니다"
                }
            }
        ]
    }
}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)
