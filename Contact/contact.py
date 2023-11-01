import sqlite3

# Creating a SQLite database and table

conn = sqlite3.connect('contacts.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS contacts
             (id INTEGER PRIMARY KEY,
             name TEXT,
             phone TEXT,
             email TEXT,
             address TEXT)''')
conn.commit()

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    
    c.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
              (name, phone, email, address))
    conn.commit()
    view_contacts()
    print("\nContact added successfully!")

def view_contacts():
    print(f"|{'Name':<15}|{'Phone':<15}|{'Email':<30}|{'Address':<20}")
    c.execute("SELECT name, phone, email, address FROM contacts")
    contacts = c.fetchall()
    for contact in contacts:
        print(f"|{contact[0]:<15}|{contact[1]:<15}|{contact[2]:<30}|{contact[3]:<20}")

def search_contact():
    query = input("Enter Name or Phone Number to search: ")
    c.execute("SELECT name, phone, email, address FROM contacts WHERE name LIKE ? OR phone LIKE ? OR email LIKE ? OR address LIKE ?",
              (f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%'))
    contacts = c.fetchall()
    if contacts:
        print(f"|{'Name':<15}|{'Phone':<15}|{'Email':<30}|{'Address':<20}")
        for contact in contacts:
            print(f"|{contact[0]:<15}|{contact[1]:<15}|{contact[2]:<30}|{contact[3]:<20}")
            
    else:
        print("No matching contacts found.")

def update_contact():
    query = input("Enter Name or Phone Number to update: ")
    c.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?",
              (f'%{query}%', f'%{query}%'))
    contact = c.fetchone()
    if contact:
        print(f"Current Details - Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}, Address: {contact[4]}")
        name = input("Enter New Name (press Enter to keep current): ") or contact[1]
        phone = input("Enter New Phone Number (press Enter to keep current): ") or contact[2]
        email = input("Enter New Email (press Enter to keep current): ") or contact[3]
        address = input("Enter New Address (press Enter to keep current): ") or contact[4]

        c.execute("UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE id=?",
                  (name, phone, email, address, contact[0]))
        conn.commit()
        view_contacts()
        print("Contact updated successfully!")
        
    else:
        print("No matching contacts found.")

def delete_contact():
    query = input("Enter Name or Phone Number to delete: ")
    c.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?",
              (f'%{query}%', f'%{query}%'))
    contact = c.fetchone()
    if contact:
        print(f"Deleting Contact - Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}, Address: {contact[4]}")
        confirm = input("Are you sure you want to delete this contact? (yes/no): ")
        if confirm.lower() == 'yes':
            c.execute("DELETE FROM contacts WHERE id=?", (contact[0],))
            conn.commit()
            print("Contact deleted successfully!")
    else:
        print("No matching contacts found.")

# Main loop
while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        conn.close()
        break
    else:
        print("Invalid choice. Please try again.")




