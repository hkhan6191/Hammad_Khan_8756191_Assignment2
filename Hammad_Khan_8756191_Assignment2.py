print("Welcome, to Abby's Merchandizing! This tool can be used to place an order with us as well as to calculate the total cost of your order. Let's get started!")

polo = 1
tshirt = 2

zipup = 11
pullover = 12

blue = 3
red = 4
green = 5
yellow = 6
orange = 7
white = 8
black = 9
brown = 10

cost = 9.99
cost2 = 14.99
hst = 1.13

print("")

print("We offer a wide range of colors for our shirts starting at $9.99 each! Please enter in the number that corresponds with the color you want!")
print("Blue = 3")
print("Red = 4")
print("Green = 5")
print("Yellow = 6")
print("Orange = 7")
print("White = 8")
print("Black = 9")
colorinput = int(input("What color shirt would you like?: ")) 

if colorinput == blue:
    print("Blue, great choice! ")

elif colorinput == red:
    print("Red, great choice! ")

elif colorinput == green:
    print("Green, great choice! ")

elif colorinput == yellow:
    print("Yellow, great choice! ")

elif colorinput == orange:
    print("Orange, great choice! ")

elif colorinput == white:
    print("White, great choice! ")

elif colorinput == black:
    print("Black, great choice! ")

else:
    print("Oops! The color you want is not in stock  :( ")
    colorinput = int(input("Please select a different shirt color: "))

print("")

print("Next, select the type of shirt would you would like. We offer two types of shirts. Please enter in the number that corresponds with the one you want!")
print("Polo = 1")
print("T-Shirt = 2")
typeinput = int(input("Please select the type of shirt would you like!: "))

if typeinput == polo:
    print("Polo. Great choice!")

elif typeinput == tshirt:
    print("T-Shirt. Great choice!")

else:
    print("Looks like we are all out of that type of shirt... ")
    typeinput = int(input("Please select either a Polo or a T-Shirt: "))

print("")

numinput = int(input("Lastly, decide how many shirts you would like!: "))

print("")

print("We are excited to announce that we are now selling hoodies starting at $14.99 each! Please enter in the number that corresponds with the color hoodie you want!")
print("White = 8")
print("Black = 9")
print("Brown = 10")
colorinput2 = int(input("What color hoodie would you like?: "))

if colorinput2 == white:
    print("White, great choice! ")

elif colorinput2 == black:
    print("Black, great choice! ")

elif colorinput2 == brown:
    print("Brown, great choice! ")

else:
    print("Oops! The color you want is not in stock  :( ")
    colorinput2 = int(input("Please select a different hoodie color: "))

print("")

print("Next, select the type of hoodie would you would like. We offer two types of hoodies. Please enter in the number that corresponds with the one you want!")
print("Zip-Up = 11")
print("Pullover = 12")
typeinput2 = int(input("Please select the type of hoodie would you like!: "))

if typeinput2 == zipup:
    print("Zip-Up. Great choice!")

elif typeinput2 == pullover:
    print("Pullover. Great choice!")

else:
    print("Looks like we are all out of that type of hoodie... ")
    typeinput2 = int(input("Please select either a Zip-Up or a Pullover: "))

print("")

numinput2 = int(input("Lastly, decide how many hoodies you would like!: "))

print("")

print("Alright, lets recap your order.")

print("")

print("Color of shirt: " + str(colorinput))
print("Type of shirt: " + str(typeinput))
print("Number of shirt(s): " + str(numinput))
print("Color of hoodie: " + str(colorinput2))
print("Type of hoodie: " + str(typeinput2))
print("Number of hoodie(s): " + str(numinput2))

print("")

totalcost = (cost*numinput)
totalcost2 = (cost2*numinput2)
finalcost = (totalcost + totalcost2)

print("Your total cost today will be: $%.2f" % (finalcost * hst))

print("Thank you for choosing Abby's Merchandizing today! We hope you enjoyed your shopping experience with us! ")