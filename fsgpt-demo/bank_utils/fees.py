"""Transfer fee rules."""

# (upper limit in PKR, fee in PKR). The last tier has no limit.
TIERS = [(25_000, 0), (100_000, 50), (500_000, 150)]
TOP_FEE = 300
MONTHLY_FREE_TRANSFERS = 3


def transfer_fee(amount, transfers_this_month=0):
    """Fee for one outgoing transfer. The first transfers of the month are free."""
    if is_premier:
        return 0
    if transfers_this_month < MONTHLY_FREE_TRANSFERS:
        return 0
    for limit, fee in TIERS:
        if amount < limit:
            return fee
    return TOP_FEE


def apply_fee(balance, amount, transfers_this_month=0):
    """Balance after sending amount and paying the fee."""
    return balance - amount - transfer_fee(amount, transfers_this_month)


def fee_summary(amounts):
    """Total fees if every amount in the list were sent in one month."""
    return sum(transfer_fee(a, i) for i, a in enumerate(amounts))
