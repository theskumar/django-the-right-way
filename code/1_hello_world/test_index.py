from django.test import SimpleTestCase


class IndexPageTest(SimpleTestCase):
    def test_get_index(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response.content, 'Hello World')
        self.assertIn(response.content, "Hello World")
