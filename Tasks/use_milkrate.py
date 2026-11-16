"""Task 7 - A separate script that imports the milkrate module in three ways."""
import sys
import time

print("__name__ in this script:", __name__)

start = time.perf_counter()
import milkrate                      # 1. whole module, use milkrate.payout
first = time.perf_counter() - start
print("milkrate.__name__ when imported:", milkrate.__name__)
print("import milkrate             -> milkrate.payout(8.5, 4.2, 8.7) =",
      milkrate.payout(8.5, 4.2, 8.7))

from milkrate import payout          # 2. one name copied into this script
print("from milkrate import payout -> payout(12, 3.1, 8.3) =", payout(12, 3.1, 8.3))

start = time.perf_counter()
import milkrate as mr                # 3. same module, shorter alias
second = time.perf_counter() - start
print("import milkrate as mr       -> mr.rate_per_litre(4.2, 8.7) =",
      mr.rate_per_litre(4.2, 8.7))
print("mr is milkrate:", mr is milkrate, "(the module object is shared)")

print(f"\nfirst import  : {first * 1e6:8.1f} microseconds (file found, compiled, run)")
print(f"second import : {second * 1e6:8.1f} microseconds (taken from sys.modules)")
print("'milkrate' in sys.modules:", "milkrate" in sys.modules)
print("milkrate was loaded from :", milkrate.__file__)
print("\nWhere Python looks for modules (sys.path):")
for folder in sys.path[:4]:
    print("  ", folder)

import math
import decimal
print("\nstandard modules:", "math.floor(-2.5) =", math.floor(-2.5), "|",
      "decimal.Decimal('8.5') * 2 =", decimal.Decimal("8.5") * 2)
