import sys

current_key = None
total_count = 0

for line in sys.stdin:
    key, count = line.strip().split("\t")
    try:
        count = int(count)
    except ValueError:
        continue

    if key == current_key:
        total_count += count
    else:
        if current_key:
            print "%s,%d" %(key, total_count)
        current_key = key
        total_count = count

print("%s,%d" %(current_key, total_count))
