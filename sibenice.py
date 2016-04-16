from random import randint

# nacte slova
with open('slova_sibenice.txt', 'r') as f:
    words = f.read().splitlines()

# vygeneruje slovo
l = len(words)
k = random.randint(0, l-1)
uknownWord = words[k]
