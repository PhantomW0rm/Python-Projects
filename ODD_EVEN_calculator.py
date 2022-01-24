# Takes user input for a number
num = int(input("Enter a number: "))
# if statement to decide if the user has entered an even or odd number using modulo 
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))