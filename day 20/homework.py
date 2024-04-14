

"""1)
first task in codewar:
Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse)."""

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

"""2)
second task in codewar:
We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?"""

def number_to_string(num):
    # Return a string of the number here!
    return str(num)

"""3)
third task in codewar:
 Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse)."""

def opposite(number):
    return -number


"""4)
fourth task in codewar:
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?"""

def make_negative( number ):
    if number >= 0:
        return -number
    else:
        return number
    


"""5)
fifth task in codewar:
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false."""

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
    


"""6)
sixth task in codewar:
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0."""


def positive_sum(arr):
    sum = 0
    for num in arr:
        if num > 0:
            sum += num
    return sum

print(positive_sum([1,-4,7,12]))  


"""7)
seventh task in codewar:
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry about strings with less than two characters."""

def remove_char(s):
    #your code here
    return s[1:-1]



"""😎
eighth task in codewar:
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 
1
2
+
2
2
+
2
2
=
9
1 
2
 +2 
2
 +2 
2
 =9."""

def square_sum(numbers):
    #your code here
    return sum(x**2 for x in numbers)




"""9)
ninth task in codewar:"""









"""10)
tenth task in codewar:
Code as fast as you can! You need to double the integer and return it."""

def double_integer(i):
    return i * 2
