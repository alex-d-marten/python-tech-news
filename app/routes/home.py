from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')

# route for hompage
@bp.route('/')
def index():
    return render_template('homepage.html')

# route for user to login
@bp.route('/login')
def login():
    return render_template('login.html')

# route for a single post by id
@bp.route('/post/<id>')
def single(id):
    return render_template('single-post.html')