def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return palindrome(s[1:-1])
    else:
        return False

print(palindrome("madam"))


# -------------Working-----------

# Call is_palindrome("madam")
# Compare first 'm' and last 'm' → ✅ match
# Recurse on "ada"
#
# Call is_palindrome("ada")
# Compare first 'a' and last 'a' → ✅ match
# Recurse on "d"
#
# Call is_palindrome("d")
#
# Length = 1 → Base case → return True