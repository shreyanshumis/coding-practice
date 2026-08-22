import unittest

from fastapi.testclient import TestClient

from backend.app.main import app


class ApiTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")
        self.assertEqual(response.json()["provider"], "groq")
        self.assertIn("groq_configured", response.json())

    def test_meeting_list(self):
        response = self.client.get("/api/meetings")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)


if __name__ == "__main__":
    unittest.main()
