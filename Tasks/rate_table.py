"""Task 10 - Alternative concept: a dictionary rate table vs recalculating every time."""
import sys
import time
from decimal import Decimal

sys.path.insert(0, "../Task09")
from calculator import rate_per_litre
from compare_scales import make_readings

rows = [(Decimal(l), Decimal(f), Decimal(s)) for l, f, s in make_readings(150000)]

start = time.perf_counter()
total_calc = sum(l * rate_per_litre(f, s) for l, f, s in rows)
t_calc = time.perf_counter() - start

start = time.perf_counter()
table = {}
total_table = Decimal("0")
for l, f, s in rows:
    rate = table.get((f, s))
    if rate is None:
        rate = table[(f, s)] = rate_per_litre(f, s)
    total_table += l * rate
t_table = time.perf_counter() - start

full = {(Decimal(fat) / 10, Decimal(snf) / 10): rate_per_litre(Decimal(fat) / 10, Decimal(snf) / 10)
        for fat in range(20, 71) for snf in range(70, 101)}
size = sys.getsizeof(full) + sum(sys.getsizeof(k) + sys.getsizeof(v) for k, v in full.items())
n = len(rows)
print(f"same total: {total_calc == total_table}  (Rs {total_calc:.2f})")
print(f"recalculate every entry : {t_calc * 1000:7.1f} ms  {t_calc / n * 1e9:6.0f} ns per entry")
print(f"rate table (dict lookup): {t_table * 1000:7.1f} ms  {t_table / n * 1e9:6.0f} ns per entry")
print(f"pairs met in the data k = {len(table)}; all possible pairs = {len(full)} "
      f"(51 fat x 31 SNF), about {size / 1024:.0f} KB")
