from groq import Groq
from src.config import GROQ_API_KEY

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# ---------------- Prompt Builders ---------------- #


def build_zero_shot_prompt(topic):
    return f"""
You are an AI Learning Resource Recommender. 
Provide curated tutorials, documents, and example projects for the topic: {topic}.
Explain step by step how these resources are helpful.
Output as JSON array: {{topic, resource_type, link}}
"""


