from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """用户模型"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    
    # 建立与任务的关系，级联删除
    tasks = db.relationship('Task', backref='author', lazy='dynamic', cascade="all, delete-orphan")
    # 建立与番茄钟记录的关系，级联删除
    pomodoros = db.relationship('Pomodoro', backref='user', lazy='dynamic', cascade="all, delete-orphan")

    def set_password(self, password):
        """对密码进行 hash 并保存"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """校验密码是否正确"""
        return check_password_hash(self.password_hash, password)

class Task(db.Model):
    """任务模型"""
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    priority = db.Column(db.Integer, default=2) # 1-低, 2-中, 3-高
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    pomodoros = db.relationship('Pomodoro', backref='task', lazy=True)

class Pomodoro(db.Model):
    """番茄钟专注记录模型"""
    __tablename__ = 'pomodoros'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=True)
    duration_minutes = db.Column(db.Integer, default=25)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
