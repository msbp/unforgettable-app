from server import app
from models import Messages

def create_db():
    db.create_all()
