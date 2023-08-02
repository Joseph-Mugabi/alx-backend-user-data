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


def filter_datum(fields, redaction, message, separator):
    """filters the logs"""
    for field in fields:
        message = re.sub(f'({field}=)(.*?){separator}',
                         rf'\1{redaction}{separator}', message)
    return message
