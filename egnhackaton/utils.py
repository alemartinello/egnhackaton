def get_api_key():
    """
    Read content of file `apikey.secret` and returns it as string
    """
    return open("apikey.secret", "r").read()
