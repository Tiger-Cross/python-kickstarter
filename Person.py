class Person:

    def __init__(self, first_name, last_name, phone_number, email):
        self.fname = first_name
        self.lname = last_name
        self.pnum = phone_number
        self.email = email

    def __str__(self) -> str:
        return f"{self.fname}, {self.lname}, {self.pnum}, {self.email}"

    def change_name(self, newName):
        oldName = self.fname
        self.fname = newName
        print(f"{oldName} changed their name to {newName}")

    def matches(self, query: str) -> bool:
        return self.fname.startswith(query) or self.lname.startswith(query) or self.pnum.startswith(query) or self.email.startswith(query)


    def say_name(self):
        print(f"My full name is {self.fname} {self.lname}")    