class Profile:
    def __init__(self):
        self.name = "Ikram Afakhar"
        self.role = "Software Engineering Student"
        self.skills = ["Java", "Python", "DevOps", "Full Stack"]

    def greet(self):
        print(f"Hi! I'm {self.name}, a {self.role}.")
        print("Welcome to my GitHub profile!")

if __name__ == "__main__":
    me = Profile()
    me.greet()
