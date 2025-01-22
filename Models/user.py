import mysql.connector
from datetime import datetime

class User:
    def __init__(self, user_id, username, email, role, preferences, created_at, last_login, is_active):
        self.userID = user_id
        self.username = username
        self.email = email
        self.role = role
        self.preferences = preferences
        self.createdAt = created_at
        self.lastLogin = last_login
        self.isActive = is_active

    @staticmethod
    def get_user_by_id(user_id):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="your_password", database="business_advisor"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Users WHERE UserID = %s", (user_id,))
        user_data = cursor.fetchone()
        connection.close()
        if user_data:
            return User(**user_data)
        return None

    def save(self):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="your_password", database="business_advisor"
        )
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Users (Username, Email, Role, Preferences, CreatedAt, LastLogin, IsActive) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            (self.username, self.email, self.role, self.preferences, self.createdAt, self.lastLogin, self.isActive),
        )
        connection.commit()
        connection.close()
