import os

from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from model.Animals import Animals
import json

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Animal_in_db(Animals, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=False)
    kind = db.Column(db.String(32), unique=False)
    size_in_m = db.Column(db.Float, unique=False)
    weight_in_kg = db.Column(db.Float, unique=False)
    point = db.Column(db.String(32), unique=False)
    age_in_years = db.Column(db.Integer, unique=False)
    hunt_for_prey = db.Column(db.Integer, unique=False)
    classes = db.Column(db.String(32), unique=False)
    color = db.Column(db.String(32), unique=False)
    number_of_paws = db.Column(db.Integer, unique=False)

    def __init__(self, name=None, kind=None, size_in_m=None, weight_in_kg=None, point=None,
                 age_in_years=None,
                 hunt_for_prey=None, classes=None, color=None, number_of_paws=None):
        super().__init__(name, kind, size_in_m, weight_in_kg, point, age_in_years,
                         hunt_for_prey, classes)

        self.color = color
        self.number_of_paws = number_of_paws


class Animal_in_db_schema(ma.Schema):
    class Meta:
        fields = ('name', 'kind', 'size_in_m', 'weight_in_kg',
                  'point', 'age_in_years', 'hunt_for_prey',
                  'classes', 'color', 'number_of_paws')


animal_schema = Animal_in_db_schema()
animals_schema = Animal_in_db_schema(many=True)


@app.route("/animal", methods=["POST"])
def add_animal_in_db():
    animal_db = Animal_in_db(request.json['name'],
                             request.json['kind'],
                             request.json['size_in_m'],
                             request.json['weight_in_kg'],
                             request.json['point'],
                             request.json['age_in_years'],
                             request.json['hunt_for_prey'],
                             request.json['classes'],
                             request.json['color'],
                             request.json['number_of_paws'])
    db.session.add(animal_db)
    db.session.commit()
    return animal_schema.jsonify(animal_db)


@app.route("/animals", methods=["GET"])
def get_animal_in_db():
    all_animals = Animal_in_db.query.all()
    result = animals_schema.dump(all_animals)
    return jsonify({'animals': result})


@app.route("/animal/<id>", methods=["GET"])
def animal_in_db_detail(id):
    animal_db = Animal_in_db.query.get(id)
    if not animal_db:
        abort(404)
    return animal_schema.jsonify(animal_db)


@app.route("/animal/<id>", methods=["PUT"])
def animal_in_db_update(id):
    animal_db = Animal_in_db.query.get(id)
    if not animal_db:
        abort(404)
    animal_db.name = request.json['name']
    animal_db.kind = request.json['kind']
    animal_db.size_in_m = request.json['size_in_m']
    animal_db.weight_in_kg = request.json['weight_in_kg']
    animal_db.point = request.json['point']
    animal_db.age_in_years = request.json['age_in_years']
    animal_db.hunt_for_prey = request.json['hunt_for_prey']
    animal_db.classes = request.json['classes']
    animal_db.color = request.json['color']
    animal_db.number_of_paws = request.json['number_of_paws']
    db.session.commit()
    return animal_schema.jsonify(animal_db)


@app.route("/animal/<id>", methods=["DELETE"])
def animal_in_db_delete(id):
    animal_db = Animal_in_db.query.get(id)
    if not animal_db:
        abort(404)
    db.session.delete(animal_db)
    db.session.commit()
    return animal_schema.jsonify(animal_db)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
