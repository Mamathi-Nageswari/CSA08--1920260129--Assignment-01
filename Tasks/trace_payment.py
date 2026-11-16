"""Task 8 - The pseudocode written as Python, printing a trace of every step."""
BASE_RATE, FAT_STEP_VALUE, SNF_STEP_VALUE = 30.00, 0.40, 0.30

entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]

total = 0.0
print(f"{'#':>2} {'litres':>6} {'fat':>4} {'snf':>4} {'valid':>6} {'fat_steps':>9} "
      f"{'snf_steps':>9} {'rate':>6} {'amount':>8} {'total':>8}")
for number, (litres, fat, snf) in enumerate(entries, start=1):
    valid = litres > 0 and 2.0 <= fat <= 7.0 and 7.0 <= snf <= 10.0
    if valid:
        fat_steps = round((fat - 3.5) / 0.1)
        snf_steps = round((snf - 8.5) / 0.1)
        rate = round(BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE, 2)
        amount = round(litres * rate, 2)
        total = round(total + amount, 2)
        print(f"{number:>2} {litres:>6} {fat:>4} {snf:>4} {'yes':>6} {fat_steps:>9} "
              f"{snf_steps:>9} {rate:>6.2f} {amount:>8.2f} {total:>8.2f}")
    else:
        print(f"{number:>2} {litres:>6} {fat:>4} {snf:>4} {'no':>6}  invalid entry")
print("OUTPUT total =", f"{total:.2f}")
