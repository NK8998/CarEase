# views/about.py
from flask import render_template
from . import bp  # import the Blueprint instance

@bp.route('/booking')
def booking():
    return render_template('booking.html')
