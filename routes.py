from flask import Blueprint, render_template, request, current_app

page = Blueprint('page', __name__, static_folder='static', template_folder='templates')


@page.route('/', methods=['GET'])
def index():
    messages = [(entry['name'], entry['message']) for entry in
                current_app.db.poems.find({})]
    return render_template('index.html', messages=messages, all_test=all_test)


@page.route('/submit_message', methods=['POST'])
def submit_message():
    name = request.form.get('name')
    message = request.form.get('message')
    current_app.db.poems.insert_one({'message': message, 'name': name})
    if name != '':
        response = f"""
        <h4>{name}</h4>
        <p>{message}</p>
        """
    else:
        response = f"""
                <p>{message}</p>
                """
    return response
