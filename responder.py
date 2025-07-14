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
    def extract_intent(PROMPT = "Tell me your model name, version and the amount of weights.") -> str:

        chat = client.chat.completions.create(messages=[
                {
                    "role": "user",
                    "content": PROMPT
                }
            ],
            model="llama3-70b-8192")

        intent = chat.choices[0].message.content

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
    ("Looks fancy, but I doubt it's worth the money. How much?", "not interested"),
    ("Can you tell me what it does and how much it is?", "price-features"),
    ("I liked the design. Hope it's not overpriced.", "other"),
    ("Just checking out your page. Nice work!", "other"),
    ("Why is this so damn expensive?", "not interested"),
    ("Is it washable? And do you offer discounts?", "features-other"),
    ("What's the point of buying this crap anyway?", "not interested"),
    ("Hi, I’d love to know more about the material and the price.", "price-features"),
    ("If this really costs more than 100 TL, then you're insane.", "not interested"),
    ("I saw it on someone’s story. Looks interesting.", "other"),
    ("How do I use it? And where is the price listed?", "price-features"),
    ("Beautiful product, but way out of my budget. Bye.", "not interested"),
    ("Hey! Can I come by and see it in person?", "other"),
    ("What's this made of?", "features"),
]

for message, expected in examples:


    intent_prompt = f"""
    You are an Instagram seller account owner.
    You are trying to understand the intent from the customers DM or comment. 

    Customers Message : {message}

    You can only say the intent of the customer and nothing else. Your output, The intent, must be one or many of the followings: 
    -price 
    -features 
    -not interested 
    -other

    If the message is not only talking about the price but also asking, you will say "price".
    If the customer asking about the features of the product, you will say "feature"
    If the customer seems not interested, or using a mean language, you will say "not interested"
    If the customer seems interested, but still mean, you will say "not interested". Which means, if the intent has "not interested" trait, you will ignore anything else and say "not interested"
    If the customer is not asking for the price, or features, you will say "other". Please note that the customer may talk about the price and features but if the customer does not ask about any detail of them, you will ignore it.
    If the customer is trying to make an appoinment or trying to start a conversation without asking the price or features, you will say other.

    Note that you could say more than one intent. If you decide to use multiple intents, use "-" and not a comma. You can find some examples below for better understanding and filtering: 
    -How much is this? Output: price 
    -Can you tell me the features? Output: features
    -Too expensive for what it is.  Output: not interested
    -Hi, can we chat?   Output: other
    -What's the content and price?  Output: price-features
    -A friend of mine got it and loved it.  Output: other
    -This is a terrible product.    Output: not interested
    -What's included in the box?    Output: features
    -I'd like to visit and talk in person.  Output: other
    -Looks good, but I’m not buying.    Output: not interested
    -It looks perfect. How much is it? If it's above 50 dollars, then go to hell!   Output: not interested
    -Looks fancy, but I doubt it's worth the money. How much?   Output: not interested
    -Can you tell me what it does and how much it is?   Output: price-features
    -I liked the design. Hope it's not overpriced.  Output: other
    -Just checking out your page. Nice work!    Output: other
    -Why is this so damn expensive?     Output: not interested
    -Is it washable? And do you offer discounts?    Output: features-other
    -What's the point of buying this crap?      Output: not interested


    Note: The output must NOT include anything else but intents. Expressions like "The intent: price" will not be accepted. Only say the intent as "price" or "price-other".
    """

    print(f"Expected:{expected}     Output:{Responder.extract_intent(intent_prompt)}")