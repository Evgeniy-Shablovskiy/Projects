from coursework2_source.configuration.development.load_env import posts_patch
from .load_from_json import load_from_json
from coursework2_source.posts_and_comments.Posts import Posts
from .all_comments import all_comments


def get_posts_all():
    posts = load_from_json(posts_patch)
    posts_as_object = []
    comments = all_comments()
    for post in posts:
        post_as_object = Posts(poster_name=post['poster_name'], poster_avatar=post['poster_avatar'], pic=post['pic'], content=['content'], views_count=['views_count'], likes_count=['likes_count'], pk=['pk'])
        for comment in comments:
            if post_as_object.pk == comment.post_id:
                post_as_object.add_comment(comment)
        posts_as_object.append(post_as_object)
    return posts_as_object
