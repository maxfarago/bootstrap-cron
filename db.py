import os
import psycopg2

from log import logger

# look for DB credentials in the app environment
# if none are available, assume local development
DB_HOSTNAME = os.getenv("DB_HOSTNAME", "localhost")
DB_USERNAME = os.getenv("DB_USERNAME", "bootstrap")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_CXN_STRING = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:5432/bootstrap"

cxn = None


def get_cxn():
    global cxn
    if cxn and not cxn.closed:
        return cxn

    try:
        cxn = psycopg2.connect(DB_CXN_STRING)
        logger.info(f"Connected to {DB_CXN_STRING}")
    except (Exception, psycopg2.Error) as e:
        logger.error(f"Error connecting to the database: {e}")
        return None

    return cxn


def close_cxn():
    global cxn
    cxn.close()
