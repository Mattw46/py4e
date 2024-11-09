fname = input('Enter a file name: ')
fhand = open(fname)
count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        numString = line[20:26]
        total += float(numString)
print('Average spam confidence: ' + str(total / count))