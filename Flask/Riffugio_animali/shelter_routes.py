from flask import Flask, jsonify, request, url_for

from Classi.cat import Cat
from Classi.dog import Dog
from Classi.shelter import Shelter

animal1: Cat = Cat(id='1', name='Garfield', age_years=3, weight_kg=5.1, favourite_toy='ball', indoor_only=True)
animal2: Cat = Cat(id='2', name='Tom', age_years=4, weight_kg=3.5, favourite_toy='mouse', indoor_only=False)
animal3: Dog = Dog(id='3', name='Spike', age_years=1, weight_kg=5, breed='bool dog', is_trained=True)
animal4: Dog = Dog(id='4', name='Spek', age_years=8, weight_kg=10.1, breed='russel', is_trained=True)


shelter1: Shelter = Shelter()

shelter1.add_animal(animal=animal1)
shelter1.add_animal(animal=animal2)
shelter1.add_animal(animal=animal3)
shelter1.add_animal(animal=animal4)

app = Flask(__name__)


@app.route('/')
def home():
    home_out = {
        'message': "Welcome to Animal Shelter API",
        'links': {
            'list_animals': url_for("list_animals"),
            'sample_dog': url_for("get_animal", animal_id="1"),
            'sample_dog_food': url_for('get_food', animal_id="1"),
            'sample_dog_adoption': url_for('get_adoption', animal_id="1")
        }
    }

    return jsonify(home_out)


@app.route('/Animals')
def list_animals() -> None:
    out_dict = {id: animal.info() for id, animal in shelter1.animals.items()}

    return jsonify(out_dict)
    

@app.route('/Animals/<string:animal_id>')
def get_animal(animal_id):
    if animal_id in shelter1.animals:
        animal_out = shelter1.get(animal_id).info()
        return jsonify(animal_out)

    else:
        return {'errore': "Animal not found"}, 404
    

@app.route('/Animals/<string:animal_id>/food')
def get_food(animal_id):
    if animal_id in shelter1.animals:
        food_out = {'id': animal_id, 'daily_food_grams': shelter1.get(animal_id).daily_food_grams()}
        return jsonify(food_out)
    
    else:
        return {'errore': "Animal not found"}, 404
    

@app.route('/Animals/<string:animal_id>/adoption')
def get_adoption(animal_id):
    if animal_id in shelter1.animals:
        adoption_out = {'id': animal_id, 'adopted': shelter1.is_adopted(animal_id)}
        return adoption_out
    
    else:
        return {'errore': "Animal not found"}, 404
    

@app.post('/Animals/add')
def add_animal():
    pass