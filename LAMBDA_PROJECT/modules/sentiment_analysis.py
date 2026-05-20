POSITIVE_WORDS = [
    "good", "great", "excellent", "positive",
    "success", "growth", "profit", "up"
]

NEGATIVE_WORDS = [
    "bad", "poor", "negative",
    "loss", "down", "crash", "fail"
]


def analyze_sentiment(text):

    text = text.lower()

    positive_score = sum(
        word in text for word in POSITIVE_WORDS
    )

    negative_score = sum(
        word in text for word in NEGATIVE_WORDS
    )

    if positive_score > negative_score:
        sentiment = "Positive"

    elif negative_score > positive_score:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    # sentiment + numeric score
    score = positive_score - negative_score

    return sentiment, score