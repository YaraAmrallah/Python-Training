"""
try:
    hrs = input("Enter Hours:")
    h = float(hrs)

    rate = float(input('Enter Rate:'))

    if h <= 40 :
        print(rate*h)
    else:
        pay = (h-40)*1.5*rate + 40*rate
        print(pay)

except:
    print('Error, please enter numeric input')
"""

"""
score = input("Enter Score: ")

try:
    fScore = float(score)
except:
    print('Error, please enter a valid score between 0.0 and 1.0')
    quit()

if fScore < 0.6 and fScore >= 0:
    print('F')
elif fScore < 0.7 and fScore >= 0:
    print('D')
elif fScore < 0.8 and fScore >= 0:
    print('C')
elif fScore < 0.9 and fScore >= 0:
    print('B')
elif fScore <= 1.0 and fScore >= 0:
    print('A')
else:
    print('Value out of range')
"""
"""
def computepay(h,rate):
    if h <= 40 :
        return rate*h
    else:
        return (h-40)*1.5*rate + 40*rate


hrs = input("Enter Hours:")
rate = float(input('Enter Rate:'))
h = float(hrs)

p = computepay(h,rate)
print('Pay', p)
"""

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : break

    try:
        temp = float(num)
        if largest is None and smallest is None:
            largest = temp
            smallest = temp

        if largest < temp:
            largest = temp
        elif smallest > temp:
            smallest = temp

    except:
        print('Invalid Input')

print("Maximum", largest)
print('Minimum', smallest)
