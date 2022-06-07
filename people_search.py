from fileinput import filename
from typing import List

from Person import Person

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
        print(p)
