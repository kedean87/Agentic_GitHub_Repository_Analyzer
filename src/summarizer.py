from transformers import pipeline
import re

class Summarizer:
	def __init__(self, model_name="google/flan-t5-large", max_tokens=1024, temperature=0.2):
		self.summarizer = pipeline(
			"text2text-generation",
			model=model_name,
			max_new_tokens=max_tokens,
			temperature=temperature
			)
	
	def summarize_readme(self, text):
		if not text.strip():
			return "No README available."

		cleaned = re.sub(r"[#>*`]", "", text)

		prompt = (
			"Summarize this GitHub README into 5 concise bullet points focusing on: "
			"purpose, key features, architecture, and intended use.\n\n"
			+ cleaned
		)

		try:
			output = self.summarizer(prompt)[0]["generated_text"]
			return output
		except Exception as e:
			return f"Summary failed: {e}"
