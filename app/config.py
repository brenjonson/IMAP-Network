import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from cryptography.fernet import Fernet

class Settings(BaseSettings):
    # เพิ่ม encryption key - ใช้ค่าคงที่เป็น default ที่ถูกต้อง
    ENCRYPTION_KEY: str = os.getenv("ENCRYPTION_KEY", "Xx8EAo8PwvHGX24cSqVL574AHoEaB_wkKVeC-5SHRcg=")
    
    # Database - เปลี่ยนจาก MySQL เป็น PostgreSQL
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://receipt_manager_db_user:oQngMMcIfHjxHQhmthD93k1qExIp7ivl@dpg-cvj397ali9vc73egb0v0-a/receipt_manager_db")
    
    # JWT Authentication
    SECRET_KEY: str = os.getenv("SECRET_KEY", "15dc89e6a2f34e0d96c7638509f8a9c8e61d3abe2bf846688f3fdb9e5f4a63cf")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    CORS_ORIGINS: list = ["http://localhost:3000", "https://your-frontend-url.com"]
    API_V1_PREFIX: str = "/api/v1"
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()