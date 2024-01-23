#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Scrivere un algoritmo che, dato un numero, ne mostri la sua rappresentazione 
# a lettere in italiano. Esempio:
#   input: 1234 -> output: milleduecentotrentaquattro
#
# Come funziona?
# Per i primi venti numeri, non c'è altra strada che quella di prevedere una 
# traduzione semplice attraverso una tabella: 0 -> zero, 1 -> uno, 2 -> due, ..., 19 -> diciannove

def translate_to_20(n):
    if n > 19:
        return "Out of range"

    NUMBERS = ["","uno", "due", "tre", "quattro", "cinque", "sei", "sette",
               "otto", "nove", "dieci", "undici", "dodici", "tredici",
               "quattordici", "quindici", "sedici", "diciassette",
               "diciotto", "diciannove"]
    return NUMBERS[n]

# dal 20, fino al 100 (escluso), ho la possibilità di prevedere una "traduzione" 
# della decina e demandare la "traduzione" dell'unità alla funzione che traduce fino a 20
# 25 -> decina = 2, unità = 5


def translate_to_100(n):
    if n < 20:
        return translate_to_20(n)
    if n > 99:
        return "Out of range"
    DECADES = ["venti", "trenta", "quaranta", "cinquanta", "sessanta",
               "settanta", "ottanta", "novanta"]
    decade =  n // 10 # la decina da n
    unit = n % 10 # l'unità di n
    return DECADES[decade-2] + translate_to_20(unit)

def translate_number(n):
    return translate_to_100(n)

for x in range(1, 101):
    print(translate_number(x))


# In[9]:


# Scrivere un algoritmo che, dato un numero, ne mostri la sua rappresentazione 
# a lettere in italiano. Esempio:
#   input: 1234 -> output: milleduecentotrentaquattro

def translate_to_20(n):
    if n > 19:
        return "Out of range"

    NUMBERS = ["","uno", "due", "tre", "quattro", "cinque", "sei", "sette",
               "otto", "nove", "dieci", "undici", "dodici", "tredici",
               "quattordici", "quindici", "sedici", "diciassette",
               "diciotto", "diciannove"]
    return NUMBERS[n]

# dal 20, fino al 100 (escluso)

def translate_to_100(n):
    if n < 20:
        return translate_to_20(n)
    if n > 99:
        return "Out of range"
    DECADES = ["venti", "trenta", "quaranta", "cinquanta", "sessanta",
               "settanta", "ottanta", "novanta"]
    decade =  n // 10 # la decina da n
    unit = n % 10 # l'unità di n
    return DECADES[decade-2] + translate_to_20(unit)

# "traduzione" del centinaio e "traduzione" fino a 1000
# 25 -> decina = 2, unità = 5


def translate_to_1000(n):
    if n < 100:
        return translate_to_100(n)
    if n>999:
        return "Out of range"
    DECADES = ["venti", "trenta", "quaranta", "cinquanta", "sessanta",
               "settanta", "ottanta", "novanta"]
    HUNDREDS = ["cento", "duecento", "trecento", "quattrocento", "cinquecento",
               "seicento", "settecento", "ottocento","novecento"]
    hundred =  n // 100 # il centinaio di n
    decade = (n % 100)//10 # la decina da n
    unit = n % 10 # l'unità di n
    return HUNDREDS[hundred-1] + translate_to_100(n%100)

def translate_number(n):
    return translate_to_1000(n)

for x in range(1010):
    print(translate_number(x))


# In[ ]:




