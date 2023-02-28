import pprint

print("What is your message?")
message = input()
count = {}

for character in message:
    count.setdefault(character,0) # define como 0 se não existir no dicionário
    count[character] += 1

pprint.pprint(count)
