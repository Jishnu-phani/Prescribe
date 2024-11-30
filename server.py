from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('./home.html')

@app.route('/record')
def record():
    return render_template('/record.html')

@app.route('/register_doctor')
def register_doctor():
    return render_template('register_doctor.html')

@app.route('/register_patient')
def register_patient():
    return render_template('register_patient.html')

if __name__ == '__main__':
    app.run(debug=True)