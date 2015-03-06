# Chapter_8 Challenge 1
class critter(object):
    """A Virual Pet"""
    def __init__(self, name, hunger = 0, boredom=0):
        self.name=name
        self.hunger=hunger
        self.boredom=boredom

    def __pass_time(self):
        self.hunger+=1
        self.boredom +=1


    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m="happy"
        elif 5 <= unhappiness <=10:
            m="okay"
        elif 11<=unhappiness <=15:
            m="frustrated"
        else:
            m="mad"
        return m
    def talk(self):
        print(self.name,"is feeling",self.mood,".\n")
        self.__pass_time()
    def eat(self):
        food = int(input("How many ounces do you want to feed "+self.name+"? "))
        print("Brrrrupp.")
        self.hunger -= food
        if self.hunger <0:
            self.hunger=0
        self.__pass_time()

    def play(self, fun=0):
        play_Time= int(input("How many hours do you want to play with " +self.name+"? "))
        print("Wheeeeee!")
        self.boredom -=play_Time
        if self.boredom < 0:
            self.boredom =0
        self.__pass_time

def main():
    crit_name=input("What do you want to name your critter?: ")
        
    crit = critter(crit_name)
    choice= None
    while choice !="0":
        print \
         ("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
            """)

        choice = input("Choice: ")
        print()

        if choice =="0":
            input("Press <enter> to exit...")
        elif choice == "1":
            crit.talk()
        elif choice=="2":
            crit.eat()
        elif choice =="3":
            crit.play()

        else:
            print(choice,"is not a valid choice.")
main()

