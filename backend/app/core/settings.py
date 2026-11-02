from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class S3Settings(BaseModel):
    access_key: str = "minioadmin"
    secret_key: str = "minioadmin"
    endpoint_url: str = "localhost"
    bucket_name: str = ""


class DBSettings(BaseModel):
    host: str = "localhost"
    port: int = 5432
    user: str = "user"
    password: str = "password"
    name: str = "meta_info"
    drivername: str = ""
    database: str = ""

    def get_url(self):
        return URL.create(drivername=self.drivername, database=self.name)


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
    s3: S3Settings = S3Settings()


settings = Settings()
print(settings.db.name, settings.db.password)
print(settings.app.name)
print(settings.app.port)
print(settings.db.get_url())
print(settings.s3.access_key)
print(settings.s3.bucket_name)
