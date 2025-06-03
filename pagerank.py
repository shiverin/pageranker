import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    result = {}
    cl = len(corpus)
    pl = len(corpus[page])
    if pl != 0:
        temp = damping_factor/pl
        for n in corpus[page]:
            result[n] = temp
        temp = (1-damping_factor)/cl
        for c in corpus:
            if c not in result:
                result[c] = temp
            else:
                result[c] += temp
    else:
        temp = 1/cl
        for c in corpus:
            result[c] = temp
    return result


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    count = {p: 0 for p in corpus}
    sample = random.choice(list(corpus.keys()))
    count[sample] += 1
    i = 1
    while i < n:
        pd = transition_model(corpus, sample, damping_factor)
        # Randomly pick next page based on probability distribution
        pages = list(pd.keys())
        weights = list(pd.values())
        sample = random.choices(pages, weights=weights, k=1)[0]
        count[sample] += 1
        i += 1
    res = {}
    for c in count:
        res[c] = count[c]/n
    return res


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    cl = len(corpus)
    res = {p: 1/cl for p in corpus}
    change = float('inf')
    while change > 0.001:
        change = 0
        newres = {}
        for page in corpus:
            new = (1-damping_factor)/cl
            for i in corpus:
                links = corpus[i]
                if links:
                    if page in links:
                        new += damping_factor*res[i]/len(corpus[i])
                else:
                    new += damping_factor*res[i]/cl
            change = max(change, new-res[page])
            newres[page] = new
        res = newres
    # Optional normalization (should already sum close to 1)
    total = sum(res.values())
    for page in res:
        res[page] /= total
    return res


if __name__ == "__main__":
    main()
