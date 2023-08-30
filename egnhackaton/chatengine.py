"""
"""
import numpy as np


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
