from flask import Flask, render_template 
import requests
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

def get_iss_data():
    url = "http://api.open-notify.org/iss-now.json"
    req = requests.get(url)
    iss_data = req.json()

    raw_time = datetime.datetime.fromtimestamp(iss_data['timestamp'])
    time = raw_time.strftime('%Y-%m-%d %H:%M:%S')
    latitude = iss_data['iss_position']['latitude']
    longitude = iss_data['iss_position']['longitude']

    return {
        "time": time,
        "latitude": latitude,
        "longitude": longitude
    }
def get_astronauts_data():
    astronauts_url = "http://api.open-notify.org/astros.json"
    astronauts_req = requests.get(astronauts_url)
    astronauts_data = astronauts_req.json()
    astronauts = {} 
    for astronaut in astronauts_data["people"]:  # Iterate directly over astronauts_data
        astronauts[astronaut["name"]] = astronaut["craft"]
    return astronauts


scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(func=get_iss_data, trigger='interval', seconds=5)


@app.route('/')
def home():
    data = get_iss_data()
    astronauts = get_astronauts_data()
    return render_template('index.html', data=data, astronauts=astronauts)

if __name__ == "__main__":
    app.run(debug=True)
