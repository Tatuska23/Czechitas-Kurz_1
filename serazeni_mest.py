"""
Python kurz
Datové typy
@author: Nasťa
Cvičení 2.4
Máte seznam měst seřazených dle počtu obyvatel
cities = ['Praha','Brno', 'Ostrava', 'Plzeň', 'Liberec', 'Olomouc', 'Ústí nad Labem', 'Hradec Králové', 'České Budějovice', 'Pardubice']
Seřaďte města abecedně
Pomocí příkazu "".join() spojte města do jednoho řetězce oddělené hvězdičkou (*)
"""

cities = ['Praha','Brno', 'Ostrava', 'Plzeň', 'Liberec', 'Olomouc', 'Ústí nad Labem', 'Hradec Králové', 'České Budějovice', 'Pardubice']
print('cities = \n', cities)
cities.sort()
print('cities = \n', cities)
" * ".join(cities)
print('cities = ', " * \n * ".join(cities))
