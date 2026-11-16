"""Rate card module, revised for the milk analyser, seasonal rates and the 500-litre bonus."""
from datetime import date
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

STD_FAT = Decimal("3.5")
STD_SNF = Decimal("8.5")
STEP_SIZE = Decimal("0.1")
RATE_CARDS = {
    "April-June": {"base": Decimal("32.00"), "fat_step": Decimal("0.45"), "snf_step": Decimal("0.30")},
    "regular":    {"base": Decimal("30.00"), "fat_step": Decimal("0.40"), "snf_step": Decimal("0.30")},
}
SEASON_MONTHS = {4: "April-June", 5: "April-June", 6: "April-June"}
BONUS_LIMIT = Decimal("500")          # litres in a ten-day period; exactly 500 gets no bonus
BONUS_PER_LITRE = Decimal("0.50")     # paid on all litres of the period
READING_PLACES = 2                    # the analyser sends two decimal places
FAT_MIN, FAT_MAX = Decimal("2.0"), Decimal("7.0")
SNF_MIN, SNF_MAX = Decimal("7.0"), Decimal("10.0")
PAISA = Decimal("0.01")


def parse_reading(text, low, high):
    """Converts an analyser value such as '4.25' to Decimal; rejects text, more than
    two decimals and values outside low..high by raising ValueError."""
    try:
        value = Decimal(str(text).strip())
    except InvalidOperation:
        raise ValueError(f"'{text}' is not a number") from None
    if not value.is_finite() or value.as_tuple().exponent < -READING_PLACES:
        raise ValueError(f"'{text}' has over {READING_PLACES} decimals")
    if not low <= value <= high:
        raise ValueError(f"{value} must be {low} to {high}")
    return value


def season_for(day):
    """Returns the season name for a datetime.date."""
    return SEASON_MONTHS.get(day.month, "regular")


def rate_card_for(day):
    """Returns the rate card that applies on the given date."""
    return RATE_CARDS[season_for(day)]


def steps(value, standard):
    """Exact (pro-rata) number of 0.1 % steps: 4.25 % fat is 7.5 steps above 3.5 %."""
    return (value - standard) / STEP_SIZE


def rate_per_litre(fat, snf, card):
    """Price per litre for the given readings and rate card, rounded half up to the paisa."""
    rate = card["base"] + steps(fat, STD_FAT) * card["fat_step"] + steps(snf, STD_SNF) * card["snf_step"]
    return rate.quantize(PAISA, rounding=ROUND_HALF_UP)


def payout(litres, fat, snf, card):
    """Amount for one entry, rounded half up to the paisa."""
    return (litres * rate_per_litre(fat, snf, card)).quantize(PAISA, rounding=ROUND_HALF_UP)


def bonus(period_litres):
    """Rs 0.50 per litre on all litres if the period total is more than 500 litres."""
    if period_litres > BONUS_LIMIT:
        return (period_litres * BONUS_PER_LITRE).quantize(PAISA, rounding=ROUND_HALF_UP)
    return Decimal("0.00")


def period_of(day):
    """Ten-day period of a date: (year, month, 1 | 2 | 3) for days 1-10, 11-20, 21-end."""
    return day.year, day.month, min((day.day - 1) // 10 + 1, 3)


def ten_day_bills(entries):
    """entries: (farmer_id, date, shift, litres, fat, snf). Returns
    {(farmer_id, period): {"litres", "milk", "bonus", "total"}}."""
    bills = {}
    for farmer_id, day, _shift, litres, fat, snf in entries:
        bill = bills.setdefault((farmer_id, period_of(day)),
                                {"litres": Decimal("0"), "milk": Decimal("0.00")})
        bill["litres"] += litres
        bill["milk"] += payout(litres, fat, snf, rate_card_for(day))
    for bill in bills.values():
        bill["bonus"] = bonus(bill["litres"])
        bill["total"] = bill["milk"] + bill["bonus"]
    return bills


if __name__ == "__main__":
    print("Rate per litre for analyser readings in both seasons")
    print(f"{'fat':>5} {'snf':>5} | {'regular':>8} | {'April-June':>10}")
    for fat, snf in (("3.50", "8.50"), ("4.25", "8.63"), ("4.20", "8.70"), ("3.10", "8.30"), ("2.95", "8.47")):
        f = parse_reading(fat, FAT_MIN, FAT_MAX)
        s = parse_reading(snf, SNF_MIN, SNF_MAX)
        print(f"{fat:>5} {snf:>5} | {rate_per_litre(f, s, RATE_CARDS['regular']):>8} |"
              f" {rate_per_litre(f, s, RATE_CARDS['April-June']):>10}")

    def period(farmer_id, first, litres_each, fat="4.25", snf="8.63"):
        """Twenty entries (10 days x 2 shifts) for one farmer from the date 'first'."""
        return [(farmer_id, first.replace(day=first.day + d), shift, Decimal(litres_each),
                 Decimal(fat), Decimal(snf)) for d in range(10) for shift in "ME"]

    entries = (period("F101", date(2026, 5, 1), "26.0")      # 520 L in May  -> bonus
               + period("F102", date(2026, 5, 1), "25.0")    # 500 L in May  -> no bonus
               + period("F101", date(2026, 7, 1), "26.0"))   # 520 L in July -> bonus, regular rate
    print("\nTen-day bills")
    print(f"{'farmer':<7}{'period':<12}{'season':<11}{'litres':>8}{'milk Rs':>11}{'bonus Rs':>10}{'total Rs':>11}")
    for (farmer_id, (y, m, p)), bill in sorted(ten_day_bills(entries).items()):
        season = season_for(date(y, m, 1))
        print(f"{farmer_id:<7}{y}-{m:02d} P{p:<4}{season:<11}{bill['litres']:>8}{bill['milk']:>11}"
              f"{bill['bonus']:>10}{bill['total']:>11}")
