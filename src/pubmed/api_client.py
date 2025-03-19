import requests
from typing import List, Dict, Any

# Base URL for PubMed API
PUBMED_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_paper_ids(query: str) -> List[str]:
    """Fetch paper IDs from PubMed API based on the user query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10  # Fetch up to 10 results (for testing)
    }

    response = requests.get(PUBMED_URL, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Error fetching paper IDs: {response.status_code}")
    
    data = response.json()
    paper_ids = data.get("esearchresult", {}).get("idlist", [])
    
    return paper_ids

def fetch_paper_details(paper_ids: List[str]) -> List[Dict[str, Any]]:
    """Fetch detailed information for each paper ID."""
    
    if not paper_ids:
        return []

    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }

    response = requests.get(SUMMARY_URL, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Error fetching paper details: {response.status_code}")

    data = response.json()
    result = data.get("result", {})
    
    papers = []
    
    for paper_id in paper_ids:
        paper_data = result.get(paper_id, {})
        
        paper = {
            "PubmedID": paper_id,
            "Title": paper_data.get("title", "N/A"),
            "Publication Date": paper_data.get("pubdate", "N/A"),
            "Authors": paper_data.get("authors", []),
            "Company Affiliation": "N/A",
            "Corresponding Author Email": "N/A"
        }

        # Mocking author data (since PubMed doesn’t always provide it)
        # Add sample company affiliation logic for testing
        if "pharma" in paper["Title"].lower() or "biotech" in paper["Title"].lower():
            paper["Company Affiliation"] = "Pharma Co."
            paper["Corresponding Author Email"] = "author@pharma.com"
        
        papers.append(paper)

    return papers
