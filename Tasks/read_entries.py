"""Task 5 - Reading the clerk's entries safely and printing an aligned slip."""

FAT_MIN, FAT_MAX = 2.0, 7.0
SNF_MIN, SNF_MAX = 7.0, 10.0
LITRES_MAX = 100.0


def looks_like_number(text):
    """True if text is digits with at most one decimal point (checked with str methods)."""
    text = text.strip()
    whole, dot, fraction = text.partition(".")
    if whole == "" and fraction == "":
        return False
    return (whole == "" or whole.isdigit()) and (fraction == "" or fraction.isdigit())


def read_number(prompt, low, high):
    """Asks again and again until the clerk types a number between low and high."""
    while True:
        text = input(prompt)
        cleaned = text.strip().replace(",", ".", 1) if text.count(",") == 1 else text.strip()
        if cleaned != text.strip():
            print(f"  read '{text}' as {cleaned} (comma taken as decimal point)")
        if not looks_like_number(cleaned):
            print(f"  '{text}' is not a number, please type it again (example 8.5)")
            continue
        value = float(cleaned)
        if not low <= value <= high:
            print(f"  {value} is outside {low} to {high}, please check the reading")
            continue
        return value


def rate_per_litre(fat, snf):
    """Price per litre in Rs, rounded to 2 decimals."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(30.00 + fat_steps * 0.40 + snf_steps * 0.30, 2)


if __name__ == "__main__":
    print("input() always gives a str:", type(input("Type 8.5 : ")))
    farmer = input("Farmer ID : ").strip().upper()
    litres = read_number("Litres    : ", 0.1, LITRES_MAX)
    fat = read_number("Fat %     : ", FAT_MIN, FAT_MAX)
    snf = read_number("SNF %     : ", SNF_MIN, SNF_MAX)
    rate = rate_per_litre(fat, snf)
    amount = round(litres * rate, 2)
    print()
    print(f"{'Farmer':<8}{'Litres':>8}{'Fat':>6}{'SNF':>6}{'Rate':>8}{'Amount':>10}")
    print(f"{farmer:<8}{litres:>8.1f}{fat:>6.1f}{snf:>6.1f}{rate:>8.2f}{amount:>10.2f}")
