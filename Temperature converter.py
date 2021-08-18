print("This is a Temperature Converter created by Sandesh Basnet aka Heptasec!!!!")
input_method = int(input('''Choose from the following option to begin the conversion process!!!
   		     			1) Celsius(C) to Fahrenheit(F)
   		     			2) Celsius(C) to Kelvin(K)
   		     			3) Fahrenheit(F) to Celsius(C)
   		     			4) Fahrenheit(F) to Kelvin(K)
   		    			5) Kelvin(K) to Celsius(C)
   		     			6) Kelvin(K) to Fahrenheit(F)
>'''))
if input_method == 1:
	input_temp = int(input("Enter the the value of Celsius:"))
	sum = (input_temp*9/5)+32
	print(input_temp ,'Celsius is', sum ,'Fahrenheit')
elif input_method == 2:
	input_temp = int(input("Enter the value of Celsius:"))
	sum = (input_temp-273.15)*9/5+32
	print(input_temp ,'Celsius is', sum ,'Kelvin')
elif input_method == 3:
	input_temp = int(input("Enter the value of Fahrenheit:"))
	sum = (input_temp-32)*5/9
	print(input_temp ,'Fahrenheit is', sum ,'Celsius')
elif input_method == 4:
	input_temp = int(input("Enter the value of Fahrenheit:"))
	sum = (input_temp-32)*5/9+273.15
	print(input_temp ,'Fahrenheit is', sum ,'Kelvin')
elif input_method == 5:
	input_temp = int(input("Enter the value of Kelvin:"))
	sum = input_temp-273.15
	print(input_temp ,'Kelvin is', sum ,'Celsius')
elif input_method == 6:
	input_temp = int(input("Enter the value of Kelvin:"))
	sum = (input_temp-273.15)*9/5+32
else:
	print("Error!! 404 value not found!!")
