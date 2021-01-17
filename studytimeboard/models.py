
from datetime import datetime, timedelta
from flask_login import UserMixin

from .utils.data_utils import *
from studytimeboard import login_manager
from studytimeboard import db, login_manager



@login_manager.user_loader
def load_user(user_id):
    print("load user {}".format(user_id))
    return User(username=user_id)


class User(UserMixin):
    id = ""
    username = ""

    def __init__(self, username):
        self.username = username
        self.id = username

    @staticmethod
    def query_via_username(username):
        raise NotImplemented

    def __repr__(self):
        return "User"


class StudyEvent:

    def __init__(self, start_time: str = None, end_time: str = None, name=None, date=None):
        self.start_time = start_time
        self.end_time = end_time
        self.name = name
        self.date = date

    @property
    def default_end_time(self):
        return datetime2time(time2datetime(self.start_time) + timedelta(minutes=30))

    @property
    def default_start_time(self):
        return datetime2time(time2datetime(self.end_time) - timedelta(minutes=30))


class StudyEventDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"'{self.username}', study from '{self.start_time}' to '{self.end_time}')"

# db.create_all()