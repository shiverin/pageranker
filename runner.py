from parse import crawl_corpus
from pagerank import iterate_pagerank, sample_pagerank

folder_path = "/workspaces/200508238/cs50ai/week2/pagerank/corpus1"

corpus = crawl_corpus(folder_path)

damping_factor = 0.85
samples = 10000  # Number of samples to take for sample_pagerank

# Run iterative PageRank
pagerank_iter = iterate_pagerank(corpus, damping_factor)
print("Iterative PageRank Results:")
for page, rank in pagerank_iter.items():
    print(f"{page}: {rank:.4f}")

print("\nSampled PageRank Results:")
# Run sample PageRank
pagerank_sample = sample_pagerank(corpus, damping_factor, samples)
for page, rank in pagerank_sample.items():
    print(f"{page}: {rank:.4f}")
