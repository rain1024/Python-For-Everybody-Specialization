# 7.2 Assignment Solution
filename = input("Enter file name: ")
try:
    fhandle = open(filename)
except FileNotFoundError:
    print("File cannot be opened:", filename)
    quit()

count = 0
accumulator = 0.0
for line in fhandle:
    line = line.strip()
    if line.startswith("X-DSPAM-Confidence:"):
        colon_pos = line.find(":")
        value = float(line[colon_pos+1:].strip())
        accumulator += value
        count += 1

if count > 0:
    average = accumulator / count
    print("Average spam confidence:", average)
else:
    print("No matching lines found.") 