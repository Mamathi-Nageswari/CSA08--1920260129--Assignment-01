"""Task 4 - Expressions for the steps, the rate and the amount, and their surprises."""
import math

BASE_RATE, STD_FAT, STD_SNF, STEP_SIZE = 30.00, 3.5, 8.5, 0.1
FAT_STEP_VALUE, SNF_STEP_VALUE = 0.40, 0.30

litres, fat, snf = 8.5, 4.2, 8.7

raw_fat_steps = (fat - STD_FAT) / STEP_SIZE
fat_steps = round((fat - STD_FAT) / STEP_SIZE)
snf_steps = round((snf - STD_SNF) / STEP_SIZE)
rate = round(BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE, 2)
amount = round(litres * rate, 2)
print("(fat - STD_FAT) / STEP_SIZE  =", raw_fat_steps)
print("fat_steps  = round(...)      =", fat_steps)
print("snf_steps                    =", snf_steps)
print("rate                         =", rate)
print("amount                       =", amount)

print("\nPrecedence and associativity")
print("-2 ** 2        =", -2 ** 2, "  (** before unary minus: -(2**2))")
print("(-2) ** 2      =", (-2) ** 2)
print("2 ** 3 ** 2    =", 2 ** 3 ** 2, " (** is right-associative: 2**(3**2))")
print("(2 ** 3) ** 2  =", (2 ** 3) ** 2)
print("30 - 4 - 1     =", 30 - 4 - 1, "  (- is left-associative: (30-4)-1)")
print("30 + 7 * 0.40  =", 30 + 7 * 0.40, "(* before +)")
print("100 / 10 * 2   =", 100 / 10 * 2, " (left to right, not 100/(10*2))")

print("\nSurprises")
print("4.2 - 3.5               =", 4.2 - 3.5)
print("(4.2 - 3.5) / 0.1       =", (4.2 - 3.5) / 0.1)
print("(4.1 - 3.5) / 0.1       =", (4.1 - 3.5) / 0.1)
print("int((4.1 - 3.5) / 0.1)  =", int((4.1 - 3.5) / 0.1), " <- one step lost")
print("round(2.5), round(3.5)  =", round(2.5), round(3.5), " (round half to even)")
print("round(2.675, 2)         =", round(2.675, 2), "(2.675 is stored as 2.67499999...)")
print("0.1 * 3                 =", 0.1 * 3)

print("\nround(), int() and math.floor() for negative values")
print(f"{'x':>6} {'round':>6} {'int':>6} {'floor':>6}")
for x in (-2.7, -2.5, -2.3, -0.5, 2.7):
    print(f"{x:>6} {round(x):>6} {int(x):>6} {math.floor(x):>6}")

print("\nComparison chaining and Boolean operators")
for fat in (1.9, 2.0, 4.2, 7.0, 7.1):
    print(f"fat={fat}: 2.0 <= fat <= 7.0 -> {2.0 <= fat <= 7.0}")
snf = 8.7
print("2.0 <= 4.2 <= 7.0 and 7.0 <= snf <= 10.0 ->", 2.0 <= 4.2 <= 7.0 and 7.0 <= snf <= 10.0)
print("not (fat < 2.0 or fat > 7.0) with fat=7.1 ->", not (7.1 < 2.0 or 7.1 > 7.0))
