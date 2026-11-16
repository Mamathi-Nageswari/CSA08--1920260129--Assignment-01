"""Task 1 - The data of one payment: inputs, constants, outputs and rules."""

# Values that never change during a run (named constants)
BASE_RATE = 30.00        # Rs per litre at the standard quality
STD_FAT = 3.5            # standard fat %
STD_SNF = 8.5            # standard SNF %
STEP = 0.1               # size of one quality step (%)
FAT_STEP_VALUE = 0.40    # Rs per litre for each 0.1 % of fat
SNF_STEP_VALUE = 0.30    # Rs per litre for each 0.1 % of SNF
FAT_MIN, FAT_MAX = 2.0, 7.0
SNF_MIN, SNF_MAX = 7.0, 10.0
LITRES_MAX = 100.0       # assumed upper limit for one farmer in one shift
SHIFTS = ("M", "E")      # morning, evening
DAYS_PER_PERIOD = 10

# One entry = one tuple: (farmer_id, day, shift, litres, fat, snf)
entries = [
    ("F001", 1, "M", 10.0, 3.5, 8.5),
    ("F001", 1, "E", 8.5, 4.2, 8.7),
    ("F002", 1, "M", 12.0, 3.1, 8.3),
]


def check(entry):
    """Returns a list of the rules this entry breaks (empty list = valid)."""
    farmer_id, day, shift, litres, fat, snf = entry
    problems = []
    if not (farmer_id.startswith("F") and farmer_id[1:].isdigit()):
        problems.append("farmer ID must look like F001")
    if not 1 <= day <= DAYS_PER_PERIOD:
        problems.append("day must be 1 to 10")
    if shift not in SHIFTS:
        problems.append("shift must be M or E")
    if not 0 < litres <= LITRES_MAX:
        problems.append("litres must be above 0 and at most 100")
    if not FAT_MIN <= fat <= FAT_MAX:
        problems.append("fat must be 2.0 to 7.0")
    if not SNF_MIN <= snf <= SNF_MAX:
        problems.append("SNF must be 7.0 to 10.0")
    return problems


if __name__ == "__main__":
    print(f"{'Value':12}{'Example':>10}  Python type")
    names = ("farmer_id", "day", "shift", "litres", "fat", "snf")
    for name, value in zip(names, entries[1]):
        print(f"{name:12}{value!s:>10}  {type(value).__name__}")
    print()
    tests = entries + [("F003", 2, "E", -4.0, 3.6, 8.5),
                       ("F004", 2, "M", 9.0, 7.5, 8.5),
                       ("X9", 11, "N", 5.0, 3.5, 6.0)]
    for entry in tests:
        problems = check(entry)
        print(entry, "->", "valid" if not problems else "; ".join(problems))
