from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_FILE: str

    @property
    def DATABASE_URL_sqlite(self):
        return f"sqlite:///{self.DB_FILE}"

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()
