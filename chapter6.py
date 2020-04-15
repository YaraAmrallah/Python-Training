text = 'X-DSPAM-Confidence:    0.8475'

index = text.find('0')
number = float(text[index:])
print(number)
