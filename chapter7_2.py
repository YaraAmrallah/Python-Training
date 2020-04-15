# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

total = 0;
count = 0;

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    location = line.find('.')
    total = total + float(line[(location - 1):])
    count = count + 1

total = total/count

print(total)
