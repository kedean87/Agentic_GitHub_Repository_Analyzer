import faiss
import numpy as np
from encoder import *

class Database:
	def __init__(self, texts):
		self.encoder = Encoder()
		self.texts = texts
		
		self.index = None
		self.vectors = None
	
	def build_vector_index(self):
		if self.index != None:
			return self.index, _
		
		dim = len(self.encoder.embed("test"))
		self.index = faiss.IndexFlatL2(dim)
		
		self.vectors = np.array([self.encoder.embed(t) for t in self.texts])
		self.index.add(self.vectors)
		
		return self.index, self.vectors
