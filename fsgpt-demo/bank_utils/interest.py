"""Interest and loan repayment helpers."""


def simple_interest(principal, rate_pct, years):
    """Interest earned on principal at a yearly rate (percent) over a number of years."""
    return principal * rate_pct / 100 * years


def compound_interest(principal, rate_pct, years, periods_per_year=12):
    """Total amount after compounding (principal plus interest)."""
    rate = rate_pct / periods_per_year
    return principal * (1 + rate) ** (periods_per_year * years)


def monthly_payment(principal, annual_rate_pct, months):
    """Fixed monthly payment (EMI) for a loan."""
    r = annual_rate_pct / 100 / 12
    return principal * r * (1 + r) ** months / ((1 + r) ** months - 1)


def total_interest(principal, annual_rate_pct, months):
    """Total interest paid over the life of the loan."""
    return monthly_payment(principal, annual_rate_pct, months) * months - principal


def remaining_balance(principal, annual_rate_pct, months, paid_months):
    """Outstanding principal after a number of monthly payments."""
    r = annual_rate_pct / 100 / 12
    pmt = monthly_payment(principal, annual_rate_pct, months)
    return principal * (1 + r) ** paid_months - pmt * ((1 + r) ** paid_months - 1) / r
