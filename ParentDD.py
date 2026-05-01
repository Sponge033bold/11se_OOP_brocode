class ParentDD:

    def __init__(self, name ,food ,hobby):
        self.name = name
        self.food = food
        self.hobby = hobby

    def introduce(self):
        print(f"{self.name} enjoys {self.hobby} and eating {self.food}.")
    def relax(self):
        print(f"{self.name} is now chilling.")
    def indulge(self):
        print(f"{self.name} is now eating {self.food}.")