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

def qf_search_for_people(people: List[Person], query: str) -> List[Person]:
    results = []
    for person in people:
        if person.matches(query):
            results.append(person)
    return results


if __name__ == "__main__":

    people = read_people_from_file("people.txt")

    query = ""

    with keyboard.Events() as events:
        for event in events:
            if isinstance(event, keyboard.Events.Press):
                try:
                    query += event.key.char
                    query_results = qf_search_for_people(people, query)
                    print(query)
                    for person in query_results:
                        print(person)
                except AttributeError:
                    if event.key == keyboard.Key.space:
                        query += " "
                    else:
                        print(f"your query was {query}")
                        break
        