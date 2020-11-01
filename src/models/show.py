from src.api_src.data import alchemy
from src.models import episode
from src.models.database_handler import DatabaseHandler


class ShowModel(alchemy.Model, DatabaseHandler):
    __tablename__ = 'shows'
    __table_args__ = {'extend_existing': True}
    id = alchemy.Column(alchemy.Integer, primary_key=True)
    name = alchemy.Column(alchemy.String(80))
    episodes = alchemy.relationship(episode.EpisodeModel, lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'episodes': [episodes.json() for episodes in self.episodes.all()]
        }

    @classmethod
    def filter_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def filter_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
