from flask_cors import CORS
from flask import Flask, render_template
from views import bp as views_bp
from api import bp as api_bp

app = Flask(__name__, template_folder='templates', static_folder='static')

# Enable CORS for all domains
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(views_bp)
app.register_blueprint(api_bp)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

