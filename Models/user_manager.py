import mysql.connector
from datetime import datetime

class UserManager:
    def __init__(self, user_data_id, user_id, data_key, data_value, last_updated):
        self.userDataID = user_data_id
        self.userID = user_id
        self.dataKey = data_key
        self.dataValue = data_value
        self.lastUpdated = last_updated

    @staticmethod
    def get_user_data_by_user(user_id):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="your_password", database="business_advisor"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM UserData WHERE UserID = %s", (user_id,))
        user_data = cursor.fetchall()
        connection.close()
        return [UserManager(**data) for data in user_data]

    def save(self):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="your_password", database="business_advisor"
        )
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO UserData (UserID, DataKey, DataValue, LastUpdated) 
            VALUES (%s, %s, %s, NOW())""",
            (self.userID, self.dataKey, self.dataValue),
        )
        connection.commit()
        connection.close()
