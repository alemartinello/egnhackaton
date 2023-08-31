import json
import openai
import numpy as np

# Setup azure openai
openai.api_type = "azure"
openai.api_base = "https://cs-openai-us-jml.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = "ff9de7d753b5443b9846bfb3de8e6edb"

EMBEDDING_DTYPE = np.float32

def generate_embedding(text:str) -> np.ndarray:
	"""
	function to get embedding from openai

	Args:
		text (str): string to get embedding for

	Returns:
		np.ndarray: numpy array of embedding
	"""

	embedding = openai.Embedding.create(input=text, engine='text-embedding-ada-002')['data'][0]['embedding']
	return np.array(embedding, dtype=EMBEDDING_DTYPE)


def process_batch_data(input_chunks):
	"""
	Parameters
	----
	input_chunks: dict

	"""
	embeddings = []
	for chunk in input_chunks:
		embeddings.append(generate_embedding(chunk['txt']))
	return embeddings


if __name__=='__main__':


	input_data = json.load(open('./example.json'))
	print(input_data['txt'])

	embeddings = process_batch_data([input_data])

	print(embeddings)
		