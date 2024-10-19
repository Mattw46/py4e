total = 0
count = 0
while True:
    line = input('Enter a number: ')
    if line == 'done':
        break
    try:
        total += int(line)
        count = count + 1
    except:
        print('Invalid input')

print(str(total) + ' ' + str(count) + ' ' + str(float(total/count)))