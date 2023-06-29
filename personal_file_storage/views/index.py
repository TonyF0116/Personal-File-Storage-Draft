from flask import Blueprint, request, redirect, url_for, render_template, make_response
import jwt
from ..config import key

# Handle requests from the account page
blueprint = Blueprint('index', __name__)


# Empty URL redirected to /index
@blueprint.route('/')
def empty():
    return redirect(url_for('index.index'))


# Index page
@blueprint.route('/index')
def index():
    # Try get token from url args
    token = request.args.get('token')
    # Token not in url args
    if token == None:
        # If url doesn't contain token, then check whether token is in cookie
        token = request.cookies.get('token')
        # If not, redirect to account page, with the current url passed in
        if token == None:
            return redirect(url_for('account.account', redirect=request.url))
    # Token in url, put the token in cookie
    else:
        response = make_response(redirect(url_for('index.index')))
        response.set_cookie(key='token', value=token, path='/index')
        return response

    # Decode the token, if it expired, redirect to account page
    # If decode failed, render warning page
    try:
        jwt.decode(jwt=token, key=key, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return redirect(url_for('account.account', redirect=request.url))
    except jwt.DecodeError:
        return render_template('warning.html')

    return render_template('index.html')


# Called on Vue rendering the index page, sends the basic information of the user to the client
@blueprint.route('/index/get_data', methods=['POST'])
def get_data():
    token = request.cookies.get('token')
    payload = jwt.decode(jwt=token, key=key, algorithms=["HS256"])
    return payload['username']
