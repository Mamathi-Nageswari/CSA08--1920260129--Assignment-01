"""Task 10 - Round each payment, or round only the total?

With the original card every litres x rate product already ends in whole paise,
so a rounding rule only matters once a product has a third decimal. The April-June
card (Rs 0.45 per fat step) with two-decimal analyser readings produces such products.
"""
import random
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

PAISA = Decimal("0.01")


def summer_rate(fat, snf):
    rate = Decimal("32.00") + (fat - Decimal("3.5")) / Decimal("0.1") * Decimal("0.45") \
        + (snf - Decimal("8.5")) / Decimal("0.1") * Decimal("0.30")
    return rate.quantize(PAISA, ROUND_HALF_UP)


rnd = random.Random(2026)
for n in (300, 6000, 150000):
    rows = [(Decimal(f"{rnd.uniform(2, 20):.1f}"), Decimal(f"{rnd.uniform(2.5, 6.0):.2f}"),
             Decimal(f"{rnd.uniform(7.5, 9.5):.2f}")) for _ in range(n)]
    exact_products = [l * summer_rate(f, s) for l, f, s in rows]
    each_half_up = sum(p.quantize(PAISA, ROUND_HALF_UP) for p in exact_products)
    each_half_even = sum(p.quantize(PAISA, ROUND_HALF_EVEN) for p in exact_products)
    only_total = sum(exact_products).quantize(PAISA, ROUND_HALF_UP)
    float_sum = sum(float(l) * float(summer_rate(f, s)) for l, f, s in rows)
    print(f"n = {n:,}")
    print(f"  bank pays (round each, half up)   Rs {each_half_up:>14}")
    print(f"  round each, half even             Rs {each_half_even:>14}   diff {each_half_even - each_half_up:+}")
    print(f"  round only the total              Rs {only_total:>14}   diff {only_total - each_half_up:+}")
    print(f"  float total, then round           Rs {round(float_sum, 2):>14.2f}   diff "
          f"{Decimal(f'{round(float_sum, 2):.2f}') - each_half_up:+}")
