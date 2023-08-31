import json
import openai
import numpy as np

# Setup azure openai
openai.api_type = "azure"
openai.api_base = "https://cs-openai-us-jml.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = "ff9de7d753b5443b9846bfb3de8e6edb"

EMBEDDING_DTYPE = np.float32

def get_embedding_from_input(input:str) -> np.ndarray:
	"""
	function to get embedding from openai

	Args:
		text (str): string to get embedding for (must be cleaned of punctuation)

	Returns:
		np.ndarray: numpy array of embedding
	"""

	embedding = openai.Embedding.create(input=input, engine='text-embedding-ada-002')['data'][0]['embedding']
	return np.array(embedding, dtype=EMBEDDING_DTYPE)


def process_batch_data(input_chunks):
	"""
	Parameters
	----
	input_chunks: dict

	"""
	embeddings = []
	for chunk in input_chunks:
		print(chunk)
		embeddings.append(get_embedding_from_input(chunk['txt']))
	return embeddings


def load_embeddings():
	embeddings = pickle.load(open('./embeddings.pckl','rb'))


def retrieve_from_indices(indices:list):
	"""Given a list of row numbers, retrieve the relevant
	text snippets from the original tex
	"""

	original_text = json.load(open('../../hackathon_data/queens_speeches/embeddings_data/datafile-18318495166876.json'))

	max_l = len(original_text[0])
	selected_statements = []

	for i in indices:
		selected_statements.append(original_text[0][i])
	return selected_statements


if __name__=='__main__':
	import os
	import argparse
	import pickle

	parser = argparse.ArgumentParser('produce embeddings')
	parser.add_argument('-i','--input-json', help='name of json file', default='./example.json')
	parser.add_argument('-o', '--output', help='output pckl file', default='embeddings.pckl')
	args = parser.parse_args()

	if os.path.isfile(args.output):
		embeddings = pickle.load(open(args.output, 'rb'))
	else:
		input_data = json.load(open(args.input_json))
		embeddings = process_batch_data(input_data[0])
		pickle.dump(embeddings, open(args.output,'wb'))
	for element in retrieve_from_indices([0,1,5]):
		print(element)