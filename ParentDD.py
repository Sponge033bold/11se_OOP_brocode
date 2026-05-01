class ParentDD:
    def __init__(self, name, food, hobby, catchphrase, age):
        self.name = name
        self.food = food
        self.hobby = hobby
        self.catchphrase = catchphrase
        self.age = age

    def speak(self):
        print(f"Hello my name is {self.name}, I am {self.age} years old, {self.catchphrase}, {self.name} loves relaxing at home.")

class ChildTL(ParentDD):

    def __init__(self, name, food, hobby, catchphrase, age):
        super().__init__(name, food, hobby, catchphrase, age)

        self.activities = {
            "Bart": "Riding my skateboard",
            "Lisa": "Reading my books",
            "Maggie": "Sucking on my pacifier"
        }
