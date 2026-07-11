"""Contact Book - Main Entry Point.

This module demonstrates the usage of the ContactBook and Contact classes
by initializing a contact book instance, populating it with sample data,
and executing a search query.

Author: https://github.com/Taha-26
"""

from Contact import Contact
from ContactBook import ContactBook


def main():
    """Execute the main lifecycle of the contact book demonstration.

    Initializes the ContactBook repository, registers multiple Contact
    instances with varying completeness of profile data, and executes
    a search operation.
    """

    # ==========================================
    # TEST SECTION
    # ==========================================

    print("--- Starting ContactBook Tests ---")

    my_contacts = ContactBook()
    # 1. Test: add() function constraints (Duplicate Prevention)
    try:
        # Attempting to add a duplicate entry with David's phone number
        my_contacts.add(Contact(phone="+442079460192", name="Clone David"))
        assert False, "Test Add Failed: Duplicate phone number was accepted."
    except ValueError:
        print("Test Add (Duplicate Check): Passed")

    # 2. Test: search_by_name() verification
    # Searching for a case-insensitive partial match
    search_results = my_contacts.search_by_name("emily")
    assert len(search_results) == 1, "Test Search Failed: Expected exactly 1 match."
    assert search_results[0]["last_name"] == "Watson", (
        "Test Search Failed: Incorrect contact returned."
    )
    print("Test Search By Name: Passed")

    # 3. Test: update() functionality
    # Updating existing fields dynamically for David's contact
    update_status = my_contacts.update(
        phone="+442079460192",
        email="david.updated@techcorp.com",
        address="New Street 12",
    )
    assert update_status is True, "Test Update Failed: Target contact was not found."

    # Verify the updated fields through search retrieval
    updated_contact = my_contacts.search_by_name("David")[0]
    assert updated_contact["email"] == "david.updated@techcorp.com", (
        "Test Update Failed: Email mismatch."
    )
    assert updated_contact["address"] == "New Street 12", (
        "Test Update Failed: Address mismatch."
    )
    print("Test Update: Passed")

    # 4. Test: remove() functionality
    # Removing Liam's contact via his unique identifier (phone)
    delete_status = my_contacts.remove("+35316130000")
    assert delete_status is True, (
        "Test Remove Failed: Existing contact was not deleted."
    )

    # Verify the contact no longer exists in the system
    liam_search = my_contacts.search_by_name("Liam")
    assert len(liam_search) == 0, (
        "Test Remove Failed: Deleted contact is still retrievable."
    )

    # Attempting to delete a non-existent contact identifier
    delete_non_existent = my_contacts.remove("+35316130000")
    assert delete_non_existent is False, (
        "Test Remove Failed: Deleting non-existent contact should return False."
    )
    print("Test Remove: Passed")

    print("--- All Tests Completed Successfully ---")


if __name__ == "__main__":
    main()
