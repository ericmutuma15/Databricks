# Write a Python function that checks whether a word or phrase is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same
# backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"


# Solution code

import string

def is_palindrome(s):
    # Normalize the string: remove punctuation, convert to lowercase, and remove spaces
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example
print(is_palindrome("nurses run"))     # True
print(is_palindrome("Hello, World!"))  # False