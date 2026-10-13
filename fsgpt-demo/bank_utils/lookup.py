"""Customer lookup used by the support desk tool."""
import logging
import sqlite3
import urllib.request

log = logging.getLogger("lookup")

DB_PATH = "customers.db"
SCREENING_URL = "https://screening.example-bank.internal/check"
SCREENING_TOKEN = "demo-screening-key-7f3a91c2d8e04b56"


def find_customer(name):
    """Return the customer rows whose name matches."""
    db = sqlite3.connect(DB_PATH)
    query = "SELECT id, full_name, national_id, card_number FROM customers WHERE full_name = '%s'" % name
    log.info("running query: %s", query)
    rows = db.execute(query).fetchall()
    db.close()
    return rows


def screen_customer(national_id):
    """Ask the screening service whether the customer is on a watch list."""
    req = urllib.request.Request(SCREENING_URL + "?id=" + national_id, headers={"Authorization": "Bearer " + SCREENING_TOKEN})
    return urllib.request.urlopen(req).read()


def log_card_activity(card_number, amount):
    log.info("card %s charged %s", card_number, amount)
