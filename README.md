# s86_yashmeein_AI-LEARN-RECOMMENDER
# AI Learning Resource Recommender for Developers

## **Project Overview**

The **AI Learning Resource Recommender** is an AI-powered platform that helps developers quickly find high-quality tutorials, documentation, and example projects for any skill or topic. By simply entering a developer topic (e.g., React, Kubernetes, Node.js), the AI generates curated learning resources with explanations and structured output.

This tool is designed to save time for developers, improve learning efficiency, and provide step-by-step reasoning for why each resource is recommended.

---

## **Features**

* **Zero-Shot Prompting:** Generate resource recommendations without examples.
* **One-Shot Prompting:** Guide AI using a single example resource.
* **Multi-Shot Prompting:** Guide AI using multiple example resources.
* **Chain of Thought:** AI explains reasoning before generating recommendations.
* **Dynamic Prompting:** Recommendations are tailored to the user’s input topic.
* **Structured Output:** JSON format `{topic, resource_type, link}` for easy parsing.
* **LLM Features:** Adjustable temperature, Top P/K, stop sequences for creative responses.
* **Token Logging:** Track token usage per AI call for cost and efficiency monitoring.

---

## **Tech Stack**

* **Backend & AI Integration:** Python, Groq LLM
* **Frontend/UI:** Streamlit
* **Environment Management:** Python-dotenv for API keys

---

## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ai-learning-recommender.git
cd ai-learning-recommender
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## **Usage**

Run the Streamlit app:

```bash
streamlit run app.py
```

* Enter a developer topic or skill in the input field.
* Choose **prompt type**: Zero-Shot, One-Shot, Multi-Shot.
* Enable **streaming mode** if you want to see responses generated in real-time.
* The AI outputs structured JSON recommendations with topic, resource type, and link.

### **Sample Topics**

* React
* Kubernetes
* Node.js
* Docker
* Python Async Programming

---

## **Folder Structure**

```
AI-Learning-Recommender/
│-- app.py
│-- README.md
│-- requirements.txt
│-- .env
│-- src/
    │-- config.py
    │-- groq_client.py
    │-- utils.py
```

---

## **8 GenAI Concepts Covered**

1. **Create Project Readme** – Explains project idea, setup, and usage.
2. **System and User Prompt** – AI system role defined, user input provided.
3. **Zero-Shot Prompting** – Generate recommendations without examples.
4. **One-Shot Prompting** – Generate recommendations with a single example.
5. **Multi-Shot Prompting** – Generate recommendations with multiple examples.
6. **Chain of Thought Prompting** – AI explains reasoning before output.
7. **Tokens and Tokenization** – Logs token usage for efficiency tracking.
8. **LLM Features (Temperature, Top P/K, Stop Sequence, Structured Output)** – Adjust creativity, randomness, stopping criteria, and structured output format.

---

## **License**

MIT License
