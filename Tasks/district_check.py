"""Task 11 - Is the recommended (Decimal, round each payment half up) design fast and exact
at district-union scale? 150,000 farmers x 20 entries (10 days x 2 shifts) = 3,000,000 entries."""
import sys
import time
from decimal import Decimal

sys.path.insert(0, "../Task09")
sys.path.insert(0, "../Task10")
from calculator import payout, rate_per_litre
from compare_scales import make_readings, total_paise

rows = make_readings(150000)
dec_rows = [(Decimal(l), Decimal(f), Decimal(s)) for l, f, s in rows]

start = time.perf_counter()
total = Decimal("0")
for _ in range(20):
    for l, f, s in dec_rows:
        total += payout(l, f, s)
seconds = time.perf_counter() - start

paise = total_paise(rows) * 20
print(f"entries                : {len(dec_rows) * 20:,}")
print(f"Decimal total          : Rs {total:,}")
print(f"int paise total (check): Rs {paise // 100:,}.{paise % 100:02d}")
print(f"agree to the paisa     : {total == Decimal(paise) / 100}")
print(f"time                   : {seconds:.1f} s for the whole district ten-day run")
