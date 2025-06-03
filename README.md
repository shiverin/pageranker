# 📄 PageRanker in Python

This project implements a **PageRank algorithm**, a common technique in search engine technology, to rank webpages based on their importance within a network. Inspired by the original algorithm used by Google, this Python project processes a corpus of HTML files, extracts their internal links, and computes PageRank scores using two core probability-based methods.

---

## 📂 Corpus Crawler

The program first parses a directory of HTML files to build a **link graph**. It extracts all internal hyperlinks and constructs a mapping of which pages link to which. This forms the basis of the web structure that the PageRank algorithm operates on.

---

## 🧠 PageRank Using Probability-Based Methods

This project implements two core probability-driven methods to rank webpages by importance:

### 1. Sampling Method (Monte Carlo Simulation)

- Simulates a "random surfer" who visits pages according to a transition probability model.
- At each step, the next page is chosen either from the current page’s links (with probability *d*) or uniformly at random from the entire corpus (with probability *1 - d*).
- After a large number of samples (*n = 10,000*), the PageRank of each page is estimated as the proportion of visits.
- This method applies stochastic sampling and probability distributions to approximate steady-state behavior.

### 2. Iterative Method (Power Iteration)

- Initializes all pages with equal rank and updates them iteratively.
- At each iteration, a page’s new rank is computed as the weighted sum of contributions from all pages linking to it, accounting for the damping factor.
- Iterations continue until rank changes fall below a small threshold (convergence).
- This deterministic method uses concepts from Markov chains and transition matrices to compute the stationary distribution.

Both methods reflect foundational principles in **probability theory**, including random processes, expected value estimation, and matrix convergence behavior.

---

## ⚙️ How It Works

1. **Input**: A folder of `.html` files representing the website corpus.
2. **Parsing**: Internal links are extracted to construct a directed graph of pages.
3. **Transition Model**: Built for each page based on the damping factor (default: 0.85).
4. **Sampling or Iteration**: PageRanks are calculated using either:
   - `sample_pagerank(corpus, damping_factor, n)`
   - `iterate_pagerank(corpus, damping_factor)`
5. **Output**: Ranks of each page printed with values summing to 1.

---

## 📈 Example Output
Iterative PageRank Results:
2.html: 0.4289
1.html: 0.2202
3.html: 0.2202
4.html: 0.1307

Sampled PageRank Results:
2.html: 0.4294
1.html: 0.2232
3.html: 0.2196
4.html: 0.1278

## 🛠️ Tech Stack

- **Language**: Python 3
- **Libraries**: `os`, `re`, `random`, `sys`
- **Concepts**: Monte Carlo Simulation, Markov Chains, Transition Matrices, Probability Distributions

---

## 🚀 Learning Outcomes

- Practical application of probability theory.
- Deepened understanding of stochastic modeling and convergence in probabilistic systems.
- Gained experience implementing and comparing Monte Carlo and iterative algorithms.

---

## 📁 Directory Structure
```
pageranker/
│
├── pagerank.py # Main PageRank implementation
├── parse.py # HTML parsing utilities
├── runner.py # Script to run and test the pagerank pipeline
├── corpus0/ # Corpus directory 0 with HTML pages
├── corpus1/ # Corpus directory 1 with HTML pages
├── corpus2/ # Corpus directory 2 with HTML pages
└── README.md # Project documentation
```
