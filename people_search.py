from typing import List

from Person import Person

from pynput import keyboard


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

    query = ""

    with keyboard.Events() as events:
        for event in events:
            if isinstance(event, keyboard.Events.Press):
                try:
                    query += event.key.char
                except AttributeError:
                    if event.key == keyboard.Key.space:
                        query += " "
                    else:
                        print(f"your query was {query}")
                        break
