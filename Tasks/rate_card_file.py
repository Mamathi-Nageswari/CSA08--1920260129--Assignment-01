"""Task 11 - Alternative concept: reading the rate card from a JSON file at start-up."""
import json
import sys
import time
from decimal import Decimal, ROUND_HALF_UP

PAISA = Decimal("0.01")


def load_rate_card(path="rate_card.json"):
    """Reads the rate card; values are kept as text in the file so Decimal stays exact."""
    with open(path) as file:
        raw = json.load(file)
    return {key: Decimal(value) for key, value in raw.items()}


def rate_per_litre(card, fat, snf):
    """Price per litre using a rate card dictionary."""
    fat_steps = ((fat - card["std_fat"]) / card["step_size"]).to_integral_value(ROUND_HALF_UP)
    snf_steps = ((snf - card["std_snf"]) / card["step_size"]).to_integral_value(ROUND_HALF_UP)
    rate = card["base_rate"] + fat_steps * card["fat_step_value"] + snf_steps * card["snf_step_value"]
    return rate.quantize(PAISA, ROUND_HALF_UP)


if __name__ == "__main__":
    start = time.perf_counter()
    card = load_rate_card()
    load_time = time.perf_counter() - start
    size = sys.getsizeof(card) + sum(sys.getsizeof(k) + sys.getsizeof(v) for k, v in card.items())
    print("rate card read from rate_card.json:")
    for key, value in card.items():
        print(f"  {key:15} {value}")
    print(f"start-up cost: {load_time * 1e6:.0f} microseconds, about {size} bytes in memory")
    print("rate for fat 4.2, SNF 8.7:", rate_per_litre(card, Decimal("4.2"), Decimal("8.7")))

    revised = dict(card, fat_step_value=Decimal("0.45"), base_rate=Decimal("32.00"))
    print("same code, April-June values (base 32.00, fat step 0.45):",
          rate_per_litre(revised, Decimal("4.2"), Decimal("8.7")))
    try:
        json.loads('{"base_rate": "30.00",}')
    except json.JSONDecodeError as error:
        print("a typing mistake in the file is caught at start-up:", error)
