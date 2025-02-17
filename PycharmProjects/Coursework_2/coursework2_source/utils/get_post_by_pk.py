from .get_posts_all import get_posts_all


def get_post_by_pk(pk):
    posts = get_posts_all()
    for post in posts:
        if post.pk == pk:
            return post
