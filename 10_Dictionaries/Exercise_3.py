emailCount = dict()
file = input('Enter file name: ')
fhand = open(file)
for line in fhand:
    if line.startswith('From '):
        line = line.split()
        if len(line) > 1:
            emailCount[line[1]] = emailCount.get(line[1],0) + 1

print(emailCount)