#!/usr/bin/python
# -*- coding: latin-1 -*-

import nltk
import string
from nltk.corpus import brown

# **************************** Oppgave 1 ****************************

linje = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

print linje, '\n[Oppgave 1]\n', linje, '\n'


brown_news = nltk.corpus.brown.tagged_words(categories='news')

print brown_news[:10], '\n'

# **************************** Oppgave 2 ****************************

print linje, '\n[Oppgave 2]\n', linje, '\n'


# Hvor mange ord forekommer kun én gang (såkalte hapax legomena)?
# Skriv ut resultatet av beregningene dine.
a = {} # for ord med antall forekomster
b = {} # for tag med antall forekomster
teller = 0

for ord, tag in brown_news:
    ord = ord.lower()
    try:
        # Referencing this will cause a KeyError exception
        # if it doesn't already exist
        a[ord]
        # ... meaning if we get this far it didn't happen so
        # we'll increment
        a[ord] += 1
    except KeyError:
        # If we got a KeyError we need to create the
        # dictionary key
        a[ord] = 1
    
    # Keep overwriting maxItemCount with the latest number,
    # if it's higher than the existing itemCount
    if a[ord] > teller:
        teller = a[ord]
        mostPopularItem = ord

print 'Det mest frekvente ordet er: "', mostPopularItem, '" med', teller, 'forekomster'

# nullstiller teller
teller = 0

for ord, tag in brown_news:
    try:
        # Referencing this will cause a KeyError exception
        # if it doesn't already exist
        b[tag]
        # ... meaning if we get this far it didn't happen so
        # we'll increment
        b[tag] += 1
    except KeyError:
        # If we got a KeyError we need to create the
        # dictionary key
        b[tag] = 1
    
    # Keep overwriting maxItemCount with the latest number,
    # if it's higher than the existing itemCount
    if b[tag] > teller:
        teller = b[tag]
        mostPopularTag = tag

print 'Den mest frekvente ordklassetaggen er: "', mostPopularTag,'" med', teller,'forekomster'


# nullstiller teller
teller = 0

# lopper gjennom verdier (antall forekomster) som ble lagret i dictionary 'a'
# og finner alle som er '1' og oppdaterer telleren
for antall in a.values():
    if antall == 1:
        teller += 1

print 'Antall ord som forekommer kun én gang:', teller, '\n'


# **************************** Oppgave 3 ****************************

print linje, '\n[Oppgave 3A]\n', linje, '\n'


c = {} # for å finne flertydige ord

for ord, tag in brown_news:
    ord = ord.lower()
    # hvis ordet ikke finnes i 'c', blir det lagt til med tag
    if ord not in c:
        c[ord] = set([tag])
    # hvis ordet allerede finnes i 'c', blir taggen lagt til (set har ikke duplikater)
    else:
        c[ord].add(tag)

# nullstiller telleren
teller = 0
max = 0
maxOrd=''

# finner flertydige ord ved å telle alle tags som har en lengde på større eller lik 2
for tag in c:
    lengde = len(c[tag])
    
    if lengde >= 2:
        teller += 1
    
    if lengde > max:
        max = lengde
        maxOrd = tag

print 'Antall ord som er flertydige:', teller, '\n'


print linje, '\n[Oppgave 3B]\n', linje, '\n'

print 'Ord som har størst antall tagger',maxOrd
print 'med antall tagger:',max,'\n'



# **************************** Oppgave 4 ****************************

print linje, '\n[Oppgave 4]\n', linje, '\n'


brown_sents = nltk.corpus.brown.tagged_sents(categories="news")

par=[]
eksempler =0

# finner alle ord-tag-par med ordet med størst antall tagger og lagrer de i en liste
for klasse in c[maxOrd]:
    par.append((maxOrd,klasse))

# looper gjennom par-lista og endrer storbokstav
for p in par:
	lowp = (p[0].lower(), p[1].lower())
    #looper gjennom setningene og initialiserer en ny liste som samler på alle setningene med bare små bokstaver
        for sent in brown_sents:
            slow = []
            for t in sent:
                tlow = (t[0].lower(), t[1].lower())
                slow.append(tlow)
            # hvis ordet finnes i lista, skal en teller oppdateres og resultatene skrives ut
            if lowp in slow:
                eksempler += 1
                print 'Eksempel ',eksempler,' for ',p,':',sent, '\n'
                break


# **************************** Oppgave 5 ****************************

print linje, '\n[Oppgave 5]\n', linje, '\n'

feminine = [('her','PP$'),('hers','PP$$'),('Her','PP$'),('Hers','PP$$')]
maskuline = [('his','PP$'),('his','PP$$'), ('His','PP$'),('His','PP$$')]
f = 0
m = 0
# looper gjennom brown_news og oppdaterer ganske enkelt tellerne når den enten finner fem. eller mask.
for tuple in brown_news:
    if tuple in feminine:
        f += 1
    elif tuple in maskuline:
        m += 1

print 'Antall feminine:',f
print 'Antall maskuline:',m