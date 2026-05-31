import googlemaps
from flask import current_app
from datetime import datetime

class GoogleMapsService:
    """Handle Google Maps API operations"""
    
    @staticmethod
    def get_client():
        """Get Google Maps client"""
        api_key = current_app.config['GOOGLE_MAPS_API_KEY']
        return googlemaps.Client(key=api_key)
    
    @staticmethod
    def get_directions(origin, destination, mode='driving'):
        """
        Get directions between two locations
        """
        try:
            gmaps = GoogleMapsService.get_client()
            result = gmaps.directions(
                origin,
                destination,
                mode=mode,
                departure_time=datetime.now()
            )
            
            if result:
                route = result[0]
                leg = route['legs'][0]
                
                return {
                    'status': 'success',
                    'distance': leg['distance']['text'],
                    'duration': leg['duration']['text'],
                    'steps': [
                        {
                            'instruction': step['html_instructions'].replace('<b>', '').replace('</b>', ''),
                            'distance': step['distance']['text'],
                            'duration': step['duration']['text']
                        }
                        for step in leg['steps']
                    ]
                }
            return {'status': 'error', 'message': 'No route found'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    @staticmethod
    def search_nearby(location, radius=5000, place_type='tourist_attraction'):
        """
        Search for nearby places
        """
        try:
            gmaps = GoogleMapsService.get_client()
            result = gmaps.places_nearby(
                location=location,
                radius=radius,
                type=place_type
            )
            
            places = []
            for place in result.get('results', [])[:10]:
                places.append({
                    'name': place['name'],
                    'latitude': place['geometry']['location']['lat'],
                    'longitude': place['geometry']['location']['lng'],
                    'rating': place.get('rating', 'N/A'),
                    'place_id': place['place_id'],
                    'types': place.get('types', []),
                    'vicinity': place.get('vicinity', '')
                })
            
            return {'status': 'success', 'places': places}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    @staticmethod
    def get_place_details(place_id):
        """
        Get detailed information about a place
        """
        try:
            gmaps = GoogleMapsService.get_client()
            result = gmaps.place(place_id)
            
            if result['status'] == 'OK':
                place = result['result']
                return {
                    'status': 'success',
                    'name': place['name'],
                    'address': place.get('formatted_address', ''),
                    'phone': place.get('formatted_phone_number', 'N/A'),
                    'website': place.get('website', 'N/A'),
                    'rating': place.get('rating', 'N/A'),
                    'reviews': place.get('reviews', [])[:5],
                    'opening_hours': place.get('opening_hours', {})
                }
            return {'status': 'error', 'message': 'Place not found'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    @staticmethod
    def geocode(address):
        """
        Convert address to latitude and longitude
        """
        try:
            gmaps = GoogleMapsService.get_client()
            result = gmaps.geocode(address)
            
            if result:
                location = result[0]['geometry']['location']
                return {
                    'status': 'success',
                    'latitude': location['lat'],
                    'longitude': location['lng'],
                    'formatted_address': result[0]['formatted_address']
                }
            return {'status': 'error', 'message': 'Address not found'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}