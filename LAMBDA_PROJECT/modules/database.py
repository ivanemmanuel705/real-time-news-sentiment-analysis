from sqlalchemy import create_engine
from modules.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

def save_to_rds(df):

    try:

        df.to_sql(
            "news_sentiment",
            engine,
            if_exists="append",
            index=False
        )

        print("Data saved to PostgreSQL successfully!")

    except Exception as e:

        print("Error saving to PostgreSQL:")
        print(e)