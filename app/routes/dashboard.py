from flask import Blueprint, render_template

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# route for the home dashboard page
@bp.route('/')
def dash():
    return render_template('dashboard.html')

# route for user to edit a post
@bp.route('edit/<id>')
def edit(id):
    return render_template('edit-post.html')