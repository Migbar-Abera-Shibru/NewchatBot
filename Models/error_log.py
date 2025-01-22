import mysql.connector
from datetime import datetime

class ErrorLog:
    def __init__(self, log_id, user_id, action, timestamp, error_message):
        self.logID = log_id
        self.userID = user_id
        self.action = action
        self.timestamp = timestamp
        self.errorMessage = error_message

    @staticmethod
    def get_error_logs_by_user(user_id):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="your_password", database="business_advisor"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Logs WHERE UserID = %s", (user_id,))
        error_logs = cursor.fetchall()
        connection.close()
        return [ErrorLog(**log) for log in error_logs]

    def save(self):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="your_password", database="business_advisor"
        )
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Logs (UserID, Action, Timestamp, Details) 
            VALUES (%s, %s, %s, %s)""",
            (self.userID, self.action, self.timestamp, self.errorMessage),
        )
        connection.commit()
        connection.close()
