from ..data import alchemy


class EpisodesModel(alchemy.Model):
    __tablename__ = 'episodes'
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
            'name': self.name,
            'season': self.season
        }

    @classmethod
    def filter_names(cls, name):
        cls.query.filter_by(name=name).first()

    def save_to_db(self):
        alchemy.session.add(self)
        alchemy.session.commit()

    def delete_from_db(self):
        alchemy.session.delete(self)
        alchemy.session.commit()
