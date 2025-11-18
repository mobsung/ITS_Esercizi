from flask import Flask, url_for, jsonify
from Classi.carousel import Carousel
from Classi.rollerCoaster import RollerCoaster
from Classi.park import Park


par1 = Park()

cau1 = Carousel(ride_id='#1', name='Caurusel1', min_height=100)
cau2 = Carousel(ride_id='#3', name='Caurusel2', min_height=120)
roll1 = RollerCoaster(ride_id='#2', name='RollerCoaster1', min_height=140)
roll2 = RollerCoaster(ride_id='#4', name='RollerCoaster2', min_height=180)

par1.add(cau1)
par1.add(cau2)
par1.add(roll1)
par1.add(roll2)

app = Flask(__name__)

# ride_routes = {par1.get(ride_id).ride_id: f"<a href='{url_for('show_rides', ride_id=f'{ride_id}')}'>{par1.get(ride_id).name}</a>" for ride_id in par1.list_all()}

@app.route('/')
def home():
    str_out: str = 'Welcome to Park API<br>'
    
    for ride in par1.list_all():
        str_out += f"<a href='{url_for('show_rides', ride_id=f'{ride.ride_id}')}'>{ride.name}</a><br>"

    return str_out

@app.route('/rides/<string:ride_id>')
def show_rides(ride_id: str) -> str:
    return f"<a href='/'>Home</a><br>" + f'{par1.get(ride_id).info()}'
