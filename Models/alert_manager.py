import mysql.connector
from datetime import datetime

class AdviceManager:
    def __init__(self, advice_id, user_id, context, advice_text, created_at):
        self.adviceID = advice_id
        self.userID = user_id
        self.context = context
        self.adviceText = advice_text
        self.createdAt = created_at

    @staticmethod
    def get_advice_by_user(user_id):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="your_password", database="business_advisor"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Advice WHERE UserID = %s", (user_id,))
        advice_data = cursor.fetchall()
        connection.close()
        return [AdviceManager(**advice) for advice in advice_data]

    def save(self):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="your_password", database="business_advisor"
        )
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Advice (UserID, Context, AdviceText, CreatedAt)
            VALUES (%s, %s, %s, %s)""",
            (self.userID, self.context, self.adviceText, self.createdAt),
        )
        connection.commit()
        connection.close()
