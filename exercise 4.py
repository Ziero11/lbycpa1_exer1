counter = 0

while counter == 0:

    #Screen Select
    print("Welcome, choose which equation you want to use. \n\n [1] P\u2081V\u2081 = P\u2082V\u2082 \n [2] V\u2093 = V\u2092 + a * t \n [Q] Quit \n")
    x = str(input("Your choice? "))
    if x=="1":
        #Boyle's Law
        counter = 0
        while counter == 0:
            print("Boyle's Law: \n\n [a] Initial Pressure\n [b] Initial Volume\n [c] Final Pressure\n [d] Final Volume\n [e] Return to equation selection screen\n")
            x = str(input("Select the variable you want to solve: "))
            if x=="a":
                print("Give the value for initial volume, final pressure, and final volume \n equation: P\u2081 = (P\u2082V\u2082)/V\u2081")
                iv = int(input("Initial Volume [L]: "))
                fp = int(input("Final Pressure [atm]: "))
                fv = int(input("Final Volume [L]: "))
                import math
                ans = (fp * fv) / iv
                print("Answer: \n", ans)
                input("\n")

            elif x=="b":
                print("Give the value for initial pressure, final pressure, and final volume \n equation: V\u2081 = (P\u2082V\u2082)/P\u2081")
                ip = int(input("Initial Pressure [atm]: "))
                fp = int(input("Final Pressure [atm]: "))
                fv = int(input("Final Volume [L]: "))
                import math
                ans = (fp * fv) / ip
                print("Answer: \n", ans)
                input("\n")

            elif x=="c":
                print("Give the value for initial volume, initial pressure, and final volume \n equation: P\u2082 = (P\u2081V\u2081)/V\u2082")
                iv = int(input("Initial Volume [L]: "))
                ip = int(input("Initial Pressure [atm]: "))
                fv = int(input("Final Volume [L]: "))
                import math
                ans = (ip * iv) / fv
                print("Answer: \n", ans)
                input("\n")

            elif x=="d":
                print("Give the value for initial volume, initial pressure, and final pressure \n equation: V\u2082 = (P\u2081V\u2081)/P\u2082")
                ip = int(input("Initial Volume [L]: "))
                fp = int(input("Initial Pressure [atm]: "))
                fv = int(input("Final Pressure [atm]: "))
                import math
                ans = (fp * fv) / ip
                print("Answer: \n", ans)
                input("\n")

            elif x=="e":
                break
                print("Welcome, choose which equation you want to use. \n\n [1] P\u2081V\u2081 = P\u2082V\u2082 \n [2] V\u2093 = V\u2092 + a * t \n [Q] Quit \n")
                x = str(input("Your choice? "))
                input("\n")

    elif x=="2":
        #Kinematic Equation
        counter = 0
        while counter == 0:
            print("Kinematic Equation with final velocity, initial velocity, time, and acceleration: \n\n [a] Final Velocity \n [b] Initial Velocity \n [c] Time \n [d] Acceleration \n [e] Return to equation selection screen\n")
            x = str(input("Select the variable you want to solve: "))
            if x=="a":
                print("Give the value for initial velocity, time, and acceleration \n equation: V\u2093 = V\u2092 + a * t")
                iv = int(input("Initial Velocity: "))
                t = int(input("Time: "))
                a = int(input("Acceleration: "))
                import math
                ans = iv + (a*t)
                print("Answer: \n", ans)
                input("\n")

            elif x=="b":
                print("Give the value for final velocity, time, and acceleration \n equation: V\u2092 = V\u2093 - a * t")
                fv = int(input("Final Velocity: "))
                t = int(input("Time: "))
                a = int(input("Acceleration: "))
                import math
                ans = fv - (a*t)
                print("Answer: \n", ans)
                input("\n")

            elif x=="c":
                print("Give the value for final velocity, initial velocity, and acceleration \n equation: t = (V\u2093/a) - V\u2092")
                fv = int(input("Final Velocity: "))
                iv = int(input("Initial Velocity: "))
                a = int(input("Acceleration: "))
                import math
                ans = (fv/a) - iv
                print("Answer: \n", ans)
                input("\n")

            elif x=="d":
                print("Give the value for final velocity, initial velocity, and time \n equation: a = (V\u2093/t) - V\u2092")
                fv = int(input("Final Velocity: "))
                iv = int(input("Initial Velocity: "))
                t = int(input("Time: "))
                import math
                ans = (fv/t) - iv
                print("Answer: \n", ans)
                input("\n")

            elif x=="e":
                break
                print("Welcome, choose which equation you want to use. \n\n [1] P\u2081V\u2081 = P\u2082V\u2082 \n [2] V\u2093 = V\u2092 + a * t \n [Q] Quit \n")
                x = str(input("Your choice? "))
                input("\n")

    elif x=="Q" or "q":
        print("See you next time")
        break

    else:
        print("Error")
        input("Press Enter to continue...")