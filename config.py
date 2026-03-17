import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    ACCESS_TOKEN = os.getenv("LONG_ACCESS_TOKEN")
    IG_USER_ID = os.getenv("IG_USER_ID")