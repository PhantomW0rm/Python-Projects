#def add_calc(number1, number2):
#    answer = number1 + number2
#    return answer

#added_number = add_calc(5,5)
#print(added_number + 20)

def maxtwo( x, y ):
    if x > y:
        return x
    return y
def maxthree( x, y, z ):
    return maxtwo( x, maxtwo( y, z ) )
print(maxthree(3, 6, 23))