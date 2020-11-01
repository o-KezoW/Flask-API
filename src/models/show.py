from ..data import alchemy
from . import episodes


class ShowModel(alchemy.Model):
    __tablename__ = 'shows'
    id = alchemy.Column(alchemy.Integer, primary_key=True)
    name = alchemy.Column(alchemy.String(100))

    # Episodes, do something to automatically load episodes
    episodes = alchemy.relationship(episodes.EpisodesModel, lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            'id': self.id,
            'episodes': []
        }

    def save_to_db(self):
        alchemy.session.add(self)
        alchemy.session.commit()

    @classmethod
    def filter_names(cls, name):
        cls.query.filter_by(name=name).first()

    @classmethod
    def filter_ids(cls, id):
        cls.query.filter_by(name=id).first()
