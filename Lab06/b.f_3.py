def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

#Example
input_string = "A man a plan canel Plama"
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")