import logging
import json
from flask import Flask, request, render_template, jsonify, redirect
from utils import get_comments_by_post_id, get_posts_all, get_post_by_pk, search_for_posts, get_posts_by_user, get_bookmarks, add_bookmarks, remove_bookmarks, find_bookmarks

logger_api = logging.getLogger()
console_handler = logging.StreamHandler()
file_handler_api = logging.FileHandler("logs/api.log", 'w', 'utf-8')
logger_api.addHandler(console_handler)
logger_api.addHandler(file_handler_api)
formatter_api = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/api/posts")
def get_json_all_posts():
    data = get_posts_all()
    logger_api.warning("Запрос всех постов JSON")
    return jsonify(data)


@app.route("/api/posts/<post_id>")
def get_json_post_by_id(post_id):
    post = get_post_by_pk(post_id)
    logger_api.warning(f"Запрос поста JSON по ID{post_id}")
    return jsonify(post)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/", methods=["GET"])
def main_page():
    posts = get_posts_all()
    bookmarks_count = len(get_bookmarks())
    return render_template('index.html', posts=posts, bookmarks_count=bookmarks_count)


@app.route("/post/id=<post_id>", methods=["GET"])
def page_post_form(post_id):
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    len_comments = len(comments)
    return render_template('post.html', post=post, comments=comments, len_comments=len_comments)


@app.route('/search', methods=["GET"])
def page_search():
    s = request.args.get("s").lower()
    searches = search_for_posts(s)[0:10]
    post_count = len(searches)
    return render_template('search.html', searches=searches, post_count=post_count)


@app.route("/users/<username>", methods=["GET"])
def get_posts_by_username(username):
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts)


@app.route("/bookmarks/add/<post_id>", methods=["GET"])
def page_add_bookmarks(post_id):
    add_bookmarks(post_id)
    return redirect("/", code=302)


@app.route("/bookmarks/remove/<post_id>", methods=["GET"])
def page_remove_bookmarks(post_id):
    remove_bookmarks(post_id)
    return redirect("/", code=302)


@app.route("/bookmarks/edit/<post_id>", methods=["GET"])
def page_edit_bookmarks(post_id):
    if find_bookmarks(post_id):
        return redirect(f"/bookmarks/remove/{post_id}", code=302)
    else:
        return redirect(f"/bookmarks/add/{post_id}", code=302)


@app.route("/bookmarks", methods=["GET"])
def page_bookmarks():
    posts = get_bookmarks()
    return render_template('bookmarks.html', posts=posts)


app.run()
