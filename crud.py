
# CREATE DATABASE card;

# USE card;

# CREATE TABLE card (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     email VARCHAR(100) UNIQUE
# );



import mysql.connector

# -------------------------
# Connect to MySQL database
# -------------------------
conn = mysql.connector.connect(
    host="localhost",
    user='root',      # Replace with your MySQL username
    password='1989',  # Replace with your MySQL password
    database='netligent'
)
cursor = conn.cursor()

# -------------------------
# CREATE - Insert a user
# -------------------------
def create_user(name, email):
    sql = "INSERT INTO card (name, email) VALUES (%s, %s)"
    values = (name, email)
    cursor.execute(sql, values)
    conn.commit()
    print(f"User '{name}' created with ID {cursor.lastrowid}")

# -------------------------
# READ - Fetch all card
# -------------------------
def read_card():
    cursor.execute("SELECT * FROM card")
    rows = cursor.fetchall()
    print("All card:")
    for row in rows:
        print(row)

# -------------------------
# UPDATE - Update user
# -------------------------
def update_user(user_id, name, email):
    sql = "UPDATE card SET name = %s, email = %s WHERE id = %s"
    values = (name, email, user_id)
    cursor.execute(sql, values)
    conn.commit()
    print(f"User ID {user_id} updated.")

# -------------------------
# DELETE - Delete user
# -------------------------
def delete_user(user_id):
    sql = "DELETE FROM card WHERE id = %s"
    value = (user_id,)
    cursor.execute(sql, value)
    conn.commit()
    print(f"User ID {user_id} deleted.")
    
    

while True:
        print("\n CRUD stands for Create, Read, Update, and Delete,")
        print("1. Create  Details")
        print("2. Read  Details")
        print("3. Update  Details")
        print("4. Delete")
        print("0. Exit")
        b = int(input("Enter your choice:"))
        
        if b==1:
            name= input("Enter Your Name :- ")
            email= input("Enter Your Name email :- ")
            create_user(name, email)
            print(f"Sussfully Update ,{name, email} ")
        elif b==2:
            read_card()
        elif b==3:
            user_id = int(input("Enter employee ID to edit: "))
            name = input("Enter new employee name: ")
            email = input("Enter new email: ")
            update_user(user_id, name, email)
        elif b==4:
            user_id = int(input("Enter employee ID to edit: "))
            delete_user(user_id)
        elif b==0:
            break

            
            
            

# # -------------------------
# # Example Usage
# # -------------------------
# create_user("Alice", "alice@example.com")
# create_user("Bob", "bob@example.com")

# read_card()

# update_user(1, "Alicia", "alicia@example.com")

# read_card()

# delete_user(2)

# read_card()

# Close connection
cursor.close()
conn.close()
