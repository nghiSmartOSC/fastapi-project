from pydantic import BaseSettings


class Settings(BaseSettings):
    # Base
    api_prefix: str
    debug: bool
    project_name: str
    version: str

    # Database
    db_async_connection_str: str
    db_async_test_connection_str: str
