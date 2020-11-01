from src.api_src.data import alchemy
from src.models.database_handler import DatabaseHandler


class EpisodeModel(alchemy.Model, DatabaseHandler):
    __tablename__ = 'episodes'
    __table_args__ = {'extend_existing': True}
    id = alchemy.Column(alchemy.Integer, primary_key=True)
    name = alchemy.Column(alchemy.String(100))
    season = alchemy.Column(alchemy.Integer)
    show_id = alchemy.Column(alchemy.Integer, alchemy.ForeignKey('shows.id'))

    def __init__(self, name, season, show_id):
        self.name = name
        self.season = season
        self.show_id = show_id

    def json(self):
        return {
            'show id': self.show_id,
            'name': self.name,
            'season': self.season
        }

    @classmethod
    def filter_name(cls, name):
        return cls.query.filter_by(name=name).first()
