# PIG LATIN
# If word starts with vowel, add 'ay' to the end
# If word does not start with vowel, then put first letter to the end and add 'ay'

def pig_latin(word):

    first_letter = word[0]

    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word

print(pig_latin('goat'))
