"""
"""
import numpy as np
import string
import egnhackaton.text_processing
import openai

# Setup azure openai
openai.api_type = "azure"
openai.api_base = "https://cs-openai-us-jml.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = "ff9de7d753b5443b9846bfb3de8e6edb"


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


def get_prompt(input, vector_database, closest=None):
    if closest is None:
        closest = 3

    # transform input in vector/embedding (Etienne)
    input_embedding = egnhackaton.text_processing.get_embedding_from_input(strip_input(input))

    # From vector find closest n vectors (Alessandro)
    closest_vectors_index = closest_vectors_indexes(input_embedding, vector_database, closest=closest)

    # Get text from vector index
    # evt think of string.join() ing it
    context = egnhackaton.text_processing.retrieve_from_indices(closest_vectors_index)
    context = " ".join([par[0] for par in context])

    # Construct prompt
    prompt = construct_prompt_to_chatgpt(input, context)
    return prompt


def get_response_real(input, vector_database, closest=None, temperature=0.1):
    """
    """
    prompt = get_prompt(input, vector_database, closest=None)
    # Send prompt to gpt
    answer = answer_question(prompt, temperature=temperature)
    
    # Return answer
    return answer['choices'][0]['message']['content']


def construct_prompt_to_chatgpt(input, context):
    prompt =  f"""
    Spørgsmalet er {input}.
    Dit contekst er udelukkende nytårstaler af dronning Margrete, og er {context}.
    Giv et kort svar. Finish the sentence with "GUD BEVARE DANMARK!"
    """.strip()
    return prompt


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

    return np.argpartition(similarities, -closest)[-closest:]


def answer_question(question:str, temperature=0.1) -> dict:
    """
    This function takes a question as input and returns a response generated by the OpenAI GPT engine.

    Args:
        question (str): Question to be answered

    Returns:
        dict: Raw response from azure openai
    """
    # Add system message to conversation
    selected_conversation_hist = [
        {
            "role": "system",
            "content": """You are a polite and helpful assistant having a conversation with a human.
            You are answering questions to the best of your ability.
            You are not trying to be funny or clever. You are trying to be helpful.
            You are not trying to show off.""".strip()
            },
        ]

    # Add question to conversation
    messages = selected_conversation_hist + [{"role": "user", "content":question}]

    raw_answer = openai.ChatCompletion.create(
        engine="gpt-35-turbo",
        messages=messages,
        temperature = temperature
    )

    return raw_answer
