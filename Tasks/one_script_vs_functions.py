"""Task 6 - Alternative concept: one long script, lambdas, or functions."""
import random
import time

random.seed(8)
entries = [(round(random.uniform(2, 20), 1), round(random.uniform(2.5, 6.0), 1),
            round(random.uniform(7.5, 9.5), 1)) for _ in range(150_000)]

# 1. One long script: the formula is written inline (and copied wherever needed)
start = time.perf_counter()
total_script = 0.0
for litres, fat, snf in entries:
    rate = round(30.00 + round((fat - 3.5) / 0.1) * 0.40 + round((snf - 8.5) / 0.1) * 0.30, 2)
    total_script += round(litres * rate, 2)
t_script = time.perf_counter() - start

# 2. Lambdas: short anonymous functions, no docstrings, one expression each
rate_l = lambda fat, snf: round(30.00 + round((fat - 3.5) / 0.1) * 0.40
                                + round((snf - 8.5) / 0.1) * 0.30, 2)
payout_l = lambda litres, fat, snf: round(litres * rate_l(fat, snf), 2)
start = time.perf_counter()
total_lambda = sum(payout_l(*e) for e in entries)
t_lambda = time.perf_counter() - start

# 3. Named functions with docstrings
from payment_functions import payout
start = time.perf_counter()
total_func = 0.0
for e in entries:
    total_func += payout(*e)
t_func = time.perf_counter() - start

n = len(entries)
print(f"n = {n} entries")
for name, total, t in (("one long script", total_script, t_script),
                       ("lambdas", total_lambda, t_lambda),
                       ("named functions", total_func, t_func)):
    print(f"{name:16}: total Rs {total:14.2f}  time {t * 1000:7.1f} ms"
          f"  ({t / n * 1e9:5.0f} ns per entry)")
print(f"function-call overhead: {(t_func - t_script) / n * 1e9:.0f} ns per entry")
