from flask import Blueprint, request, redirect, url_for, render_template, make_response
from ..models.account import sign_up, check_username, check_password
from ..config import key
import jwt
from datetime import datetime, timedelta, timezone

# Handle requests from the account page
blueprint = Blueprint('account', __name__)


# Account index page
@blueprint.route('/account')
def account():
    # Check current token in cookie
    token = request.cookies.get('token')
    # If token exist, decode the token
    if token != None:
        try:
            jwt.decode(jwt=token, key=key, algorithms=["HS256"])
        # If successfully decoded, redirect back with the token added as a arg
        except jwt.ExpiredSignatureError:
            pass
        except jwt.DecodeError:
            pass
        else:
            return redirect(request.args.get('redirect')+'?token={}'.format(token))

    return render_template('account.html')


# Login request handler
@blueprint.route('/account/login', methods=['POST'])
def login():
    # Parse the username and password input from the request
    form = request.get_json()
    username = form['username']
    password = form['password']

    # If the number of users with the given username is not 1,
    # then there is an no such user in the database, return the error msg
    if check_username(username) != 1:
        return "Username doesn't exist."

    # Login using the given username and password
    login_user = check_password(username, password)

    # If matched user found is not 1, then the input doesn't match, return the error msg
    if len(login_user) != 1:
        return "Incorrect password"

    # Login successful, build JWT token
    token_info = {"accountid": login_user[0][0],
                  "username": login_user[0][1],
                  "administrator": login_user[0][3],
                  "exp": datetime.now(tz=timezone.utc) + timedelta(hours=1),
                  "nbf": datetime.now(tz=timezone.utc)}
    token = jwt.encode(payload=token_info, key=key, algorithm="HS256")

    # Make redirect response if passed in url has redirect attribute
    if request.args.get('redirect') != None:
        response = make_response(
            redirect(request.args.get('redirect')+'?token={}'.format(token)))
        print('ran')
    else:
        response = make_response(
            redirect(url_for('index.index', token=token)))

    # Set cookie for account page
    response.set_cookie(key='token', value=token, path='/account')

    return response


# Sign up request handler
@blueprint.route('/account/signup', methods=['POST'])
def signup():
    # Parse the username and password input from the request
    form = request.get_json()
    username = form['username']
    password = form['password']

    # If the number of users with the given username is not 0,
    # then this is a duplicated username, return the error msg
    if check_username(username) != 0:
        return "Username already existed."

    # Sign up using the given username and password
    sign_up(username, password)

    return redirect(url_for('account.account'))
