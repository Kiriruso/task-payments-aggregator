from pydantic_settings import BaseSettings, SettingsConfigDict


class TelegramBotSettings(BaseSettings):
    TOKEN: str

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="BOT_", extra="ignore"
    )


class MongoDBSettings(BaseSettings):
    HOST: str
    PORT: int
    NAME: str
    COLLECTION: str

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="MONGO_DB_", extra="ignore"
    )

    @property
    def url(self) -> str:
        return f"mongodb://{self.HOST}:{self.PORT}"


bot_settings = TelegramBotSettings()
mongodb_settings = MongoDBSettings()
