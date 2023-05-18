class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.fname = first_name
        self.lname = last_name
        self.treat = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self, pet): #walks the ninja's pet invoking the pet play() method
        Pet.play(pet)
    def feed(self, pet): #feeds the ninja's pet invoking the pet eat() method
        Pet.eat(pet)
    def bathe(self, pet): #cleans the ninja's pet invoking the pet noise() method
        Pet.noise(pet)




class Pet:
    def __init__(self, name , type , tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 50
        self.health = 100

    def sleep(self): # increases the pets energy by 25
       self.energy += 25
       print(self.energy)
    
    def eat(self): # increases the pet's energy by 5 & health by 10
        self.energy += 5
        self.health += 10
        print(self.health)
        print(self.energy)

    def play(self): # increases the pet's health by 5
        self.health += 5
        print(self.health)

    def noise(self): # prints out the pet's sound
        print("pet's sound")

ninja = Ninja("med", "kahla", "mekla", "croquette", "diva")
diva = Pet("Diva", "dog", "magic")

ninja.feed(diva)
ninja.walk(diva)
ninja.bathe(diva)

