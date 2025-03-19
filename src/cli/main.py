import argparse
import logging

import sys
import os

# Add the src folder to Python's import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.pubmed.api_client import fetch_paper_ids, fetch_paper_details
from src.pubmed.csv_exporter import export_to_csv

def main():
    """Main CLI program to fetch and export PubMed research papers."""

    # Configure CLI arguments
    parser = argparse.ArgumentParser(description="Fetch and export PubMed research papers.")
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-f", "--file", type=str, default="papers.csv", help="Output CSV filename")

    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    try:
        logging.info(f"🔍 Searching for papers with query: {args.query}")

        # Fetch paper IDs
        paper_ids = fetch_paper_ids(args.query)
        if not paper_ids:
            logging.info("❌ No papers found.")
            return

        logging.info(f"✅ Found {len(paper_ids)} papers.")

        # Fetch paper details
        papers = fetch_paper_details(paper_ids)
        if not papers:
            logging.info("❌ No paper details found.")
            return

        # Export to CSV
        export_to_csv(papers, args.file)

        logging.info(f"✅ Results saved to {args.file}")

    except Exception as e:
        logging.error(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
