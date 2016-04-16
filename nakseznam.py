nakseznam = ['caj', 'maso', 'mleko', 'maslo', 'voda']

s = input('Co mam koupit? ')

if s not in nakseznam:
    print('To kupovat nemusim!')
else:
    for i in nakseznam:
        if i.lower()==s:
            print('Mam koupit', i)
            break
        print('Uz mam', i)
