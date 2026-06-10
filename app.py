import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# OpenRouter Client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

# App Title
st.title("📚 AI Study Assistant")

# Notes Input
notes = st.text_area(
    "Paste your Notes Here",
    height=250
)

# ---------------------------
# SUMMARY GENERATOR
# ---------------------------

if st.button("Generate Summary"):

    prompt = f"""
    Summarize these notes in simple student-friendly language.

    Notes:
    {notes}
    """

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    st.subheader("📖 Summary")
    st.write(response.choices[0].message.content)

# ---------------------------
# QUIZ GENERATOR
# ---------------------------

if st.button("Generate Quiz"):

    prompt = f"""
    Create 10 multiple choice questions from these notes.

    Include answers at the end.

    Notes:
    {notes}
    """

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    st.subheader("📝 Quiz")
    st.write(response.choices[0].message.content)

# ---------------------------
# FLASHCARD GENERATOR
# ---------------------------

if st.button("Generate Flashcards"):

    prompt = f"""
    Create 10 flashcards from these notes.

    Format:

    Question:
    Answer:

    Notes:
    {notes}
    """

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    st.subheader("🎯 Flashcards")
    st.write(response.choices[0].message.content)

# ---------------------------
# ASK AI
# ---------------------------

st.subheader("🤖 Ask AI")

question = st.text_input(
    "Ask any topic-related question"
)

if st.button("Explain Topic"):

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    st.subheader("📚 Explanation")
    st.write(response.choices[0].message.content)