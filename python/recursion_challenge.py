def factorial(x):
	if x == 1:
		return 1 
	
	return x * factorial(x-1)

print(factorial(1))
print(factorial(5))


def reverse(string): 
	if len(string) <= 1:
		return string
	else: return reverse(string[1:]) + string[0]

def palindrome(string):
	if reverse(string) == string:
		return True
	else:
		return False

print(palindrome('racecar'))
print(palindrome("Apple"))
	







# def bottles(num):
# 	pass

def roman_num(num):
    # Map of integer values to their corresponding Roman numeral symbols.
    value_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    # Base case: when num is 0, return an empty string.
    if num == 0:
        return ""

    # Recursive case: find the highest value less than or equal to num.
    for value, symbol in value_map:
        if num >= value:
            # Return the symbol and recursively process the remainder of num.
            return symbol + roman_num(num - value)

# Example usage:
print(roman_num(1994))  # Output: "MCMXCIV"