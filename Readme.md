# SMS - IEDC HACKATHON VOID FRAME 2024

![Screenshot 2024-10-16 at 18-44-54 Online Font Style Generator   Text Effects](https://github.com/user-attachments/assets/be0ba55d-73d3-4c52-b65f-ab2cadfe0c9b)


**SEC-MY_SITE** a.k.a SMS is a simple Flask-based web application that allows users to scan a domain for key security headers such as CSP (Content-Security-Policy), CSRF, CORS, and Host header protection.

## Features OF SMS
- Accepts domain input from the user.
- Scans the domain for the following headers:
  - **Content-Security-Policy (CSP)**: Checks if the Content-Security-Policy header is present.
  - **CSRF Token**: Checks for headers like X-CSRF-Token or X-Requested-With.
  - **CORS Protection**: Checks for the Access-Control-Allow-Origin header and whether it's set to restrict origins.
  - **Host Header Validation**: Provides a manual check for host header validation.

## Project Structure OF SMS
SEC-MY_SITE/
├── static/
│   └── style.css # Styling for the website
├── templates/
│   └── index.html # HTML template for the frontend
└── app.py         # Main Flask application

## Setup and Installation

### Clone the repository:
`git clone https://github.com/yourusername/SEC-MY_SITE.git`

`cd SEC-MY_SITE`

### Install the required dependencies:
`pip install -r requirements.txt`

### Run the Flask app:
`python app.py`

### Open your browser and go to:
`http://127.0.0.1:5000/`
