#import pdb

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
#pdb.set_trace()
for line in fh:
    pieces = line.split()
    if len(pieces) > 0:
        if pieces[0] == 'From':
            print(pieces[1])
            count = count + 1;


print("There were", count, "lines in the file with From as the first word")
