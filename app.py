from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Homepage route
@app.route('/')
def index():
    alerts = []  # You can fetch from DB or leave empty for now
    return render_template('index.html', alerts=alerts)

# Upload route
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        logfile = request.files['logfile']
        if logfile:
            # Save or process the log here
            print(f"Received file: {logfile.filename}")
            return redirect(url_for('index'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
