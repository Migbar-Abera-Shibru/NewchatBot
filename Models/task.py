import mysql.connector
from datetime import datetime

class Task:
    def __init__(self, task_id, project_id, assigned_to, task_name, description, due_date, status, progress_percentage, created_at):
        self.taskID = task_id
        self.projectID = project_id
        self.assignedTo = assigned_to
        self.taskName = task_name
        self.description = description
        self.dueDate = due_date
        self.status = status
        self.progressPercentage = progress_percentage
        self.createdAt = created_at

    @staticmethod
    def get_task_by_id(task_id):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="your_password", database="business_advisor"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Tasks WHERE TaskID = %s", (task_id,))
        task_data = cursor.fetchone()
        connection.close()
        if task_data:
            return Task(**task_data)
        return None

    def save(self):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="your_password", database="business_advisor"
        )
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Tasks (ProjectID, AssignedTo, TaskName, Description, DueDate, Status, ProgressPercentage, CreatedAt)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (self.projectID, self.assignedTo, self.taskName, self.description, self.dueDate, self.status, self.progressPercentage, self.createdAt),
        )
        connection.commit()
        connection.close()
