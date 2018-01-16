from server import db

# Note:
#       Could change id column to have the database
#       change by itself. To be implemented later.

# This class holds the model of the Messages table that is
# resposible for holding the data of each Message being
# stored on the server.
# Format of table is as follow:
# id    day     hour    minute  body
class Messages(db.Model):
    __tablename__ = 'Messages'
    id = db.Column(db.Integer, nullable=False)
    day = db.Column(db.String, nullable=False)
    hour = db.Column(db.String, nullable=False)
    minute = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)

    def __init__(self, id, day, hour, minute, body):
        self.id = id
        self.day = day
        self.hour = hour
        self.minute = minute
        self.body = body

    def __repr__(self):
        return 'Message id:{}'.format(self.id)
