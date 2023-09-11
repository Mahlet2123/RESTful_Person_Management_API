#!/usr/bin/python3
""" The app module """
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os


# set up the Flask app and SQLAlchemy

app = Flask(__name__)
# configure the SQLAlchemy database URI
# using enviromental variables
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app)

class Person(db.Model):
    """
    This class will define the structure of the database table.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, age):
        """ constructor """
        self.name = name
        self.age = age


# CREATE a new person
@app.route('/api/person', methods=['POST'])
def create_person():
    data = request.get_json()
    name = data['name']
    age = data['age']
    person = Person(name=name, age=age)
    db.session.add(person)
    db.session.commit()
    return jsonify({"message": "Person created successfully"}), 201

# READ details of a person
@app.route('/api/person/<int:id>', methods=['GET'])
def get_person(id):
    person = Person.query.get(id)
    if person:
        return jsonify({"name": person.name, "age": person.age}), 200
    return jsonify({"message": "Person not found"}), 404

# UPDATE details of an existing person
@app.route('/api/person/<int:id>', methods=['PUT'])
def update_person(id):
    person = Person.query.get(id)
    if person:
        data = request.get_json()
        person.name = data['name']
        person.age = data['age']
        db.session.commit()
        return jsonify({"message": "Person updated successfully"}), 200
    return jsonify({"message": "Person not found"}), 404

# DELETE a person
@app.route('/api/person/<int:id>', methods=['DELETE'])
def delete_person(id):
    person = Person.query.get(id)
    if person:
        db.session.delete(person)
        db.session.commit()
        return jsonify({"message": "Person deleted successfully"}), 200
    return jsonify({"message": "Person not found"}), 404
