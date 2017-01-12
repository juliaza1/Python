#!/usr/bin/python
# -*- coding: latin-1 -*-

import nltk
from nltk.corpus import brown

linje = '---------------------------------------------------------------'

# **************************** Oppgave 1 ****************************

# 3 muligheter:
# 1. alle taggene er like , 2. én tagg er lik, 3. ingen, (2 like gir logisk at den tredje også er lik - dermed 3 like)
# det gir 1/3 + 1/3 = 2/3
# da blir sannsynligheten for at Astrid og Bjarne har valgt samme tagg for et ord: 0.67


# **************************** Oppgave 2 ****************************

print linje, '\n[Oppgave 2]\n',linje, '\n'

# Zipfs lov f = 1 / r

n = 1000000
the = 62702
x = 56000
teller = 2
countOne = 0

for i in range(n):
    while x != 0:
        resultat = round((float(the)) / teller)
        print resultat
        teller += 1
        x -= 1
        if resultat == 1.0:
            countOne += 1

print '\n', countOne, 'ord har frekvens 1'

print '\n'


# **************************** Oppgave 3 ****************************

# 1.
# Overskrift 1: MAN EATING PIRANHA MISTAKENLY SOLD AS PET FISH
# flertydighet: The man who is eating a piranha is sold as pet fish.
# flertydighet: Dangerous (man-eating) piranha was sold as pet fish.
# 'MAN EATING' kan bety 'mannen som spiser' eller noe som spiser mennesker.

# Overskrift 2: STOLEN PAINTING FOUND BY TREE
# flertydighet: Either a tree found a stolen painting.
# flertydighet: A stolen painting was found sitting next to a tree.
# 'BY' beskriver her noe lokalt eller indikerer en aktør
# by = particle, preposition
# by = literal in case 2 or indicating relations in case2


# Overskrift 3: DRUNK GETS NINE MONTHS IN VIOLIN CASE
# flertydighet: The defendant (the drunk) has to live 9 months in a violin case as punishment.
# flertydighet: Case as in lawsuit. The drunk has to go to jail for 9 months.
# 'VIOLIN CASE' kan være en koffert til en fiolin eller som det er ment her en betegnelse for en rettsak som har et eller annet med fioliner å gjøre.

# 2.
# MAN EATING/JJ PIRANHA/NN MISTAKENLY/RB SOLD/V AS/RB PET FISH/NN

# STOLEN/JJ PAINTING/NN FOUND/V BY/P TREE/NN

# DRUNK/NN GETS/V NINE MONTHS/NN IN/P VIOLIN CASE/NNP /// NINE = NUMBER

# 3.
# Kunnskap om ordklasser hjelper ofte for å entydeliggjøre overskriftene. Men som i eksempel 2 er 'BY' en prepsosisjon i begge tilfellene.
# The significance of POS for language processing is the large amount of information they give about a word and its neighbours (J&M p. 157)

# **************************** Oppgave 4 ****************************

print linje, '\n[Oppgave 4]\n', linje, '\n'



# Du kan utvikle taggeren din ved å teste den på “adventure”-kategorien fra Brown-korpuset underveis. Når du er ferdig med
# regelskrivingen, skal du teste taggerens nøyaktighet (s.k. accuracy) på “fiction”-kategorien fra Brown-korpuset, samt
# rapportere resultatene.

# Til slutt skal programmet ditt lese inn filen test_setninger.txt som ligger ute på emne- siden, tagge den og skrive ut
# resultatet. Kopier inn output’en i filen din og diskuter minst 3 av feilene taggeren gjør, samt gi forslag til hvordan
# den kan forbedres.

file = brown.sents(categories=['adventure'])


patterns = [# fra boka
            (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),   # cardinal numbers
            (r'(The|the|A|a|An|an)$', 'AT'),   # articles
            (r'.*able$', 'JJ'),                # adjectives
            (r'.*ness$', 'NN'),                # nouns formed from adjectives
            (r'.*ly$', 'RB'),                  # adverbs
            (r'.*s$', 'NNS'),                  # plural nouns
            (r'.*ing$', 'VBG'),                # gerunds
            (r'.*ed$', 'VBD'),                 # past tense verbs
            
            #******* egne
            (r'.*er$', 'JJR'),                 # comparative (SUBSTANTIVER SOM ENDER PÅ -ER BLIR TAGGET FEIL)
            # f.eks. simpler
            (r'.*est$', 'JJS'),                # superlative
            # f.eks. easiest
            (r'(Aboard|aboard|About|about|Above|above|Absent|absent|Across|across|After|after|Against|against|Along|along|Alongside|alongside|Among|among|Amongst|amongst|Around|around|Aside|aside|At|at|Before|before|Behind|behind|Below|below|Beneath|beneath|Beside|beside|Besides|besides|Between|between|Beyond|beyond|But|but|By|by|Circa|circa|Concerning|concerning|Despite|despite|Down|down|During|during|Except|except|Excluding|excluding|Failing|failing|Following|following|For|for|From|from|Given|given|In|in|Including|including|Inside|inside|Into|into|Like|like|Minus|minus|Near|near|Next|next|Of|Off|of|off|On|on|Onto|onto|Opposite|opposite|Out|out|Outside|outside|Over|over|past|Past|Plus|Pro|Regarding|plus|pro|regarding|Round|round|Sinde|since|Through|through|Throughout|throughout|till|Till|Toward|Towards|toward|towards|Under|under|Underneath|underneath|unlike|Unlike|Until|until|Up|up|Upon|upon|Versus|versus|Via|via|With|with|Within|within|Without|without)$', 'PRP'), # preposisjon
            # f.eks. about
            (r'(I|You|you|He|he|She|she|It|it|We|we|They|they|Who|who)$','PPS'), # personalpronomen (subjekt)
            # f.eks you
            (r'(Me|me|Us|us|You|you|Him|him|Her|her|It|it|Them|them|One|one|Whom|whom|Who|who)$', 'PPO'), # personalpronomen (objekt)
            # f.eks us
            (r'(Myself|myself|Ourself|ourself|Ourselves|ourselves|Yourself|yourself|Yourselves|yourselves|Himself|himself|Hisself|hisself|Herself|herself|itself|Itself|Themself|themself|Themselves|themselves|Theirself|theirself|Theirselves|theirselves|Oneself|oneself)$', 'PPR'), # personalpronomen (refleksiv)
            # f.eks Theirselves
            (r'.*ion$', 'NN'),  # Nouns
            # f.eks creation
            (r'(Be|be|Am|am|Are|are|Is|is|Can|can|Could|could|Dare|dare|Do|do|Have|have|Has|has|May|may|Might|might|Must|must|Need|need|Ought|ought|Shall|shall|Should|should|Will|will|Would|would)$', 'VBA'),  # Hilfsverben
            # f.eks are
            (r'(One|one|Two|two|Three|three|Four|four|Five|five|Six|six|Seven|seven|Eight|eight|Nine|nine|Zero|zero)$', 'NUM'),  # Numerals 0 - 9
            # f.eks Three
            (r'.*hood$', 'NN'),  # noun
            # f.eks childhood
            (r'.*ism$', 'NN'),  # noun
            # f.eks Totalitarism
            (r'.*ice$', 'NN'),  # noun (kan også være verb f.eks. to practice)
            # f.eks Practice
            (r'.*ment$', 'NN'),  # noun
            # f.eks. movement
            (r'.*ive$', 'NN'),  # noun (kan også være noe annet f.eks. to survive, to be active)
            # f.eks. narrative
            (r'.*ness$', 'NN'),  # noun
            # f.eks. darkness
            (r'.*ship$', 'NN'),  # noun (kan også være verb f.eks. to worship)
            # f.eks. relationship
            (r'.*ure$', 'NN'),  # noun (kan også være verb f.eks. to endure)
            # f.eks. seizure
            (r'.*tude$', 'NN'),  # noun
            # f.eks. attitude
            (r'.*ize$', 'VB'),  # verb
            # f.eks. summarize
            (r'.*ise$', 'VB'),  # verb
            # f.eks. despise
            (r'.*ify$', 'VB'),  # verb
            # f.eks. simplify

            #******* egne
            (r'.*', 'XX'),                      # niks (default)

            ]






tagger = nltk.RegexpTagger(patterns)
print len(file)

print tagger.tag(file[600])


# Beklager, jeg har ikke hatt tid til å bli ferdig (grunnet 2 andre obliger og sykdom). Men fikk 100 poeng på oblig 2a. Og skal prøve det samme på oblig 3a :)



