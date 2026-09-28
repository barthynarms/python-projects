text = input("Enter a sentence: ")
vowels = ['a','e','i','o','u']
vowel_count = consonant_count = digit_count = space_count = punctuation_count = 0

for ch in text.lower():
    if ch in vowels:
        vowel_count += 1
    elif ch.isalpha():
        consonant_count += 1
    elif ch.isdigit():
        digit_count += 1
    elif ch == ' ':
        space_count += 1
    elif ch in '.,!?;:\'"-()':
        punctuation_count += 1

print(f"Vowels: {vowel_count}, Consonants: {consonant_count}, Digits: {digit_count}, Spaces: {space_count}, punctuation: {punctuation_count}")