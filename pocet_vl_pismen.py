def number_upper_lower(str):
    l = len(str)
    lower = 0
    upper = 0
    for i in range(l):
        if str[i].islower():
            lower+=1
        if str[i].isupper():
            upper+=1
    print('Pocet vsech znaku retezce: ', l)
    print('Pocet velkych pismen: ', upper)
    print('Pocet malych pismen: ', lower)

x = input('Zadej textovy retezec: ')

number_upper_lower(x)
