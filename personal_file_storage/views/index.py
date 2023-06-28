from flask import Blueprint, request, redirect, url_for, render_template, send_from_directory

# Handle requests from the account page
blueprint = Blueprint('index', __name__)


# To implement: Index page
@blueprint.route('/')
def index():
    return redirect(url_for('account.account'))


# Send requested css files
@blueprint.route('/css/<path:path>')
def serve_css(path):
    return send_from_directory('templates/css', path)


# Send requested js files
@blueprint.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory('templates/js', path)
