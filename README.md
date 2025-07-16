# 🛍️ InstaIntent: AI-Powered Message Responder for Instagram Sellers

**InstaAgent** is a modular AI-powered system designed to help Instagram sellers automatically classify and respond to customer messages (DMs or comments), manage listings, and store all data in a relational database. It uses **LLaMA 3 70B via Groq API** for language understanding and is fully extensible.

---

## 🔧 Project Goals

1. **Intent Detection** ✅
2. **Canned Responses (based on intent)** 🔄
3. **Instagram Comment/DM Scraping** ✅ (basic version)
4. **Message Storage in PostgreSQL** ✅
5. **Automatic Response Dispatcher** 🔲
6. **Admin Dashboard / UI** 🔲
7. **Deployment & Hosting** 🔲

---

## 🤖 What It Does

- Classifies Instagram messages as:
  - `price`
  - `features`
  - `not interested`
  - `other`
- Uses Groq API and LLaMA 3 70B for high-quality understanding
- Responds automatically with rule-based or LLM-based replies *(planned)*
- Fetches **comments** from posts using [`instagrapi`](https://github.com/adw0rd/instagrapi)
- Saves messages, clients, and listings into a **PostgreSQL** database

---

##🗃️ Database
All customer messages, post metadata, and detected intents are stored in a PostgreSQL database.

🛠️ The full database schema and ER diagram will be added once development is complete.

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

## 📦 Dependencies
instagrapi – Used for fetching comments and DMs from Instagram

groq – Used to access LLaMA 3 70B models via the Groq API

psycopg2, SQLAlchemy – For interacting with PostgreSQL

python-dotenv – For environment variable management

## 🙌 Acknowledgements
This project uses the excellent instagrapi library to interact with Instagram's private API.
Special thanks to the contributors of that project for maintaining such a powerful tool.

## 🔒WARNING🔒

Ensure your .env file is listed in .gitignore to avoid exposing your GROQ_API_KEY publicly.
