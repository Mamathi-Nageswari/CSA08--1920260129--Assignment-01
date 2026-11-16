"""Task 7 - Alternative concept: copying the functions into every script vs importing."""
import os
import subprocess
import sys
import timeit

scripts = ["daily_slip.py", "ten_day_bill.py", "bank_file.py", "union_report.py"]
print(f"Scripts that need the rate: {len(scripts)}")
print(f"Copy-paste design : a rate revision means editing {len(scripts)} files")
print("Module design     : a rate revision means editing 1 file (milkrate.py)")

here = os.path.dirname(os.path.abspath(__file__))
cold = []
for _ in range(5):
    out = subprocess.run([sys.executable, "-c",
                          "import time; s=time.perf_counter(); import milkrate; "
                          "print(time.perf_counter()-s)"],
                         cwd=here, capture_output=True, text=True).stdout
    cold.append(float(out))
warm = timeit.timeit("import milkrate", setup=f"import sys; sys.path.insert(0, {here!r})",
                     number=100_000) / 100_000
print(f"\nfirst import in a new program : {min(cold) * 1e6:7.1f} microseconds (once)")
print(f"every later import            : {warm * 1e9:7.1f} nanoseconds (sys.modules lookup)")
