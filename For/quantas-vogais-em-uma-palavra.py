palavra = input("informe uma palavra -> ")
vogais = 0
for letra in palavra:
    #if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    if letra == "a" or \
       letra == "e" or \
       letra == "i" or \
       letra == "o" or \
       letra == "u" :
        vogais += 1
print(vogais)