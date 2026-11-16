"""Task 5 - What int() and float() do with the clerk's typing mistakes."""
for text in ("8.5", " 8.5 ", "8,5", "eight", "", "10", "1e2", "nan"):
    try:
        print(f"float({text!r:8}) = {float(text)}")
    except ValueError as error:
        print(f"float({text!r:8}) -> ValueError: {error}")
for text in ("10", "10.0"):
    try:
        print(f"int({text!r:6}) = {int(text)}")
    except ValueError as error:
        print(f"int({text!r:6}) -> ValueError: {error}")
