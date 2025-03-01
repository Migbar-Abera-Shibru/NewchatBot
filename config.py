import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Fetch database configuration from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
