# Ex-1
# Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def lesser_function(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
result = lesser_function(2,6)
print(result)

# Ex-2
# Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def letter_function(word):
    word_list = word.split()
    return word_list[0][0] == word_list[1][0]

result1 = letter_function('Crazy Kangaroo')
print(result1)

# Ex-3
# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def int_function(i1,i2):
    return (i1 + i2) == 20 or i1 == 20 or i2 == 20
result3 = int_function(10,20)
print(result3)

# Ex-4
# Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald

def cap_function(word):
    if len(word) > 3:
        return word[:3].capitalize() + word[3:].capitalize()
    else:
        return 'Word is too short'
result4 = cap_function('macdonald')
print(result4)

# Ex-5
# Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def rev_function(sentence):
    return ' '.join(sentence.split()[::-1])
result5 = rev_function('Reverse the sentence')
print(result5)

# Ex-6
# Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True

def compare_function(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10
result6 = compare_function(49)
print(result6)
