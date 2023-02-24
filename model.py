from datetime import datetime
from uuid import uuid4
from flask_bcrypt import generate_password_hash, check_password_hash
from marshmallow_sqlalchemy import fields

from config import db, ma


def generate_uuid():
    return str(uuid4())

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __init__(self, **kwargs):
        """
        The function takes in a dictionary of keyword arguments and assigns the values to the class
        attributes
        """
        self.id = kwargs.get("id")
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")

    def __repr__(self):
        """
        The __repr__ function is used to return a string representation of the object
        :return: The username of the user.
        """
        return "<User {}>".format(self.first_name)

    def hash_password(self):
        """
        It takes the password that the user has entered, hashes it, and then stores the hashed password in
        the database
        """
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        """
        It takes a plaintext password, hashes it, and compares it to the hashed password in the database
        
        :param password: The password to be hashed
        :return: The password is being returned.
        """
        return check_password_hash(self.password, password)


class BookSharing(db.Model):
    __tablename__ = "booksharing"
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    book_id = db.Column(db.String, db.ForeignKey("books.id"))
    user_id = db.Column(db.String, db.ForeignKey("users.id"))
    start_date = db.Column(
        db.DateTime, default=datetime.utcnow
    )
    end_date = db.Column(
        db.DateTime, default=datetime.utcnow
    )

class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    book_id = db.Column(db.String, db.ForeignKey("books.id"))
    user_id = db.Column(db.String, db.ForeignKey("users.id"))
    comment = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    user_id = db.Column(db.String, db.ForeignKey("users.id"))
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    book_image_url = db.Column(db.String, nullable=False)
    book_url = db.Column(db.String, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    reviews = db.relationship(
        Review,
        backref="book",
        cascade="all, delete, delete-orphan",
    )
    book_sharing = db.relationship(
        BookSharing,
        backref="book",
        cascade="all, delete, delete-orphan",
    )

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
        include_fk = True

class BookSharingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookSharing
        load_instance = True
        sqla_session = db.session
        include_fk = True

class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        load_instance = True
        sqla_session = db.session
        include_fk = True

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True
        sqla_session = db.session
        include_fk = True
        include_relationships = True

    reviews = fields.Nested(ReviewSchema, many=True)
    book_sharing = fields.Nested(BookSharingSchema, many=True)

class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        load_instance = True
        sqla_session = db.session
        include_fk = True


user_schema = UserSchema()
book_schema = BookSchema(many=True)
