from .get_posts_all import get_posts_all


def get_posts_by_user(user_name):
    posts_by_user = []
    posts = get_posts_all()
    for post in posts:
        if user_name == post.poster_name:
            posts_by_user.append(post)
    if posts_by_user == []:
        raise ValueError("У пользователя нет ни одного поста")
    return posts_by_user
