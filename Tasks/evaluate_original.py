"""Task 12 B - The original milkrate module (Task 7) given the new analyser readings."""
import sys
from decimal import Decimal

sys.path.insert(0, "../Task07")
import milkrate
import milkrate2

print(f"{'fat':>5} {'snf':>5} {'float steps':>20} {'round()':>7} {'old rate':>8} | "
      f"{'exact steps':>11} {'new rate':>8}")
for fat, snf in ((4.25, 8.63), (4.35, 8.5), (4.45, 8.5), (3.05, 8.5), (4.24, 8.5), (4.26, 8.5)):
    raw = (fat - 3.5) / 0.1
    new = milkrate2.rate_per_litre(Decimal(str(fat)), Decimal(str(snf)), milkrate2.RATE_CARDS["regular"])
    print(f"{fat:>5} {snf:>5} {raw!r:>20} {round(raw):>7} {milkrate.rate_per_litre(fat, snf):>8.2f} | "
          f"{milkrate2.steps(Decimal(str(fat)), milkrate2.STD_FAT):>11} {new:>8}")

print("\nThe old module has one rate card only:")
print("  milkrate.BASE_RATE =", milkrate.BASE_RATE, "| FAT_STEP_VALUE =", milkrate.FAT_STEP_VALUE)
print("  To pay May milk the constants must be edited, then edited back on 1 July,")
print("  and a bill that is re-run later for May would use whatever values are in the file.")
print("  There is no function for the 500-litre bonus and no idea of a ten-day period.")
