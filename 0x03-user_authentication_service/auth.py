#!/usr/bin/env python3
"""
auth module
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
from typing import Union
from uuid import uuid4


def _hash_password(password: str) -> str:
    """returns a salted hash of the input password,
    hashed with bcrypt.hashpw"""
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_pw


def _generate_uuid() -> str:
    """string representtion of a new uuid is returned"""
    UUID = uuid4
    return str(UUID)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registering a user in database"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

        else:
            raise ValueError(f'user {email} aready exists')
