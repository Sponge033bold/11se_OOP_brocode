class ParentDD:

    def __init__(self,name,food,hobby,catchphrase,age):
        self.name = name
        self.food = food
        self.hobby = hobby
        self.catchphrase = catchphrase
        self.age = age

    def introduce(self):
        print(f"{self.name} enjoys {self.hobby} and eating {self.food}.")
    def relax(self):
        print(f"{self.name} is now chilling.")
    def indulge(self):
        print(f"{self.name} is now eating {self.food}.")

    class ChildTL(ParentDD):

        def __init__(self,name,food,hobby,catchphrase,age):
            super().__init__(name,food,hobby,catchphrase,age)

            self.activities = {
                "Bart": "Riding my skateboard",
                "Lisa": "Reading my books",
                "Maggie": "Sucking on my pacifier"
            }