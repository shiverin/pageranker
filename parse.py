import os
import re
from bs4 import BeautifulSoup

def crawl_corpus(folder_path):
    """
    Given a folder path containing HTML files,
    returns a dictionary mapping each file to the set of pages
    it links to (only links to pages in the folder).
    """
    corpus = {}

    # List all HTML files in the folder
    files = set(os.listdir(folder_path))

    # Filter only .html files for safety
    html_files = {f for f in files if f.endswith(".html")}

    for filename in html_files:
        filepath = os.path.join(folder_path, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            contents = f.read()

            # Parse HTML and extract links
            soup = BeautifulSoup(contents, "html.parser")
            links = set()

            for a_tag in soup.find_all("a", href=True):
                href = a_tag['href']

                # Only consider links to other html files in the corpus folder
                if href in html_files:
                    links.add(href)

            corpus[filename] = links

    return corpus
