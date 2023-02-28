def printlist(list):
    for index, item in enumerate(list):
        if index == len(list) - 2:
            print(item, end=', and ')
        elif index == len(list) - 1:
            print(item)
        else:
            print(item, end=', ')


spam = ['apples', 'bananas', 'tofu', 'cats']
printlist(spam)
