age_input = int(input("What is is your age: "))
age_year_type = input("In which date you want your age to be (AD or BS): ")
if age_year_type == "AD":
    age = 2020 - age_input
    print("You were born on", age)
elif age_year_type == "BS":
    age_two = 2077 - age_input
    print("You were born on", age_two)
elif age_year_type == "bs":
    print("Please type in Capital Letter")
elif age_year_type == "ad":
    print("Please type in Capital Letter")
elif age_year_type == "Bs":
    print("Please type in Capital Letter")
elif age_year_type == "bS":
    print("Please type in Capital Letter")
elif age_year_type == "ad":
    print("Please type in Capital Letter")
elif age_year_type == "Ad":
    print("Please type in Capital Letter")
elif age_year_type == "aD":
    print("Please type in Capital Letter")
else:
    print("Error! Your date type is not recognized")
