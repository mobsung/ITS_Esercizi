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
    new_animal: dict = request.get_json()
    if "id" not in new_animal or "type" not in new_animal or "name" not in new_animal or "age_years" not in new_animal or "weight_kg" not in new_animal:
        return jsonify({"errore": "Per aggiungere un animale, fornire tutti i dati!"}), 400
    
    if new_animal["type"] == "dog" and "breed" in new_animal and "is_trained" in new_animal:
        d: Dog = Dog(id=new_animal["id"], name=new_animal["name"], age_years=new_animal["age_years"], weight_kg=new_animal["weight_kg"], breed=new_animal["breed"], is_trained=new_animal["is_trained"])
        shelter1.add_animal(animal=d)
        return jsonify({ "status": "ok", "added": { "id": d.get_id(), "species": d.species() }}), 200
    
    elif "type" == "cat" and "favourite_toy" in new_animal and "indoor_only" in new_animal:
        c: Cat = Cat(id=new_animal["id"], name=new_animal["name"], age_years=new_animal["age_years"], weight_kg=new_animal["weight_kg"], favourite_toy=new_animal["favourite_toy"], indoor_only=new_animal["indoor_only"])
        shelter1.add_animal(c)
        return jsonify({ "status": "ok", "added": { "id": c["id"], "species": c.species() }}), 200

    else:
        return jsonify({"errore": "Per aggiungere un animale, fornire tutti i dati!"}), 400


@app.post('/Animals/<string:animal_id>/adopt')
def adopt_animal(animal_id: str):
    new_adoption: dict = request.get_json()

    if "adopter_name" not in new_adoption:
        return jsonify({"errore": "Per procedere con l'adozione, fornire tutti i dati!"}), 400

    if shelter1.get(animal_id=animal_id) == None:
        return jsonify({"errore": "L'animale non esiste!"}), 400
    
    if shelter1.is_adopted(animal_id=animal_id):
        return jsonify({"errore": "L'animale risulta già adottato!"}), 400
    
    shelter1.set_adopted(animal_id=animal_id, adopter_name=new_adoption["adopter_name"])
    return jsonify({ "id": animal_id, "adopted": True, "adopter_name": new_adoption["adopter_name"]}), 200


