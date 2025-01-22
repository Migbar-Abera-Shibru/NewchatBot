import mysql.connector
from datetime import datetime

class Project:
    def __init__(self, project_id, project_name, description, start_date, end_date, owner_id, status, created_at):
        self.projectID = project_id
        self.projectName = project_name
        self.description = description
        self.startDate = start_date
        self.endDate = end_date
        self.ownerID = owner_id
        self.status = status
        self.createdAt = created_at

    @staticmethod
    def get_project_by_id(project_id):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="your_password", database="business_advisor"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Projects WHERE ProjectID = %s", (project_id,))
        project_data = cursor.fetchone()
        connection.close()
        if project_data:
            return Project(**project_data)
        return None

    def save(self):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="your_password", database="business_advisor"
        )
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Projects (ProjectName, Description, StartDate, EndDate, OwnerID, Status, CreatedAt)
            VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            (self.projectName, self.description, self.startDate, self.endDate, self.ownerID, self.status, self.createdAt),
        )
        connection.commit()
        connection.close()
