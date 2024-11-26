emailCount = dict()
file = input('Enter file name: ')
fhand = open(file)
for line in fhand:
    if line.startswith('From '):
        line = line.split()
        if len(line) > 1:
            emailCount[line[1]] = emailCount.get(line[1],0) + 1

email = None
count = 0

for key in emailCount.keys():
    if emailCount.get(key) > count:
        count = emailCount.get(key)
        email = key

print(email + ' ' + str(count))