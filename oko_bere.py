from random import randint

i = 0
print('Mate %d bodu' % i)

while True:
    #print('Dostal/a jste ', i, 'bodu')
    x = input('Chcete pokracovat? y/n\n')
    if x.lower() == 'y' :
        rnd = randint(2,10)
        i += rnd
        if i>21:
            print('Mate %d bodu. Oops! Jste prohrali!' % i)
            break
        elif i==21:
            print('%d bodu! Hura! Jste vyhral/a!' % i)
            break
        else:
            print('Mate %d bodu' % i)
    elif x.lower() == 'n':
        print('Mate %d bodu. Konec hry!' % i)
        break
    else:
        print('Preklep')
print('Na shledanou!')
