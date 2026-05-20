import json
import boto3
from datetime import datetime
from modules.config import S3_BUCKET

s3 = boto3.client("s3")

def save_to_s3(news_data):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"raw_news/news_{timestamp}.json"

    s3.put_object(
        Bucket=S3_BUCKET,
        Key=filename,
        Body=json.dumps(news_data)
    )

    print("Raw JSON uploaded to S3 successfully!")