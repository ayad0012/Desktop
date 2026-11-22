import sqlite3
from datetime import datetime

# 1. Database aur Table banana
def init_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# 2. Naya Contact add karna
def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email (optional): ").strip()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not name or not phone:
        print("❌ Name aur Phone Number zaroori hai!\n")
        return

    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contacts (name, phone, email, created_at) VALUES (?, ?, ?, ?)",
        (name, phone, email, created_at)
    )
    conn.commit()
    conn.close()
    print("✅ Contact successfully add ho gaya!\n")

# 3. Saare Contacts dekhna
def view_contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("📭 Koi contact nahi mila.\n")
        return

    print("\n--- ALL CONTACTS ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]} | Email: {row[3]} | Added: {row[4]}")
    print("--------------------\n")

# 4. Contact Search karna
def search_contact():
    keyword = input("Search by Name or Phone: ").strip()
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?",
        (f"%{keyword}%", f"%{keyword}%")
    )
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("❌ Koi matching contact nahi mila.\n")
        return

    print("\n--- SEARCH RESULTS ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]} | Email: {row[3]}")
    print("----------------------\n")

# 5. Contact Update karna
def update_contact():
    contact_id = input("Enter Contact ID to update: ").strip()
    new_name = input("Enter New Name: ").strip()
    new_phone = input("Enter New Phone: ").strip()
    new_email = input("Enter New Email: ").strip()

    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ?",
        (new_name, new_phone, new_email, contact_id)
    )
    conn.commit()
    if cursor.rowcount == 0:
        print("❌ Contact ID nahi mila.\n")
    else:
        print("✅ Contact update ho gaya!\n")
    conn.close()

# 6. Contact Delete karna
def delete_contact():
    contact_id = input("Enter Contact ID to delete: ").strip()
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    if cursor.rowcount == 0:
        print("❌ Contact ID nahi mila.\n")
    else:
        print("🗑️ Contact delete ho gaya!\n")
    conn.close()

# Main Menu
def main():
    init_db()
    while True:
        print("=== CONTACT BOOK MANAGEMENT SYSTEM ===")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Apna option chunein (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Galat option! Please 1 se 6 ke beech chunein.\n")

if __name__ == "__main__":
    main()