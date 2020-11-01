from flask import Flask, request, jsonify
from models import show

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'SECRET'


@app.before_first_request
def create_tables():
    alchemy.create_all()


@app.route('/', methods=['GET'])
def home():
    return 'The API is working', 200


@app.route('/show', methods=['POST'])
def post_show():
    request_data = request.get_json()
    new_show = show.ShowModel(request_data['name'])
    new_show.save_to_db()
    result = show.ShowModel.filter_ids(new_show.id)
    return jsonify(result.json())


if __name__ == '__main__':
    from src.api_src.data import alchemy
    alchemy.init_app(app)
    app.run(port=5000, debug=True)
