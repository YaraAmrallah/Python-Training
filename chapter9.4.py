name = input('Enter file:')
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if len(line) < 2:
        continue
    words = line.split()
    if words[0] == 'From':
        counts[words[1]] = counts.get(words[1],0) + 1

bigCount = None
bigWord = None

for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count

print(bigWord, bigCount)
