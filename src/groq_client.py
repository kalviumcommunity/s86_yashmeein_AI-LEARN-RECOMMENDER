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


# ---------------- LLM Call ---------------- #



def get_ai_response(prompt, stream=False):
    if stream:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
            stop=None
        )
        response_text = ""
        for chunk in completion:
            delta = getattr(chunk.choices[0], "delta", None)
            if delta and getattr(delta, "content", None):
                content = delta.content
                print(content, end="", flush=True)
                response_text += content
        print()
        return response_text
    else:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_completion_tokens=1024,
            top_p=1
        )
        tokens_used = response.usage.total_tokens
        print(f"Tokens used: {tokens_used}")
        return response.choices[0].message.content
    
    

    
    
