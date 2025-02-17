import unittest
from coursework2_source.utils import get_posts_by_user, get_posts_all, all_comments, search_post, sort_, top, get_post_by_pk, load_from_json, get_comment_by_post


class TestFunctions(unittest.TestCase):
    def test_get_posts_by_user(self):
        self.assertIsInstance(get_posts_by_user('leo'), list)
