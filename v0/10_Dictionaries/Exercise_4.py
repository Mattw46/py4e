# Exercise 4: Add code to the above program to figure out who has the most messages in the file. 
# After all the data has been read and the dictionary has been created, 
# look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) 
# to find who has the most messages and print how many messages the person has.
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