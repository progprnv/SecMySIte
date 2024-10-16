from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    domain = request.form.get('domain')

    if not domain.startswith('http'):
        domain = 'https://' + domain

    try:
        response = requests.get(domain)
        headers = response.headers

        csp = "Present" if 'Content-Security-Policy' in headers else "Missing"
        csrf = "Present" if 'X-CSRF-Token' in headers or 'X-Requested-With' in headers else "Missing"
        cors = "Protected" if 'Access-Control-Allow-Origin' in headers and headers['Access-Control-Allow-Origin'] != '*' else "Not Protected"
        host_protected = "Host Header Protection not detected (manual check needed)"  # Custom logic if needed

        result = {
            'csp': csp,
            'csrf': csrf,
            'cors': cors,
            'host': host_protected,
        }
        return render_template('index.html', headers=result)

    except Exception as e:
        return f"Error scanning domain: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
