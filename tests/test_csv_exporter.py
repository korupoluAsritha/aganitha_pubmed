import unittest
import os
from src.pubmed.csv_exporter import export_to_csv # type: ignore

class TestCsvExporter(unittest.TestCase):

    def test_export_to_csv(self):
        # Sample data
        papers = [
            {"title": "Cancer Research", "authors": ["John Doe", "Jane Smith"], "journal": "Nature", "year": 2023},
            {"title": "COVID-19 Vaccine", "authors": ["Alice Brown"], "journal": "Science", "year": 2024}
        ]
        
        output_file = "test_output.csv"
        
        # Export to CSV
        export_to_csv(papers, output_file)

        # Check if the file is created
        self.assertTrue(os.path.exists(output_file))

        # Cleanup
        os.remove(output_file)


if __name__ == "__main__":
    unittest.main()
