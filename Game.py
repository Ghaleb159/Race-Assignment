from Challenger import Vehicle
from Mustang import Vehicle
from Camero import Vehicle
from Charger import Vehicle
car1 = Vehicle("2023 Dodge Challenger SRT", 807, 8, 100)
car2 = Vehicle("2023 Ford Mustang GT500", 760, 8, 100)
car3 = Vehicle("2023 Chevrolet Camero ZL1", 650, 8, 100)
car4 = Vehicle("2023 Dodge Charger Hellcat", 807, 8, 100)

#MAIN MENU
def mainmenu():
    username = input("\nENTER USER NAME? ")
    print("\nWELCOME TO THE RACE " + username)
    start = input("\nWOULD YOU LIKE TO START THE RACE " + username + ", TYPE YES OR NO:\n\n")

    if start == "yes" or start == "YES":
        print("\n======================================================")
        print("\n RACE IS ON")
        print("\n======================================================")
    elif start == "no" or start == "NO":
        print("YOU HAVE QUIT THE GAME")
        exit()
    else:
        print("\nINVALID\n")
        exit()
menu = mainmenu()

#Lets the user choose the vehicle to race with
def driver_1():

    print("\nPress 1 - 2023 DODGE CHALLENGER SRT, 807, 8, 100")
    print("\nPress 2 - 2023 FORD MUSTANG SHELBY GT500, 760, 8, 100")
    print("\nPress 3 - 2023 CHEVROLET CAMERO ZL1, 650, 8, 100")
    print("\nPress 4 - 2023 DODGE CHARGER HELLCAT, 807, 8, 100")
   
    print("\n======================================================")
    select_1 = int(input("\nWHICH VEHICLE WOULD YOU LIKE TO RACE WITH?  "))
    print("\n======================================================")

    if select_1 == 1:
        return car1
    elif select_1 == 2:
        return car2
    elif select_1 == 3:
        return car3
    elif select_1 == 4:
        return car4
    else:
        print("==================\n==================")
        print("Invalid Entry!!!")
        print("==================\n==================")
        return

#Lets the user choose the vehicle they want to go against
def driver_2():
    

    print("\nPress 1 - 2023 DODGE CHALLENGER SRT, 807, 8, 100")
    print("\nPress 2 - 2023 FORD MUSTANG SHELBY GT500, 760, 8, 100")
    print("\nPress 3 - 2023 CHEVROLET CAMERO ZL1, 650, 8, 100")
    print("\nPress 4 - 2023 DODGE CHARGER HELLCAT, 807, 8, 100")

    print("\n======================================================")
    select_2 = int(input("\nWHICH VEHICLE WOULD YOU LIKE TO RACE AGAINST?  "))
    print("\n======================================================")
    
    if select_2 == 1:
        return car1
    elif select_2 == 2:
        return car2
    elif select_2 == 3:
        return car3
    elif select_2 == 4:
        return car4
    else:
        print("\n==================")
        print("\nInvalid Entery!!! ")
        print("\n==================")
        return
    
def main():
    num_races = 1
    while num_races < 6: # editable number of races

        racer1 = driver_1()
        racer2 = driver_2()

        if racer1 == racer2:
            print("\n======================================================")
            print("\n!!!SAME VEHICLES ARE NOT ALLOWED TO RACE!!!") #user cannot race with the same vehicle
            print("\n======================================================")
            continue
        
        cars = [racer1, racer2]
        winner = None
        Race_score = 0
        score = 0

        print(f"race {num_races}")
        #runs the function race depending on which vehicle chosen 
        for car in cars:
            score = car.race()
            print("\n======================================================")
            print(f"{car.name} IS READY TO RACE!!!")
            print("\n======================================================")


            Race_score = score
            winner = car

        print("\n======================================================")
        print("\n3\n\n2\n\n1\n\nGOOOOOOOO!!!\n")
        print("\n======================================================")
        #the score of each race decides if the user lost/won
        if score < 2000:
            print("CRITICAL LOSS")
        elif score < 4000 and score > 2000:
            print("LOSS")
        elif score < 6000 and score > 4000:
            print("WIN")
        elif score < 8000 and score > 6000:
            print("CRITICAL WIN")

        num_races += 1
        print ("\nRACE IS OVER")
        print (f"\nWINNER IS {winner.name} WITH THE SCORE OF {Race_score}\n\n")
    
    print("\n======================================================")
    print("==================THANKS FOR PLAYING==================")
    print("================Professor Sara Shaheen================")
    print("======================================================")
    print("=========================/\====/\=====================")
    print("========================/  \  /  \====================")
    print("=======================/ P  \/  4 \===================")
    print("=======================\ R  \/  0 /===================")
    print("========================\ O    0 /====================")
    print("=========================\ G  0 /=====================")
    print("==========================\  1 /======================")
    print("===========================\  /=======================")
    print("============================\/========================")
    print("======================================================")
    print("===================Ghaleb Abualhaija==================")
    print("======================================================\n")
    

