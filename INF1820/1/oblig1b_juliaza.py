#!/usr/bin/python
# -*- coding: latin-1 -*-


import re

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#                                       oppgave 1
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

print '[Oppgave 1A]\n'


with open ('/Users/julia/Documents/inf1820/obliger/built/Obliger/1/cotw.txt', 'r') as f:
    data = f.read() #.replace('\n', '')
    data = data.lower()

    funnet = re.findall(r"\b((?:[bcdfghjklmnpqrstvwxyz]*)(?:[aeiou]+)(?:[bcdfghjklmnpqrstvwxyz]*))\b", data)
    
    
    
    print "Antall enstavelsesord"
    print len(funnet)

f.close()

print''

print '[Oppgave 1B]\n'

print 'Ett ord som ikke er et enstavelsesord men som dekkes av regelen: friendly'

print 'Ett ord som er et enstavelsesord men som ikke dekkes av regelen: white'

print ''

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#                                       oppgave 2
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

print '[Oppgave 2]\n'



setn1 = 'Neste torsdag skal jeg ikke være med.'
setn2 = 'I går var torsdag 13 januar, 1998.'
setn3 = 'Hun ble født før 25 desember, 1899.'
setn4 = 'Forrige mandag var jeg syk.'
setn5 = 'Dette her blir en litt lengre string. Den skal ikke inneholde noe dato.'
setn6 = 'Hva kan være bedre enn å bli født på søndag 17 mai, 2014?'
setn7 = 'Neste uke skal vi på tur.'




def findDate(string):
    string = string.lower()
    funnet1 = re.findall(r"\b((?:mandag|tirsdag|onsdag|torsdag|fredag|lørdag|søndag)\s(?:[0-9]{1,2})\s(?:januar|februar|mars|april|mai|juni|juli|august|september|oktober|november|desember)[,]\s(?:[0-9]{4}))\b",string)
    funnet2 = re.findall(r"\b((?:neste|forrige)\s(?:mandag|tirsdag|onsdag|torsdag|fredag|lørdag|søndag))\b",string)
    if (funnet1):
        funnet1 = ' '.join(funnet1)
        funnet1 = funnet1.split(' ')
        aar = int(funnet1[3])
        dag = int(funnet1[1])

        if ((aar >= 1900) and (aar <= 2099) and (dag <= 31) and (dag >= 1)):
            print "Funnet følgende gyldige datouttrykk: " + (' '.join(funnet1))

    elif (funnet2):
            print "Funnet følgende gyldige datouttrykk: " + (''.join(funnet2))



findDate(setn1)
findDate(setn2)
findDate(setn3)
findDate(setn4)
findDate(setn5)
findDate(setn6)
findDate(setn7)