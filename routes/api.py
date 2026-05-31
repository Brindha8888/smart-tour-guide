from flask import Blueprint, jsonify, request
from services.maps_service import GoogleMapsService
from services.weather_service import WeatherService

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/weather', methods=['POST'])
def get_weather():
    """Get weather data"""
    data = request.json
    lat = data.get('latitude')
    lon = data.get('longitude')
    
    weather = WeatherService.get_weather(lat, lon)
    return jsonify(weather)

@api_bp.route('/nearby-places', methods=['POST'])
def nearby_places():
    """Get nearby places"""
    data = request.json
    lat = data.get('latitude')
    lon = data.get('longitude')
    place_type = data.get('type', 'tourist_attraction')
    
    result = GoogleMapsService.search_nearby((lat, lon), place_type=place_type)
    return jsonify(result)

@api_bp.route('/directions', methods=['POST'])
def get_directions():
    """Get directions"""
    data = request.json
    origin = data.get('origin')
    destination = data.get('destination')
    mode = data.get('mode', 'driving')
    
    result = GoogleMapsService.get_directions(origin, destination, mode)
    return jsonify(result)

@api_bp.route('/geocode', methods=['POST'])
def geocode():
    """Geocode address"""
    data = request.json
    address = data.get('address')
    
    result = GoogleMapsService.geocode(address)
    return jsonify(result)