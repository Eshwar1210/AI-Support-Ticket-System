import pandas as pd
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

df = pd.read_excel("support_tickets.xlsx")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_question(question):
    sample = df.head(50).to_string()
    prompt = f"""You are a support ticket analyst.

Dataset:
{sample}

Question:
{question}
"""
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
