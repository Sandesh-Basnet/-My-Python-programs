# getting age year input
age_input = int(input("In which year were you born: "))
# getting in which year input
in_which_year = input("In which date BS or AD: ")
# using if and elif statement to find the result
if in_which_year == "AD":
    ad_year = 2022 - age_input
    print("You are",ad_year,"year old." )
elif in_which_year == "BS":
    bs_year = 2079 - age_input
    print("You are",bs_year,"year old." )
elif in_which_year == "bs":
    print("Please type in Capital Letter")
elif in_which_year == "Bs":
    print("Please type in Capital Letter")
elif in_which_year == "bS":
    print("Please type in Capital Letter")
elif in_which_year == "ad":
    print("Please type in Capital Letter")
elif in_which_year == "aD":
    print("Please type in Capital Letter")
elif in_which_year == "Ad":
    print("Please type in Capital Letter")
# if the value is not recognized the it will print your value is not reconized 
else:
    print("Not rercognized value or date")
