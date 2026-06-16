from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    # API Settings
    ENV: str = "development"
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 10000

    # CORS
    ALLOWED_ORIGINS: list = [
        "http://localhost:3000",
        "https://auto-meta-ml.vercel.app"
    ]

    # File Upload
    MAX_UPLOAD_SIZE: int = 1024 * 1024 * 1024
    TEMP_DIR: str = "./temp"

    # Paths
    BASE_DIR: Path = Path(__file__).resolve().parent.parent  # backend/
    DATA_DIR: Path = BASE_DIR / "data"                      # backend/data/

    MODEL_PATH: Path = DATA_DIR / "mlknn_model.pkl"
    FEATURES_PATH: Path = DATA_DIR / "selected_features.pkl"
    IMPUTER_PATH: Path = DATA_DIR / "imputer.pkl"

    # OpenAI (optional)
    OPENAI_API_KEY: str = ""

    class Config:
        env_file = ".env"

settings = Settings()

# Debug logs (remove later)
print(f"BASE_DIR: {settings.BASE_DIR}")
print(f"DATA_DIR: {settings.DATA_DIR}")
print(f"MODEL_PATH: {settings.MODEL_PATH}")
print(f"MODEL_EXISTS: {settings.MODEL_PATH.exists()}")
print(f"FEATURES_EXISTS: {settings.FEATURES_PATH.exists()}")
print(f"IMPUTER_EXISTS: {settings.IMPUTER_PATH.exists()}")