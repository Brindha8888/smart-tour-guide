# Smart Tour Guide - AI-Powered Travel Planning Application

A comprehensive web application built with Python Flask that helps users plan their perfect trips with AI-powered destination recommendations, real-time weather integration, Google Maps functionality, and automated itinerary generation.

## Features

✨ **Key Features:**
- 🧠 **Smart Destination Recommendations** - AI-powered suggestions based on budget, duration, and interests
- 🗺️ **Google Maps Integration** - Interactive maps, directions, and nearby attractions
- 🌤️ **Real-time Weather** - Current conditions and 5-day forecast for destinations
- 📋 **Itinerary Generation** - Automated day-by-day travel plans with activities and timings
- 🎒 **Smart Packing List** - Destination-specific packing recommendations
- 👤 **User Management** - Secure registration and authentication
- 📱 **Trip Management** - Save, edit, and organize your travel plans
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile devices

## Tech Stack

**Backend:**
- Python 3.8+
- Flask 2.3.0
- Flask-MySQLdb for database operations

**Database:**
- MySQL 8.0+

**Frontend:**
- HTML5
- CSS3
- Bootstrap 5.3
- JavaScript (Vanilla)
- Google Maps API

**APIs:**
- Google Maps API (directions, places, geocoding)
- OpenWeather API (weather data)

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- MySQL 8.0 or higher
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/Brindha8888/smart-tour-guide.git
cd smart-tour-guide
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your configuration
# Add your API keys:
# - GOOGLE_MAPS_API_KEY
# - OPENWEATHER_API_KEY
```

### Step 5: Create MySQL Database
```bash
mysql -u root -p

CREATE DATABASE smart_tour_guide;
EXIT;
```

### Step 6: Configure Database Connection
Update your `.env` file with MySQL credentials:
```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=smart_tour_guide
```

### Step 7: Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Getting API Keys

### Google Maps API
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable Maps, Places, and Geocoding APIs
4. Create an API key
5. Add the key to `.env`

### OpenWeather API
1. Sign up at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your free API key
3. Add the key to `.env`

## File Structure

```
smart-tour-guide/
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables example
├── .gitignore            # Git ignore file
│
├── services/
│   ├── __init__.py
│   ├── weather_service.py          # Weather integration
│   ├── maps_service.py             # Google Maps integration
│   ├── recommendation_service.py   # Recommendation engine
│   └── itinerary_service.py        # Itinerary generation
│
├── models/
│   ├── __init__.py
│   ├── database.py       # Database setup
│   └── models.py         # Data models (User, Trip, etc.)
│
├── routes/
│   ├── __init__.py
│   ├── auth.py           # Authentication routes
│   ├── tours.py          # Trip management routes
│   ├── recommendations.py # Recommendation routes
│   └── api.py            # API endpoints
│
├── static/
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   └── js/
│       └── app.js        # JavaScript functionality
│
└── templates/
    ├── base.html                # Base template
    ├── index.html               # Home page
    ├── login.html               # Login page
    ├── register.html            # Registration page
    ├── dashboard.html           # User dashboard
    ├── recommendations.html     # Recommendations page
    ├── destination_detail.html  # Destination details
    ├── trips.html               # My trips page
    ├── create_trip.html         # Create trip form
    ├── edit_trip.html           # Edit trip form
    └── trip_details.html        # Trip details view
```

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Trips Table
```sql
CREATE TABLE trips (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(10, 2),
    latitude FLOAT,
    longitude FLOAT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

## Usage Guide

### 1. User Registration
- Navigate to the registration page
- Fill in your details (name, email, password)
- Click "Register"

### 2. Explore Destinations
- Go to "Explore" section
- Set your budget, trip duration, and interests
- View AI-powered recommendations
- Click on any destination for details

### 3. Check Weather
- View current weather and 5-day forecast for destinations
- Make informed decisions based on weather conditions

### 4. Create Itineraries
- Select a destination
- View auto-generated day-by-day itinerary
- Get smart packing recommendations

### 5. Manage Trips
- Create, view, edit, and delete your trips
- Access all trip details from your dashboard
- Track your travel plans in one place

## API Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /auth/logout` - User logout

### Recommendations
- `GET /recommendations/` - Recommendations page
- `POST /recommendations/search` - Search recommendations
- `GET /recommendations/destination/<id>` - Destination details
- `POST /recommendations/generate-itinerary` - Generate itinerary

### Trips
- `GET /tours/` - List user trips
- `POST /tours/create` - Create new trip
- `GET /tours/<id>` - View trip details
- `POST /tours/<id>/edit` - Edit trip
- `POST /tours/<id>/delete` - Delete trip

### API
- `POST /api/weather` - Get weather data
- `POST /api/nearby-places` - Get nearby attractions
- `POST /api/directions` - Get directions
- `POST /api/geocode` - Geocode address

## Security Considerations

- Passwords are hashed using Werkzeug security
- Environment variables store sensitive information
- CORS and CSRF protections implemented
- Input validation on all forms
- SQL injection prevention through parameterized queries

## Performance Optimization

- Database indexing on frequently queried columns
- API response caching where applicable
- Lazy loading of maps and weather data
- Minified CSS and JavaScript
- Bootstrap CDN for faster loading

## Troubleshooting

### Database Connection Error
- Verify MySQL is running
- Check credentials in `.env`
- Ensure database exists

### API Key Errors
- Verify API keys are correct in `.env`
- Check API quotas and limits
- Ensure APIs are enabled in respective consoles

### Map Not Displaying
- Verify Google Maps API key is valid
- Check browser console for errors
- Ensure JavaScript is enabled

## Future Enhancements

- 🤖 Machine learning for better recommendations
- 💬 Chat-based trip planning
- 🎫 Booking integration (flights, hotels, activities)
- 📸 Social features and trip sharing
- 💳 Payment integration
- 📱 Native mobile app
- 🌐 Multi-language support
- 🔔 Notification system

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, email support@smarttourguide.com or open an issue on GitHub.

## Author

**Brindha8888**
- GitHub: [@Brindha8888](https://github.com/Brindha8888)

## Acknowledgments

- Flask documentation
- Bootstrap team
- Google Maps API
- OpenWeather API
- MySQL documentation

---

**Happy Traveling! 🌍✈️🎒**