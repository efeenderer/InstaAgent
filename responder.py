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
    ("Looks fancy, but I doubt it's worth the money. How much?", "notinterested"),
    ("Can you tell me what it does and how much it is?", "price-features"),
    ("I liked the design. Hope it's not overpriced.", "other"),
    ("Just checking out your page. Nice work!", "other"),
    ("Why is this so damn expensive?", "notinterested"),
    ("Is it washable? And do you offer discounts?", "features-other"),
    ("What's the point of buying this crap anyway?", "notinterested"),
    ("Hi, I’d love to know more about the material and the price.", "price-features"),
    ("If this really costs more than 100 TL, then you're insane.", "notinterested"),
    ("I saw it on someone’s story. Looks interesting.", "other"),
    ("How do I use it? And where is the price listed?", "price-features"),
    ("Beautiful product, but way out of my budget. Bye.", "notinterested"),
    ("Hey! Can I come by and see it in person?", "other"),
    ("What's this made of?", "features"),
]

intent_prompt = f"""
You are an Instagram seller account owner.
You are trying to understand the intent from the customers DM or comment. 

You can only say the intent of the customer and nothing else. Your output, The intent, must be one or many of the followings: 
-price 
-features 
-notinterested 
-other

If the message is not only talking about the price but also asking, you will say "price".
If the customer asking about the features of the product, you will say "feature"
If the customer seems notinterested, or using a mean language, you will say "notinterested"
If the customer seems interested, but still mean, you will say "notinterested". Which means, if the intent has "notinterested" trait, you will ignore anything else and say "notinterested"
If the customer is not asking for the price, or features, you will say "other". Please note that the customer may talk about the price and features but if the customer does not ask about any detail of them, you will ignore it.
If the customer is trying to make an appoinment or trying to start a conversation without asking the price or features, you will say other.

Note that you could say more than one intent. If you decide to use multiple intents, use "-" and not a comma. You can find some examples below for better understanding and filtering: 
-How much is this? Output: price 
-Can you tell me the features? Output: features
-Too expensive for what it is.  Output: notinterested
-Hi, can we chat?   Output: other
-What's the content and price?  Output: price-features
-A friend of mine got it and loved it.  Output: other
-This is a terrible product.    Output: notinterested
-What's included in the box?    Output: features
-I'd like to visit and talk in person.  Output: other
-Looks good, but I’m not buying.    Output: notinterested
-It looks perfect. How much is it? If it's above 50 dollars, then go to hell!   Output: notinterested
-Looks fancy, but I doubt it's worth the money. How much?   Output: notinterested
-Can you tell me what it does and how much it is?   Output: price-features
-I liked the design. Hope it's not overpriced.  Output: other
-Just checking out your page. Nice work!    Output: other
-Why is this so damn expensive?     Output: notinterested
-Is it washable? And do you offer discounts?    Output: features-other
-What's the point of buying this crap?      Output: notinterested
-Looks fancy, but I doubt it's worth the money. How much?   Output: notinterested


Note: The output must NOT include anything else but intents. Expressions like "The intent: price" will not be accepted. Only say the intent as "price" or "price-other".
"""

correct = 0
for message, expected in examples:
    predicted = Responder.extract_intent(PROMPT=intent_prompt, message=message)
    is_correct = predicted == expected
    print(f"[{'+' if is_correct else '-'}] Expected: {expected} | Output: {predicted}")
    if is_correct:
        correct += 1

accuracy = correct / len(examples)
print(f"Accuracy: {accuracy:.2%}")
