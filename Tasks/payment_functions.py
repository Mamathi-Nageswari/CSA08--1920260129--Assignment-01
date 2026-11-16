"""Task 6 - The calculation divided into small functions with docstrings."""

BASE_RATE = 30.00
STD_FAT, STD_SNF, STEP_SIZE = 3.5, 8.5, 0.1
FAT_STEP_VALUE, SNF_STEP_VALUE = 0.40, 0.30
FAT_MIN, FAT_MAX = 2.0, 7.0
SNF_MIN, SNF_MAX = 7.0, 10.0
LITRES_MAX = 100.0


def steps(value, standard):
    """Returns the whole number of 0.1 % steps of value from the standard."""
    return round((value - standard) / STEP_SIZE)


def rate_per_litre(fat, snf):
    """Returns the price per litre in Rs, rounded to 2 decimals."""
    rate = (BASE_RATE + steps(fat, STD_FAT) * FAT_STEP_VALUE
            + steps(snf, STD_SNF) * SNF_STEP_VALUE)
    return round(rate, 2)


def payout(litres, fat, snf):
    """Returns the amount for one entry in Rs, rounded to 2 decimals."""
    return round(litres * rate_per_litre(fat, snf), 2)


def is_valid(litres, fat, snf):
    """Returns True if all three readings are inside the allowed limits."""
    return 0 < litres <= LITRES_MAX and FAT_MIN <= fat <= FAT_MAX and SNF_MIN <= snf <= SNF_MAX


def ten_day_total(entries):
    """Returns the total of the rounded payouts of all valid (litres, fat, snf) entries."""
    total = 0.0
    for litres, fat, snf in entries:
        if is_valid(litres, fat, snf):
            total += payout(litres, fat, snf)
    return round(total, 2)


def print_payout(litres, fat, snf):
    """Prints a payout. Returns nothing (None), so the value cannot be reused."""
    print(f"payout = {round(litres * rate_per_litre(fat, snf), 2)}")


if __name__ == "__main__":
    entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3), (-2, 3.5, 8.5)]
    for e in entries:
        print(e, "valid" if is_valid(*e) else "invalid",
              "rate", rate_per_litre(e[1], e[2]), "payout", payout(*e))
    print("ten_day_total:", ten_day_total(entries))

    print("\nReturn vs print")
    returned = payout(8.5, 4.2, 8.7)
    printed = print_payout(8.5, 4.2, 8.7)
    print("returned value:", returned, "| value from the print function:", printed)
    print("returned * 2 =", returned * 2)

    print("\nhelp text from the docstring:")
    print("payout.__doc__ =", payout.__doc__)
