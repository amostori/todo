from flask import Blueprint, render_template, request, current_app

page = Blueprint('page', __name__, static_folder='static', template_folder='templates')


@page.route('/', methods=['GET'])
def index():
    messages = [entry['message'] for entry in
                current_app.db.entries.find({})]
    all_test = current_app.db.entries.find({})
    return render_template('index.html', messages=messages, all_test=all_test)


@page.route('/submit_message', methods=['POST'])
def submit_message():
    message = request.form.get('message')
    current_app.db.entries.insert_one({'message': message})
    response = f"""
    <li>{message}</li>
    """
    return response
