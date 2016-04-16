veci = ['elektrina', 'internet', 'notebook', 'cokolada', 'plavky', 'kapesní nůž', 'léky', 'rybářský prut', 'solární generátor']

with open('pusty_ostrov.txt', 'w', encoding='utf-8') as f:
    l = len(veci)
    i = 1
    while i<=l:
        f.write(str(i) + '\t' + veci[i-1] + '\n')
        i+=1




# f = open('pusty_ostrov.txt', 'w', encoding='utf-8')
# i = 1
# for vec in veci:
#     f.write(str(i) + '\t' + vec + '\n')
#     i+=1
