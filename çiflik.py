import random

class MammalAnimal:
    def __init__(self, name, color, born):
        self.name = name
        self.color = color
        self.age = random.randint(1, 10)  
        self.born = born
        self.population = random.randint(10, 50)
        
        
    def compare_age(self, other_animal):
        if self.age > other_animal.age:
            print(f"{self.name} is older than {other_animal.name}.")
        elif self.age < other_animal.age:
            print(f"{other_animal.name} is older than {self.name}.")
        else:
            print(f"{self.name} and {other_animal.name} are of the same age.")
      
        if self.color == "black":
            print(f"{self.name} is black.")
        else:
            print(f"{self.name} is not black.")
      
    def check_mammal(self):
        born_input = input(f"Does {self.name} give birth? (yes/no): ").lower()
        if born_input == "yes":
            print(f"{self.name} is a mammal.")
        elif born_input == "no":
            print(f"{self.name} is non-mammalian.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    def feed(self):
        feed_input = input(f"Does {self.name} eat? (yes/no): ").lower()
        if feed_input == "yes":
            print(f"{self.name} is growing up.")
        elif feed_input == "no":
            print(f"{self.name} is dead.")
            self.dead()  
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    def dead(self):
        dead_amount = int(input("How many animals died? "))
        self.population -= dead_amount
        print(f"New population after death: {self.population}")
        
        if self.population == 0:
            print("You don't have any animals.")
        elif self.population < 0:
            print("You have a population (debt).")
            
    
    def rise(self):
        rise_amount = int(input("How many new animals are rising? "))
        self.population += rise_amount
        print({self.population})
    
      
    
      

mammal1 = MammalAnimal("Köpek", "Black", "yes")
mammal2 = MammalAnimal("Tavuk", "White", "no")

mammal1.compare_age(mammal2)
mammal1.check_mammal()
mammal1.feed()
mammal1.dead()
mammal1.rise()
