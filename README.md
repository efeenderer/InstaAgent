# 🛍️ InstaIntent: AI-Powered Intent Classifier for Instagram Sellers

This project is a lightweight yet powerful Python-based AI responder that helps Instagram seller accounts automatically classify customer messages into actionable intents using LLaMA 3 70B via the Groq API.

---

## ✨ Features

- 📥 Handles incoming **DMs or comments**
- 🔍 Classifies messages into these four intents:
  - `price`
  - `features`
  - `not interested`
  - `other`
- 🤖 Uses **LLaMA 3 70B** through Groq API for accurate natural language understanding
- 🧠 Smart logic to prioritize `not interested` even if other intents are present
- 🔧 Easy to extend with canned responses or message routing logic

---

## 🧠 Example Intents

| Message | Intent |
|--------|--------|
| "How much is this?" | `price` |
| "Is it washable?" | `features` |
| "Too expensive. Bye." | `not interested` |
| "Can we talk?" | `other` |
| "What's the content and price?" | `price-features` |
| "Overpriced crap. No thanks." | `not interested` |

---

## 🚀 Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Add your Groq API key in a `.env` file
echo "GROQ_API_KEY=your_key_here" > .env
```

## 🔒WARNING🔒

Ensure your .env file is listed in .gitignore to avoid exposing your GROQ_API_KEY publicly.
