# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. 
# You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. 
# Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

hourCount = dict()
file = input('Enter file name: ')
fhand = open(file)
for line in fhand:
    if line.startswith('From '):
        line = line.split()
        if len(line) > 1:
            hour = line[5].split(':')
            #print(hour)
            hourCount[hour[0]] = hourCount.get(hour[0],0) + 1

#print(hourCount)

hourList = list()
for key, val in list(hourCount.items()):
    hourList.append((key, val))

hourList.sort()
for key, val in hourList:
    print(key, val)