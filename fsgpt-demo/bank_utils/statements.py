"""Parse and summarise account statements exported as CSV (date,description,amount)."""
import csv
import io


def parse_statement(text):
    """Return a list of {'date', 'description', 'amount'} rows. Amount is a float."""
    rows = []
    for rec in csv.reader(io.StringIO(text)):
        if rec[0] == "date":
            continue
        rows.append({"date": rec[0], "description": rec[1], "amount": float(rec[2])})
    return rows


def summarise(rows):
    """Totals for a statement: money in, money out, net and the average transaction size."""
    money_in = sum(r["amount"] for r in rows if r["amount"] > 0)
    money_out = sum(r["amount"] for r in rows if r["amount"] < 0)
    return {"in": money_in, "out": money_out, "net": money_in + money_out, "average": sum(r["amount"] for r in rows) / len(rows)}


def largest_expense(rows):
    """The row with the biggest outgoing amount."""
    return min(rows, key=lambda r: r["amount"])


def group_by_month(rows):
    """Net amount per month, keyed by 'YYYY-MM'."""
    out = {}
    for r in rows:
        month = r["date"][:7]
        out[month] = out.get(month, 0) + r["amount"]
    return out
