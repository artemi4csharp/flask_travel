from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.models import Tour, User, Booking

@app.route('/')
@app.route('/home')
def home():
    tours = Tour.query.all()
    return render_template('home.html', tours=tours, title='Available tours:')

@app.route('/book/<int:tour_id>', methods=['GET', 'POST'])
def book(tour_id):
    tour = Tour.query.get(tour_id)
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        user = User.query.filter_by(email=email)
        if not user:
            user = User(name=name, email=email)
            db.session.add(user)
            db.session.commit()
        booking = Booking(user_id=user.id, tour_id=tour.id)
        db.session.add(booking)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('book.html', tour=tour)

@app.route('success')
def success():
    return render_template('success.html')

