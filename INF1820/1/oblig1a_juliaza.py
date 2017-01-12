print ("\n1. ikke-gyldige variabelnavn:")
print ("d: variabelnavn skal ikke begynne med tall.")
print ("h: variabelnavn maa vaere uten mellomrom.")
print ("i: 'else' er et noekkelord i python.")


# 2.a)
print ("\n2.a)")

mystring = "After the glimpse I had had of the Martians emerging from the cylinder in which they had come to the earth from their planet, a kind of fascination paralysed my actions. I remained standing kneedeep in the heather, staring at the mound that hid them. I was a battleground of fear and curiosity. I did not dare to go back towards the pit, but I felt a passionate longing to peer into it. I began walking, therefore, in a big curve, seek- ing some point of vantage and continually looking at the sand heaps that hid these newcomers to our earth. Once a leash of thin black whips, like the arms of an octopus, flashed across the sunset and was immediately withdrawn, and afterwards a thin rod rose up, joint by joint, bearing at its apex a circular disk that spun with a wobbling motion. What could be going on there?"
print ("Forekomster 'of':")
print (mystring.count("of"))


# 2.b)
print ("\n2.b)")
antall = 0
for word in mystring.split():
    if word.endswith(('ing')) :
    	antall = antall + 1
print ("Antall ord som ender paa '-ing':")    	
print antall                


# 2.c)
print ("\n2.c)")

mylist = [] 
for word in mystring.split(): 
	mylist.append(word[:-2])
print mylist
print(" ")



# 2.d)
print ("\n2.d)")

mystring2 = ""
for word in mylist:
	mystring2 += word + " "
print mystring2	



# 3.a)
print ("\n3.a)")

kvadrat_list = []
def sum_av_kvadrater(kvadrat_list):
	sum = 0
	for i in kvadrat_list:
		sum = sum + (i * i)
	print sum

	return;	
	 
sum_av_kvadrater([4])


# 3.b)
print ("\n3.b)")

def liste_av_kvadrater(kvadrat_list):
	sum = 0
	resultat_liste = []

	for i in kvadrat_list:
		sum = i * i
		resultat_liste.append(sum)
		
	print resultat_liste
	return;	

liste_av_kvadrater([5,2,4])	
	

