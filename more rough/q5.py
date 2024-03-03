#WAP to accept a character from user and display weather it is a vowel or consonant

alphabet=(input("Input your alphabet="))

y=("aeiouAEIOU")

for i in alphabet:
    if i in y:
        print("Vowel")
    else:
        print("Consonant")
