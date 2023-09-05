## Installing the environment

If you're using poetry

```
git clone git@github.com:alemartinello/egnhackaton.git
cd egnhackaton
poetry config virtualenvs.in-project true
poetry install
```

If not, you can manually set up the environment using the `requirements.txt` file

## Running MargretheGPT

1. Generate a file `apikey.secret` in the main folder where you copy your own OpenAI API key
2. run `poetry run streamlit run streamlitapp.py` or `streamlit run streamlitapp.py` if you are not using poetry
