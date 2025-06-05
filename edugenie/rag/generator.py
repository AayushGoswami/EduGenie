# generator.py
# Prompt template + LLM call

# edugenie/rag/generator.py

import os
import requests
from typing import List
from configparser import ConfigParser
from dotenv import load_dotenv

# Load environment variables (for GROQ_API_KEY)
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
LLM_MODEL = "llama3-8b-8192"  # Groq’s LLaMA 3 model

def build_prompt(context_chunks: List[str], question: str) -> str:
    context = "\n\n".join([chunk["content"] for chunk in context_chunks])
    prompt = f"""
    [INSTRUCTION]:
    You are a helpful science teacher. Use the information provided below to answer the question.
    Structure the answer in clear steps or paragraphs without repeating information.
    If the context has a process, explain it in logical, chronological order.
    
    [CONTEXT]:
    {context}

    [QUESTION]:
    {question}

    [ANSWER]:
    """
    return prompt.strip()

def generate_answer(context_chunks: List[str], question: str) -> str:
    prompt = build_prompt(context_chunks, question)

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": LLM_MODEL,
        "messages": [
            {"role": "system", "content": "You are an expert science tutor. Provide structured, concise answers based on provided text. No repetition or hallucination."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 512,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        raise Exception(f"Groq API error: {response.status_code} - {response.text}")
