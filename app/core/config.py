from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = 'Finance tracker api'
    environment: str = 'local'
    DATABASE_URL: str 

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


settings = Settings()
