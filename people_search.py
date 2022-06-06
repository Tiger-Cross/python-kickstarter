from fileinput import filename
from typing import List

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

    def say_name(self):
        print(f"My full name is {self.fname} {self.lname}")    

def say_name(person):
    print(f"The person's full name is {person.fname} {person.lname}")

def get_attribute(attribute_name: str) -> str:
    print(f"Please enter the user's {attribute_name}:")
    attribute = input()
    return attribute

def read_people_from_file(file_name: str) -> List[Person]:
    people_file = open(file_name, "r")
    lines = people_file.readlines()
    people = list()
    for person_data in lines:
        person_attributes = person_data.split()
        person = Person(person_attributes[0], person_attributes[1], person_attributes[2], person_attributes[3])
        people.append(person)
    return people
        

if __name__ == "__main__":
    
    people = read_people_from_file("people.txt")

    for p in people:
        p.change_name("frank")
