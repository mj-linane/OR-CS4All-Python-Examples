# PROBLEM
"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.
"""

# SOLUTION
s = 'abcdaslkmwen'

# Set up variables
longeststr = ''
longest_sub = [s[0]]
current_sub = [s[0]]

# Iterates over each letter in string s
for index in range(len(s) - 1):
    # Set up variables for easier access to char at index and the one after
    currentchar = s[index]
    nextchar = s[index + 1]
    # Compare the ordinal value of the next char to current
    if nextchar >= currentchar:
        # If next char is larger, add it to the list of the current longest substring list
        current_sub += nextchar
    else:
        # Otherwise, the current_sub gets the next char. This will make sure that the list doesn't include alphabetical substrings tht might later appear in the same string
        current_sub = nextchar
    # After each letter is added to the current substring list, the current_sub list is compared to the longest_sub list. If longer, it takes the place of the longest_sub list.
    if len(current_sub) > len(longest_sub):
        longest_sub = current_sub

# Prints out a joined string from the list of characters.
print("The longest substring in alphabetical order is:",
      longeststr.join(longest_sub))
