from server import db
from models import Messages

# This method creates tables from models imported above
# in database
def create_db():
    db.create_all()
    db.session.commit()

# This method adds a Message object to the database
def add_entry(entry):
    db.session.add(entry)
    db.session.commit()

# This method removes an entry from the Messages table
# by using its id
def delete_by_id(entry_id):
    obj = Messages.query.filter_by(id = entry_id)
    db.session.delete(obj)

# This method deletes all rows in Messages table
# It returns the number of rows deleted
def delete_all_entries():
    num = db.session.query(Messages).delete()
    db.session.commit()
    return num
