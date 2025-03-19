import unittest
from src.pubmed.api_client import fetch_paper_ids, fetch_paper_details # type: ignore


class TestApiClient(unittest.TestCase):

    def test_fetch_paper_ids(self):
        paper_ids = fetch_paper_ids("cancer therapy")
        self.assertIsInstance(paper_ids, list)
        self.assertGreater(len(paper_ids), 0)

    def test_fetch_paper_details(self):
        paper_ids = ["38011978", "38011979"]
        details = fetch_paper_details(paper_ids)
        self.assertIsInstance(details, list)
        self.assertGreater(len(details), 0)


if __name__ == "__main__":
    unittest.main()
