class ProgressAnalyzer:
    @staticmethod
    def analyze_progress(project_id):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="your_password", database="business_advisor"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Tasks WHERE ProjectID = %s", (project_id,))
        tasks = cursor.fetchall()
        connection.close()

        completed_tasks = sum(1 for task in tasks if task['Status'] == 'Completed')
        total_tasks = len(tasks)
        progress_percentage = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

        return f"Project progress: {progress_percentage}%"
