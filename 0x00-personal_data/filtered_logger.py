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


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """format"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ returns logger user data"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    Logger.propagate = False
    formatter = RedactingFormatter(list(PII_FIELDS))
    st_handler = logging.StreamHandler()
    st_handler.setFormatter(formatter)
    logger.addHandler(st_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ returns connector to a database """
    db_pass = os.environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    db_user = os.environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
    db_host = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.environ.get('PERSONAL_DATA_DB_NAME')
    return mysql.connector.connect(user=db_user, password=db_pass,
                                   host=db_host, database=db_name)
