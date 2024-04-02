# ISS Tracker

## Overview
This project is a web application that tracks the International Space Station (ISS) in real-time and provides information about its current location, as well as details about the astronauts on board.

## Features
- Real-time tracking of the ISS using the Open Notify API
- Display of ISS location details including latitude, longitude, and timestamp
- Display of information about astronauts currently on board the ISS
- Dynamic updating of data at regular intervals
- Visualization of ISS location on an interactive map

## Installation
To run this project locally, follow these steps:
1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the Flask application by executing `python run.py`.
4. Access the web application by navigating to `http://localhost:5000` in your web browser.

## Deployment
This project is deployed on [Azure](https://iss-tracker.azurewebsites.net/). You can access it [here](https://iss-tracker.azurewebsites.net/).

## Technologies Used
- Python
- Flask
- HTML
- CSS
- JavaScript
- Leaflet.js (for map visualization)
- Open Notify API (for ISS data)

## Project Structure
- `app.py`: Contains the Flask application code.
- `templates/`: Directory containing HTML templates for rendering pages.
- `static/`: Directory containing static files such as CSS stylesheets and JavaScript scripts.
- `requirements.txt`: File listing the project dependencies.

## Contributing
Contributions to this project are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new pull request.

## License
This project is licensed under the [MIT License](LICENSE).
