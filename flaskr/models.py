import datetime

from flaskr import db


class Borne(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cycle_datetime = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    cycle_time = db.Column(db.Integer, nullable=False)
    cycle_dist = db.Column(db.Float, nullable=False)
    cycle_type = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        info = {
            '_id': self.id,
            '_time': self.cycle_time,
            '_dist': self.cycle_dist,
            '_type': self.cycle_type,
            '_datetime': self.cycle_datetime,
        }
        return '<Borne {_id}: {_time} {_dist} {_type} ({_datetime})>'.format(**info)
