fhand = open('exercise2.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From' : continue
    print(words[2])