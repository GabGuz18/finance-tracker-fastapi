from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = 'Finance tracker api'
    environment: str = 'local'
    DATABASE_URL: str 

    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 14

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


settings = Settings()
