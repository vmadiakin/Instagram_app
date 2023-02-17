import json
import regex


def get_posts_all():
    try:
        with open("data/posts.json", "r", encoding="utf8") as file:
            posts = json.load(file)
            # tags_posts = add_tag(posts)
            return posts
    except FileNotFoundError:
        return "Отсутствует файл posts.json"


def get_posts_by_user(user_name):
    with open("data/posts.json", "r", encoding="utf8") as file:
        posts = json.load(file)
        user_posts = []
        for post in posts:
            if post["poster_name"].lower() == user_name.lower():
                user_posts.append(post)
        return user_posts


def get_comments_by_post_id(post_id):
    with open("data/posts.json", "r", encoding="utf8") as file1:
        posts = json.load(file1)
        if f"{post_id}".isdigit():
            for post in posts:
                if int(post_id) == int(post["pk"]):
                    with open("data/comments.json", "r", encoding="utf8") as file2:
                        comments = json.load(file2)
                        comments_by_post_id = []
                        for comment in comments:
                            if int(post_id) == int(comment["post_id"]):
                                comments_by_post_id.append(comment)
                        return comments_by_post_id
            raise ValueError("Нет поста с таким ID")
        else:
            raise ValueError("Вы ввели недопустимое значение")


def search_for_posts(query):
    with open("data/posts.json", "r", encoding="utf8") as file:
        posts = json.load(file)
        query_posts = []
        for post in posts:
            if query.lower() in post["content"].lower():
                query_posts.append(post)
        return query_posts


def get_post_by_pk(pk):
    with open("data/posts.json", "r", encoding="utf8") as file:
        posts = json.load(file)
        # posts = add_tag(posts_all)
        if f"{pk}".isdigit():
            for post in posts:
                if int(pk) == int(post["pk"]):
                    return post
            raise ValueError("Нет поста с таким ID")
        else:
            raise ValueError("Вы ввели недопустимое значение")


def get_bookmarks():
    try:
        with open("data/bookmarks.json", "r", encoding="utf8") as file:
            bookmarks = json.load(file)
            return bookmarks
    except FileNotFoundError:
        return "Отсутствует файл bookmarks.json"


def add_bookmarks(post_id):
    bookmarks = get_bookmarks()
    post = get_post_by_pk(post_id)
    bookmarks.append(post)
    with open("data/bookmarks.json", "w", encoding="utf8") as file:
        json.dump(bookmarks, file, ensure_ascii=False)


def remove_bookmarks(post_id):
    bookmarks = get_bookmarks()
    for bookmark in bookmarks:
        if int(bookmark['pk']) == int(post_id):
            bookmark_index = bookmarks.index(bookmark)
            bookmarks.pop(bookmark_index)
    with open("data/bookmarks.json", "w", encoding="utf8") as file:
        json.dump(bookmarks, file, ensure_ascii=False)


def find_bookmarks(post_id):
    bookmarks = get_bookmarks()
    for bookmark in bookmarks:
        if int(bookmark["pk"]) == int(post_id):
            return True
    return False


# def add_tag(posts_list):
#     tags_posts = []
#     for posts in posts_list:
#         content = posts["content"]
#         new_str = ''
#         if '#' in content:
#             for word in content.split(' '):
#                 if "#" in word:
#                     new_str += ' ' + f'</p><p><a href="/tag/{word[1:]}">#{word[1:]}</a></p><p>'
#                 else:
#                     new_str += ' ' + word
#             new_obj = {
#                 "poster_name": posts["poster_name"],
#                 "poster_avatar": posts["poster_avatar"],
#                 "pic": posts["pic"],
#                 "content": new_str.strip(),
#                 "views_count": posts["views_count"],
#                 "likes_count": posts["likes_count"],
#                 "pk": posts["pk"]
#             }
#             tags_posts.append(new_obj)
#         else:
#             tags_posts.append(posts)
#     return tags_posts



