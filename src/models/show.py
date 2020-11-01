from src.api_src.data import alchemy
from src.models import episode


class ShowModel(alchemy.Model):
    __tablename__ = 'shows'
    __table_args__ = {'extend_existing': True}
    id = alchemy.Column(alchemy.Integer, primary_key=True)
    name = alchemy.Column(alchemy.String(100))

    # Episodes, do something to automatically load episodes
    episodes = alchemy.relationship(episode.EpisodesModel, lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            'id': self.id,
            'episodes': []
        }

    @classmethod
    def filter_names(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def filter_ids(cls, id):
        return cls.query.filter_by(name=id).first()

    def save_to_db(self):
        alchemy.session.add(self)
        alchemy.session.commit()

    def delete_from_db(self):
        alchemy.session.delete(self)
        alchemy.session.commit()
