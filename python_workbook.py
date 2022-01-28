#Create a program that displays your name and complete mailing address formatted in
#the manner that you would usually see it on the outside of an envelope. Your program
#does not need to read any input from the user.

#fullname = " Andrew Irvine\n"
#address = "67 Deanfield Crescent\n"
#town = "Borrowstounness\n"
#county = "Stirlingshire\n"
#postcode = "EH51 0ET\n"

#print(fullname,address,town,county,postcode)

#Write a program that asks the user to enter his or her name. The program should
#respond with a message that says hello to the user, using his or her name.

#name = str(input("Please Enter A Name: "))
#print("Hello",name)

#Write a program that asks the user to enter the width and length of a room. Once
#the values have been read, your program should compute and display the area of the
#room. The length and the width will be entered as floating point numbers. Include
#units in your prompt and output message; either feet or meters, depending on which
#unit you are more comfortable working with.

#length = float(input("Please Enter The Length of your room in metres: "))
#width = float(input("Please Enter The Width of your room in metres: "))

#print("The area of your room is", length * width, "square meters")

#Create a program that reads the length and width of a farmer’s field from the user in
#feet. Display the area of the field in acres. There are 43560 feet in an acre

#length = int(input("Please Enter The Length of your field in feet: "))
#width = int(input("Please Enter The Width of your field in feet: "))

#print("The area of your field is", length * width /43560, "acres")

#In many jurisdictions a small deposit is added to drink containers to encourage people
#to recycle them. In one particular jurisdiction, drink containers holding one liter or
#less have a $0.10 deposit, and drink containers holding more than one liter have a
#$0.25 deposit.
#Write a program that reads the number of containers of each size from the user.
#Your program should continue by computing and displaying the refund that will be
#received for returning those containers. Format the output so that it includes a dollar
#sign and always displays exactly two decimal places.

#smallbottles = 0.10
#largebottles = 0.25

#less = int(input("Please Enter The number of containers, you have, that hold 1 liter or less: "))
#more = int(input("Please Enter The number of containers, you have, that hold 1 liter or more: "))

#refund = less * smallbottles + more * largebottles

#print("Your total refund is $%.2f." % refund)

#The program that you create for this exercise will begin by reading the cost of a meal
#ordered at a restaurant from the user. Then your program will compute the tax and
#tip for the meal. Use your local tax rate when computing the amount of tax owing.
#Compute the tip as 18 percent of the meal amount (without the tax). The output from
#your program should include the tax amount, the tip amount, and the grand total for
#the meal including both the tax and the tip. Format the output so that all of the values
#are displayed using two decimal places.

#cost = float(input("Please Enter The cost of your meal in £'s and pence: "))

#tax = cost /100 * 20
#tip = cost - tax 
#actualtip = tip /100 * 18
#total = cost + tax + actualtip

#print("Subtotal is £ %.2f" %cost)
#print("Total Sales Tax is £ %.2f" %tax)
#print("Gratuity is £ %.2f" %actualtip)
#print("Grandtotal is £ %.2f" %total)

#An online retailer sells two products: widgets and gizmos. Each widget weighs 75
#grams. Each gizmo weighs 112 grams. Write a program that reads the number of
#widgets and the number of gizmos in an order from the user. Then your program
#should compute and display the total weight of the order.

#widget = 75
#gizmo = 112
#
#total_widgets = int(input("Please Enter The number of widgets, you have: "))
#total_gizmos = int(input("Please Enter The number of gizmos, you have: "))
#
#total_weight = total_widgets * widget + total_gizmos * gizmo
#
#print("Your total gram weight is,",total_weight,"g")

#Pretend that you have just opened a new savings account that earns 4 percent interest
#per year. The interest that you earn is paid at the end of the year, and is added
#to the balance of the savings account. Write a program that begins by reading the
#amount of money deposited into the account from the user. Then your program should
#compute and display the amount in the savings account after 1, 2, and 3 years. Display
#each amount so that it is rounded to 2 decimal places.

deposit_year1 = float(input("Please Enter The amount of money, you have to deposit: "))
deposit_year2 = float(input("Please Enter The amount of money, you have to deposit: "))
deposit_year3 = float(input("Please Enter The amount of money, you have to deposit: "))

interest_year1 = deposit_year1 /100 *4
interest_year2 = (deposit_year2 + total_year1) /100 *4
interest_year3 = deposit_year3 /100 *4

total_year1 = deposit_year1 + interest_year1
