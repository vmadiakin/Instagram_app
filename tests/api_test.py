import requests
from utils import get_posts_all


def test_get_json_all_posts_type():
    response = requests.get("http://127.0.0.1:5000/api/posts")
    assert type(response.json()) == list


def test_get_json_all_posts_keys():
    response = requests.get("http://127.0.0.1:5000/api/posts")
    data = response.json()
    for d in data:
        assert d["poster_name"]
        assert d["poster_avatar"]
        assert d["pic"]
        assert d["content"]
        assert d["views_count"]
        assert d["likes_count"]
        assert d["pk"]


def test_get_json_post_by_id_dict():
    posts = get_posts_all()
    for post in posts:
        post_id = post["pk"]
        response = requests.get(f"http://127.0.0.1:5000/api/posts/{post_id}")
        assert type(response.json()) == dict


def test_get_json_post_by_id_keys():
    posts = get_posts_all()
    for post in posts:
        post_id = post["pk"]
        response = requests.get(f"http://127.0.0.1:5000/api/posts/{post_id}")
        assert response.json()["poster_name"]
        assert response.json()["poster_avatar"]
        assert response.json()["pic"]
        assert response.json()["content"]
        assert response.json()["views_count"]
        assert response.json()["likes_count"]
        assert response.json()["pk"]
