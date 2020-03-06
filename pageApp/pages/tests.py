from django.test import SimpleTestCase

# Create your tests here.

class SimpleTest(SimpleTestCase):
	"""docstring for SimpleTestCase"""
	def test_home_page_status_code(self):
		respuesta = self.client.get('/')
		self.assertEqual(respuesta.status_code,200)

	def test_about_page_status_code(self):
		respuesta = self.client.get('/about/')
		self.assertEqual(respuesta.status_code,200)


