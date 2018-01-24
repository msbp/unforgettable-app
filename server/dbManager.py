from server import db
from models import MessagesModel
from sqlalchemy.exc import IntegrityError

# This method creates tables from models imported above
# in database
def create_db():
    db.create_all()
    db.session.commit()

# This method creates a MessagesModel object from a dictionary,
# adds and commits it to the database. It then returns the id
# given to it by the database. If there is an exception it
# returns -1
def add_entry(entryDict):
    entry = MessagesModel(\
    entryDict['day'], entryDict['hour'],\
    entryDict['minute'], entryDict['body']\
    )
    db.session.add(entry)
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print('There was an IntegrityError thrown:\n', e)
        return -1
    print('id given to the message:', entry.id)
    return entry.id

# This method retrieves a MessageModel object from the
# table in the database. It then translates it into a dictionary
# that is returned.
def get_entry_by_id(entry_id):
    obj = db.session.query(MessagesModel).get(entry_id)
    if obj == None:
        return None
    return obj.get_dictionary()

# This method retrieves all messages currently in the messages
# table in the database. It returns a list of dictionary
# entries.
def get_all_entries():
    message_models = db.session.query(MessagesModel).all()
    message_list = []
    for each in message_models:
        message_list.append(each.get_dictionary())
    return message_list

# This method removes an entry from the Messages table
# by using its id
# It returns -1 if the ID does not exist or -2 if there is an
# exception is thrown. Returns 0 if successful.
def delete_by_id(entry_id):
    obj = db.session.query(MessagesModel).get(entry_id)
    if (obj == None):
        print('This ID does not exist.')
        return -1
    db.session.delete(obj)
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print('There was an IntegrityError thrown:\n', e)
        return -2
    return 0

# This method deletes all rows in Messages table
# It returns the number of rows deleted if successful
# or -1 if there is an exception thrown.
def delete_all_entries():
    num = db.session.query(MessagesModel).delete()
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print('There was an IntegrityError thrown:\n', e)
        return -1
    return num
