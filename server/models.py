from server import db

# This class holds the model of the Messages table that is
# resposible for holding the data of each Message being
# stored on the server.
# Format of table is as follow:
# id    day     hour    minute  body
class MessagesModel(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String, nullable=False)
    hour = db.Column(db.Integer, nullable=False)
    minute = db.Column(db.Integer, nullable=False)
    body = db.Column(db.String, nullable=False)

    def __init__(self, day, hour, minute, body):
        #self.id = id
        self.day = day
        self.hour = hour
        self.minute = minute
        self.body = body

    def __repr__(self):
        return 'Message id:{}'.format(self.id)

    # This method returns the data in a dictionary format
    def get_dictionary(self):
        return {'day': self.day, 'hour':self.hour,
                'minute':self.minute, 'body':self.body}
