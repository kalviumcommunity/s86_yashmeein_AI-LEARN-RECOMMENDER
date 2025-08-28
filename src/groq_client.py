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

def build_one_shot_prompt(topic):
    return f"""
You are an AI Learning Resource Recommender.
Provide curated resources for the topic: {topic}.
Explain reasoning step by step.

Example:
Topic: React
Resources:
1) resource_type: Tutorial
   link: https://reactjs.org/tutorial
2) resource_type: Docs
   link: https://reactjs.org/docs/getting-started.html

Now generate resources for: {topic}
"""

def build_multi_shot_prompt(topic):
    return f"""
You are an AI Learning Resource Recommender.
Provide curated resources for the topic: {topic}.
Explain reasoning step by step.

Examples:
1) Topic: Docker
   Resources:
   - resource_type: Tutorial
     link: https://www.docker.com/get-started
   - resource_type: Docs
     link: https://docs.docker.com/

2) Topic: Kubernetes
   Resources:
   - resource_type: Tutorial
     link: https://kubernetes.io/docs/tutorials/
   - resource_type: Docs
     link: https://kubernetes.io/docs/home/

Now generate resources for: {topic}
"""
