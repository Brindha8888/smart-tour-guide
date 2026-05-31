// Global variables
let map;
let markers = [];
const API_BASE = '/api';

// Initialize map
function initMap(latitude = 40.7128, longitude = -74.0060, zoom = 12) {
    const mapElement = document.getElementById('map');
    if (!mapElement) return;
    
    const mapOptions = {
        zoom: zoom,
        center: { lat: latitude, lng: longitude },
        styles: [
            { elementType: 'geometry', stylers: [{ color: '#f5f5f5' }] },
            { elementType: 'labels.text.stroke', stylers: [{ color: '#ffffff' }] },
            { elementType: 'labels.text.fill', stylers: [{ color: '#616161' }] }
        ]
    };
    
    map = new google.maps.Map(mapElement, mapOptions);
}

// Add marker to map
function addMarker(lat, lng, title, info = '') {
    const marker = new google.maps.Marker({
        position: { lat: lat, lng: lng },
        map: map,
        title: title
    });
    
    if (info) {
        const infoWindow = new google.maps.InfoWindow({
            content: `<div><strong>${title}</strong><p>${info}</p></div>`
        });
        
        marker.addListener('click', () => {
            markers.forEach(m => {
                if (m.infoWindow) m.infoWindow.close();
            });
            infoWindow.open(map, marker);
            marker.infoWindow = infoWindow;
        });
    }
    
    markers.push(marker);
    return marker;
}

// Clear all markers
function clearMarkers() {
    markers.forEach(marker => marker.setMap(null));
    markers = [];
}

// Fetch weather data
async function getWeather(latitude, longitude) {
    try {
        const response = await fetch(`${API_BASE}/weather`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ latitude, longitude })
        });
        return await response.json();
    } catch (error) {
        console.error('Error fetching weather:', error);
        return { status: 'error' };
    }
}

// Fetch nearby places
async function getNearbyPlaces(latitude, longitude, placeType = 'tourist_attraction') {
    try {
        const response = await fetch(`${API_BASE}/nearby-places`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ latitude, longitude, type: placeType })
        });
        return await response.json();
    } catch (error) {
        console.error('Error fetching nearby places:', error);
        return { status: 'error' };
    }
}

// Get directions
async function getDirections(origin, destination, mode = 'driving') {
    try {
        const response = await fetch(`${API_BASE}/directions`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ origin, destination, mode })
        });
        return await response.json();
    } catch (error) {
        console.error('Error fetching directions:', error);
        return { status: 'error' };
    }
}

// Geocode address
async function geocodeAddress(address) {
    try {
        const response = await fetch(`${API_BASE}/geocode`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ address })
        });
        return await response.json();
    } catch (error) {
        console.error('Error geocoding address:', error);
        return { status: 'error' };
    }
}

// Format time
function formatTime(timeString) {
    const [hours, minutes] = timeString.split(':');
    const hour = parseInt(hours);
    const ampm = hour >= 12 ? 'PM' : 'AM';
    const displayHour = hour % 12 || 12;
    return `${displayHour}:${minutes} ${ampm}`;
}

// Display notification
function showNotification(message, type = 'success') {
    const alertClass = type === 'success' ? 'alert-success' : 'alert-danger';
    const alertHTML = `
        <div class="alert ${alertClass} alert-dismissible fade show" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
    
    const container = document.querySelector('.container');
    const alertElement = document.createElement('div');
    alertElement.innerHTML = alertHTML;
    container.insertBefore(alertElement.firstElementChild, container.firstChild);
}

// Document ready
document.addEventListener('DOMContentLoaded', function() {
    const mapElement = document.getElementById('map');
    if (mapElement) {
        initMap();
    }
});