from github import Github
import requests
import re
import numpy as np

from summarizer import *
from database import *

class GithubAgent:
	def __init__(self, github_token="your_token_here"):
		self.github_token = github_token
		self.g = Github(self.github_token)
	
	def fetch_readme(self, repo):
		for branch in ["main", "master"]:
			url = f"https://raw.githubusercontent.com/{repo.full_name}/{branch}/README.md"
			r = requests.get(url)
			if r.status_code == 200:
				return r.text
		return ""
	
	def run_agent(self, query, search_n=1000, summarize_k=5):
		summarizer = Summarizer()

		repos = self.g.search_repositories(query, "stars", "desc")[:search_n]
		
		readmes = []
		repo_names = []

		# Fetch README but DO NOT summarize yet
		for repo in repos:
			text = self.fetch_readme(repo)
			readmes.append(text)
			repo_names.append(repo.full_name)
		
		database = Database(texts=readmes)
		
		index, _ = database.build_vector_index()
		
		q_vec = database.encoder.embed(query)
		distances, idxs = index.search(np.array([q_vec]), summarize_k)
		
		# Summarize ONLY top-k
		results = []
		for rank, repo_i in enumerate(idxs[0]):
			repo_name = repo_names[repo_i]
			readme_text = readmes[repo_i]
			results.append({
				"repo": repo_name,
				"distance": float(distances[0][rank]),
				"summary": summarizer.summarize_readme(text=readme_text)
			})

		return results

if __name__ == "__main__":
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
	
