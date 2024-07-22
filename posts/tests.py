from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testusername',
            email='tets@email.com',
            password='testpass',
        )

        cls.post = Post.objects.create(
            title='testtitle',
            body='testbody',
            author=cls.user
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'testusername'),
        self.assertEqual(self.post.title, 'testtitle')
        self.assertEqual(self.post.body, 'testbody')
        self.assertEqual(str(self.post), 'testtitle')