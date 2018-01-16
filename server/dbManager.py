from server import db
from models import MessagesModel

# This method creates tables from models imported above
# in database
def create_db():
    db.create_all()
    db.session.commit()

# This method adds a MessageModel object to the database
def add_entry(entry):
    db.session.add(entry)
    db.session.commit()

# This method retrieves a MessageModel object from the
# table in the database
def get_entry(entry_id):
    obj = db.session.query(MessagesModel).get(entry_id)
    return obj

# This method removes an entry from the Messages table
# by using its id
def delete_by_id(entry_id):
    obj = db.session.query(MessagesModel).get(entry_id)
    db.session.delete(obj)
    db.session.commit()

# This method deletes all rows in Messages table
# It returns the number of rows deleted
def delete_all_entries():
    num = db.session.query(MessagesModel).delete()
    db.session.commit()
    return num
