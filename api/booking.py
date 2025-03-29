from flask import request, jsonify
from . import bp  # import the Blueprint instance
import sqlite3
import nanoid
from .util import sendMail

@bp.route("/create_booking", methods=["POST"])
async def create_booking():
    data = request.json  # Get JSON data from frontend
    customer_name = data.get("name")
    email = data.get("email")
    special_request = data.get("srequest")
    appointment_date = data.get("date")
    service_id = data.get("service")
    receipt_id = nanoid.generate(size=15)
    status = "pending"

    if not all([customer_name, email, appointment_date, service_id]):
        return jsonify({"error": "All fields are required"}), 400
    if not isinstance(customer_name, str) or not isinstance(email, str) or not isinstance(appointment_date, str) or not isinstance(service_id, str):
        return jsonify({"error": "Invalid data type"}), 400
    
    with sqlite3.connect("db/CarEase.db") as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO appointments (customer_name, email, special_request, appointment_date, service_id, receipt_id, status) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (customer_name, email, special_request, appointment_date, service_id, receipt_id, status))
            conn.commit()
        except sqlite3.Error as e:
            return jsonify({"error": str(e)}), 500
        
    await sendMail(email, customer_name, "Booking Confirmation", receipt_id)

    # Process data here...
    return jsonify({"message": "Booking created successfully", "data": data}), 201

