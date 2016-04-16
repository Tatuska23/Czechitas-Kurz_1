a = input('Zadejte jmeno: ')
if ' ' in a:
    raise Exception('Jmeno nesmi obsahovat mezeru!')
if not a[0].isupper():
    raise Exception('Jmeno se pisi velkym pismenem!')
if len(set('0123456789').intersection(set(a))) != 0:
    raise Exception('Jmeno obsahuje cislice!')
