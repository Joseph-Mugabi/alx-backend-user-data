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
