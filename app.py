from flask import Flask, render_template, request
import requests
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__, template_folder='templates', static_folder='templates/static')


@app.route('/satellite.html', methods=['POST'])
def satellite():
    BASE_URL = "https://api.wheretheiss.at"
    satellite_id = request.form.get('satellite')
    response = requests.get(f'{BASE_URL}/v1/satellites/{satellite_id}')
    satelliteData = response.json()
    name = satelliteData['name']
    name = name.upper()
    id = satelliteData['id']
    latit = satelliteData['latitude']
    longit = satelliteData['longitude']
    velocity = "{:,}".format(satelliteData['velocity'])
    return render_template('satellite.html', satellite=id, satel=name, speed=velocity, latitude=latit, longitude=longit)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/.well-known/acme-challenge/<string:id>', methods=['GET'])
def acme_challenge(id):
    # code to handle the request and return the certbot provided id
    with open('certbot_id.txt') as f:
        id = f.read()
    return id



if __name__ == '__main__':
    app.run()
