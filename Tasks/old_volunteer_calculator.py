"""A copy of the kind of quick calculator the volunteer wrote (rates typed in many places).
Kept only to show the problem; it is not used for payments."""

litres = float(input("Litres: "))
fat = float(input("Fat %: "))
snf = float(input("SNF %: "))
if fat > 3.5:
    rate = 30.00 + (fat - 3.5) * 10 * 0.40
else:
    rate = 30.00 - (3.5 - fat) * 10 * 0.40
if snf > 8.5:
    rate = rate + (snf - 8.5) * 10 * 0.30
else:
    rate = rate - (8.5 - snf) * 10 * 0.30
print("Rate:", rate)
print("Amount:", litres * rate)
morning_bonus = (fat - 3.5) * 10 * 0.40   # typed again for the report
evening_bonus = (snf - 8.5) * 10 * 0.30   # typed again for the report
print("Fat part:", morning_bonus, "SNF part:", evening_bonus)
