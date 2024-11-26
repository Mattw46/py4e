emailCount = dict()
file = input('Enter file name: ')
fhand = open(file)
for line in fhand:
    if line.startswith('From '):
        line = line.split()
        if len(line) > 1:
            index = line[1].index('@')
            domain = line[1] 
            domain = domain[index + 1:]
            emailCount[domain] = emailCount.get(domain,0) + 1

print(emailCount)