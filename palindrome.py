def is_palindrome(text):
    text = text.lower()              # convert to lowercase
    return text == text[::-1]        # compare with reversed string

# Example usage
s = input("Enter a string: ")
if is_palindrome(s):
    print("Palindrome")
else:
    print("Not a palindrome")
