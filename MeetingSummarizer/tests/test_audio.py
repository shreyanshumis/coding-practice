import unittest
from pathlib import Path
from types import SimpleNamespace

from backend.app.services.audio import prepare_for_transcription
from backend.app.services.transcription import normalize_segments


class AudioPreparationTests(unittest.TestCase):
    def test_supported_file_passes_through(self):
        source = Path("meeting.mp3")
        prepared, temporary = prepare_for_transcription(source)
        self.assertEqual(prepared, source)
        self.assertFalse(temporary)

    def test_groq_dictionary_segments_are_normalized(self):
        segments = normalize_segments([{"start": 1, "end": 2.5, "text": " Hello "}])
        self.assertEqual(segments, [{"start": 1.0, "end": 2.5, "text": "Hello", "speaker": None}])

    def test_attribute_segments_are_normalized(self):
        segments = normalize_segments([SimpleNamespace(start=3, end=4, text="World")])
        self.assertEqual(segments, [{"start": 3.0, "end": 4.0, "text": "World", "speaker": None}])


if __name__ == "__main__":
    unittest.main()
