# - Na začátku počítač vybere nějaké slovo
# - Na začátku máš 0 špatných pokusů, a žádná hádaná písmenka
# - Počítač v každém kole:
#  - ukáže hádané slovo, ale všechna písmenka která uživatel ještě nehádal
#    v něm zamění na '_'
#  - ukáže počet špatných pokusů
#    - (bonus) ukáže místo toho "obrázek" načtený ze souboru, který si stáhni z:
#        http://pyladies.cz/v1/s005-modules/obrazky.txt
#  - zeptá se na písmenko
#    - (bonus) ptá se tak dlouho, dokut uživatel nezadá jen jedno písmenko,
#      které předtím ještě nehádal
#  - pokud hádané písmenko není ve slově, přičte 1 k počtu špatných pokusů
#  - pokud je špatných pokusů 10, prohráváš a hra končí
#  - pokud jsou všechna písmenka, která se ve slově vyskytují, uhádnuta,
#    vyhráváš a hra končí

from random import randint

# nacte slova
with open('slova_sibenice.txt', 'r') as f:
    words = f.read().splitlines()

# vygeneruje slovo
l = len(words)
k = randint(0, l-1)
unknownWord = words[k].lower()
end = unknownWord
m = len(unknownWord)

# slovo na ukazku
shownWord = '-'*m

# pocet spatnych pokusu
badTry = 0

# zadana pismenka
typedLetters = set()

# obrazky
with open('obrazky_sibenice.txt', 'r') as f:
    obrazek = f.read().split('------------------')

#---------------------------------------------------------------
while shownWord != end and badTry < 10:
    print('Máte {} špatných pokusů. Zbývá {} pokusů.'.format(badTry, 10-badTry))
    #print(shownWord)
    x = input('Co hádáme? ')
    if x in typedLetters:
        print('Nic')
    else:
        if len(set(unknownWord).intersection(x)) != 0:
            index = [i for i in range(m) if unknownWord[i]==x]
            a = list(unknownWord)
            b = list(shownWord)
            for i in index:
                a[i] = '-'
                b[i] = x
            unknownWord = ''.join(a)
            shownWord = ''.join(b)
        else:
            print(obrazek[badTry])
            badTry +=1
    print(shownWord)
    typedLetters.add(x)
    print('Použitá písmena: {}'.format(typedLetters))
if shownWord == end:
    print(shownWord.upper())
    print('Vyhráváš! :-)')
if badTry >= 10:
    print('Prohráváš :-(')
    print('Hádané slovo je {}'.format(end.upper()))
