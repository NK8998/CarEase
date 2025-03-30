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
    special_request = data.get("special_request")
    appointment_date = data.get("start_date")
    service_id = data.get("service")
    end_date = data.get("end_date")
    legible_date = data.get("legible_date")
    service_name = data.get("service_name")
    phone = data.get("phone")
    receipt_id = nanoid.generate(size=15)
    status = "pending"

    if not all([customer_name, email, appointment_date, service_id, end_date, legible_date, service_name, phone]):
        return jsonify({"error": "All fields are required"}), 400
    if not isinstance(customer_name, str) or not isinstance(email, str) or not isinstance(appointment_date, str) or not isinstance(service_id, str) or not isinstance(end_date, str) or not isinstance(legible_date, str) or not isinstance(service_name, str) or not isinstance(phone, str):
        return jsonify({"error": "Invalid data type"}), 400
    
    with sqlite3.connect("db/CarEase.db") as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO appointments (customer_name, email, special_request, appointment_date, service_id, receipt_id, status, end_date, phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (customer_name, email, special_request, appointment_date, service_id, receipt_id, status, end_date, phone))
            conn.commit()
        except sqlite3.Error as e:
            return jsonify({"error": str(e)}), 500
        
    await sendMail(email, customer_name, "Booking Confirmation", receipt_id, legible_date, service_name)

    # Process data here...
    return jsonify({"message": "Booking created successfully", "data": data}), 201

