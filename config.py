import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # 密钥，用于 JWT Token 的签名和 Flask Session 的安全
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-very-secret-key-12345'
    
    # SQLite 数据库配置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'app_v2.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
