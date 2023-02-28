myDog = {'name':'Mallu', 'color':'cream', 'size':'small', 'age':4}
print(myDog['age'])
print(myDog['name'])
print(myDog.get('height'))
print(myDog.get('height','N/A'))

for k,v in myDog.items():
    print(k,v)