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

        self.activity = {
            "Bart": "riding my skateboard",
            "Lisa": "reading my books",
            "Maggie": "playing with my toys"
        }

    def activity(self):
        return self.activity.get(self.name, "Fortunately not in the Simpson family")
    
    def speak(self):
        print(f"Hello my name is {self.name}, I am {self.age} years old, {self.catchphrase}, I loves {self.activity()}.")