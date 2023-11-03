from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def test():
    data = request.data.decode('utf-8')
    get_data = json.loads(data)["data"]

    message = f"receive data : {get_data} !!!"
    
    post_data = {
        "data" : message
    }
    

    return jsonify(post_data)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5555)
