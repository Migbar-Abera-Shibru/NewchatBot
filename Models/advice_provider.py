import mysql.connector
from datetime import datetime
import config  # Importing config.py

class AdviceProvider:
    def __init__(self, advice_id, user_id, context, advice_text, created_at):
        self.adviceID = advice_id
        self.userID = user_id
        self.context = context
        self.adviceText = advice_text
        self.createdAt = created_at

    @staticmethod
    def _get_db_connection():
        """Establish a connection to the MySQL database using details from config.py."""
        return mysql.connector.connect(
            host=config.DB_HOST,           # Using host from config.py
            user=config.DB_USER,           # Using user from config.py
            password=config.DB_PASSWORD,   # Using password from config.py
            database=config.DB_NAME        # Using database name from config.py
        )

    @staticmethod
    def get_advice_by_user(user_id):
        connection = AdviceProvider._get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Advice WHERE UserID = %s", (user_id,))
        advice_data = cursor.fetchall()
        connection.close()
        return [AdviceProvider(**advice) for advice in advice_data]

    def save(self):
        connection = AdviceProvider._get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Advice (UserID, Context, AdviceText, CreatedAt)
            VALUES (%s, %s, %s, %s)""",
            (self.userID, self.context, self.adviceText, self.createdAt),
        )
        connection.commit()
        connection.close()
