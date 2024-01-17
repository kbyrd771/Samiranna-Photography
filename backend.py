from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Gallery')
def gallery():
    return render_template('pictures.html')

@app.route('/Services')
def services():
    return render_template('services.html')

@app.route('/About')
def about():
    render_template('lifestory.html')