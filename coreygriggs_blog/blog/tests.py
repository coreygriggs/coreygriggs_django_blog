from django.test import TestCase
from .models import Post


# Create your tests here.
class CreatePostTest(TestCase):

	def setUp(self):
		Post.objects.create(title='testtesttest', slug='test_slug', description='blablablablbablah',
		            content='this is some test content')

	def test_create_test_adds_time(self):
		post = Post.objects.get(title='testtesttest', slug='test_slug', description='blablablablbablah',
		            content='this is some test content')
		self.assertIsNotNone(post.created)

	def test_create_test_adds_published(self):
		post = Post.objects.get(title='testtesttest', slug='test_slug', description='blablablablbablah',
		            content='this is some test content')
		self.assertIsNotNone(post.published)