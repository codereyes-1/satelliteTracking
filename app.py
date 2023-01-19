from flask import Flask, render_template, request
import requests


app = Flask(__name__, template_folder='templates')


@app.route('/satellite.html', methods=['POST'])
def satellite():
    BASE_URL = "https://api.wheretheiss.at"
    satellite_id = request.form.get('satellite')
    response = requests.get(f'{BASE_URL}/v1/satellites/{satellite_id}')
    satelliteData = response.json()
    name = satelliteData['name']
    id = satelliteData['id']
    latitude = satelliteData['latitude']
    longitude = satelliteData['longitude']
    velocity = "{:,}".format(satelliteData['velocity'])
    return render_template('satellite.html', satellite=id, satel=name, speed=velocity)



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
