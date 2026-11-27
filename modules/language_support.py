

import re


def detect_language(message):

    message = message.lower()

    # Detect Hindi written in Devanagari script
    if re.search(r'[\u0900-\u097F]', message):
        return "Hindi"

    words = set(re.findall(r'\b[a-z]+\b', message))

    # More distinctive Roman Hindi words
    hinglish_distinctive = {
        "aap", "aapka", "aapki", "aapko", "apka", "apko",
        "hai", "hain", "tha", "thi", "the",
        "kal", "aaj", "abhi", "turant",
        "milte", "milega", "milna",
        "aaunga", "aayega", "jaunga", "jao",
        "bhejo", "bhejna", "karo", "karna",
        "jeeta", "jeeto", "inaam",
        "paise", "khata", "paisa",
        "nahi", "nahin", "mat",
        "kyun", "kaise", "kya",
        "hojaega", "hojayega",
        "chahiye", "accha", "achha",
        "bahut", "bohot", "yaar",
        "apna", "apne", "apni",
        "aaunga", "launga", "lekar"
    }

    # Common Hindi connecting words
    hinglish_common = {
        "ke", "ki", "ka", "ko", "se",
        "mein", "me", "par", "liye",
        "aur", "mera", "meri", "mere",
        "hum", "tum", "aap",
        "baad", "pehle", "bhi",
        "main", "le", "raha", "rahi",
        "rahe", "wala", "wali"
    }

    distinctive_matches = words.intersection(
        hinglish_distinctive
    )

    common_matches = words.intersection(
        hinglish_common
    )

    # Require multiple Hindi-language signals
    if (
        len(distinctive_matches) >= 2
        or (
            len(distinctive_matches) >= 1
            and len(common_matches) >= 2
        )
    ):
        return "Hinglish"

    return "English"
