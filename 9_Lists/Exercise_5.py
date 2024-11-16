fileName = input('Enter a file name: ')
try:
    fhandle = open(fileName)
except:
    print('File not found: ' + fileName)
    exit()
fromCount = 0
for line in fhandle:
    line = line.split()
    if len(line) > 0 and line[0] == 'From':
        fromCount += 1
        print(line[1])

print('There were ' + str(fromCount) + ' lines in the file with From as the first word')