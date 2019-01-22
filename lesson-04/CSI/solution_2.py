# Solution by Raphael Assa, SmartNinja instructor from Belgium

# map each person to a list of DNA sequences describing the properties of the person at hand...
# since everybody is white, we can technically leave "race" out
# but for demonstration purposes we'll simply keep it...
people = {"eva": ["TGAAGGACCTTC", "AAAACCTCA", "TTAGCTATCGC", "TTGTGGTGGC", "AGGCCTCA"],
          "larisa": ["TGAAGGACCTTC", "AAAACCTCA", "GCCAGTGCCG", "AAGTAGTGAC", "AGGCCTCA"],
          "matej": ["TGCAGGAACTTC", "AAAACCTCA", "CCAGCAATCGC", "TTGTGGTGGC", "AGGCCTCA"],
          "miha": ["TGCAGGAACTTC", "AAAACCTCA", "GCCAGTGCCG", "GGGAGGTGGC", "GCCACGG"]}

# read the dna file
with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

# simply check if all properties of a person appear in the DNA string
# as soon as one of the person's properties doesn't appear in the DNA string,
# we know that this person is innocent...
# only the real perpetrator's will have all his/her properties in the DNA string
for person in people:
    suspect = True
    for prop in people[person]:
        if prop not in dna:
            suspect = False
            break
    if suspect is True:
        print("{} is our perpetrator!".format(person.upper()))
