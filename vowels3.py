vowels=['a','e','i','o','u']
word=input("Please enter a word to search for a vowel:")
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)
for vowel in found:
    print(vowel)
