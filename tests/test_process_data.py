import unittest

from process_data import process_data


class ProcessDataTests(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(
            process_data([]),
            {
                "count": 0,
                "total": 0,
                "average": 0,
                "minimum": None,
                "maximum": None,
                "sorted": [],
            },
        )

    def test_summarizes_and_sorts_values(self):
        self.assertEqual(
            process_data([3, 1, 4, 1, 5]),
            {
                "count": 5,
                "total": 14,
                "average": 2.8,
                "minimum": 1,
                "maximum": 5,
                "sorted": [1, 1, 3, 4, 5],
            },
        )

    def test_supports_float_values(self):
        self.assertEqual(
            process_data([1.5, 2.5]),
            {
                "count": 2,
                "total": 4.0,
                "average": 2.0,
                "minimum": 1.5,
                "maximum": 2.5,
                "sorted": [1.5, 2.5],
            },
        )


if __name__ == "__main__":
    unittest.main()
