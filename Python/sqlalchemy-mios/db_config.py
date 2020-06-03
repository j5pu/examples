#!/usr/local/bin/python3.7
from common import *

db_dialect = 'mysql+pymysql://'

DB_SERVER_TEST = bool(os.getenv('DB_SERVER_TEST', 0))
DB_NAME = os.getenv('DB_NAME', PYTHON_PACKAGE)

db_engine_pool_size = 20
db_engine_max_overflow = 10
db_engine_pool_pre_ping = True
db_engine_pool_use_lifo = False
db_engine_echo = False

db_session_autocommit = True
db_session_autoflush = True

db_engine_url = f'{db_dialect}{USUARIO}:{PASSWD}@' \
                f'{MYSQL_SERVER_TEST_DOMAIN if DB_SERVER_TEST else MYSQL_SERVER_DOMAIN}:{MYSQL_PORT}/{DB_NAME}'
print(db_engine_url)
engine = sqlalchemy.create_engine(db_engine_url, echo=db_engine_echo, pool_size=db_engine_pool_size,
                                  max_overflow=db_engine_max_overflow, pool_pre_ping=db_engine_pool_pre_ping,
                                  pool_use_lifo=db_engine_pool_use_lifo)


__all__ = [n for n in globals() if n[:1] != '_']
