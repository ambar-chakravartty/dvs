from flask import Blueprint, render_template, request, redirect, url_for, flash,jsonify
from flask_login import login_required, current_user
from .models import Post
from . import mongo
import datetime


import google.generativeai as genai

genai.configure(api_key='AIzaSyC4UajwizYkqWy0M38DP29DRAfgypGt9OM')
model = genai.GenerativeModel('models/gemini-pro')


bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    posts = Post.get_all_posts()
    return render_template('index.html', posts=posts)

@bp.route('/post/<post_id>')
def post(post_id):
    post = Post.get_post(post_id)
    if not post:
        flash('Post not found', 'danger')
        return redirect(url_for('routes.index'))
    return render_template('post.html', post=post)

@bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = current_user.username
        tags = []
        Post.insert_post(title, content,author,"")
        return redirect(url_for('routes.index'))
    return render_template('new_post2.html')


@bp.route('/new_error', methods=['GET', 'POST'])
@login_required
def new_error():
    if request.method == 'POST':
        title = request.form['title']
        error = request.form['error']
        tags = request.form['tags']
        
        author = current_user.username
        if not title or not error:
            flash('Title and Content are required', 'danger')
            return render_template('new_post.html')

        response = model.generate_content('Error Context : ' + title + 'Please help me with the following error ' + error)


   

        content = response.text

        Post.insert_post(title,content,author,tags)       
        flash('New post created successfully', 'success')
        return redirect(url_for('routes.index'))
    return render_template('new_post.html')


@bp.route('/delete_post/<post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.get_post(post_id)
    if not post:
        flash('Post not found', 'danger')
        return redirect(url_for('routes.index'))
    
    if post['author'] != current_user.username:
        flash('You are not authorized to delete this post', 'danger')
        return redirect(url_for('routes.index'))
    
    try:
        Post.delete_post(post_id)
        flash('Post deleted successfully', 'success')
    except Exception as e:
        flash(f'Error deleting post: {e}', 'danger')
    
    return redirect(url_for('routes.index'))
