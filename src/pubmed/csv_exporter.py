# import csv
# from typing import List, Dict

# def export_to_csv(papers: List[Dict[str, str]], filename: str = "papers.csv") -> None:
#     """
#     Export the list of papers to a CSV file.
    
#     Args:
#         papers (List[Dict[str, str]]): List of research paper details.
#         filename (str): Name of the output CSV file.
#     """
#     if not papers:
#         print("No papers to export.")
#         return

#     # CSV headers
#     headers = [
#         "PubmedID",
#         "Title",
#         "Publication Date",
#         "Non-academic Author(s)",
#         "Company Affiliation(s)",
#         "Corresponding Author Email"
#     ]

#     try:
#         # Writing data to CSV file
#         with open(filename, mode='w', newline='', encoding='utf-8') as file:
#             writer = csv.DictWriter(file, fieldnames=headers)
#             writer.writeheader()

#             for paper in papers:
#                 writer.writerow({
#                     "PubmedID": paper.get("PubmedID", "N/A"),
#                     "Title": paper.get("Title", "N/A"),
#                     "Publication Date": paper.get("Publication Date", "N/A"),
#                     "Non-academic Author(s)": ", ".join(paper.get("Authors", [])),
#                     "Company Affiliation(s)": paper.get("Company Affiliation", "N/A"),
#                     "Corresponding Author Email": paper.get("Corresponding Author Email", "N/A")
#                 })

#         print(f"✅ CSV file saved successfully: {filename}")

#     except Exception as e:
#         print(f"❌ Error exporting CSV: {e}")

import csv
import json
import logging

def export_to_csv(papers, filename):
    """
    Export paper details to a CSV file.
    Handles mixed data types by converting them to JSON strings.
    """
    try:
        # Open CSV file for writing
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=papers[0].keys())
            writer.writeheader()

            for paper in papers:
                # Normalize values to strings
                normalized_paper = {k: json.dumps(v) if isinstance(v, (dict, list)) else str(v) for k, v in paper.items()}
                writer.writerow(normalized_paper)

        logging.info(f"✅ CSV exported successfully to {filename}")

    except Exception as e:
        logging.error(f"❌ Error exporting CSV: {e}")
