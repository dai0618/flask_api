from flask import Flask, request, jsonify, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/test', methods=['GET','POST'])
def test():

    send_data = str(request.form.get('data'))

    post_url = "http://127.0.0.1:5555"
    json = {"data": send_data}

    response = requests.post(
                    post_url,
                    json = json,
                )
    
    response = response.json()
    response = response["data"]

    return render_template("data.html", response=response)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8888)
