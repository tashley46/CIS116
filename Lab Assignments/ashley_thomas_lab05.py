# Name: Thomas Ashley
# Assignment: Lab 5
# Section: A
# Objective: Make 3 triangles, described in the lab instructions,
#            That takes user input for their widths


width = int(input("Enter the desired width of your triangles: "))
char = str(input("Enter the desired character that makes up the triangles: "))


#-----------------------------------------------------------------
#            Part: One - Bottom Right, Right Triangle
#-----------------------------------------------------------------
print()
print()
print("-------------------Part: One - Bottom Right, Right Triangle--------------------")

i = 1
while i <= width:
    j = width
    while j > 0:
        if(j <= i):
            print(char, end="")
        else:
            print(" ", end="")
        j -= 1
    print()
    i += 1

print()
print()
print("-------------------Part: Two - Top Right, Right Triangle--------------------")

#-----------------------------------------------------------------
#             Part: Two - Top Right, Right Triangle
#-----------------------------------------------------------------
i = width
while i > 0:
    j = width
    while j > 0:
        if(j >= i):
            print(" ", end="")
        else:
            print(char, end="")
        j -= 1
    print()
    i -= 1
#-----------------------------------------------------------------
#         Part: Three - Right Side, Isosceles Triangle
#-----------------------------------------------------------------
print()
print()
print("-------------------Part: Three - Right Side, Isosceles Triangle--------------------")

i = 1
while i <= 2 * width:    
    if i <= width:
        j = width       
        while j > 0:
            if(j <= i):
                print(char, end="")
            else:
                print(" ", end="")
            j -= 1
    else:
        j = width
        while j < width * 2:
            if j < i:
                print(" ", end="")
            else:
                print(char, end="")
            j += 1
    print()
    i += 1