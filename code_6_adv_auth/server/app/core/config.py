import os
from dotenv import load_dotenv

load_dotenv()

# Validate required environment variables
def get_env_or_raise(key: str, default=None):
    """Get environment variable or raise error if not set."""
    value = os.getenv(key, default)
    if value is None:
        raise ValueError(f"Environment variable {key} is required but not set. Please check your .env file.")
    return value

DATABASE_URL = get_env_or_raise("DATABASE_URL")
SECRET_KEY = get_env_or_raise("SECRET_KEY")
ALGORITHM = get_env_or_raise("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(get_env_or_raise("ACCESS_TOKEN_EXPIRE_MINUTES", "15"))
REFRESH_TOKEN_EXPIRE_MINUTES = int(get_env_or_raise("REFRESH_TOKEN_EXPIRE_MINUTES", "10080"))
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
