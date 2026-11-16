"""The same module WITHOUT the if __name__ == "__main__": guard (to show the problem)."""
from milkrate import rate_per_litre, payout

for litres, fat, snf in [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]:
    print(f"{litres:5} L fat {fat} snf {snf} rate {rate_per_litre(fat, snf):6.2f}"
          f" pay {payout(litres, fat, snf):8.2f}")
