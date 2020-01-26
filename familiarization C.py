counter = 0

while counter == 0:
    txt = "Welcome to our automated milk tea ordering system"
    x = txt.center(60, "*")
    print(x) 
    
    print("For today's milk tea, we offer:")
    
    print("[1] Original milk tea")
    print("[2] Pearl milk tea")
    print("[3] Coffee jelly milk tea")
    print("[Q] Quit")
    
    x = str(input("Your choice? "))
    if x=="1":
        print("Original milk tea costs 60 pesos")
    elif x=="2":
        print("Pearl milk tea costs 65 pesos")
    elif x=="3":
        print("Coffee jelly milk tea costs 75 pesos")
    elif x=="Q":
        print("Please come again")
    
    input("Press any key to continue...")

