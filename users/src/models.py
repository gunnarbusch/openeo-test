from os import environ
from sqlalchemy import Column, Integer, String, Boolean, TEXT, DateTime
from sqlalchemy.ext.declarative import declarative_base
from bcrypt import gensalt, hashpw
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id          = Column(Integer, primary_key=True, autoincrement=True)
    username    = Column(String, unique=True, nullable=False)
    email       = Column(String, unique=True, nullable=False)
    password    = Column(String, nullable=False)
    created_at  = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at  = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    active      = Column(Boolean, default=True, nullable=False)
    project     = Column(String, nullable=False)
    sa_token    = Column(TEXT, nullable=False)
    admin       = Column(Boolean, nullable=False)

    def __init__(self, username, email, password, project, sa_token, admin=False):
        print(environ.get('BCRYPT_LOG_ROUNDS'))
        self.username = username
        self.email = email
        self.password = self.generate_hash(password)
        self.project = project
        self.sa_token = sa_token
        self.admin = admin

    def generate_hash(self, password):
        ''' Generates the password hash '''
        return hashpw(password.encode('utf8'), gensalt(4)) #environ.get('BCRYPT_LOG_ROUNDS')
