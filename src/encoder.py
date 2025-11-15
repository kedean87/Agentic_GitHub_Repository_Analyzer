from sentence_transformers import SentenceTransformer

class Encoder:
	def __init__(self, name="all-MiniLM-L6-v2"):
		self.encoder = SentenceTransformer(name)
	
	def embed(self, text):
		return self.encoder.encode([text])[0]
