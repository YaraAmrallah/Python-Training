
name = input('Enter file:')
if len(name) < 1 : name = 'mbox-short.txt'
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    if len(line) > 3 and words[0] == 'From':
        time = words[5].split(':')
        counts[time[0]] = counts.get(time[0],0) + 1

lst = list()
for key, val in counts.items():
    newtup = (key,val)
    lst.append(newtup)

lst = sorted(lst)

for val, key in lst:
    print(val, key)
