// script.js

let latitude = document.getElementById("map").dataset.latitude;
let longitude = document.getElementById("map").dataset.longitude;

setTimeout(function () {
    window.location.reload();
}, 5000);

document.addEventListener('DOMContentLoaded', function () {
    let coordinates = [latitude, longitude];
    let map = L.map('map').setView(coordinates, 2);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker(coordinates).addTo(map);
});
