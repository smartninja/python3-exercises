# Build a CSI forensics program

The famous CSI just asked you to create a forensics program for them. Exciting, right! :)

But first, they have to teach you a bit about our DNA...

### DNA crash course

If we look deeply how our body works, it seems like a big **computer**. Our **body cells are like programs** - each of them does their own task. Each cell in our body includes DNA where our "code of life" is written. Everything about us is written here: how we look, what eye color we have, how tall are we etc. Of course part of what we are is shaped through our education and life experience, but DNA is responsible for a big chunk of what we are.

The language understood by computers is a **binary or machine code** (zeros and ones). If we write a computer program in Python, it eventually gets translated into zeros and ones (machine code), so computer knows how to run and execute commands written in the program.

Binary/machine code looks like this: 

	100011 00011 01000 00000 00001 000100

But language of our DNA code is not in a form of 0s and 1s - it's instead in the **form of four letters: A, C, T and G**. These letters represent 4 nucleobases: **adenine (A)**, **cytosine (C)**, **guanine (G)** and **thymine (T)**. So DNA can be written like this:

	ACTGCTGCATAGTCTGCAAGACTGAATCACTACGTATCG

This is as much biology as needed to finish this exercise. It's enough to understand that our DNA can be written in a **single string** made of four letters: A, C, G and T. In this DNA code we can **find genes** that define our personal characteristics (hair color, eye color, height etc.).

### Crime!

There has been a hideous crime! A full container of **ice cream** was stored in the SmartNinja fridge - and now it's **completely empty.** But the criminal made a **fatal mistake**. **S/he left a spoon** inside the container and with a spoon also **his/her DNA**. A perfect case for our CSI investigators!

<img class="img-reponsive" src="https://storage.googleapis.com/smartninja-org-assets/curriculums/wd1/img/empty-ice-cream.jpg" width="300px">

CSI lab successfully **extracted the DNA** and wrote it in the ACTG code format. The only thing needed now is **a program that would match that DNA with the suspects DNA** and find the criminal.

Here's the **DNA file**: [dna.txt](https://raw.githubusercontent.com/smartninja/wd1-py3-exercises/master/lesson-11/CSI/dna.txt). Download it (right click --> Save link as) and save it on your computer.

Like we said there are genes hidden in our DNA that define our personal characteristics. The CSI lab got us the following gene sequences for some of the **human characteristics**:

**Hair color:**

- Black: CCAGCAATCGC
- Brown: GCCAGTGCCG
- Blonde: TTAGCTATCGC

**Facial shape:**

- Square: GCCACGG
- Round: ACCACAA
- Oval: AGGCCTCA

**Eye color:**

- Blue: TTGTGGTGGC
- Green: GGGAGGTGGC
- Brown: AAGTAGTGAC

**Gender:**

- Female: TGAAGGACCTTC
- Male: TGCAGGAACTTC

**Race:**

- White: AAAACCTCA
- Black: CGACTACAG
- Asian: CGCGGGCCG

> Please note that these are not real gene sequences and the "DNA" in the file is not a real DNA. It's way too short ;) 

### Suspects

<img src="https://storage.googleapis.com/smartninja-org-assets/curriculums/py/DNA-program-suspects.jpg" class="img-responsive">

Suspects characteristics:

**Eva:**

- Gender: Female
- Race: White
- Hair color: Blonde
- Eye color: Blue
- Face shape: Oval

**Larisa:**

- Gender: Female
- Race: White
- Hair color: Brown
- Eye color: Brown
- Face shape: Oval

**Matej:** 

- Gender: Male
- Race: White
- Hair color: Black
- Eye color: Blue
- Face shape: Oval

**Miha:**

- Gender: Male
- Race: White
- Hair color: Brown
- Eye color: Green
- Face shape: Square

**Write a Python program that finds out who ate the ice cream. Your country will be grateful!**

Hint: There are Python functions that help you find a string within a string.