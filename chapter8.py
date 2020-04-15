#import pdb

fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('Invalid input!')
    quit()

lst = list()

#pdb.set_trace()
for line in fh:
    currentList = line.split()
    for word in currentList:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)
