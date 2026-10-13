# bank_utils

Small utility library for a retail banking service: interest and loan maths, transfer fees, input validation, statement parsing and business day helpers.

Python 3.10 or newer, standard library only. There is no test suite yet.

```
python -c "from bank_utils.interest import monthly_payment; print(monthly_payment(1_000_000, 14, 36))"
```
