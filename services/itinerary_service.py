from datetime import datetime, timedelta

class ItineraryService:
    """Generate and manage travel itineraries"""
    
    @staticmethod
    def generate_itinerary(destination, duration_days, interests=None, attractions=None):
        """Generate a detailed itinerary for a destination"""
        if interests is None:
            interests = []
        if attractions is None:
            attractions = destination.get('attractions', [])
        
        itinerary = {
            'destination': destination.get('name'),
            'duration': duration_days,
            'days': []
        }
        
        attractions_per_day = len(attractions) // duration_days
        if attractions_per_day == 0:
            attractions_per_day = 1
        
        current_date = datetime.now()
        
        for day in range(1, duration_days + 1):
            day_attractions = attractions[
                (day - 1) * attractions_per_day:day * attractions_per_day
            ]
            
            day_itinerary = {
                'day': day,
                'date': (current_date + timedelta(days=day - 1)).strftime('%Y-%m-%d'),
                'activities': [
                    {
                        'time': '09:00 - 12:00',
                        'activity': f'Visit {day_attractions[0] if day_attractions else "local sites"}',
                        'type': 'sightseeing'
                    },
                    {
                        'time': '12:00 - 13:00',
                        'activity': 'Lunch at local restaurant',
                        'type': 'dining'
                    },
                    {
                        'time': '14:00 - 17:00',
                        'activity': f'Explore {day_attractions[1] if len(day_attractions) > 1 else "museums and galleries"}',
                        'type': 'sightseeing'
                    },
                    {
                        'time': '18:00 - 19:30',
                        'activity': 'Rest and refreshment',
                        'type': 'rest'
                    },
                    {
                        'time': '19:30 - 21:00',
                        'activity': 'Dinner and evening entertainment',
                        'type': 'dining'
                    }
                ]
            }
            
            itinerary['days'].append(day_itinerary)
        
        return itinerary
    
    @staticmethod
    def add_activity_to_itinerary(itinerary, day, activity_details):
        """Add an activity to a specific day in the itinerary"""
        if day <= len(itinerary['days']):
            itinerary['days'][day - 1]['activities'].append(activity_details)
            return True
        return False
    
    @staticmethod
    def calculate_packing_list(destination_category, duration_days, interests=None):
        """Generate a packing list based on destination and duration"""
        base_items = [
            'Passport',
            'Travel Insurance',
            'Wallet and credit cards',
            'Phone charger',
            'Toiletries',
            'Medications',
            'Comfortable walking shoes',
            'Socks and underwear',
            'Casual clothing',
            'Light jacket'
        ]
        
        category_items = {
            'Beach': ['Swimsuit', 'Sunscreen', 'Hat', 'Sunglasses', 'Beach bag'],
            'City': ['Formal wear', 'Comfortable walking shoes', 'Backpack'],
            'Nature': ['Hiking boots', 'Weather-appropriate clothing', 'Waterproof jacket'],
            'Culture': ['Modest clothing', 'Comfortable shoes', 'Notebook'],
            'Mountain': ['Warm layers', 'Hiking boots', 'Thermal socks', 'Waterproof jacket']
        }
        
        packing_list = base_items.copy()
        
        if isinstance(destination_category, list):
            for category in destination_category:
                packing_list.extend(category_items.get(category, []))
        else:
            packing_list.extend(category_items.get(destination_category, []))
        
        return list(set(packing_list))