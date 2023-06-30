from flask import Blueprint, request, redirect, url_for, render_template

# Handle requests from the account page
blueprint = Blueprint('edit', __name__)


# Edit page
@blueprint.route('/edit')
def edit():
    return render_template('edit.html')
