import mysql.connector

class Security:
    def __init__(self, security_id, user_id, key_name, key_value, last_updated):
        self.securityID = security_id
        self.userID = user_id
        self.keyName = key_name
        self.keyValue = key_value
        self.lastUpdated = last_updated

    @staticmethod
    def get_security_key_by_user(user_id):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="your_password", database="business_advisor"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Security WHERE UserID = %s", (user_id,))
        security_data = cursor.fetchall()
        connection.close()
        return [Security(**key) for key in security_data]

    def save(self):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="your_password", database="business_advisor"
        )
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Security (UserID, KeyName, KeyValue, LastUpdated) 
            VALUES (%s, %s, %s, NOW())""",
            (self.userID, self.keyName, self.keyValue),
        )
        connection.commit()
        connection.close()
