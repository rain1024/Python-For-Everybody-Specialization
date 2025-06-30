from collections import Counter

def main():
    fname = input("Enter file name: ").strip() or "mbox-short.txt"
    try:
        with open(fname) as f:
            senders = Counter(line.split()[1] for line in f if line.startswith('From '))
    except FileNotFoundError:
        print(f"File not found: {fname}")
        return
    if senders:
        sender, count = senders.most_common(1)[0]
        print(sender, count)

if __name__ == "__main__":
    main()
