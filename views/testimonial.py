# views/about.py
from flask import render_template
from . import bp  # import the Blueprint instance

@bp.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')
