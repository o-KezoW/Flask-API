from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'The API is working', 200


app.run(port=5000)
