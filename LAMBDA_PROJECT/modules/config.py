API_KEY = "177c111d38b7453c896d42fe0a2d3d1a"

DB_HOST = "news-db.ci5e44ikyqgx.us-east-1.rds.amazonaws.com"
DB_NAME = "newsdb"
DB_USER = "postgres"
DB_PASSWORD = "newsdata123"
DB_PORT = "5432"

S3_BUCKET = "news-rawdata-bucket"

DATABASE_URL = (
    f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)