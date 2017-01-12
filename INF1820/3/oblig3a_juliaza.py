#!/usr/bin/python
# -*- coding: latin-1 -*-

import nltk
import re
from nltk.corpus import brown
from nltk.corpus import conll2000
from nltk.probability import FreqDist, ConditionalFreqDist

brown_words = nltk.corpus.brown.tagged_words()
words = nltk.corpus.brown.words()


# // BIGRAMS

# [(tagg1, ord1), (tagg2, ord2), (tagg3, ord3), ....]
brown_tags_words = [(tag, word) for (word, tag) in brown_words]

# [(tagg1, tagg2), (tagg2, tagg3), (tagg3, tagg4), ....]
brown_tags = [tag for (word, tag) in brown_words]
bigram_tags = nltk.bigrams(brown_tags)

cfd_1 = ConditionalFreqDist(brown_tags_words)
cfd_2 = ConditionalFreqDist(bigram_tags)

# OPPGAVE 1

# 1.A.1. // mest frekvent VERB
verb = cfd_1["VB"].max()

print "\n>>> Oppgave 1 \n\n1.A.1. Det mest frekvente verbet er:", verb


# 1.A.2. // TIME SUBSTANTIV
time_sub = cfd_1["NN"].items()
print "1.A.2. 'Time' som substantiv:", time_sub[0][1]


# 1.A.2. // TIME VERB
time_verb = cfd_1["VB"].items()
for wordtall in time_verb:
    if wordtall[0] == "time":
        print "1.A.2. 'Time' som verb:", wordtall[1]



# 1.A.3. mest frekvente adjektiv
adjektiv = cfd_1["JJ"].max()
print "1.A.3. Det mest frekvente adjektivet er:", adjektiv


x = cfd_2['VB'].items()
print "\n1.B.1. Taggen som forekommer oftest etter et verb er:", x[0][0]

# Bigrammet ‘DT NN’?
y = cfd_2["DT"].items()[:1]
print "1.B.2. Bigrammet 'DT NN' forekommer", y[0][1], "ganger"


cpd_wordtags = nltk.ConditionalProbDist(cfd_1, nltk.MLEProbDist)
cpd_tags = nltk.ConditionalProbDist(cfd_2, nltk.MLEProbDist)

# Fra dette objektet kan vi hente ut det mest sannsynlige adjektivet med cpd["JJ"].max() eller sannsynligheten til
# new gitt adjektivtagg med: cpd["JJ"].prob("new").
print "(Det mest sannsynlige adjektivet er", cpd_wordtags["JJ"].max(), ")"
print "(Sannsynlighet for adjektiv = 'new'", cpd_wordtags["JJ"].prob("new"), ")"


# 1.C.1. Hva er det mest sannsynlige verbet?
print "\n1.C.1. Det mest sannsynlige verbet er:", cpd_wordtags["VB"].max()
# 1.C.2. Hva er P(NN|DT),sannsynligheten for substantivtagg etter en bestemmertagg?
print "1.C.2.", cpd_tags["DT"].prob("NN"), "er sannsynligheten for P(NN|DT)"



# OPPGAVE 2


a1 = cpd_tags["VBD"].prob("PPO")    # P(PPO|VBD)
b1 = cpd_wordtags["PPO"].prob("her")# P(her|PPO)
c1 = cpd_tags["PPO"].prob("VB")     # P(VB|PPO)

a2 = cpd_tags["VBD"].prob("PP$")    # P(PP$|VBD)
b2 = cpd_wordtags["PP$"].prob("her")# P(her|PP$)
c2 = cpd_tags["PP$"].prob("NN")     # P(NN|PP$)

prob1 = a1 * b1 * c1                # I|PPSS saw|VBD her|PPO duck|VB
prob2 = a2 * b2 * c2                # I|PPSS saw|VBD her|PP$ duck|NN

print "\n>>> Oppgave 2 \n\nI|PPSS saw|VBD her|PP$ duck|NN:", prob2, "\n(***winner***)\n", "I|PPSS saw|VBD her|PPO duck|VB:", prob1, "\n(***loser***)"


# OPPGAVE 3

grammar = r"""
    NP:
    # fra boka
    
    {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and nouns
    {<NNP>+}                # sequences of proper nouns
    
    # andre
    
    {<DT|JJ>}               # chunk bestemmerord og adjektiver
    }<[\.VI].*>+{           # chink tagger som begynner med V, I, eller .
    <.*>}{<DT>              # split chunk når det kommer et bestemmerord
    <DT|JJ>{}<NN.*>         # føy sammen chunk som ender med det/adj med en som starter med et substantiv
    {<NNP>+<NN>}            # sekvens av egennavn - substantiv
    {<NN>+}                 # substantiver som følger etter hverandre
    """



cp = nltk.RegexpParser(grammar)

# training
training_chunks = conll2000.chunked_sents("train.txt", chunk_types=["NP"])
print "\n>>> Oppgave 3 \n\nAccuracy training:\t", nltk.chunk.util.accuracy(cp, training_chunks)

# test
test_chunks = conll2000.chunked_sents("test.txt", chunk_types=["NP"])
print "Accuracy test:\t\t", nltk.chunk.util.accuracy(cp, test_chunks)















