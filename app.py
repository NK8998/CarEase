from flask_cors import CORS
from flask import Flask, render_template, request
from views import bp as views_bp
from api import bp as api_bp, tracking
from flask_socketio import SocketIO, emit
clients = {}


app = Flask(__name__, template_folder='templates', static_folder='static')

# Enable CORS for all domains
CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(views_bp)
app.register_blueprint(api_bp)

socketio = SocketIO(app)  # Initialize globally

@socketio.on("connect", namespace="/track_navigator")
def handle_connect():
    try:
        session_id = request.sid
        clients[session_id] = request.remote_addr  # Optionally, store IP or any other info
        print("Remote address:", request.sid)
        print(f"Client connected: {session_id} from {clients[session_id]}")
    except Exception as e:
        print(f"Error handling connection: {e}")

@socketio.on("message", namespace="/track_navigator")
def handle_message(data):
    try:

        sender_session_id = request.sid
        print(f"Received message: {data} from {sender_session_id}")

        for session_id in clients:
            if session_id != sender_session_id:
                print("Sending message to:", session_id)
                # Send a message to all clients except the sender
                socketio.send(f"Message from {sender_session_id}: {data}", to=session_id, namespace="/track_navigator")
    except Exception as e:
        print(f"Error handling message: {e}")

@socketio.on("disconnect", namespace="/track_navigator")
def handle_disconnect():
    try:
        session_id = request.sid
        if session_id in clients:
            del clients[session_id]  
            print(f"Client disconnected: {session_id}")
    except Exception as e:
        print(f"Error handling disconnection: {e}")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)

