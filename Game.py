import random


#This is a logic module

class Vehicle:
    def __init__(self, name, HP, Enginesize, Body):
        self.name = name
        self.HP = HP
        self.Enginesize = Enginesize
        self.Body = Body


    def race(self):
        Dice_roll = random.randrange(2,12)
        return self.Body + self.Enginesize + self.HP * Dice_roll

def main():
    num_races = 1
    while num_races < 6: # editable number of races

        racer1 = driver_1()
        racer2 = driver_2()

        if racer1 == racer2:
            print("\n==================================================")
            print("\n!!!SAME VEHICLES ARE NOT ALLOWED TO RACE!!!")
            print("\n==================================================")
            continue
        
        cars = [racer1, racer2]
        winner = None
        Race_score = 0
        score = 0

        print(f"race {num_races}")
        #runs the function race depending on which vehicle chosen 
        for car in cars:
            score = car.race()
            print("======================================================")
            print(f"{car.name} IS READY TO RACE!!!")
            print("======================================================")


            Race_score = score
            winner = car

        print("\n======================================================")
        print("\n3\n\n2\n\n1\n\nGOOOOOOOO!!!\n")
        print("======================================================")
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
    