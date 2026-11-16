"""Task 5 - Alternative concept: checking with str methods vs try/except ValueError."""
import math
import timeit

from read_entries import looks_like_number


def parse_with_check(text):
    """Look before you leap: test the text, then convert."""
    text = text.strip()
    return float(text) if looks_like_number(text) else None


def parse_with_try(text):
    """Easier to ask forgiveness: convert, and catch the error."""
    try:
        value = float(text)
    except ValueError:
        return None
    return value if math.isfinite(value) else None


samples = ["8.5", " 8.5 ", "8,5", "eight", "1e2", "nan", "-3.0", ".5"]
print(f"{'input':>9} | {'str check':>9} | {'try/except':>10}")
for text in samples:
    print(f"{text!r:>9} | {parse_with_check(text)!s:>9} | {parse_with_try(text)!s:>10}")

print("\nTime per entry (average of 200,000)")
for text in ("8.5", "eight"):
    for func in (parse_with_check, parse_with_try):
        t = timeit.timeit(lambda: func(text), number=200_000) / 200_000
        print(f"{func.__name__:17} {text!r:8}: {t * 1e9:5.0f} ns")
