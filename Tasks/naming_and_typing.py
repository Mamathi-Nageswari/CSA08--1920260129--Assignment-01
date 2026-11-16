"""Task 3 - Naming, 'constants' by convention, dynamic typing and swapping."""
import keyword

from constants import BASE_RATE

# Naming rules: letters, digits and _, cannot start with a digit, not a keyword.
for name in ("fat_percent", "_total", "litres2", "2litres", "class", "snf-value"):
    ok = name.isidentifier() and not keyword.iskeyword(name)
    print(f"{name:12} -> {'valid name' if ok else 'not allowed'}")

# Python has no true constants: an UPPER_CASE name can still be reassigned.
print("\nBASE_RATE before:", BASE_RATE)
BASE_RATE = 99.0          # Python allows this; the convention says do not do it
print("BASE_RATE after :", BASE_RATE, "(changed - nothing stopped it)")

# Dynamic typing: the type belongs to the value, not to the variable.
litres = 10
print("\nlitres =", repr(litres), type(litres).__name__)
litres = "10"
print("litres =", repr(litres), type(litres).__name__)
try:
    print(litres * 2.5)
except TypeError as error:
    print("litres * 2.5 ->", "TypeError:", error)
print("litres * 2   ->", repr(litres * 2), "(string repeated, not doubled)")

# Multiple assignment and swapping
fat, snf = 4.2, 8.7
print("\nfat, snf =", fat, snf)
fat, snf = snf, fat       # the right side is built as a tuple first
print("after swap:", fat, snf)
morning = evening = 0.0   # chained assignment: both names point to 0.0
print("morning, evening =", morning, evening)
