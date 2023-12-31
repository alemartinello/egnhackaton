import json
import openai
import numpy as np
import pickle
from egnhackaton.utils import get_api_key


# openai.api_type = "azure"
# openai.api_base = "https://cs-openai-us-jml.openai.azure.com/"
# openai.api_version = "2023-05-15"
openai.api_key = f"{get_api_key()}"
print(get_api_key())


EMBEDDING_DTYPE = np.float32


def get_embedding_from_input(input: str) -> np.ndarray:
    """
    function to get embedding from openai

    Args:
            text (str): string to get embedding for (must be cleaned of punctuation)

    Returns:
            np.ndarray: numpy array of embedding
    """

    embedding = openai.Embedding.create(input=input, engine="text-embedding-ada-002")[
        "data"
    ][0]["embedding"]
    return np.array(embedding, dtype=EMBEDDING_DTYPE)


def process_batch_data(input_chunks):
    """
    Parameters
    ----
    input_chunks: dict

    """
    embeddings = []
    for chunk in input_chunks:
        embeddings.append(get_embedding_from_input(chunk["txt"]))
    return embeddings


def load_embeddings():
    embeddings = pickle.load(open("./embeddings.pckl", "rb"))
    return embeddings


def retrieve_from_indices(indices: list):
    """Given a list of row numbers, retrieve the relevant
    text snippets from the original tex
    """

    original_text = json.load(
        open("hackathon_data/queens_speeches/embeddings_data/datafile.json")
    )

    input_flat = original_text
    # for l in original_text:
    # 	for ll in l:
    # 		input_flat.append(ll)

    selected_statements = []

    for i in indices:
        selected_statements.append(input_flat[i]["txt"])
    return selected_statements


if __name__ == "__main__":
    import os
    import argparse

    parser = argparse.ArgumentParser("produce embeddings")
    parser.add_argument(
        "-i", "--input-json", help="name of json file", default="./example.json"
    )
    parser.add_argument(
        "-o", "--output", help="output pckl file", default="embeddings.pckl"
    )
    args = parser.parse_args()

    if os.path.isfile(args.output):
        embeddings = pickle.load(open(args.output, "rb"))
    else:
        input_data = json.load(open(args.input_json))
        input_flat = input_data
        # for l in input_data:
        # 	for ll in l:
        # 		input_flat.append(ll)

        embeddings = process_batch_data(input_flat)
        pickle.dump(embeddings, open(args.output, "wb"))
    for element in retrieve_from_indices([0, 1, 5]):
        print(element)
