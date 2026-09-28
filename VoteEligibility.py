def vote_eligibility(age, country):
    if age >= 18 and country == "Nigeria":
        return "Eligible"

    else:
        return "Not eligible"
    
print(vote_eligibility(18, "Nigeria"))
print(vote_eligibility(17, "Nigeria"))
print(vote_eligibility(25, "Ghana"))

