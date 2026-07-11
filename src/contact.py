from typing import Dict


class Contact:
    """Represents a single contact entity containing personal details.

    This class acts as a data model to store and manage the information
    associated with an individual contact entry.
    """

    def __init__(
        self,
        phone: str,
        name: str = "",
        last_name: str = "",
        email: str = "",
        address: str = "",
        birthday: str = "",
        note: str = "",
    ):
        """Initialize a new Contact instance.

        :param phone: The primary unique phone number identifier for the contact.
        :param name: The first name of the contact, defaults to "".
        :param last_name: The last name of the contact, defaults to "".
        :param email: The email address of the contact, defaults to "".
        :param address: The physical residential or postal address, defaults to "".
        :param birthday: The birth date of the contact, defaults to "".
        :param note: Additional remarks or descriptions, defaults to "".
        """
        self.phone = phone
        self.name = name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.birthday = birthday
        self.note = note

    def to_dict(self) -> Dict[str, str]:
        """Serialize the contact object properties into a standard dictionary.

        :return: A dictionary representation containing all contact attributes.
        """
        return {
            "phone": self.phone,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            "address": self.address,
            "birthday": self.birthday,
            "note": self.note,
        }
