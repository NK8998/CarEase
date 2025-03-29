# views/about.py
from flask import render_template
from . import bp  # import the Blueprint instance

@bp.route('/team')
def team():
    return render_template('team.html')
