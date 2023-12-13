from flask import Flask, request, jsonify
import sys
app = Flask(__name__)

@app.route('/image', methods = ['POST'])
def image(): 
    response = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleImage": {
                    #"imageUrl": "https://i.ibb.co/M658vfX/image.png",
                    "imageUrl": "'https://ifh.cc/g/qfnqXS.png",
                    "altText": "통학 셔틀 버스 시간표를 알려줍니다"
                }
            }
        ]
    }
}
    return jsonify(response)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)
