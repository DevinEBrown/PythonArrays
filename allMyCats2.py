# Program Name: allMyCats2.py
# Program Description: This program outputs a list of cats in ABC order
# Programmer Name: Devin Brown

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
          ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
catNames.sort()
print('The cat names are:')
for name in catNames:
    print('  ' + name)