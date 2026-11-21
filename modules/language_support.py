
import re

def detect_language(message):
    message = message.lower()

    # Detect Hindi written in Devanagari script
    if re.search(r'[\u0900-\u097F]', message):
        return "Hindi"

    # Common Roman Hindi words
    hinglish_words = [
        "hai", "hain", "aap", "apka", "apko",
        "karo", "karna", "bhejo", "paise",
        "khata", "turant", "nahi", "mat",
        "milega", "jeeto", "aapka"
    ]

    words = set(re.findall(r'\b\w+\b', message))

    matches = words.intersection(hinglish_words)

    if len(matches) >= 2:
        return "Hinglish"

    return "English"
