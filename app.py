from flask import Flask, render_template, request, jsonify
import json
from main import convertToInfo
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('mainpage.html')
@app.route('/mainpage')
def mainpage():
    return render_template('mainpage.html')


@app.route('/upload', methods=['POST'])
def upload():
    print('Now started...')

    uploaded_file = request.files['file']
    uploaded_file.save('uploaded_file.mp4')
    x = convertToInfo('uploaded_file.mp4')
    print(x)
    data = None
    with open('sample.json') as f:
        data = json.load(f)
    print(type(data))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
