from flask import Blueprint
from flask import render_template, request, Blueprint
from main.models import Post

general = Blueprint('general', __name__)


@general.route("/")  # these are decorators
@general.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('home.html', posts=posts)


@general.route("/about")
def about():
    return render_template('about.html', title='about')


