"""Task 3 - One set of named constants for the rate card and the limits."""

# Rate card (change a rate here and nowhere else)
BASE_RATE = 30.00          # Rs per litre at 3.5 % fat and 8.5 % SNF
STD_FAT = 3.5              # standard fat %
STD_SNF = 8.5              # standard SNF %
STEP_SIZE = 0.1            # one quality step, in %
FAT_STEP_VALUE = 0.40      # Rs per litre for each step of fat
SNF_STEP_VALUE = 0.30      # Rs per litre for each step of SNF

# Limits of a valid entry
FAT_MIN, FAT_MAX = 2.0, 7.0
SNF_MIN, SNF_MAX = 7.0, 10.0
LITRES_MAX = 100.0
SHIFTS = ("M", "E")
DAYS_PER_PERIOD = 10

if __name__ == "__main__":
    for name, value in list(globals().items()):
        if name.isupper():
            print(f"{name:15} = {value!r:12} {type(value).__name__}")
