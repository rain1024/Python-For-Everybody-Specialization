from collections import Counter

def main():
    fname = input("Enter file name: ").strip() or "mbox-short.txt"
    try:
        with open(fname) as f:
            hours = Counter()
            for line in f:
                if line.startswith('From '):
                    parts = line.split()
                    if len(parts) > 5:
                        time = parts[5]
                        hour = time.split(':')[0]
                        hours[hour] += 1
    except FileNotFoundError:
        print(f"File not found: {fname}")
        return
    for hour in sorted(hours):
        print(hour, hours[hour])

if __name__ == "__main__":
    main()
