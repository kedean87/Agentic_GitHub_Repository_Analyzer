# Agentic GitHub Repository Analyzer

# GitHub Search Summarization Agent

This repository contains a custom-built **GitHub Search Summarization Agent** implemented in Python, using a modular class-based architecture. The agent automatically:
- Searches GitHub repositories or code using user-defined queries
- Selects the **top-k most relevant** results
- Summarizes them using a **free Hugging Face LLM**
- Returns high-quality, concise insights suitable for research, documentation, or automation

The project demonstrates hands-on experience building agents, orchestrating LLM pipelines, integrating external APIs, and structuring production-ready Python code.

---

## 🚀 Features
- **Class-based architecture** for clarity and modularity
- **GitHub search integration** using `PyGithub`
- **Top-k ranking & filtering** to avoid unnecessary LLM calls
- **Hugging Face text generation pipeline** using a reliable, free model
- **Summarization agent** capable of multi-document reasoning
- Fully extensible for vector search, RAG, or custom scoring later

---

## 🧩 Project Structure
```
project/
 ├── github_agent.py       # Handles GitHub API search, retrieval, embeddings, database, top-k results, summarization
 ├── summarizer.py         # Wraps HuggingFace pipeline for summarization
 ├── database.py           # FAISS database of vector embeddings
 ├── encoder.py            # text encoder for embeddings
 ├── README.md             # This file
```

---

## 📦 Installation
```bash
pip install pygithub transformers torch
```

If running on CPU-only environment, select a lightweight Hugging Face model (e.g., `google-t5-small` or `facebook/bart-base`).

---

## ⚙️ Configuration
Set your GitHub personal access token:
```bash
export GITHUB_TOKEN="your_token_here"
```

---

## 🧠 How the Agent Works
### 1. **GitHub Search Module**
- Sends search queries to GitHub
- Retrieves repositories, code, or issues
- Ranks results based on:
  - GitHub relevance score
  - Star count (optional)
  - Text match priority
- Returns only the **top-k results** to reduce cost & processing

### 2. **Summarization Module**
Uses a Hugging Face model to summarize each selected result by:
- Cleaning result text
- Chunking if needed
- Producing a short insight-rich summary

### 3. **Agent Orchestration Layer**
Coordinates the entire pipeline:
- Accepts user query
- Runs GitHub search
- Chooses top-k items
- Summarizes them
- Combines output into a final aggregated response

---

## 🧪 Example Usage
```python
python github_agent.py

# or

ga = GithubAgent()
results = ga.run_agent(
  query="VTK Point Cloud Visualizer",
  search_n = 100,
  summarize_k = 3
  )
	
for r in results:
  print("-" * 80)
  print("Repository:", r["repo"])
  print("Similarity Score:", r["distance"])
  print("Summary:\n", r["summary"])
```

---

## 🔍 Example Output
The agent returns a structured summary like:
> "Across the top 3 results, the common classifiers used for fake news detection include Logistic Regression, SVMs, and LSTMs. Vectorization methods include TF-IDF and CountVectorizer. Most repos focus on preprocessing pipelines, feature extraction, and benchmark datasets such as LIAR."

---

## 🎯 Why This Project Matters
This repository demonstrates:
- Agent design patterns (modular, orchestrated pipelines)
- LLM integration with open‑source models
- API data fetching + ranking algorithms
- Practical production-quality Python organization
- Real-world automation using AI

This project can be extended into:
- RAG systems
- Code intelligence agents
- DevOps automation
- Research assistants

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **PyGithub** for repository/code search
- **Transformers** for HF inference
- **HuggingFace pipeline** (summarization)
- **top-k extraction** for optimized processing

---

## 📘 Future Enhancements
- Vector embeddings + semantic ranking
- Multi-hop summarization
- Integration with LangChain or LlamaIndex
- FastAPI endpoint for deployment
- UI dashboard with Streamlit

---


