from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL=os.getenv("DATABASE_URL")
HASHING_SECRET=os.getenv("HASHING_SECRET")