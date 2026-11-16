"""Task 10 - Float vs Decimal vs integer paise at 300, 6,000 and 150,000 payments.

The readings are synthetic (random.seed(2026)), one decimal place, like the clerk's register.
"""
import random
import sys
import time
from decimal import Decimal, ROUND_HALF_UP

sys.path.insert(0, "../Task09")
import calculator as exact  # the Decimal calculator from Task 9

SIZES = (300, 6000, 150000)


def make_readings(n, seed=2026):
    """Returns n (litres, fat, snf) readings as text, as the clerk would type them."""
    rnd = random.Random(seed)
    return [(f"{rnd.uniform(2, 20):.1f}", f"{rnd.uniform(2.5, 6.0):.1f}",
             f"{rnd.uniform(7.5, 9.5):.1f}") for _ in range(n)]


def float_rate(fat, snf):
    return 30.00 + round((fat - 3.5) / 0.1) * 0.40 + round((snf - 8.5) / 0.1) * 0.30


def total_float_raw(rows):
    """float, nothing rounded."""
    return sum(float(l) * float_rate(float(f), float(s)) for l, f, s in rows)


def total_float_rounded(rows):
    """float, each payment rounded with round(x, 2)."""
    return sum(round(float(l) * round(float_rate(float(f), float(s)), 2), 2) for l, f, s in rows)


def total_float_truncated(rows):
    """float, each payment cut to paise with int(x * 100) / 100 (the volunteer's way)."""
    return sum(int(float(l) * round(float_rate(float(f), float(s)), 2) * 100) / 100 for l, f, s in rows)


def total_decimal(rows):
    """Decimal, each payment rounded to the paisa (what the bank pays)."""
    return sum((exact.payout(Decimal(l), Decimal(f), Decimal(s)) for l, f, s in rows), Decimal("0"))


def paise_rate(fat_tenths, snf_tenths):
    """Rate in paise from readings in tenths of a percent (whole numbers only)."""
    return 3000 + (fat_tenths - 35) * 40 + (snf_tenths - 85) * 30


def total_paise(rows):
    """int paise: litres in tenths x rate in paise = tenths of paise, exact."""
    total = 0
    for l, f, s in rows:
        tenth_paise = int(l.replace(".", "")) * paise_rate(int(f.replace(".", "")), int(s.replace(".", "")))
        total += (tenth_paise + 5) // 10   # round half up to the paisa
    return total


def timed(func, rows):
    start = time.perf_counter()
    value = func(rows)
    return value, time.perf_counter() - start


if __name__ == "__main__":
    for n in SIZES:
        rows = make_readings(n)
        d, td = timed(total_decimal, rows)
        fr, tfr = timed(total_float_raw, rows)
        fo, tfo = timed(total_float_rounded, rows)
        ft, tft = timed(total_float_truncated, rows)
        p, tp = timed(total_paise, rows)
        print(f"n = {n:,} payments")
        print(f"  Decimal (bank)        Rs {d:>16}           {td * 1000:8.1f} ms")
        print(f"  float, not rounded    Rs {fr!r:>16}  diff {float(Decimal(repr(fr)) - d):+.2e} {tfr * 1000:8.1f} ms")
        print(f"  float, round(x, 2)    Rs {fo!r:>16}  diff {float(Decimal(repr(fo)) - d):+.2e} {tfo * 1000:8.1f} ms")
        print(f"  float, int(x*100)/100 Rs {ft:>16.2f}  diff {float(Decimal(f'{ft:.2f}') - d):+.2e} {tft * 1000:8.1f} ms")
        print(f"  int paise             Rs {p // 100:>13}.{p % 100:02d}  diff "
              f"{float(Decimal(p) / 100 - d):+.2e} {tp * 1000:8.1f} ms")
        print(f"  round(float total,2) == bank total? {round(fr, 2) == float(d)}"
              f"    rounded floats printed as {fo:.2f}")
