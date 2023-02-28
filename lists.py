import copy

def eggs(cheese):
    cheese.append('egg')

spam = [1,2,3]
spam2 = spam
spambkp = copy.deepcopy(spam)
eggs(spam)
print(spam)
print(spam2)
print(spambkp)