from flask import Flask, render_template, request, redirect
import requests
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__, template_folder='templates', static_folder='templates/static')


@app.before_request
def before_request():
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

@app.route('/.well-known/acme-challenge/<string:id>')
def acme_challenge(id):
    with open('.well-known/acme-challenge/'+id+'.txt') as f:
        certbot_id = f.read()
    return certbot_id


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



if __name__ == '__main__':
    app.run()
