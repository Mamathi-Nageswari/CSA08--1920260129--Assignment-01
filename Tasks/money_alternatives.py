"""Task 2 - Alternative concept: Decimal vs integer paise vs float with round()."""
import sys
import timeit
from decimal import Decimal

payments = ["33.40"] * 1000 + ["0.10"] * 3
BANK_TOTAL = "33400.30"


def total_decimal(items):
    """Exact total using Decimal created from the text."""
    total = Decimal("0")
    for amount in items:
        total += Decimal(amount)
    return total


def to_paise(text):
    """Converts '33.40' to 3340 without using float."""
    rupees, _, paise = text.partition(".")
    return int(rupees) * 100 + int((paise + "00")[:2])


def total_paise(items):
    """Exact total kept as a whole number of paise (int)."""
    total = 0
    for amount in items:
        total += to_paise(amount)
    return total


def total_float_round(items):
    """Float total, rounded to 2 decimals after every addition."""
    total = 0.0
    for amount in items:
        total = round(total + float(amount), 2)
    return total


def total_float(items):
    """Plain float total, no rounding."""
    total = 0.0
    for amount in items:
        total += float(amount)
    return total


paise = total_paise(payments)
results = {
    "float (no round)": f"{total_float(payments)!r}",
    "float + round()": f"{total_float_round(payments)!r}",
    "Decimal": str(total_decimal(payments)),
    "int paise": f"{paise} paise = Rs {paise // 100}.{paise % 100:02d}",
}
print(f"Bank total expected : Rs {BANK_TOTAL}")
for name, value in results.items():
    print(f"{name:20}: {value}")

print("\nMemory per value (sys.getsizeof, bytes)")
print(f"{'float 33.4':20}: {sys.getsizeof(33.4)}")
print(f"{'int 3340 (paise)':20}: {sys.getsizeof(3340)}")
print(f"{'Decimal(33.40)':20}: {sys.getsizeof(Decimal('33.40'))}")

print("\nTime per addition (average of 1,000,000 additions)")
setup = "from decimal import Decimal; a=33.4; b=0.1; c=3340; d=10; e=Decimal('33.40'); f=Decimal('0.10')"
tests = {"float a + b": "a + b", "round(a + b, 2)": "round(a + b, 2)",
         "int c + d": "c + d", "Decimal e + f": "e + f"}
for name, stmt in tests.items():
    seconds = timeit.timeit(stmt, setup=setup, number=1_000_000)
    print(f"{name:20}: {seconds * 1000:6.1f} ns")

print("\nDoes each method give the bank total for n payments of Rs 33.40?")
for n in (300, 6000, 150000):
    items = ["33.40"] * n
    exact = Decimal("33.40") * n
    f = total_float(items)
    fr = total_float_round(items)
    d = total_decimal(items)
    p = total_paise(items)
    print(f"n={n:>6}: exact {str(exact):>10}  float {f!r:<20} float+round {fr!r:<10} "
          f"Decimal {str(d):>10}  paise {p}")
