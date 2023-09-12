#!/usr/bin/python3
""" The app module """
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


# set up the Flask app and SQLAlchemy

app = Flask(__name__)
# configure the SQLAlchemy database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)


class Person(db.Model):
    """
    This class will define the structure of the database table.
    """

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, age):
        """constructor"""
        self.name = name
        self.age = age


with app.app_context():
    db.create_all()


@app.route("/api", methods=["POST"], strict_slashes=False)
def create_person():
    """CREATE a new person"""
    data = request.get_json()
    name = data["name"]
    age = data["age"]
    person = Person(name=name, age=age)
    db.session.add(person)
    db.session.commit()
    return jsonify({"message": "Person created successfully"}), 201


@app.route("/api/<int:user_id>", methods=["GET"], strict_slashes=False)
def get_person(user_id):
    """READ details of a person"""
    person = Person.query.get(user_id)
    if person:
        return jsonify({"name": person.name, "age": person.age}), 200
    return jsonify({"message": "Person not found"}), 404


@app.route("/api/<int:user_id>", methods=["PUT"], strict_slashes=False)
def update_person(user_id):
    """UPDATE details of an existing person"""
    person = Person.query.get(user_id)
    if person:
        data = request.get_json()
        person.name = data["name"]
        person.age = data["age"]
        db.session.commit()
        return jsonify({"message": "Person updated successfully"}), 200
    return jsonify({"message": "Person not found"}), 404


# DELETE a person
@app.route("/api/<int:user_id>", methods=["DELETE"], strict_slashes=False)
def delete_person(user_id):
    """DELETE a person"""
    person = Person.query.get(user_id)
    if person:
        db.session.delete(person)
        db.session.commit()
        return jsonify({"message": "Person deleted successfully"}), 200
    return jsonify({"message": "Person not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
