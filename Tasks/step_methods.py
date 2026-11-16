"""Task 4 - Alternative concept: steps by round() vs int() vs math.floor()."""
import math
import timeit

BASE_RATE, FAT_STEP_VALUE = 30.00, 0.40


def rate_for(fat, step_function):
    """Rate per litre at standard SNF, using the given step function."""
    steps = step_function((fat - 3.5) / 0.1)
    return round(BASE_RATE + steps * FAT_STEP_VALUE, 2), steps


print(f"{'fat':>4} {'raw steps':>22} | {'round':>12} | {'int':>12} | {'floor':>12}")
for fat in (4.2, 3.1, 4.1, 3.4, 2.0, 7.0):
    raw = (fat - 3.5) / 0.1
    cells = []
    for func in (round, int, math.floor):
        rate, steps = rate_for(fat, func)
        cells.append(f"{steps:>3} Rs{rate:6.2f}")
    print(f"{fat:>4} {raw!r:>22} | " + " | ".join(cells))

print("\nCost of one step calculation (all are O(1) time, O(1) space)")
for name in ("round", "int", "math.floor"):
    t = timeit.timeit(f"{name}((4.2 - 3.5) / 0.1)", setup="import math", number=1_000_000)
    print(f"{name:10}: {t * 1000:5.0f} ns per call")
