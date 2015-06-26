#Zip file password cracker#

---

##A simple python script to crack a zip file password.

###Methods supported:

1. **Bruteforce attack** - all charset to be tested with provided minimum and maximum password length.

2. **Advance Bruteforce attack**- all charset to be tested from provided charset with provided minimum and maximum password length.

3. **Dictionary attack** - all passwords from dictionary file will be tested

###Usage

---

usage: script.py filename [-b | -ab charset=charset | -m=[2,5] | -d file=dictionary.txt]

option:

-b                      :Bruteforce attack.

-ab -file=charset       :Advance Bruteforce attack from the given charset.

-d file=dictionary.txt        :Dictionary attack. Provide dictionary name in present working directory

-m=[min, max]           :Minimum and Maximum length of passwords to be consider.

###Includes

---

1. test.zip : open zip file

2. test1.zip. password protected zip file. password: 123