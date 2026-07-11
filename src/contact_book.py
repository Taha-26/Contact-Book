import json
from typing import Dict, List

import Contact


class ContactBook:
    """Manages an in-memory repository of Contact instances.

    Provides core CRUD operations including adding, removing, updating,
    and searching for contact records based on specific field values.
    """

    def __init__(self):
        """Initialize an empty ContactBook instance."""
        # Internal dictionary mapping unique phone numbers to Contact objects
        self._contacts: Dict[str, Contact] = {}

    def add(self, contact: Contact):
        """Add a new contact to the repository.

        :param contact: The Contact object instance to be registered.
        :raises ValueError: If the contact's phone number already exists in the repository.
        """
        if contact.phone in self._contacts:
            raise ValueError(
                f"Contact with phone number {contact.phone} already exists."
            )
        self._contacts[contact.phone] = contact

    def remove(self, phone: str) -> bool:
        """Remove a contact from the repository using their phone number.

        :param phone: The unique phone number identifier of the target contact.
        :return: True if the contact was found and successfully deleted, False otherwise.
        """
        if phone in self._contacts:
            del self._contacts[phone]
            return True
        return False

    def search_by_name(self, query: str) -> List[Contact]:
        """Search contacts by performing a substring match against names.

        Matches the provided query string against both first and last names,
        ignoring letter casing.

        :param query: The search term for names.
        :return: A list of dictionaries representing matching contacts.
        """
        if not query:
            return []
        return [
            c.to_dict()
            for c in self._contacts.values()
            if query.lower() in c.name.lower() or query.lower() in c.last_name.lower()
        ]

    def update(self, phone: str, **kwargs) -> bool:
        """Dynamically update attributes of an existing contact.

        Modifies the properties of the contact matching the provided phone number.
        Prevents modification of the unique identifier ('phone').

        :param phone: The phone number of the contact to update.
        :param kwargs: Keyword arguments representing fields and their new values.

        :return: True if the contact exists and was updated, False if not found.
        """
        contact = self._contacts.get(phone)
        if not contact:
            return False

        # Iterate and apply valid updates dynamically using reflection
        for key, value in kwargs.items():
            if hasattr(contact, key) and key != "phone":
                setattr(contact, key, value)
        return True

    def show(self) -> str:
        """Generate a formatted JSON string containing all contacts.

        Serializes the entire repository with non-ASCII preservation
        and standard indentation.

        :return: A JSON-formatted string of the complete database state.
        """
        raw_data = {phone: obj.to_dict() for phone, obj in self._contacts.items()}
        return json.dumps(raw_data, indent=3, ensure_ascii=False)
