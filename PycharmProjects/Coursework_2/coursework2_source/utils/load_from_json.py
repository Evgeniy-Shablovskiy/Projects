import json
from coursework2_source.configuration.development.load_env import posts_patch, comments_patch


def load_from_json(path):
    if path == posts_patch:
        with open(posts_patch, 'r', encoding='utf-8') as file:
            posts = json.load(file)
            return posts
    if path == comments_patch:
        with open(comments_patch, 'r', encoding='utf-8') as file:
            comments = json.load(file)
            return comments

