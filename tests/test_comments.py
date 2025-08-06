import unittest
from app import app

class CommentAPITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.comment_data = {
            "text": "Test comment",
            "author": "Test user"
        }

    def test_create_comment(self):
        response = self.client.post('/comments', json=self.comment_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.get_json())

    def test_get_comments(self):
        response = self.client.get('/comments')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_update_comment(self):
        # First create
        post_res = self.client.post('/comments', json=self.comment_data)
        cid = post_res.get_json()['id']

        update_data = {"text": "Updated", "author": "Updated user"}
        response = self.client.put(f'/comments/{cid}', json=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['text'], "Updated")

    def test_delete_comment(self):
        # Create first
        post_res = self.client.post('/comments', json=self.comment_data)
        cid = post_res.get_json()['id']

        response = self.client.delete(f'/comments/{cid}')
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.get_json())

if __name__ == '__main__':
    unittest.main()