import json
import os
from datetime import datetime

# Create data folder
os.makedirs("data", exist_ok=True)

def save_json(news_data):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    json_file_path = f"data/news_raw_{timestamp}.json"

    with open(json_file_path, "w", encoding="utf-8") as file:

        json.dump(news_data, file, indent=4)

    print(f"Raw JSON saved: {json_file_path}")

    return timestamp


def save_csv(df, timestamp):

    csv_file_path = f"data/news_processed_{timestamp}.csv"

    df.to_csv(csv_file_path, index=False)

    print(f"Processed CSV saved: {csv_file_path}")