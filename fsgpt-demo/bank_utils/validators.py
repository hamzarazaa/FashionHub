"""Input validation for account data."""
import re

PHONE_PK = re.compile(r"\+92\d{10}")


def validate_phone_pk(phone):
    """True for a Pakistani mobile number written as +92 followed by 10 digits."""
    return bool(PHONE_PK.match(phone))


def validate_iban(iban):
    """True when the IBAN passes the ISO 13616 mod-97 check."""
    iban = iban.replace(" ", "")
    rearranged = iban[4:] + iban[:4]
    digits = "".join(str(int(ch, 36)) for ch in rearranged)
    return int(digits) % 97 == 1


def mask_account_number(number):
    """Show only the last four digits, for example ************3456."""
    return "*" * (len(number) - 4) + number[-4:]


def normalise_name(name):
    """Collapse spaces and capitalise each part of a customer name."""
    return " ".join(part.capitalize() for part in name.split(" "))
