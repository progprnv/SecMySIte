![Screenshot 2024-10-16 183117](https://github.com/user-attachments/assets/c1fcfc97-695d-4e0c-aa05-47221532d69e)


This project is a simple Flask-based web application that allows users to scan a domain for key security headers such as CSP (Content-Security-Policy), CSRF, CORS, and Host header protection.

Features
Accepts domain input from the user.
Scans the domain for the following headers:
Content-Security-Policy (CSP): Checks if the Content-Security-Policy header is present.
CSRF Token: Checks for headers like X-CSRF-Token or X-Requested-With.
CORS Protection: Checks for the Access-Control-Allow-Origin header and whether it's set to restrict origins.
Host Header Validation: Provides a manual check for host header validation.
Project Structure
php
Copy code
SEC-MY_SITE
│
├── static
│   └── style.css         # Styling for the website
│
├── templates
│   └── index.html        # HTML template for the frontend
│
└── app.py                # Main Flask application
Setup and Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/SEC-MY_SITE.git
cd SEC-MY_SITE
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask app:

bash
Copy code
python app.py
Open your browser and go to:

arduino
Copy code
http://127.0.0.1:5000/
