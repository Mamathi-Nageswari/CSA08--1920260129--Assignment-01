"""Task 9 - Ksheera co-operative payment calculator (exact to the paisa).

Run:  python calculator.py entries.csv
Each line of the CSV file: farmer_id,day,shift,litres,fat,snf
"""
import csv
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

# Rate card - the only place where a rate is written
BASE_RATE = Decimal("30.00")
STD_FAT = Decimal("3.5")
STD_SNF = Decimal("8.5")
STEP_SIZE = Decimal("0.1")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

# Limits of a valid entry
FAT_MIN, FAT_MAX = Decimal("2.0"), Decimal("7.0")
SNF_MIN, SNF_MAX = Decimal("7.0"), Decimal("10.0")
LITRES_MAX = Decimal("100")
SHIFTS = ("M", "E")
DAYS_PER_PERIOD = 10
PAISA = Decimal("0.01")


def to_decimal(text):
    """Converts the clerk's text to a Decimal; accepts ' 8.5 ' and '8,5'. Raises ValueError."""
    cleaned = str(text).strip().replace(",", ".")
    try:
        value = Decimal(cleaned)
    except InvalidOperation:
        raise ValueError(f"'{text}' is not a number") from None
    if not value.is_finite():
        raise ValueError(f"'{text}' is not a number")
    return value


def steps(value, standard):
    """Whole number of 0.1 % steps of value from the standard (nearest step, half up)."""
    return ((value - standard) / STEP_SIZE).to_integral_value(rounding=ROUND_HALF_UP)


def rate_per_litre(fat, snf):
    """Price per litre in Rs for the given fat % and SNF % (Decimal, 2 places)."""
    rate = BASE_RATE + steps(fat, STD_FAT) * FAT_STEP_VALUE + steps(snf, STD_SNF) * SNF_STEP_VALUE
    return rate.quantize(PAISA, rounding=ROUND_HALF_UP)


def payout(litres, fat, snf):
    """Amount payable for one entry, rounded to the paisa (half up)."""
    return (litres * rate_per_litre(fat, snf)).quantize(PAISA, rounding=ROUND_HALF_UP)


def check_entry(row):
    """Validates one raw row. Returns (entry, None) if valid or (None, reason) if not."""
    if len(row) != 6:
        return None, "needs 6 values"
    farmer_id, day, shift, litres, fat, snf = (field.strip() for field in row)
    if not (len(farmer_id) >= 2 and farmer_id[0].upper() == "F" and farmer_id[1:].isdigit()):
        return None, f"farmer ID '{farmer_id}' must look like F001"
    if not day.isdigit() or not 1 <= int(day) <= DAYS_PER_PERIOD:
        return None, f"day '{day}' must be 1 to {DAYS_PER_PERIOD}"
    if shift.upper() not in SHIFTS:
        return None, f"shift '{shift}' must be M or E"
    try:
        litres, fat, snf = to_decimal(litres), to_decimal(fat), to_decimal(snf)
    except ValueError as error:
        return None, str(error)
    if not 0 < litres <= LITRES_MAX:
        return None, f"litres {litres} must be > 0 and <= {LITRES_MAX}"
    if not FAT_MIN <= fat <= FAT_MAX:
        return None, f"fat {fat} must be {FAT_MIN} to {FAT_MAX}"
    if not SNF_MIN <= snf <= SNF_MAX:
        return None, f"SNF {snf} must be {SNF_MIN} to {SNF_MAX}"
    return (farmer_id.upper(), int(day), shift.upper(), litres, fat, snf), None


def ten_day_totals(entries):
    """Adds the rounded payouts of valid entries for each farmer. Returns {farmer_id: total}."""
    totals = {}
    for farmer_id, _day, _shift, litres, fat, snf in entries:
        totals[farmer_id] = totals.get(farmer_id, Decimal("0.00")) + payout(litres, fat, snf)
    return totals


def read_entries(path):
    """Reads the CSV file. Returns (valid_entries, rejected) where rejected = [(line, row, reason)]."""
    valid, rejected = [], []
    with open(path, newline="") as file:
        for line_no, row in enumerate(csv.reader(file), start=1):
            if not row or row[0].strip().lower() == "farmer_id":
                continue
            entry, reason = check_entry(row)
            if entry:
                valid.append(entry)
            else:
                rejected.append((line_no, row, reason))
    return valid, rejected


def main(path):
    """Prints the payment slip of every entry, the rejected entries and the ten-day totals."""
    valid, rejected = read_entries(path)
    print(f"{'Farmer':<7}{'Day':>4}{'Shift':>6}{'Litres':>8}{'Fat':>6}{'SNF':>6}{'Rate':>8}{'Amount':>10}")
    for farmer_id, day, shift, litres, fat, snf in valid:
        print(f"{farmer_id:<7}{day:>4}{shift:>6}{litres:>8}{fat:>6}{snf:>6}"
              f"{rate_per_litre(fat, snf):>8}{payout(litres, fat, snf):>10}")
    if rejected:
        print("\nRejected entries")
        for line_no, row, reason in rejected:
            print(f"  line {line_no}: {','.join(row)}  ->  {reason}")
    print("\nTen-day totals")
    totals = ten_day_totals(valid)
    for farmer_id, total in sorted(totals.items()):
        print(f"  {farmer_id:<6}Rs {total:>10}")
    print(f"  {'All':<6}Rs {sum(totals.values(), Decimal('0.00')):>10}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "entries.csv")
