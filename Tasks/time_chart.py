"""Task 10 - Chart of the running time of each method against n."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from compare_scales import (make_readings, timed, total_decimal, total_float_raw,
                            total_float_rounded, total_paise)

sizes = [300, 1000, 6000, 30000, 75000, 150000]
methods = {"Decimal": total_decimal, "float": total_float_raw,
           "float + round": total_float_rounded, "int paise": total_paise}
times = {name: [] for name in methods}
for n in sizes:
    rows = make_readings(n)
    for name, func in methods.items():
        times[name].append(timed(func, rows)[1] * 1000)

plt.figure(figsize=(7, 4))
for name, values in times.items():
    plt.plot(sizes, values, marker="o", label=name)
plt.xlabel("number of payments n")
plt.ylabel("time (ms)")
plt.title("Time to total n payments")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("time_chart.png", dpi=160)
print("saved time_chart.png")
for name, values in times.items():
    print(f"{name:14}" + " ".join(f"{v:8.1f}" for v in values))
