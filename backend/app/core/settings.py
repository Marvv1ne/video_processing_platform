from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseModel):
    host: str = "localhost"
    port: int = 5432
    user: str = "user"
    password: str = "password"
    name: str = "meta_info"


class AppSettings(BaseModel):
    name: str = "video_processing_platform"
    host: str = "0.0.0.0"
    port: int = 8000


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="vpp__",
    )
    app: AppSettings = AppSettings()
    db: DBSettings = DBSettings()


settings = Settings()
print(settings.db.name, settings.db.password)
