from flask import Flask, render_template 
import requests
import datetime

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

data = get_iss_data()

#print(time, latitude, longitude)
@app.route('/')
def home():
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
