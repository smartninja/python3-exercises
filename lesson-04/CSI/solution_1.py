# Solution by Raphael Assa, SmartNinja instructor from Belgium

# first we need to put our given data into a suitable data-structure
# in this case we use dictionaries to map human properties to their respective dna-sequence
hair = {"black" : "CCAGCAATCGC", "brown" : "GCCAGTGCCG", "blonde" : "TTAGCTATCGC"}
face = {"square" : "GCCACGG", "round" : "ACCACAA", "oval" : "AGGCCTCA"}
eyes = {"blue" : "TTGTGGTGGC", "green" : "GGGAGGTGGC", "brown" : "AAGTAGTGAC"}
gender = {"female" : "TGAAGGACCTTC", "male" : "TGCAGGAACTTC"}
race = {"white" : "AAAACCTCA", "black" : "CGACTACAG", "asian" : "CGCGGGCCG"}

# map each person to a list of properties describing the person at hand...
# mind that the order of properties in the list is important
people = {"eva" : ["female", "white", "blonde", "blue", "oval"],
          "larisa" : ["female", "white", "brown", "brown", "oval"],
          "matej" : ["male", "white", "black", "blue", "oval"],
          "miha" : ["male", "white", "brown", "green", "square"]}

# read the dna file
with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

person = []  # will represent our suspect...

#  now we check properties in the same order
for i in gender:  # check all genders, i.e. male & female
    #  now check the gender[i] is a substring of dna,
    #  i.e. does dna contain gender[i]...
    if gender[i] in dna:  # if the current gender is present in the dna
        print(i)
        person.append(i)  # add this property to our suspect
for i in race:  # check all races...
    if race[i] in dna:  # same idea as gender, only 1 race will match
        print(i)
        person.append(i)
for i in hair:
    if hair[i] in dna:
        print(i)
        person.append(i)
for i in eyes:
    if eyes[i] in dna:
        print(i)
        person.append(i)
for i in face:
    if face[i] in dna:
        print(i)
        person.append(i)

# now we have a description of our suspect,
# so now check who corresponds to this description...
for p in people:
    if people[p] == person:
        print("The person we're looking for is %s" % p.upper())
        break
