import requests
from flask import current_app

class WeatherService:
    """Handle weather-related operations"""
    
    @staticmethod
    def get_weather(latitude, longitude):
        """
        Get weather information for a location
        """
        try:
            api_key = current_app.config['OPENWEATHER_API_KEY']
            url = f"https://api.openweathermap.org/data/2.5/weather"
            
            params = {
                'lat': latitude,
                'lon': longitude,
                'appid': api_key,
                'units': 'metric'
            }
            
            response = requests.get(url, params=params)
            data = response.json()
            
            if response.status_code == 200:
                return {
                    'status': 'success',
                    'temperature': data['main']['temp'],
                    'feels_like': data['main']['feels_like'],
                    'description': data['weather'][0]['description'],
                    'humidity': data['main']['humidity'],
                    'wind_speed': data['wind']['speed'],
                    'icon': data['weather'][0]['icon']
                }
            else:
                return {'status': 'error', 'message': 'Failed to fetch weather'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    @staticmethod
    def get_forecast(latitude, longitude):
        """
        Get 5-day weather forecast
        """
        try:
            api_key = current_app.config['OPENWEATHER_API_KEY']
            url = f"https://api.openweathermap.org/data/2.5/forecast"
            
            params = {
                'lat': latitude,
                'lon': longitude,
                'appid': api_key,
                'units': 'metric'
            }
            
            response = requests.get(url, params=params)
            data = response.json()
            
            if response.status_code == 200:
                forecast_list = []
                for item in data['list'][::8]:
                    forecast_list.append({
                        'date': item['dt_txt'],
                        'temp': item['main']['temp'],
                        'description': item['weather'][0]['description'],
                        'icon': item['weather'][0]['icon']
                    })
                return {'status': 'success', 'forecast': forecast_list}
            else:
                return {'status': 'error', 'message': 'Failed to fetch forecast'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}