def is_palindrome(word):
    # Convert the word to lowercase to ensure case-insensitive comparison
    word = word.lower()
    # Check if the word is equal to its reverse
    return word == word[::-1]

# Example usage
word = "Level"
if is_palindrome(word):
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome")

