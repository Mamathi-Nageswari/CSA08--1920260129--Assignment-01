"""Task 1 - Alternative concept: three separate variables per entry vs one list of tuples."""
import sys
import time

# Design 1: separate variables. For 300 farmers this needs 900 names
# (litres1, fat1, snf1 ... litres300, fat300, snf300) and 300 copies of the
# same line of code. Only three are written here, the rest would be the same.
litres1, fat1, snf1 = 10.0, 3.5, 8.5
litres2, fat2, snf2 = 8.5, 4.2, 8.7
litres3, fat3, snf3 = 12.0, 3.1, 8.3
total_1 = 0.0
total_1 += litres1 * (30 + round((fat1 - 3.5) / 0.1) * 0.40 + round((snf1 - 8.5) / 0.1) * 0.30)
total_1 += litres2 * (30 + round((fat2 - 3.5) / 0.1) * 0.40 + round((snf2 - 8.5) / 0.1) * 0.30)
total_1 += litres3 * (30 + round((fat3 - 3.5) / 0.1) * 0.40 + round((snf3 - 8.5) / 0.1) * 0.30)
print(f"Design 1 (separate variables), 3 entries : Rs {total_1:.2f}")

# Design 2: one tuple per entry inside a list. The same loop works for any n.
entries = [(10.0, 3.5, 8.5), (8.5, 4.2, 8.7), (12.0, 3.1, 8.3)]


def total_of(entries):
    """Adds the amount of every (litres, fat, snf) entry."""
    total = 0.0
    for litres, fat, snf in entries:
        total += litres * (30 + round((fat - 3.5) / 0.1) * 0.40
                           + round((snf - 8.5) / 0.1) * 0.30)
    return total


print(f"Design 2 (list of tuples),     3 entries : Rs {total_of(entries):.2f}")

# Design 1 would need the code itself to grow with n: generate it to count lines.
for n in (300, 6000, 150000):
    print(f"n={n:>6}: design 1 needs {3 * n:>6} variable names and {n:>6} lines of code;"
          f" design 2 needs 1 list and 1 loop")

print("\nDesign 2: time and space for n entries")
for n in (300, 6000, 150000):
    data = entries * (n // 3)
    start = time.perf_counter()
    total_of(data)
    ms = (time.perf_counter() - start) * 1000
    size = sys.getsizeof(data) + sum(sys.getsizeof(e) for e in data[:3]) * (n // 3)
    print(f"n={n:>6}: time {ms:8.2f} ms, list + tuples about {size / 1024:8.1f} KB")
