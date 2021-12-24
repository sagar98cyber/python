credit_is_good = True
good_income = True
has_criminal_record = False
#and, not operators
if credit_is_good and good_income and not has_criminal_record:
    print("Eligible for loan")
#or opeartor
elif credit_is_good or good_income:
    print("Lucky there is an OR operator")
