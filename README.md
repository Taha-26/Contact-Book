<img src="assets/banner.jpg" >

---

# Contact Book Application

An in-memory, Object-Oriented Contact Management System implemented in Python. This project is built following standard software engineering practices, separating the domain model from the data repository layer to ensure clean code, testability, and seamless future database integration.

## ⚙️ Architecture & Design Principles

The application avoids global state and static class structures, adhering tightly to Object-Oriented Programming (OOP) paradigms. It is split into two primary components:

*   **`Contact` (Domain Model):** Represents a single contact entity, holding all personal attributes (phone, name, email, etc.) and handling its own serialization.
*   **`ContactBook` (Repository Layer):** Manages the collection of contacts, enforcing unique constraints on primary keys (phone numbers) and executing CRUD workflows.

> **Data Integrity:** The contact's phone number acts as the unique primary identifier. While it is stored as the key in the repository dictionary for $O(1)$ fast lookups, it is also retained inside the object property to maintain data portability.

---

## ✨ Features

*   **Complete CRUD Operations:** Fully implemented methods to Add, Read, Update, and Delete entries.
*   **Dynamic Updates:** Utilizes Python reflection mechanisms (`hasattr` and `setattr`) to dynamically update only the provided keyword arguments (`**kwargs`) while explicitly protecting the primary identifier.
*   **Safe Lookups:** Features case-insensitive partial substring searching by name, as well as multi-attribute matching logic.
*   **Self-Contained Testing:** Built-in automated unit checks utilizing native `assert` statements to guarantee regression-free updates.

---

## 📁 File Structure

```text
│
├── src/
│   ├── main.py             # Main entry point 
│   └── contact.py          # The Contact entity class definition
│   └── contact_book.py     # The collection repository managing the entities
│
└── README.md      
```
---
## 💻 Getting Started
### Prerequisites

+ Python 3.8 or higher is recommended.

### Running the Project & Tests
The `main.py` script serves as the executable entry point. It populates the repository with sample mock data and automatically triggers the test suite verifying core functionalities.

Run the following command in your terminal:

```bash
python main.py
```

### Expected Test Output
Upon successful execution, the console will output the following confirmation:

```text
--- Starting ContactBook Tests ---
Test Add (Duplicate Check): Passed
Test Search By Name: Passed
Test Update: Passed
Test Remove: Passed
--- All Tests Completed Successfully ---
```