#!/usr/bin/env python3
"""
filtered logs
"""
import re
import logging
from typing import List
import mysql.connector
import os

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """filters logsthat replaces fields with redaction in message """
    for field in fields:
        message = re.sub(f'({field}=)(.*?){separator}',
                         rf'\1{redaction}{separator}', message)
    return message
