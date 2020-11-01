from flask import Flask, request, jsonify
from models import show, episode

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
    result = show.ShowModel.filter_id(new_show.id)
    return jsonify(result.json())


@app.route('/show/<string:name>', methods=['GET'])
def get_show(name):
    result = show.ShowModel.filter_name(name)
    if result:
        return result.json()
    else:
        return {'message': f'The api couldn\'t found "{name}"'}, 404


@app.route('/show/<string:name>/episode', methods=['POST'])
def post_episode_to_show(name):
    request_data = request.get_json()
    parent = show.ShowModel.filter_name(name)
    if parent:
        new_episode = episode.EpisodeModel(name=request_data['name'], season=request_data['season'], show_id=parent.id)
        new_episode.save_to_db()
        return new_episode.json()
    else:
        return {'message': f'The api couldn\'t found "{name}"'}, 404


if __name__ == '__main__':
    from src.api_src.data import alchemy
    alchemy.init_app(app)
    app.run(port=5000, debug=True)
