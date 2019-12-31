from contact import Contact
import csv

class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def _save(self):
        with open('contacts.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )

    def delete(self, email):
        for idx, contact in enumerate(self._contacts):
            if contact.email.lower() == email.lower():
                del self._contacts[idx]
                self._save()
                break
