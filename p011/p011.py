usr_in = input("Enter words: ").split(',')
vowels = "a e i o u".split(" ")

long_word = shor_word = usr_in[0]
vowels_count = 0
joined = ""

for word in usr_in:
    word = word.strip()
    # Longest word
    if len(word) >= len(long_word):
        long_word = word

    # Shortest word
    if len(word) <=len(shor_word):
        shor_word = word
    
    # Count of words that start with a vowel
    if word[0].lower() in vowels:
        vowels_count += 1
    
    joined = joined +  word + "-" 
joined = joined[:-1]
    
    

print(f"Longest word: {long_word}")
print(f"Shortest word: {shor_word}")
print(f"Starts with vowel: {vowels_count}")
print(f"Joined: {joined}")
