import streamlit as st
from streamlit_chat import message
import egnhackaton.chatengine
import egnhackaton.text_processing

st.title("Welcome to MargretheGPT!")

st.image("dronning-margrethe-nytar.jpg")

# See https://github.com/AI-Yash/st-chat/blob/main/examples/chatbot.py for inspiration

temperature = st.slider("Margrethes humør", min_value=0.0, max_value=1.0, value=0.1)

db = egnhackaton.text_processing.load_embeddings()


if "input_field" not in st.session_state:
    st.session_state.input_field = ""

if "input" not in st.session_state:
    st.session_state.input = ""

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "history" not in st.session_state:
    st.session_state["history"] = []


def on_btn_click():
    del st.session_state.history[:]
    del st.session_state.generated[:]
    del st.session_state.input


def submit():
    st.session_state.input = st.session_state.input_field
    st.session_state.input_field = ""


def get_text():
    with st.container():
        st.text_input("You: ", "", key="input_field", on_change=submit)
    return st.session_state.input


user_input = get_text()


st.button("Clear chat", on_click=on_btn_click)


if user_input:
    output = egnhackaton.chatengine.get_response_real(user_input, db, temperature=temperature)

    st.session_state.history.append(user_input)
    st.session_state.generated.append(output)


if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i), seed=1)
        message(
            st.session_state["history"][i],
            is_user=True,
            key=str(i) + "_user",
            avatar_style="adventurer",
            seed="diocan",
        )
