from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.models import Trip
from functools import wraps

tours_bp = Blueprint('tours', __name__, url_prefix='/tours')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login first.', 'error')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@tours_bp.route('/')
@login_required
def index():
    """My trips page"""
    user_id = session['user_id']
    trips = Trip.get_by_user(user_id)
    return render_template('trips.html', trips=trips)

@tours_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    """Create new trip"""
    if request.method == 'POST':
        user_id = session['user_id']
        title = request.form.get('title')
        destination = request.form.get('destination')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        budget = request.form.get('budget')
        
        result = Trip.create(user_id, title, destination, start_date, end_date, budget)
        
        if result['status'] == 'success':
            flash('Trip created successfully!', 'success')
            return redirect(url_for('tours.index'))
        else:
            flash(result['message'], 'error')
    
    return render_template('create_trip.html')

@tours_bp.route('/<int:trip_id>')
@login_required
def view_trip(trip_id):
    """View trip details"""
    trip = Trip.get_by_id(trip_id)
    
    if trip and trip[1] == session['user_id']:
        return render_template('trip_details.html', trip=trip)
    else:
        flash('Trip not found.', 'error')
        return redirect(url_for('tours.index'))

@tours_bp.route('/<int:trip_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_trip(trip_id):
    """Edit trip"""
    trip = Trip.get_by_id(trip_id)
    
    if not trip or trip[1] != session['user_id']:
        flash('Trip not found.', 'error')
        return redirect(url_for('tours.index'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        destination = request.form.get('destination')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        budget = request.form.get('budget')
        
        result = Trip.update(trip_id, title, destination, start_date, end_date, budget)
        
        if result['status'] == 'success':
            flash('Trip updated successfully!', 'success')
            return redirect(url_for('tours.view_trip', trip_id=trip_id))
        else:
            flash(result['message'], 'error')
    
    return render_template('edit_trip.html', trip=trip)

@tours_bp.route('/<int:trip_id>/delete', methods=['POST'])
@login_required
def delete_trip(trip_id):
    """Delete trip"""
    trip = Trip.get_by_id(trip_id)
    
    if trip and trip[1] == session['user_id']:
        result = Trip.delete(trip_id)
        flash(result['message'], 'success' if result['status'] == 'success' else 'error')
    else:
        flash('Trip not found.', 'error')
    
    return redirect(url_for('tours.index'))