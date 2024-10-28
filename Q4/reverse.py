# Write a program that takes an integer as input and returns an integer with
# reversed digit ordering.
# Examples:
# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19.


# Solution code

def reverse_int(n):
    # Check if the number is negative
    is_negative = n < 0
    
    # Convert the number to string, remove the sign if negative
    str_n = str(abs(n))
    
    # Reverse the string representation of the number
    reversed_str_n = str_n[::-1]
    
    # Convert back to integer and restore the sign if negative
    reversed_int = int(reversed_str_n)
    if is_negative:
        reversed_int = -reversed_int
    
    return reversed_int

# Example
print(reverse_int(500))   # Output: 5
print(reverse_int(-56))   # Output: -65
print(reverse_int(-90))   # Output: -9
print(reverse_int(91))    # Output: 19
