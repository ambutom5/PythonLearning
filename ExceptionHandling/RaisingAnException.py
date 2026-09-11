def checkage(age):

    if age < 18:
        raise ValueError("Not Eligible")
    return "Eligible"

print(checkage(12))