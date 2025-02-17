from coursework2_source.configuration.development.load_env import comments_patch
from .load_from_json import load_from_json
from coursework2_source.posts_and_comments.Comments import Comments


def all_comments():  # возвращает список объектов класса Comments
    comments = load_from_json(comments_patch)
    comments_as_object = []
    for comment in comments:
        comment_as_object = Comments(post_id=comment['post_id'], commenter_name=comment['commenter_name'], comment=comment['comment'], pk=comment['pk'])
        comments_as_object.append(comment_as_object)
    return comments_as_object
