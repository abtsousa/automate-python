import os

helloFile = open("hello.txt")
print(helloFile.read())
helloFile.close()
print("---")
helloFile = open("hello.txt")
print(helloFile.readlines())
helloFile.close()
print("---")
helloFile = open("hello.txt")
print(helloFile.readline())
helloFile.close()