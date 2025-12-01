usr_in = input("Enter a sentence: ")
letters = [ch for ch in usr_in if ch!=' ']
vowels = "a e i o u".split()

#Vowels
no_vowels = 0

for letter in letters:
    for vowel in vowels:
        if vowel == letter.lower():
            no_vowels += 1

# Words Count
no_words = len(usr_in.split())

# Sentence Reverse
rev = ""
for i in usr_in:
    rev = i + rev

print(f"Vowels: {no_vowels}")
print(f"Words: {no_words}")
print(f"Reversed: {rev}")