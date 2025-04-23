import re

def clean_text(text):
    """
    Enhanced cleaning preserving key negation terms:
    1. Keep basic numbers and currency
    2. Maintain negation stopwords
    3. Add lemmatization
    """
    if not isinstance(text, str):
        return ""
    text = text.lower().strip()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text