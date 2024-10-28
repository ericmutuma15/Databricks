# Write a program that accepts a string as input, capitalizes the first letter of each
# word in the string, and then returns the result string.
# Examples:
# "hi"=> returns "Hi"
# "i love programming"=> returns "I Love Programming"


# Solution code

def to_jaden_case(str):
    # Split the phrase into words, capitalize each word, and join them back together
    return ' '.join(word.capitalize() for word in str.split())

# Example 
input_str = "i love programming"
jaden_cased_phrase = to_jaden_case(input_str)
print(jaden_cased_phrase)  # "I Love Programming"