from flask import Blueprint, render_template, request, current_app

page = Blueprint('page', __name__, static_folder='static', template_folder='templates')


@page.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        current_app.db.completions.insert_one({'name': name,
                                               'email': email,
                                               'message': message})
    completions = [(completion['message'], completion['email'], completion['name']) for completion in
                   current_app.db.completions.find({})]
    # entries = current_app.db.completions.find({})
    return render_template('index.html', completions=completions)
