print("Enter your 8-digt ID Number: ")

a = int(input("1st digit: "))
b = int(input("2nd digit: "))
c = int(input("3rd digit: "))
d = int(input("4th digit: "))
e = int(input("5th digit: "))
f = int(input("6th digit: "))
g = int(input("7th digit: "))
h = int(input("8th digit: "))

x = (a*8) + (b*7) + (c*6) + (d*5) + (e*4) + (f*3) + (g*2) + (h*1)

if x % 11 == 0:
    print()

    if x/11 < 16:
        print("STUDENT")
    elif x/11 >= 16:
        print("FACULTY")
        
else:
    print("INVALID")
