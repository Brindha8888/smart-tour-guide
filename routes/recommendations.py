from flask import Blueprint, render_template, request, jsonify
from services.recommendation_service import RecommendationService
from services.weather_service import WeatherService
from services.itinerary_service import ItineraryService

recommendations_bp = Blueprint('recommendations', __name__, url_prefix='/recommendations')

@recommendations_bp.route('/')
def index():
    """Recommendations page"""
    return render_template('recommendations.html')

@recommendations_bp.route('/search', methods=['POST'])
def search():
    """Search for recommendations"""
    data = request.json
    
    preferences = {
        'budget': data.get('budget', 2000),
        'duration': data.get('duration', 5),
        'categories': data.get('categories', [])
    }
    
    recommendations = RecommendationService.get_recommendations(preferences)
    
    return jsonify({
        'status': 'success',
        'recommendations': recommendations
    })

@recommendations_bp.route('/destination/<dest_id>')
def destination_detail(dest_id):
    """Destination detail page"""
    destination = RecommendationService.get_destination_by_id(dest_id)
    
    if destination:
        weather = WeatherService.get_weather(destination['latitude'], destination['longitude'])
        forecast = WeatherService.get_forecast(destination['latitude'], destination['longitude'])
        
        return render_template('destination_detail.html', 
                             destination=destination,
                             weather=weather,
                             forecast=forecast)
    else:
        return "Destination not found", 404

@recommendations_bp.route('/generate-itinerary', methods=['POST'])
def generate_itinerary():
    """Generate itinerary"""
    data = request.json
    
    destination = RecommendationService.get_destination_by_id(data.get('destination_id'))
    duration = data.get('duration', 5)
    interests = data.get('interests', [])
    
    if destination:
        itinerary = ItineraryService.generate_itinerary(destination, duration, interests)
        packing_list = ItineraryService.calculate_packing_list(destination['category'], duration)
        
        return jsonify({
            'status': 'success',
            'itinerary': itinerary,
            'packing_list': packing_list
        })
    
    return jsonify({'status': 'error', 'message': 'Destination not found'})