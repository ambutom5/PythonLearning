def reversestring(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reversestring(s[:-1])

print(reversestring("ABCDEFG"))

#     Working
# ----------------
# For "hello":
# o + reverse("hell")
# o + l + reverse("hel")
# o + l + l + reverse("he")
# o + l + l + e + reverse("h")
# o + l + l + e + h = "olleh"