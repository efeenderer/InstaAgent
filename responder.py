from dotenv import load_dotenv
load_dotenv()
import os
from groq import Groq


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

# ---- Responder Class ----#
class Responder:
    def __init__(self):
        pass

    # ----  Intent Extractor    ----#
    @staticmethod
    def extract_intent(PROMPT = "Tell me your model name, version and the amount of weights.",message = "") -> str:

        chat = client.chat.completions.create(messages=[
                {
                    "role": "system",
                    "content": PROMPT
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            model="llama3-70b-8192",
            temperature=0,
            max_tokens=10)

        intent = chat.choices[0].message.content.lower().replace(" ","").replace(",","-")

        if intent not in ["price", "features", "notinterested", "other", "price-features", "features-other","price-other","price-features-other"]:
            intent = "other"


        return intent

    # ----  Respond    ----#
    # The required respond will be given according to the intent. If not required, LLM will not be used. Canned messages will be sent.
    @staticmethod
    def respond(self, intent:str) -> str:
        if "price" in intent:
            pass
        if "features" in intent:
            pass
        if "other" in intent:
            pass

examples = [
    ("Hi how much this one", "price"),
    ("Whats the price pls?", "price"),
    ("Is it like water proof and stuff?", "features"),
    ("Bro this ugly and way too much", "notinterested"),
    ("can u tell me more abt it", "features"),
    ("yo how much dis cost?", "price"),
    ("so expensive lol no thanks", "notinterested"),
    ("interested. msg me", "other"),
    ("hey can i come to ur shop", "other"),
    ("I need more infos", "features"),
    ("what do u even sell", "other"),
    ("give price pls and wats inside", "price-features"),
    ("ugly product sorry", "notinterested"),
    ("This looks cool ngl how much tho?", "price"),
    ("Can u explain how it works", "features"),
    ("i dont wanna buy just lookin", "notinterested"),
    ("looks clean! dm me", "other"),
    ("what is it good for? and cost?", "price-features"),
    ("u sell these in other colors?", "features"),
    ("lol nah not for me", "notinterested"),
    ("how do i use it?", "features"),
    ("Why is it this price??", "notinterested"),
    ("is that it or comes with more?", "features"),
    ("not interested", "notinterested"),
    ("heyyy looks nice", "other"),
    ("can u say whats included?", "features"),
    ("damn too much $$$", "notinterested"),
    ("where do i pickup", "other"),
    ("does it glow or smth?", "features"),
    ("do u deliver?", "other"),
    ("how to use and how much", "price-features"),
    ("can i visit or call u", "other"),
    ("looks cheap tbh", "notinterested"),
    ("is it strong? need price too", "price-features"),
    ("tell me what it do", "features"),
    ("you mad asking that price", "notinterested"),
    ("Just browsing ur page", "other"),
    ("u got better options?", "features"),
    ("wanna get one maybe", "other"),
    ("nope not for me", "notinterested"),
    ("Hey, do u have size options?", "features"),
    ("Hey I'm curious, what's the cost?", "price"),
    ("Shipping fee included?", "features"),
    ("ok but does it last long", "features"),
    ("why ppl buying this", "other"),
    ("what ur offer now?", "other"),
    ("Damn this overpriced as hell", "notinterested"),
    ("so how much total?", "price"),
    ("yo tell me features pls", "features"),
    ("got any bundle? and price?", "price-features"),
    ("is this only online or shop?", "other")
]

intent_prompt = f"""
You are an Instagram seller account owner.  
You are trying to understand the intent behind the customer’s DM or comment.  

You must output only the customer's *intent*, and nothing else. Your output must be *one or more* of the following, joined by a hyphen if needed:  
- price  
- features  
- notinterested  
- other  

*Rules:*  
- If the customer is *asking about the price*, you must say: `price`.  
- If the customer is *asking about the features*, you must say: `features`.  
- If the customer is *rude, uninterested, mocking*, or says they don’t want to buy, you must say: `notinterested`.  
- If a message includes signs of *both interest and rudeness*, you will still say only `notinterested`.  
- If the customer is *not asking* about price or features, you must say: `other`. This includes compliments, greetings, trying to make an appointment, or starting a conversation.  
- If a customer talks about price or features *without asking*, you must *ignore it* and say `other`.  

*Multiple Intents:*  
If the message clearly asks about more than one intent (e.g., both price and features), you can use a combination like `price-features`. Always use *hyphens*, never commas.

*Output Format:*  
Your output must include *only* the intent(s). Do *not* add extra words like “The intent is…” or any punctuation. Examples below:

*Examples:*  
- How much is this? → `price`  
- Can you tell me the features? → `features`  
- Too expensive for what it is. → `notinterested`  
- Hi, can we chat? → `other`  
- What's the content and price? → `price-features`  
- A friend of mine got it and loved it. → `other`  
- This is a terrible product. → `notinterested`  
- What's included in the box? → `features`  
- I'd like to visit and talk in person. → `other`  
- Looks good, but I’m not buying. → `notinterested`  
- It looks perfect. How much is it? If it's above 50 dollars, then go to hell! → `notinterested`  
- Looks fancy, but I doubt it's worth the money. How much? → `notinterested`  
- Can you tell me what it does and how much it is? → `price-features`  
- I liked the design. Hope it's not overpriced. → `other`  
- Just checking out your page. Nice work! → `other`  
- Why is this so damn expensive? → `notinterested`  
- Is it washable? And do you offer discounts? → `features-other`  
- What's the point of buying this crap? → `notinterested`  
- How do I use it? And where is the price listed? → `price-features`  

*Messy Examples with Grammar Issues:*  
- can u tell me more abt it → `features`  
- I need more infos → `features`  
- This looks cool ngl how much tho? → `price`  
- Can u explain how it works → `features`  
- i dont wanna buy just lookin → `notinterested`  
- u sell these in other colors? → `features`  
- how do i use it? → `features`  
- is it strong? need price too → `price-features`  
- tell me what it do → `features`  
- u got better options? → `features`  
- Hey, do u have size options? → `features`  
- Shipping fee included? → `features`  
- got any bundle? and price? → `price-features`  

"""

errors = ""

from time import sleep

correct = 0
for message, expected in examples:
    sleep(1.5)
    predicted = Responder.extract_intent(PROMPT=intent_prompt, message=message)
    is_correct = predicted == expected
    print(f"[{'+' if is_correct else '-'}] Expected: {expected} | Output: {predicted}")
    if is_correct:
        correct += 1
        continue
    errors += f"- {message} → {expected}\n"

accuracy = correct / len(examples)
print(f"Accuracy: {accuracy:.2%}")
print(f"\n\n{errors}")
