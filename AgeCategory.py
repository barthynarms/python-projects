#age category using if, elif, else
def age_category(age):
    if age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

print(age_category(10))
print(age_category(15))
print(age_category(30))