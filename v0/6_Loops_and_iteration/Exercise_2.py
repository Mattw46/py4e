max_value = 0
min_value = None
while True:
    line = input('Enter a number: ')
    if line == 'done':
        break
    try:
        value = int(line)
        if value > max_value:
            max_value = value
            continue
        elif value < min_value or min_value == None:
            min_value = value
    except:
        print('Invalid input')

print('Max: ' + str(max_value) + ' Min: ' + str(min_value))