
# CarEase - Car Service Management Application

## Project Overview
CarEase is designed to help users manage their car services efficiently. It allows users to book appointments, track service progress, and make payments using M-Pesa. The application is built using Flask, a lightweight WSGI web application framework in Python.

## Features
- View different services offered
- Book appointments for services
- View and manage appointments
- Pay for services using M-Pesa
- Keep track of service progress
- Service tracking
- Email notifications

## Requirements
- Python 3.x
- Flask
- SQLite
- ngrok for daraja api integration


# Project Structure

```
project/
├── api/
│   ├── __init__.py
│   ├── appointments.py
│   ├── booking.py
│   ├── contact.py
│   ├── daraja.py
│   ├── tracking.py
│   ├── users.py
│   └── util.py
├── db/
│   ├── __init__.py
│   ├── util/
│   │   ├── create.py
│   │   ├── drop.py
│   │   ├── insert.py
│   └── carease.db
│   └── initialize.py
├── misc/
│   ├── __init__.py
│   ├── helpers.py
│   └── constants.py
├── static/
│   ├── css/
│   ├── js/
│   └── img/
│   └── lib/
│   └── scss/
├── templates/
│   ├── 404.html
│   └── index.html
│   └── about.html
│   └── contact.html
│   └── progress.html
│   └── services.html
│   └── tracking.html
├── views/
│   ├── __init__.py
│   ├── index.py
│   └── about.py
│   └── contact.py
│   └── progress.py
│   └── services.py
│   └── tracking.py
├── app.py
├── requirements.txt
├── README.md
```
## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/NK8998/CarEase.git
    cd CarEase
    ```
2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
5. Initialize the database:
    ```bash
    python db/initialize.py
    ```
6. Run the application:
    ```bash
    python app.py
    ```
7. Access the application in your web browser at `http://localhost:5000`
