#x = int(input('Zadej cislo:'))

#if x % 2 == 0:
#    print(x, 'je sude')
#else:
#    print(x, 'je liche')

names_list = ['Jiří', 'Jan', 'Marie', 'Petr', 'Jana', 'Josef', 'Pavel', 'Martin', 'Jaroslav', 'Tomáš', 'Eva', 'Miroslav', 'Hana', 'Anna', 'Zdeněk', 'František', 'Václav', 'Michal', 'Lenka', 'Kateřina']

x = input('Zadej jmeno: ')

if x in names_list:
    print('Jmeno', x, 'je v seznamu. Vtipna hlaska :-)')
else:
    print('Jmeno', x, 'neni v seznamu.')
