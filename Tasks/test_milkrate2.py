"""Task 12 - Tests for the revised module (both seasons, two-decimal readings, bonus)."""
from datetime import date
from decimal import Decimal as D

from milkrate2 import (FAT_MAX, FAT_MIN, RATE_CARDS, bonus, parse_reading, payout, period_of,
                       rate_card_for, rate_per_litre, season_for, ten_day_bills)

REG, SUM = RATE_CARDS["regular"], RATE_CARDS["April-June"]
passed = 0


def check(case, expected, actual):
    """One row of the test table; stops on a mismatch."""
    global passed
    status = "PASS" if expected == actual else "FAIL"
    print(f"{case:<44}{str(expected):<29}{str(actual):<29}{status}")
    assert expected == actual, case
    passed += 1


def bill(litres_each, first=date(2026, 5, 1)):
    entries = [("F1", first.replace(day=first.day + d), s, D(litres_each), D("3.5"), D("8.5"))
               for d in range(10) for s in "ME"]
    return ten_day_bills(entries)[("F1", period_of(first))]


def rejected(text):
    """Returns the error message parse_reading gives for a fat reading."""
    try:
        parse_reading(text, FAT_MIN, FAT_MAX)
    except ValueError as error:
        return str(error)
    return "accepted"


print(f"{'Case':<44}{'Expected':<29}{'Actual':<29}Result")
check("regular 3.50 / 8.50", D("30.00"), rate_per_litre(D("3.50"), D("8.50"), REG))
check("April-June 3.50 / 8.50", D("32.00"), rate_per_litre(D("3.50"), D("8.50"), SUM))
check("regular 4.25 / 8.63 (7.5 and 1.3 steps)", D("33.39"), rate_per_litre(D("4.25"), D("8.63"), REG))
check("April-June 4.25 / 8.63 (35.765 -> 35.77)", D("35.77"), rate_per_litre(D("4.25"), D("8.63"), SUM))
check("April-June 4.2 / 8.7", D("35.75"), rate_per_litre(D("4.2"), D("8.7"), SUM))
check("April-June 3.1 / 8.3", D("29.60"), rate_per_litre(D("3.1"), D("8.3"), SUM))
check("regular 4.24 -> 4.25: +Rs 0.04", D("0.04"),
      rate_per_litre(D("4.25"), D("8.5"), REG) - rate_per_litre(D("4.24"), D("8.5"), REG))
check("payout 8.5 L April-June 4.25/8.63", D("304.05"), payout(D("8.5"), D("4.25"), D("8.63"), SUM))
check("payout 8.5 L regular 4.2/8.7 (as before)", D("283.90"), payout(D("8.5"), D("4.2"), D("8.7"), REG))
check("31 March is regular", "regular", season_for(date(2027, 3, 31)))
check("1 April is April-June", "April-June", season_for(date(2027, 4, 1)))
check("30 June is April-June", "April-June", season_for(date(2027, 6, 30)))
check("1 July is regular", "regular", season_for(date(2027, 7, 1)))
check("rate card for 15 May has fat step 0.45", D("0.45"), rate_card_for(date(2027, 5, 15))["fat_step"])
check("bonus for exactly 500 L", D("0.00"), bonus(D("500")))
check("bonus for 500.1 L", D("250.05"), bonus(D("500.1")))
check("bonus for 520 L", D("260.00"), bonus(D("520")))
check("May bill 20 x 25 L = 500 L, no bonus", "500.0 L, bonus 0.00",
      "{litres} L, bonus {bonus}".format(**bill("25.0")))
check("May bill 20 x 26 L = 520 L, bonus 260", D("16900.00"), bill("26.0")["total"])
check("July bill 20 x 26 L = 520 L, bonus 260", D("15860.00"), bill("26.0", date(2026, 7, 1))["total"])
check("31st day is in period 3", (2026, 7, 3), period_of(date(2026, 7, 31)))
check("reading '4.255' rejected", "'4.255' has over 2 decimals", rejected("4.255"))
check("reading 'four' rejected", "'four' is not a number", rejected("four"))
check("reading '7.05' rejected (range)", "7.05 must be 2.0 to 7.0", rejected("7.05"))
check("reading ' 4.25 ' accepted", D("4.25"), parse_reading(" 4.25 ", FAT_MIN, FAT_MAX))
print(f"\nAll {passed} tests passed.")
