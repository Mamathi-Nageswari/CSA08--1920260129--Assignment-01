# CSA08 - Python Programming - Assignment 1
## Payment Calculator for a Village Milk Co-operative (Ksheera)

| | |
|---|---|
| Name | __________________ |
| Register number | __________________ |
| Python version | Python 3.10.12 (any Python 3.10 or newer works) |
| Libraries | Python standard library only; `matplotlib 3.10.9` for the chart in Task 10 (see `requirements.txt`) |

Install the one extra library (only needed for the chart):

```
pip install -r requirements.txt
```

Every program is run from inside its own task folder, for example `cd Task07` and then `python milkrate.py`.
(On Linux/macOS type `python3` instead of `python`.)

## Folder layout

```
Task01 ... Task12   one folder per task: .py source files, input files, output screenshots
requirements.txt    library versions
README.md           this file
```

## How to run each task and what the result was

| Task | Command(s) | Result |
|---|---|---|
| 1 Data | `python data_model.py`<br>`python separate_variables.py` | Every input is one tuple `(farmer_id, day, shift, litres, fat, snf)`. The six validation rules reject a negative quantity, fat outside 2.0-7.0, SNF outside 7.0-10.0, a bad ID, day and shift. A list of tuples needs 1 loop for any n; separate variables would need 3n names and n lines of code. |
| 2 Types | `python` (interactive, commands in `interpreter_session.txt`)<br>`python decimal_total.py`<br>`python decimal_from_float.py`<br>`python money_alternatives.py` | Output matches the expected output: `float : 33400.30000000061`, `Decimal: 33400.30`, `False True`. `Decimal(float(amount))` gives `33400.29999999999857893118278` because the float error is copied into the Decimal. Integer paise and Decimal give the exact bank total; plain float does not. |
| 3 Constants | `python constants.py`<br>`python naming_and_typing.py`<br>`python magic_vs_dict.py` | One set of UPPER_CASE constants. Python does not stop a "constant" from being reassigned. The old volunteer program types 0.40 in 3 places; named constants need 1 change. Speed is the same. |
| 4 Expressions | `python expressions.py`<br>`python step_methods.py` | `(4.2 - 3.5) / 0.1` is `7.000000000000002`, `round()` fixes it to 7. `int()` loses a step for fat 3.1 and 4.1, `math.floor()` for 3.4. `round()` is used. |
| 5 Input | `python conversion_demo.py`<br>`python check_vs_try.py`<br>`python read_entries.py` (type the values) | `"8,5"` and `"eight"` raise `ValueError` in `float()`. `read_entries.py` accepts `" 8.5 "` and `"8,5"`, asks again for `"eight"` and out-of-range values, and prints an aligned slip. |
| 6 Functions | `python payment_functions.py`<br>`python scope_demo.py`<br>`python one_script_vs_functions.py` | `rate_per_litre()`, `payout()`, `is_valid()`, `ten_day_total()` with docstrings. The function-call overhead is about 40 ns per entry (150,000 entries, under 0.1 s). |
| 7 Module | `python milkrate.py`<br>`python use_milkrate.py`<br>`python use_no_main.py`<br>`python copy_vs_import.py` | Table matches the expected output (30.00/300.00, 33.40/283.90, 27.80/333.60). When imported, the table is not printed because `__name__` is `"milkrate"`, not `"__main__"`. A second import is about 0.4 microseconds because the module comes from `sys.modules`. |
| 8 Algorithm | `python trace_payment.py`<br>`python running_vs_stored.py`<br>(`flowchart.png`, made from `flowchart.dot`) | The hand trace for 3 entries gives a total of Rs 917.50. A running total uses about 3 KB of memory for any n; storing 150,000 entries uses about 21 MB. |
| 9 Calculator | `python calculator.py entries.csv`<br>`python test_calculator.py` | Valid entries are paid, 6 invalid entries are rejected with reasons, and the 5 hand-checked entries total Rs 1440.55. All 22 tests pass. |
| 10 Experiments | `python compare_scales.py`<br>`python rounding_rule.py`<br>`python rate_table.py`<br>`python time_chart.py` | Decimal and integer paise agree to the paisa at 300, 6,000 and 150,000 payments. Cutting with `int(x*100)/100` loses Rs 248 at 150,000. Rounding only the total differs from the bank by about Rs 68 at 150,000 (April-June card). A rate table is about 25 % faster. |
| 11 Design | `python rate_card_file.py`<br>`python district_check.py` | Recommended design: Decimal from text, each payment rounded half up to the paisa, one rate card. The district run (3,000,000 entries) takes about 5 s and matches the integer-paise check exactly. Reading `rate_card.json` costs about 60 microseconds. |
| 12 Design challenge | `python milkrate2.py`<br>`python evaluate_original.py`<br>`python test_milkrate2.py` | Decision: modify. Two-decimal readings (pro-rata steps), a seasonal rate card chosen from the date, and a bonus function for over 500 litres. All 25 tests pass for both seasons and the bonus. |
