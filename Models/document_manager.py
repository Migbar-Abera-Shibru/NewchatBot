import mysql.connector
from datetime import datetime

class Document:
    def __init__(self, document_id, title, file_path, uploaded_by, uploaded_at, is_read_only):
        self.documentID = document_id
        self.title = title
        self.filePath = file_path
        self.uploadedBy = uploaded_by
        self.uploadedAt = uploaded_at
        self.isReadOnly = is_read_only

    @staticmethod
    def get_document_by_id(document_id):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="your_password", database="business_advisor"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Documents WHERE DocumentID = %s", (document_id,))
        document_data = cursor.fetchone()
        connection.close()
        if document_data:
            return Document(**document_data)
        return None

    def save(self):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="your_password", database="business_advisor"
        )
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Documents (Title, FilePath, UploadedBy, UploadedAt, IsReadOnly)
            VALUES (%s, %s, %s, %s, %s)""",
            (self.title, self.filePath, self.uploadedBy, self.uploadedAt, self.isReadOnly),
        )
        connection.commit()
        connection.close()
