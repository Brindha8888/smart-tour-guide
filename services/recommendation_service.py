from datetime import datetime, timedelta

class RecommendationService:
    """Generate destination recommendations"""
    
    DESTINATIONS = {
        'paris': {
            'name': 'Paris, France',
            'latitude': 48.8566,
            'longitude': 2.3522,
            'attractions': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame', 'Arc de Triomphe'],
            'best_season': ['April-May', 'September-October'],
            'average_days': 5,
            'budget_low': 1000,
            'budget_high': 2500,
            'category': ['City', 'Culture', 'Romance']
        },
        'tokyo': {
            'name': 'Tokyo, Japan',
            'latitude': 35.6762,
            'longitude': 139.6503,
            'attractions': ['Senso-ji Temple', 'Tokyo Skytree', 'Shibuya Crossing', 'Meiji Shrine'],
            'best_season': ['March-April', 'October-November'],
            'average_days': 5,
            'budget_low': 1200,
            'budget_high': 2800,
            'category': ['City', 'Culture', 'Technology']
        },
        'dubai': {
            'name': 'Dubai, UAE',
            'latitude': 25.2048,
            'longitude': 55.2708,
            'attractions': ['Burj Khalifa', 'Dubai Mall', 'Palm Jumeirah', 'Gold Souk'],
            'best_season': ['November-March'],
            'average_days': 4,
            'budget_low': 1500,
            'budget_high': 3000,
            'category': ['City', 'Luxury', 'Shopping']
        },
        'bali': {
            'name': 'Bali, Indonesia',
            'latitude': -8.6705,
            'longitude': 115.2126,
            'attractions': ['Tanah Lot Temple', 'Ubud Rice Fields', 'Mount Batur', 'Seminyak Beach'],
            'best_season': ['April-October'],
            'average_days': 5,
            'budget_low': 600,
            'budget_high': 1500,
            'category': ['Beach', 'Nature', 'Culture']
        },
        'new-york': {
            'name': 'New York, USA',
            'latitude': 40.7128,
            'longitude': -74.0060,
            'attractions': ['Statue of Liberty', 'Central Park', 'Times Square', 'Brooklyn Bridge'],
            'best_season': ['April-May', 'September-October'],
            'average_days': 4,
            'budget_low': 1200,
            'budget_high': 2500,
            'category': ['City', 'Culture', 'Shopping']
        }
    }
    
    @staticmethod
    def get_recommendations(preferences):
        """Get destination recommendations based on user preferences"""
        recommendations = []
        budget = preferences.get('budget', 2000)
        duration = preferences.get('duration', 5)
        categories = preferences.get('categories', [])
        
        for dest_key, destination in RecommendationService.DESTINATIONS.items():
            score = 0
            
            if destination['budget_low'] <= budget <= destination['budget_high']:
                score += 30
            
            if abs(destination['average_days'] - duration) <= 2:
                score += 25
            
            if categories:
                matching_categories = len(set(destination['category']) & set(categories))
                score += matching_categories * 20
            
            if score > 0:
                recommendations.append({
                    'key': dest_key,
                    'name': destination['name'],
                    'latitude': destination['latitude'],
                    'longitude': destination['longitude'],
                    'attractions': destination['attractions'],
                    'best_season': destination['best_season'],
                    'average_days': destination['average_days'],
                    'budget': f"${destination['budget_low']}-${destination['budget_high']}",
                    'categories': destination['category'],
                    'score': score
                })
        
        recommendations.sort(key=lambda x: x['score'], reverse=True)
        return recommendations[:5]
    
    @staticmethod
    def get_destination_by_id(dest_id):
        """Get destination details by ID"""
        return RecommendationService.DESTINATIONS.get(dest_id)