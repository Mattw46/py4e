# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. 
# Count the number of messages from each person using a dictionary.
#
# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. 
# Then sort the list in reverse order and print out the person who has the most commits.

emailCount = dict()
file = input('Enter file name: ')
fhand = open(file)
for line in fhand:
    if line.startswith('From '):
        line = line.split()
        if len(line) > 1:
            emailCount[line[1]] = emailCount.get(line[1],0) + 1

emailList = list()
for key, val in list(emailCount.items()):
    emailList.append((val, key))

emailList.sort(reverse=True)
for key, val in emailList[:1]:
    print(val, key)


