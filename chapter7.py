# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Invalid Input')
    quit()

file = fh.read()
print((file.upper()).rstrip())
