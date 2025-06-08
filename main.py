from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/service/')
def service():
    return render_template('services.html')

@app.route('/portfilo/')
def portfilo():
    return render_template('portfilo.html')

@app.route('/project/')
def project():
    return render_template('project.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/aftersumbit/', methods = ['GET','POST'])
def aftersumbit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        return f"{name},{email},{phone},{message}"
    else:
        return render_template('contact.html')

