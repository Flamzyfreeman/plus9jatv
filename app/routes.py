import os
import secrets
from functools import wraps
from flask import render_template, url_for, redirect, request, flash, current_app
from app.models import Post, PostLike, User, Permission, Role
from flask_login import current_user, login_required
from app import app, db, bcrypt
from app.forms import AddPost


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, file_extention = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + file_extention
    picture_path = os.path.join(
        current_app.root_path, 'static/candidate_images', picture_fn)
    form_picture.save(picture_path)

    return picture_fn


def save_videos(video):
    hash_video = secrets.token_urlsafe(10)
    _, file_extention = os.path.splitext(video.filename)
    video_name = hash_video + file_extention
    file_path = os.path.join(current_app.root_path,
                             'static/videos', video_name)
    video.save(file_path)
    return video_name


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                #abort(403)
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)




@app.route('/')
def index():
   posts = Post.query.order_by(Post.pub_date.desc())
   return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>/<string:slug>', methods=['POST', 'GET'])
def post(post_id, slug):
   page = request.args.get('page', 1, type=int)
   post = Post.query.get_or_404(post_id)
   posts = Post.query.order_by(Post.pub_date.desc()).all()
   #  comments = Comment.query.filter_by(post_id=post.id).all()
   #  topic = Topic.query.all()
   #  topics = Topic.query.join(Post, (Topic.id == Post.topic_id)).all()
   post.views += 1
   db.session.commit()
   return render_template('single.html', post=post, posts=posts, title="Post")


@app.route('/addpost', methods=['POST'])
@login_required
@admin_required
def addpost():
   form = AddPost()
   if request.method == 'POST':
      title = form.title.data
      body = form.body.data
      #   topic = request.form.get('name')
      image = save_picture(form.picture.data)

      post = Post(title=title, body=body, image=image,  author=current_user)
      db.session.add(post)
      db.session.commit()
      flash('Your post has been publishes', 'success')
      return redirect(url_for('admin_panel'))
   return render_template('admin/create.html', title='Create Post', form=form)


@login_required
@admin_required
@app.route('/admin_panel')
def admin_panel():
    return render_template('admin/dashboard.html')
