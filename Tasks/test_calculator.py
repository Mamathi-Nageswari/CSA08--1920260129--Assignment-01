"""Task 9 - Automatic tests for calculator.py (run: python test_calculator.py)."""
from decimal import Decimal as D

from calculator import check_entry, payout, rate_per_litre, ten_day_totals

passed = 0


def check(case, expected, actual):
    """Prints one row of the test table and stops with AssertionError on a mismatch."""
    global passed
    status = "PASS" if expected == actual else "FAIL"
    print(f"{case:<36}{str(expected):<34}{str(actual):<34}{status}")
    assert expected == actual, case
    passed += 1


print(f"{'Case':<36}{'Expected':<34}{'Actual':<34}Result")
# Normal entries in each direction
check("fat up, SNF up (4.2, 8.7)", D("33.40"), rate_per_litre(D("4.2"), D("8.7")))
check("fat down, SNF down (3.1, 8.3)", D("27.80"), rate_per_litre(D("3.1"), D("8.3")))
check("fat up, SNF down (4.0, 8.2)", D("31.10"), rate_per_litre(D("4.0"), D("8.2")))
check("fat down, SNF up (3.0, 9.0)", D("29.50"), rate_per_litre(D("3.0"), D("9.0")))
check("fat 4.1 (float: 5.99.. steps)", D("32.40"), rate_per_litre(D("4.1"), D("8.5")))
# Boundary entries
check("standard 3.5 / 8.5", D("30.00"), rate_per_litre(D("3.5"), D("8.5")))
check("lowest fat 2.0", D("24.00"), rate_per_litre(D("2.0"), D("8.5")))
check("highest fat 7.0", D("44.00"), rate_per_litre(D("7.0"), D("8.5")))
check("fat 2.0 accepted", True, check_entry(["F1", "1", "M", "5", "2.0", "8.5"])[1] is None)
check("fat 7.0 accepted", True, check_entry(["F1", "1", "M", "5", "7.0", "8.5"])[1] is None)
check("' 8.5 ' and '8,6' accepted", "8.5 and 8.6",
      "{0[3]} and {0[5]}".format(check_entry(["F1", "1", "M", " 8.5 ", "3.6", "8,6"])[0]))
# Invalid entries
check("text 'eight' for litres", "'eight' is not a number",
      check_entry(["F1", "1", "M", "eight", "3.5", "8.5"])[1])
check("negative quantity -4", "litres -4 must be > 0 and <= 100",
      check_entry(["F1", "1", "M", "-4", "3.5", "8.5"])[1])
check("fat 7.1 outside range", "fat 7.1 must be 2.0 to 7.0",
      check_entry(["F1", "1", "M", "5", "7.1", "8.5"])[1])
check("fat 1.9 outside range", "fat 1.9 must be 2.0 to 7.0",
      check_entry(["F1", "1", "M", "5", "1.9", "8.5"])[1])
check("zero litres", "litres 0 must be > 0 and <= 100",
      check_entry(["F1", "1", "M", "0", "3.5", "8.5"])[1])
# Five entries calculated by hand
hand = [("F001", 1, "M", D("10"), D("3.5"), D("8.5")), ("F001", 1, "E", D("8.5"), D("4.2"), D("8.7")),
        ("F001", 2, "M", D("12"), D("3.1"), D("8.3")), ("F001", 2, "E", D("7.5"), D("5.0"), D("9.0")),
        ("F001", 3, "M", D("9.3"), D("2.8"), D("8.1"))]
for expected, entry in zip(("300.00", "283.90", "333.60", "281.25", "241.80"), hand):
    check(f"payout {entry[3]} L, {entry[4]}, {entry[5]}", D(expected), payout(*entry[3:]))
check("ten-day total of the 5 entries", D("1440.55"), ten_day_totals(hand)["F001"])
print(f"\nAll {passed} tests passed.")
