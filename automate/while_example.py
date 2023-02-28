name = ''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break  # pára o loop
print('Thank you!')

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue  # volta ao início do loop
    print('spam is ' + str(spam))
