from textblob import TextBlob

def analyze_sentiment(articles):

    processed_data = []

    for article in articles:

        title = article.get("title", "")
        description = article.get("description", "")
        source = article.get("source", {}).get("name", "")
        published_at = article.get("publishedAt", "")

        # Combine title + description
        text = f"{title} {description}"

        # Sentiment Analysis
        sentiment_score = TextBlob(text).sentiment.polarity

        # Sentiment Label
        if sentiment_score > 0:
            sentiment = "Positive"

        elif sentiment_score < 0:
            sentiment = "Negative"

        else:
            sentiment = "Neutral"

        processed_data.append({
            "title": title,
            "description": description,
            "source": source,
            "published_at": published_at,
            "sentiment_score": sentiment_score,
            "sentiment": sentiment
        })

    return processed_data