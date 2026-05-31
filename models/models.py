from flask_mysqldb import MySQL

mysql = MySQL()

class User:
    """User model"""
    
    @staticmethod
    def create(username, email, password, full_name=''):
        """Create a new user"""
        try:
            cur = mysql.connection.cursor()
            cur.execute('''
                INSERT INTO users (username, email, password, full_name)
                VALUES (%s, %s, %s, %s)
            ''', (username, email, password, full_name))
            mysql.connection.commit()
            cur.close()
            return {'status': 'success', 'message': 'User created successfully'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    @staticmethod
    def get_by_email(email):
        """Get user by email"""
        try:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM users WHERE email = %s', (email,))
            user = cur.fetchone()
            cur.close()
            return user
        except Exception as e:
            return None
    
    @staticmethod
    def get_by_id(user_id):
        """Get user by ID"""
        try:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM users WHERE id = %s', (user_id,))
            user = cur.fetchone()
            cur.close()
            return user
        except Exception as e:
            return None


class Trip:
    """Trip model"""
    
    @staticmethod
    def create(user_id, title, destination, start_date, end_date, budget=0, latitude=0, longitude=0):
        """Create a new trip"""
        try:
            cur = mysql.connection.cursor()
            cur.execute('''
                INSERT INTO trips (user_id, title, destination, start_date, end_date, budget, latitude, longitude)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ''', (user_id, title, destination, start_date, end_date, budget, latitude, longitude))
            mysql.connection.commit()
            trip_id = cur.lastrowid
            cur.close()
            return {'status': 'success', 'trip_id': trip_id}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    @staticmethod
    def get_by_id(trip_id):
        """Get trip by ID"""
        try:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM trips WHERE id = %s', (trip_id,))
            trip = cur.fetchone()
            cur.close()
            return trip
        except Exception as e:
            return None
    
    @staticmethod
    def get_by_user(user_id):
        """Get all trips for a user"""
        try:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM trips WHERE user_id = %s ORDER BY start_date DESC', (user_id,))
            trips = cur.fetchall()
            cur.close()
            return trips
        except Exception as e:
            return []
    
    @staticmethod
    def update(trip_id, title, destination, start_date, end_date, budget=0):
        """Update a trip"""
        try:
            cur = mysql.connection.cursor()
            cur.execute('''
                UPDATE trips SET title=%s, destination=%s, start_date=%s, end_date=%s, budget=%s
                WHERE id=%s
            ''', (title, destination, start_date, end_date, budget, trip_id))
            mysql.connection.commit()
            cur.close()
            return {'status': 'success', 'message': 'Trip updated successfully'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    @staticmethod
    def delete(trip_id):
        """Delete a trip"""
        try:
            cur = mysql.connection.cursor()
            cur.execute('DELETE FROM trips WHERE id = %s', (trip_id,))
            mysql.connection.commit()
            cur.close()
            return {'status': 'success', 'message': 'Trip deleted successfully'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}