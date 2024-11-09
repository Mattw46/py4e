fname = input('Enter a file name: ')
if fname == 'na na boo boo':
    print('NA NA BOO BOO To YOU - You have been punk\'d!')
    exit()
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ' + fname)
    exit()
count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        numString = line[20:26]
        total += float(numString)
print('Average spam confidence: ' + str(total / count))