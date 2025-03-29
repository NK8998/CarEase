import sqlite3

tb_create_str = '''
                -- Users (optional if you later add login)
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    phone TEXT,
                    email TEXT
                );

                -- Services you offer
                CREATE TABLE IF NOT EXISTS services (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,            -- e.g. Car Wash, Detailing, Tinting, etc.
                    description TEXT,
                    price REAL                     -- Optional for demo
                );

                -- Appointments / Bookings
                CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,               -- Can be NULL if no login
                    customer_name TEXT NOT NULL,   -- For walk-ins or demo without login
                    email TEXT NOT NULL,           -- For notifications
                    phone TEXT,
                    service_id INTEGER NOT NULL,
                    appointment_date DATETIME NOT NULL,
                    special_request TEXT,        -- Optional, for any special requests
                    receipt_id TEXT UNIQUE,        -- This will be their "ticket" for tracking
                    status TEXT DEFAULT 'pending', -- pending, confirmed, in-progress, completed
                    location_lat REAL,             -- Optional, if you want to geotag appointments
                    location_lng REAL,             -- Optional, same as above
                    FOREIGN KEY (service_id) REFERENCES services(id)
                );

                -- You can also add a table for location history if you want tracking updates
                CREATE TABLE IF NOT EXISTS appointment_tracking (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    appointment_id INTEGER,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    lat REAL,
                    lng REAL,
                    FOREIGN KEY (appointment_id) REFERENCES appointments(id)
                );
                '''

def create_tables(conn):
    """
    Create tables in the SQLite database.
    """
    try:
        cursor = conn.cursor()
        cursor.executescript(tb_create_str)
        print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

# create tables
create_tables(sqlite3.connect("CarEase.db"))