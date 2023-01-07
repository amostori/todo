from flask import Blueprint, render_template, request

page = Blueprint('page', __name__, static_folder='static', template_folder='templates')


@page.route('/', methods=['GET', 'POST'])
def index():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    data = {
        'name': name,
        'email': email,
        'message': message
    }
    print(data)
    return render_template('index.html')
