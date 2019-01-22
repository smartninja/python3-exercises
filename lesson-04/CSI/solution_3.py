characteristics = {
    'hair': {
        'black': 'CCAGCAATCGC',
        'brown': 'GCCAGTGCCG',
        'blonde': 'TTAGCTATCGC'
    },
    'face': {
        'square': 'GCCACGG',
        'round': 'ACCACAA',
        'oval': 'AGGCCTCA'
    },
    'eyes': {
        'blue': 'TTGTGGTGGC',
        'green': 'GGGAGGTGGC',
        'brown': 'AAGTAGTGAC'
    },
    'gender': {
        'female': 'TGAAGGACCTTC',
        'male': 'TGCAGGAACTTC'
    },
    'race': {
        'white': 'AAAACCTCA',
        'black': 'CGACTACAG',
        'asian': 'CGCGGGCCG'
    }
}

suspects = {
    'Eva': {
        'hair': 'blonde',
        'face': 'oval',
        'eyes': 'blue',
        'gender': 'female',
        'race': 'white'
    },
    'Larisa': {
        'hair': 'brown',
        'face': 'oval',
        'eyes': 'brown',
        'gender': 'female',
        'race': 'white'
    },
    'Matej': {
        'hair': 'black',
        'face': 'oval',
        'eyes': 'blue',
        'gender': 'male',
        'race': 'white'
    },
    'Miha': {
        'hair': 'brown',
        'face': 'square',
        'eyes': 'green',
        'gender': 'male',
        'race': 'white'
    }
}

# read the dna file
with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

suspect = {}

# iteritems() function will iterate through the characteristics data
for key, value in characteristics.items():
    for characteristic, sequence in value.items():
        if dna.find(sequence) != -1:
            suspect[key] = characteristic
            break

name = ''

for n, value in suspects.items():
    current_name = ''

    for k, v in value.items():
        if suspect[k] == v:
            current_name = n
        else:
            current_name = ''
            break

    if current_name:
        name = current_name
        break

print("The person who ate the ice cream is {0}.".format(name))
