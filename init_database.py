from datetime import datetime
from sqlalchemy.exc import OperationalError
from uuid import uuid4

from config import app, db
from model import User


new_user = {
    "first_name":"Afeez",
    "last_name":"Abu",
    "password":"Laffsgaffs0",
    "email":"haffs@yahoo.com",
    "admin": True
}

# def get_data_from_table(model):
#     try:
#         data = db.session.query(model).all()
#         db.session.close()
#         return data
#     except OperationalError:
#         return []


def create_database(db):
    db.create_all()
    new_person = User(**new_user)
    new_person.hash_password()
    db.session.add(new_person)
    db.session.commit()
    # for data in PEOPLE_NOTES:
    #     new_person = Person(lname=data.get("lname"), fname=data.get("fname"))
    #     for content, timestamp in data.get("notes", []):
    #         new_person.notes.append(
    #             Note(
    #                 content=content,
    #                 timestamp=datetime.strptime(
    #                     timestamp, "%Y-%m-%d %H:%M:%S"
    #                 ),
    #             )
    #         )
    print("Created new database")


# def update_database(db, existing_people, existing_notes):
#     db.drop_all()
#     db.create_all()
#     for person in existing_people:
#         db.session.merge(person)
#     for note in existing_notes:
#         db.session.merge(note)
#     db.session.commit()
#     print("Updated existing database")


with app.app_context():
    create_database(db)
    # existing_people = get_data_from_table(Person)
    # existing_notes = get_data_from_table(Note)

    # if not existing_people:
    #     create_database(db)
    # else:
    #     update_database(db, existing_people, existing_notes)
