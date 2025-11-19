def is_palindrome(s="madam"):   # default value is "madam"
    # Remove spaces and convert to lowercase for a clean comparison
    clean_s = s.replace(" ", "").lower()
    return clean_s == clean_s[::-1]


# Calling the function without argument (uses default)
result_default = is_palindrome()
print(f"Default value ('madam') → Palindrome? {result_default}")

