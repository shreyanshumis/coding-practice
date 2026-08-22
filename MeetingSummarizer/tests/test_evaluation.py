import unittest

from backend.app.evaluation import word_error_rate


class EvaluationTests(unittest.TestCase):
    def test_exact_transcript(self):
        self.assertEqual(word_error_rate("Sarah will finish the API", "Sarah will finish the API"), 0)

    def test_deleted_word(self):
        self.assertEqual(word_error_rate("Sarah will finish the API", "Sarah will finish API"), 0.2)

    def test_normalization(self):
        self.assertEqual(word_error_rate("Hello, team!", "hello team"), 0)


if __name__ == "__main__":
    unittest.main()
