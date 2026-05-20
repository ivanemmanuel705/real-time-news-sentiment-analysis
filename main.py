import pandas as pd

from modules.fetch_news import fetch_news
from modules.sentiment_analysis import analyze_sentiment
from modules.database import save_to_database
from modules.save_files import save_json, save_csv
from modules.display import display_results

# ==============================
# FETCH NEWS
# ==============================

news_data = fetch_news()

if news_data is None:
    exit()

# ==============================
# SAVE RAW JSON
# ==============================

timestamp = save_json(news_data)

# ==============================
# PROCESS ARTICLES
# ==============================

articles = news_data.get("articles", [])

processed_data = analyze_sentiment(articles)

# ==============================
# CREATE DATAFRAME
# ==============================

df = pd.DataFrame(processed_data)

# ==============================
# SAVE DATA
# ==============================

save_to_database(df)

save_csv(df, timestamp)

# ==============================
# DISPLAY RESULTS
# ==============================

display_results(df)