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


class ViewsResponseTest(TestCase):

	def test_index(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_contact(self):
		response = self.client.get('/contact')
		self.assertEqual(response.status_code, 301)

	def test_blog(self):
		response = self.client.get('/blog')
		self.assertEqual(response.status_code, 301)

	def test_contact_thanks(self):
		response = self.client.get('/contact/thanks/')
		self.assertEqual(response.status_code, 200)

	def test_nonexistent_path(self):
		response = self.client.get('/fakepath')
		self.assertEqual(response.status_code, 404)