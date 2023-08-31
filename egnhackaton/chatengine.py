"""
"""
import numpy as np
import string


def get_api_key():
    """
    Read content of file `apikey.secret` and returns it as string
    """
    return open("apikey.secret", "r").read()


def get_response(input):
    if np.random.random()>0.5:
        return "Cool stuff"
    else:
        return "Meh..."


def get_response_real(input, vector_database, closest=None):
    if closest is None:
        closest = 3

    # transform input in vector/embedding (Etienne)
    input_embedding = get_embedding_from_input(strip_input(input))

    # From vector find closest n vectors (Alessandro)
    closest_vectors_index = closest_vectors_indexes(input_embedding, vector_database, closest=closest)

    # Get text from vector index

    # Construct prompt

    # Send prompt to gpt
    
    # Return answer

    return


def strip_input(input):
    return input.translate(str.maketrans('', '', string.punctuation)).strip()


def get_embedding_from_input(input):
    # Etienne
    input_embedding = None
    return input_embedding


def cosine_similarity(input, vector):
    cos_sim = np.dot(input, vector)/(np.linalg.norm(input)*np.linalg.norm(vector))
    return cos_sim

def closest_vectors_indexes(input, db, closest=None):
    if closest is None:
        closest = 3
    similarities = np.array([cosine_similarity(input, i) for i in db])

    return np.argpartition(similarities, -2)[-2:]
