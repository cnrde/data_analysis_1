

def is_vowel(char):
    vowels = "aeiouAEIOU"
    return char in vowels

def capitalize_vowels(text):
    words = text.split()
    new_text = []
    for word in words:
        if word and is_vowel(word[0]):
            new_text.append(word.capitalize())
        else:
            new_text.append(word)
    return " ".join(new_text)

file_path = "indiv1.txt"
with open(file_path, "r") as file:
    text = file.read()

modified_text = capitalize_vowels(text)
print(modified_text)
