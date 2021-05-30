# Program Name: myFavoriteCars.py
# Program Description: This program outputs a list of info using tuples
# Programmer Name: Devin Brown

cars = (('1965', 'Pontiac', 'GTO', 'Blue'),
('1969', 'Plymouth', 'Roadrunner', 'Yellow'),
('2002', 'Chevrolet', 'Z-28 Camaro', 'Black'))


for car in cars:
    print(car[0] + ' ' + car[3] + ' ' + car[1] + ' ' + car[2])