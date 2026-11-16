"""Task 3 - Alternative concept: magic numbers vs named constants vs a RATE_CARD dict."""
import timeit

BASE_RATE, FAT_STEP_VALUE, SNF_STEP_VALUE = 30.0, 0.40, 0.30
RATE_CARD = {"base": 30.0, "fat": 0.40, "snf": 0.30}


def rate_magic(fat, snf):
    return 30.0 + round((fat - 3.5) / 0.1) * 0.40 + round((snf - 8.5) / 0.1) * 0.30


def rate_named(fat, snf):
    return (BASE_RATE + round((fat - 3.5) / 0.1) * FAT_STEP_VALUE
            + round((snf - 8.5) / 0.1) * SNF_STEP_VALUE)


def rate_dict(fat, snf):
    return (RATE_CARD["base"] + round((fat - 3.5) / 0.1) * RATE_CARD["fat"]
            + round((snf - 8.5) / 0.1) * RATE_CARD["snf"])


print("Same rate from all three:", rate_magic(4.2, 8.7), rate_named(4.2, 8.7), rate_dict(4.2, 8.7))

# Count how many places hold the number 0.40 in the volunteer's old program
old_program = open(__file__.replace("magic_vs_dict.py", "old_volunteer_calculator.py")).read()
print("Places where 0.40 is typed in the old program:", old_program.count("0.40"))
print("Places where it is typed with named constants : 1")

n = 1_000_000
for func in (rate_magic, rate_named, rate_dict):
    t = timeit.timeit(lambda: func(4.2, 8.7), number=n)
    print(f"{func.__name__:11}: {t / n * 1e9:6.0f} ns per call")
