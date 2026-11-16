"""Task 8 - Alternative concept: store every entry in a list vs keep a running total."""
import random
import sys
import time
import tracemalloc

sys.path.insert(0, "../Task07")
from milkrate import payout


def readings(n):
    """Produces n synthetic readings one at a time (like a clerk typing them)."""
    rnd = random.Random(8)
    for _ in range(n):
        yield (round(rnd.uniform(2, 20), 1), round(rnd.uniform(2.5, 6.0), 1),
               round(rnd.uniform(7.5, 9.5), 1))


def stored_total(n):
    """Reads everything into a list first, then adds."""
    entries = list(readings(n))
    return round(sum(payout(*e) for e in entries), 2)


def running_total(n):
    """Adds each entry as soon as it is read; nothing is kept."""
    total = 0.0
    for e in readings(n):
        total += payout(*e)
    return round(total, 2)


print(f"{'n':>7} | {'stored: time':>12} {'peak memory':>12} | {'running: time':>13} {'peak memory':>12}")
for n in (300, 6000, 150000):
    row = []
    for func in (stored_total, running_total):
        tracemalloc.start()
        start = time.perf_counter()
        total = func(n)
        seconds = time.perf_counter() - start
        peak = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        row.append((total, seconds, peak))
    assert row[0][0] == row[1][0]
    print(f"{n:>7} | {row[0][1] * 1000:9.1f} ms {row[0][2] / 1024:9.1f} KB |"
          f" {row[1][1] * 1000:10.1f} ms {row[1][2] / 1024:9.1f} KB")
