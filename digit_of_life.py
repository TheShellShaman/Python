bd = 0

while bd == 0:
    try:
        bd = int(input("Please enter your birthday in any format (Including full year)  -  "))
        if not bd.is_integer:
            raise ValueError
        if len(str(bd)) != 8:
            raise ValueError
        
    except ValueError:
        bd = 0
        print("Please  input a correct value for the question")
        
digit = 0
new_bd = ""
digit2 = 0

for n in str(bd):
        new_bd = (new_bd + (n))
        print(new_bd)

for n in new_bd:
     digit += int(n)

for n in str(digit):
     digit2 += int(n)


# for n in new_bd:
#     digit += new_bd[n]

# for n in digit:
#     digit2 += digit[n]
print("Your digit of life is ", digit2)