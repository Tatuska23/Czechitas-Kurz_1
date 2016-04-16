def meal_vouchers(cena_obed, cena_stravenka):
    hotovost = str(cena_obed % cena_stravenka)
    stravenky = str(cena_obed//cena_stravenka)
    print('Obed stoji:', cena_obed)
    print('Stravenka stoji:', cena_stravenka)
    print('Pocet stravenek:', stravenky)
    print('Zaplatit v hotovosti:', hotovost)


x = int(input('Zadej cenu obeda: '))
y = int(input('Zadej cenu stravenky: '))

meal_vouchers(x, y)
