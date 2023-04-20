class Title:
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

    def assign(self):
        if self.sex == 'male':
            return f"Mr. {self.name}"
        else:
            return f"Mrs. {self.name}"

name = input("Enter your name: ")
sex = input("Are you a male or female? ").lower() # Convert the input to lower case

e = Title(name,sex)
print(e.assign()) # Pass the 'sex' argument when calling annotate() method
