repeat = True
while repeat:
    try:
        file_name = input('Zadejte jméno souboru: ')
        with open(file_name, 'r', encoding='utf-8') as f:
            repeat = False
            print(f.read())
    except FileNotFoundError:
        print('Soubor neexistuje, tak si to dáme ještě jednou!')
