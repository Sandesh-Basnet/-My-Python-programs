weight_input = int(input("What is your weight: "))
pro = input("lbs or kg: ")
if pro == "lbs":
    sum = weight_input * 0.45359237
    print("You are ",sum,"kg")
elif pro == "kg":
    sum = weight_input/0.45359237
    print("You are",sum,"Pound(Lbs)")
else:
    print(" the value you entered is not valied!")