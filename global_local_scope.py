def spam():
    global eggs
    eggs = 'Hello'
    bacon = 3
    print(eggs, bacon)

eggs = 42
bacon = 1
spam()
print(eggs, bacon)
