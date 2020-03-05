"""
19
Write a Python program to get a new string from a given string 
where "Is" has been added to the front. 
If the given string already begins with "Is" then return the string unchanged.

"""

def string_is():
    x=input("Type sentence")
    if x.startswith("Is"):
        return x
    else:
        print("Is "+x)


#sample sollution
def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str

print(new_string("Array"))
print(new_string("IsEmpty"))

"""
20. Write a Python program to 
get a string which is n (non-negative integer) copies of a given string.
"""

def w3re_20(x, n):
    y=x*abs(int(n))
    return y

"""
21. Write a Python program to find whether a given number (accept 
from the user) is even or odd, print out an appropriate
 message to the user. 
"""
def w3re_21(x):
    if x%2==0:
        print(x, "is even")
    else:
        print(x, "is odd")


w3re_21(4)
w3re_21(5)
w3re_21(3892)

"""
22. Write a Python program to count the number 4 in a given list. 
Click me to see the sample solution
"""
def w3re_22(x):
    n=0
    for i in x:
        if i ==4:
            n +=1
        
    return n

w3re_22([4, 4, 4, 4, 4])
w3re_22([5, 6, 4, 1 ,2])





"""
23. Write a Python program to get the n (non-negative integer) 
copies of the first 2 characters of a given string. 
Return the n copies of the whole string if the length is 
less than 2. 
"""
def w3re_23(a,b):
    if len(a)<2:
        return a*int(b)
    else:
        return a[0:2]*int(b)

w3re_23("dog", 3)
w3re_23("f", 4)


"""
24. Write a Python program to test whether a passed letter 
is a vowel or not. 
"""
def w3re_24(a):
    list_vowel= ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    if a in list_vowel:
        print(a, "is a vowel")
    else:
        print(a, "is not a vowel")

w3re_24("a")
w3re_24("F")
w3re_24("I")

#sample solution
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))


"""
25. Write a Python program to check whether a specified value is 
contained in a group of values. Go to the editor
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""
def w3re_25(x, y):
    return(y for y in x)
w3re_25(8)
w3re_25(-1)
def w3re_25(x, y):
    return(y in x)


"""
26. Write a Python program to create a histogram from 
a given list of integers. Go to the editor
Click me to see the sample solution
"""

import numpy as np
import matplotlib.pyplot as plt
x=[2, 4, 5, 10, 19]
plt.hist(x)

#sample solution
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])


"""

27. Write a Python program to concatenate all elements in a list into a string and return it. Go to the editor
Click me to see the sample solution

"""

def w3re_26(str_list):
    x=""
    for i in str_list:
        x += i
    return x

w3re_26(["beatles", "rolling stones", "red hot chili peppers", "8"])
#sample solutionも全く同じアプローチ

"""
28. Write a Python program to print all even numbers from a 
given numbers list in the same order and stop the printing 
if any numbers that come after 237 in the sequence. Go to the editor
Sample numbers list :

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 
    566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 
    248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 
    553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
Click me to see the sample solution
"""

def w3re_27():
    numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 
    566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 
    248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 
    553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527]
    for i in numbers:
        if i%2==0:
            print(i)
        elif i ==237:
            break


"""
29. Write a Python program to print out a set containing 
all the colors from color_list_1 which are not present 
in color_list_2. Go to the editor
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
Click me to see the sample solution
"""

def w3re_29(x, y):
    z=[i for i in x if i not in y]
    set(z)
    return

#sample solution
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))

#もっとかんたん

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1 - color_list_2)

"""
30. Write a Python program that will accept the base and 
height of a 
triangle and compute the area. 
"""
def w3re_30(x,y):
    return x*y/2


