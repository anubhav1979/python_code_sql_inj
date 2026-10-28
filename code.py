import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Vulnerable: directly inserting user input into SQL
    query = "SELECT * FROM users WHERE username = '" + username + "'"

    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()
    return result


username = input("Enter username: ")
print(get_user(username))
