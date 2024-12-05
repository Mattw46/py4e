wordMap = dict()
file = input('Enter file name: ')
fhand = open(file)
for line in fhand:
    if line.startswith('From '):
        line = line.split()
        if len(line) > 1:
            wordMap[line[2]] = wordMap.get(line[2],0) + 1

print(wordMap)