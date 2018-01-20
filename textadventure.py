from random import randint
class Adventure:
    def yn(self, phrase):
        inp = ""
        while inp == "":
            inp = input(phrase+"? (y/n) ")
            if inp not in ("y", "n"):
                inp = ""
                print("Are you an idiot?.")
        return inp == "y"

    def numbers(self, numbers, phrase):
        inp = ""
        while inp == "":
            inp = input(phrase+"? ("+"/".join(numbers)+")")
            if inp not in numbers:
                inp = ""
                print("Are you an idiot?")
        return int(inp)

    def pt0(self):
        print("Welcome to the ETA text adventure. ETA is 2400 hours. Controls: y=yes, n=no, i=up, k=down, j=left, l=right, a=a, b=b, 1=1st option, etc.")
        if self.yn("Continue"):
            self.pt1()
        else:
            print("You're an idiot! You need to continue")
            self.gameover()
        
    def pt1(self):
        print("Welcome to the ETA, the US Department of Extra Terrestrial Arrivals.\nFor your first mission, you will need to infiltrate a dangerous secret alien base deep inside the Arctic.")
        if self.yn("Will you accept the mission"):
            self.pt2()
        else:
            print("You get executed for desertion.")
            self.gameover()

    def pt2(self):
        print("In Northern Alaska, the plane makes an emergency landing and will depart in another 24 hours.\nIn the nearby village, there is a casino resort, a 5 star hotel, and a 1 star.")
        inp = self.numbers(('1', '2', '3'), "Do you go to the casino resort, 5 star hotel, or 1 star hotel")
        if inp == 1:
            if randint(1, 100) < 30:
                print("You made a lot of money gambling.")
                self.pt3()
            else:
                print("You lost all your money gambling and lost track of time so missed your flight and couldn't get a new ticket.")
                self.gameover()
        elif inp == 2:
            print("There was a shooter at the hotel and you died.")
            self.gameover()
        else:
            print("The bad hotel, although uncomfortable, was safe. You continue onto the next flight to the North Pole.")
            self.pt3()

    def pt3(self):
        print("You successfully landed in the North Pole. There is a fat guy with a white beard there.")
        if self.yn("Should you follow your shoot to kill order and kill him"):
            print("The guy in question was Santa Claus. He ordered his elves to kill you.")
            self.gameover()
        else:
            print("Under construction.")

    def gameover(self):
        input("You died.")
adventure = Adventure()
adventure.pt0()
