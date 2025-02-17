from .get_posts_all import get_posts_all


def get_comment_by_post(post_id):
    posts = get_posts_all()
    for post in posts:
        if post.pk == post_id:
            return post.get_comments()
    raise ValueError("У пользователя нет ни одного поста")
