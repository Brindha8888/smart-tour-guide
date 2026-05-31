from flask import Flask, render_template, redirect, url_for, session, flash
from config import Config
from models.database import init_db, create_tables
from models.models import Trip
from functools import wraps

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
init_db(app)

# Create tables on startup
with app.app_context():
    try:
        create_tables(app)
    except:
        pass

# Import and register blueprints
from routes.auth import auth_bp
from routes.recommendations import recommendations_bp
from routes.api import api_bp
from routes.tours import tours_bp

app.register_blueprint(auth_bp)
app.register_blueprint(recommendations_bp)
app.register_blueprint(api_bp)
app.register_blueprint(tours_bp)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    user_id = session['user_id']
    trips = Trip.get_by_user(user_id)
    return render_template('dashboard.html', trips=trips)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)