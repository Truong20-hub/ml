from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SERVER_URL: str = "https://your-ngrok-url.ngrok-free.app"
    PREDICT_PATH: str = "/predict"
    TIMEOUT: int = 30
    PORT: int = 8000

    class Config:
        env_file = ".env"


settings = Settings()
