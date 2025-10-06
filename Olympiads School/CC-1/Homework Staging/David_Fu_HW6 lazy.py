import math
import sys

def main():
    for line in sys.stdin:
        n = int(line.strip())
        if n == 0:
            break

        amounts = [float(sys.stdin.readline()) for _ in range(n)]
        avg = sum(amounts) / n

        total_high = 0.0
        total_low = 0.0

        for spent in amounts:
            diff = spent - avg
            if diff >= 0:
                total_high += math.floor(diff * 100) / 100
            else:
                total_low -= math.ceil(diff * 100) / 100

        print(f"${max(total_low, total_high)}")

if __name__ == "__main__":
    main()
