import os

os.chdir('/Users/afonso/')
print(os.getcwd())

totalSize = 0
for filename in os.listdir(os.getcwd()):
    if not os.path.isfile(os.path.join(os.getcwd(), filename)):
        continue
    totalSize += os.path.getsize(os.path.join(os.getcwd(), filename))

print(totalSize)
