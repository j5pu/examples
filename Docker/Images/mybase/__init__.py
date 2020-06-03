# Ansible managed
import asyncio
import atexit
import concurrent.futures
import configparser
import contextlib
import enum
import functools
import http.client
import inspect
import logging
import logging.config
import logging.handlers
import multiprocessing
import pprint
import random
import socket
import subprocess
import sys
import threading
import time
import traceback
import urllib.parse
import os

import verboselogs
import hunter

USUARIO = os.getenv('USUARIO', '')
PASSWD = os.getenv('PASSWD', '')
CLOUD = os.getenv('CLOUD', '')
PYTHONPATH = os.getenv('PYTHONPATH', '')
PYTHON_COMMON_PY = os.getenv('PYTHON_COMMON_PY', '')
PYTHONDONTWRITEBYTECODE = os.getenv('PYTHONDONTWRITEBYTECODE', '')
PYTHONUNBUFFERED = os.getenv('PYTHONUNBUFFERED', '')
PYTHONASYNCIODEBUG = os.getenv('PYTHONASYNCIODEBUG', '')
DOCKER_HOST_DOMAIN = os.getenv('DOCKER_HOST_DOMAIN', '')
OPENVPN_SERVER_ALIAS = os.getenv('OPENVPN_SERVER_ALIAS', '')
BIND_MASTER_ALIAS = os.getenv('BIND_MASTER_ALIAS', '')
BIND_SLAVE_ALIAS = os.getenv('BIND_SLAVE_ALIAS', '')
USB_SERVER_ALIAS = os.getenv('USB_SERVER_ALIAS', '')
STORAGE_SERVER_ALIAS = os.getenv('STORAGE_SERVER_ALIAS', '')
MYSQL_SERVER_ALIAS = os.getenv('MYSQL_SERVER_ALIAS', '')
MYSQL_SERVER_DOMAIN = os.getenv('MYSQL_SERVER_DOMAIN', '')
MYSQL_SERVER_SLAVE_ALIAS = os.getenv('MYSQL_SERVER_SLAVE_ALIAS', '')
MYSQL_SERVER_SLAVE_DOMAIN = os.getenv('MYSQL_SERVER_SLAVE_DOMAIN', '')
MYSQL_SERVER_TEST_ALIAS = os.getenv('MYSQL_SERVER_TEST_ALIAS', '')
MYSQL_SERVER_TEST_DOMAIN = os.getenv('MYSQL_SERVER_TEST_DOMAIN', '')
MYSQL_PORT = os.getenv('MYSQL_PORT', '')
DB_ENGINE_URL_NO_DB = os.getenv('DB_ENGINE_URL_NO_DB', '')
DB_ENGINE_TEST_URL_NO_DB = os.getenv('DB_ENGINE_TEST_URL_NO_DB', '')
DB_ENGINE_URL = os.getenv('DB_ENGINE_URL', '')
DB_ENGINE_TEST_URL = os.getenv('DB_ENGINE_TEST_URL', '')
DB_NAME = os.getenv('DB_NAME', '')
DB_SERVER_TEST = os.getenv('DB_SERVER_TEST', '')
DEVPI_SERVER_ALIAS = os.getenv('DEVPI_SERVER_ALIAS', '')
DEVPI_SERVER_DOMAIN = os.getenv('DEVPI_SERVER_DOMAIN', '')
DEVPI_PORT = os.getenv('DEVPI_PORT', '')
PROXY_SERVER_ALIAS = os.getenv('PROXY_SERVER_ALIAS', '')
MAIL_SERVER_ALIAS = os.getenv('MAIL_SERVER_ALIAS', '')
PRIVOXY_SERVER_ALIAS = os.getenv('PRIVOXY_SERVER_ALIAS', '')
SOCKS_SERVER_ALIAS = os.getenv('SOCKS_SERVER_ALIAS', '')
REGISTRY_SERVER_ALIAS = os.getenv('REGISTRY_SERVER_ALIAS', '')
REGISTRY = os.getenv('REGISTRY', '')
WORDPRESS_SERVER_ALIAS = os.getenv('WORDPRESS_SERVER_ALIAS', '')
PYTHON_SERVER_ALIAS = os.getenv('PYTHON_SERVER_ALIAS', '')
PROXY_SERVICE = os.getenv('PROXY_SERVICE', '')
PRIVOXY_PORT = os.getenv('PRIVOXY_PORT', '')
PRIVOXY_DOMAIN = os.getenv('PRIVOXY_DOMAIN', '')
PRIVOXY_DOMAIN_PORT = os.getenv('PRIVOXY_DOMAIN_PORT', '')
SOCKS_VPN_PORT = os.getenv('SOCKS_VPN_PORT', '')
SOCKS_PORTS = os.getenv('SOCKS_PORTS', '')
SOCKS_DOMAIN = os.getenv('SOCKS_DOMAIN', '')
SOCKS_DOMAIN_VPN_PORT = os.getenv('SOCKS_DOMAIN_VPN_PORT', '')
TOR_PORT = os.getenv('TOR_PORT', '')
TOR_CONTROL_PORT = os.getenv('TOR_CONTROL_PORT', '')
SSH_PORT = os.getenv('SSH_PORT', '')
SSH_SOCKS_PORT = os.getenv('SSH_SOCKS_PORT', '')
DNS_PORT = os.getenv('DNS_PORT', '')
OPENVPN_PORT = os.getenv('OPENVPN_PORT', '')
DOCKER_PORT = os.getenv('DOCKER_PORT', '')
DOCKER_SWARM_LISTEN_PORT = os.getenv('DOCKER_SWARM_LISTEN_PORT', '')
DOCKER_REGISTRY_PORT = os.getenv('DOCKER_REGISTRY_PORT', '')
PROXY_PORT = os.getenv('PROXY_PORT', '')
PRIVOXY_STATS_PORT = os.getenv('PRIVOXY_STATS_PORT', '')
PRIVOXY_SOCKS_PORT = os.getenv('PRIVOXY_SOCKS_PORT', '')
REQUESTS_CA_BUNDLE = os.getenv('REQUESTS_CA_BUNDLE', '/etc/ssl/certs/ca-certificates.crt')
MEGAGROUPS_PATTERN_1 = os.getenv('MEGAGROUPS_PATTERN_1', '')
MEGAGROUPS_PATTERN_2 = os.getenv('MEGAGROUPS_PATTERN_2', '')
MEGAGROUPS_PATTERN_3 = os.getenv('MEGAGROUPS_PATTERN_3', '')
MEGAGROUPS_PATTERN_4 = os.getenv('MEGAGROUPS_PATTERN_4', '')
MEGAGROUPS_PATTERN_5 = os.getenv('MEGAGROUPS_PATTERN_5', '')
MEGAGROUPS_PATTERN_6 = os.getenv('MEGAGROUPS_PATTERN_6', '')
MEGAGROUPS_PATTERN_7 = os.getenv('MEGAGROUPS_PATTERN_7', '')
MEGAGROUPS_PATTERN_8 = os.getenv('MEGAGROUPS_PATTERN_8', '')
MEGAGROUPS_PATTERN_EXCLUDE = os.getenv('MEGAGROUPS_PATTERN_EXCLUDE', '')
PYTHON_PACKAGE = os.getenv('PYTHON_PACKAGE', '')
LOG_DIR = os.getenv('LOG_DIR', '')
WGET_DIR = os.getenv('WGET_DIR', '')
MEGAGROUPS_WGET_FILE = os.getenv('MEGAGROUPS_WGET_FILE', '')
CRAWL_SH = os.getenv('CRAWL_SH', '')
GECKODRIVER = os.getenv('GECKODRIVER', '')

REGEX_HREF_LINK_1C_2C = '(?<=link=["\'])[^"\']*(?=["\'])|(?<=href=["\'])[^"\']*(?=["\'])'
REGEX_HREF_1C_2C = '(?<=href=["\'])[^"\']*(?=["\'])'
REGEX_LINK_1C_2C = '(?<=link=["\'])[^"\']*(?=["\'])'

__all__ = [n for n in globals() if n[:1] != '_']
