import sys

def is_palindrome(s):
    return s == s[::-1]

def main():
    if len(sys.argv) < 2:
        print("Usage: python palindrome.py <string>")
        return
    s = sys.argv[1]
    if len(s) < 4 or not s.isalpha():
        print("Please enter at least 4 alphabets only")
    elif is_palindrome(s):
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")

if __name__ == "__main__":
   main()
