from flask import Blueprint, request, redirect, url_for, render_template, send_from_directory
from ..models.account import sign_up, check_username, check_password

# Handle requests from the account page
blueprint = Blueprint('account', __name__)


# Account index page
@blueprint.route('/account')
def account():
    return render_template('account.html')


# Login request handler
@blueprint.route('/login', methods=['POST'])
def login():
    # Parse the username and password input from the request
    form = request.get_json()
    username = form['username']
    password = form['password']

    # If the number of users with the given username is not 1,
    # then there is an no such user in the database, return the error msg
    if check_username(username) != 1:
        return "Username doesn't exist."

    login_user = check_password(username, password)
    if len(login_user) != 1:
        return "Incorrect password"

    return redirect(url_for('account.account', token='To add'))


# Sign up request handler
@blueprint.route('/signup', methods=['POST'])
def signup():
    # Parse the username and password input from the request
    form = request.get_json()
    username = form['username']
    password = form['password']

    # If the number of users with the given username is not 0,
    # then this is a duplicated username, return the error msg
    if check_username(username) != 0:
        return "Username already existed."
    sign_up(username, password)

    return redirect(url_for('account.account'))


# Send requested css files
@blueprint.route('/css/<path:path>')
def serve_css(path):
    return send_from_directory('templates/css', path)


# Send requested js files
@blueprint.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory('templates/js', path)
