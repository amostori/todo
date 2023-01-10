from flask import Blueprint, render_template, request, current_app

page = Blueprint('page', __name__, static_folder='static', template_folder='templates')


@page.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        current_app.db.entries.insert_one({'name': name,
                                           'email': email,
                                           'message': message})
    entries = [(entry['message'], entry['email'], entry['name']) for entry in
               current_app.db.entries.find({})]
    all_test = current_app.db.entries.find({})
    return render_template('index.html', entries=entries, all_test=all_test)
