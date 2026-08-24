from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/app"
    SECRET_KEY: str = "change-me"

    class Config:
        env_file = ".env"

settings = Settings()
