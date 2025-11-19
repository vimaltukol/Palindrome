def is_palindrome(text):

    text = text.lower()

    return text == text[::-1]



#Example usage

s = input("Enter a string: ")

if is_palindrome(s):

   print("palindrome")

else:

    print("Not a palindrome")