# Requires a letter to be input by the user
letter = input("Input a letter of the alphabet: ")
# Use of the if statement to check if it is a vowel and will print this is a vowel
if letter in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % letter)
    # use of else if statement if the letter equals to y print out it is sometimes a vowel and sometimes consonant
elif letter == 'y':
	print("Sometimes letter y is a vowel, sometimes y is a consonant.")
# Else statement if the letter is a consonant except for y then print the letter is a consonant
else:
	print("%s is a consonant." % letter) 