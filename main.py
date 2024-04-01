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
    astronaut_url = "http://api.open-notify.org/astros.json"
    astronaut_req = requests.get(astronaut_url)
    astronauts_data = astronaut_req.json()
    #for ast in astronauts_data["people"]:
        #print(ast["name"], ast["craft"])    
    return astronauts_data


scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(func=get_iss_data, trigger='interval', seconds=5)


@app.route('/')
def home():
    data = get_iss_data()
    astronauts_data = get_astronauts_data()
    return render_template('index.html', data=data, astronauts_data=astronauts_data)

if __name__ == "__main__":
    app.run(debug=True)
