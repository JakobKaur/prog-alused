class Person:

    def __init__(self, firstname: str, lastname: str, phone_number: str):
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number

    def get_full_name(self) -> str:
        if self.lastname:
            return self.firstname + " " + self.lastname
        else:
            return self.firstname


class ContactBook:

    def __init__(self):
        self.contacts = []

    def add_person_to_contacts(self, person: Person) -> None:
        if person.firstname and person.phone_number:
            self.contacts.append(person)

    def find_contact_by_number(self, number) -> Person:
        for contact in self.contacts:
            if contact.phone_number == number:
                return contact
        return None

    def get_sorted_contacts(self) -> list:
        return sorted(self.contacts, key=lambda x: x.get_full_name())